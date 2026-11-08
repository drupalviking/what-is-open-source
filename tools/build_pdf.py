"""Turns the built article (Markdown) into a printable A4 PDF.

Used by build.py. It understands the Markdown the article uses: headings,
paragraphs, bullet and numbered lists, block quotes, tables, horizontal rules,
and bold, italic, code and links inside the text. A table it can't read stops
the build.

The fonts are the ones macOS comes with. They're embedded in the PDF, so
students don't need them. The first page is a front page, from data/cover.yml.
The PDF is written in ReportLab's "invariant" mode:
the same input always gives the same file.
"""

from __future__ import annotations

import io
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily, stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
FONTS = {
    "Body": "Georgia.ttf",
    "Body-Bold": "Georgia Bold.ttf",
    "Body-Italic": "Georgia Italic.ttf",
    "Body-BoldItalic": "Georgia Bold Italic.ttf",
    "Sans": "Arial.ttf",
    "Sans-Bold": "Arial Bold.ttf",
    "Sans-Italic": "Arial Italic.ttf",
    "Sans-BoldItalic": "Arial Bold Italic.ttf",
    "Mono": "Courier New.ttf",
}

MARGIN = 2.2 * cm
TEXT_WIDTH = A4[0] - 2 * MARGIN
INK = colors.HexColor("#1f2933")
ACCENT = colors.HexColor("#1b4f72")
RULE = colors.HexColor("#c5ccd3")
SHADE = colors.HexColor("#eef1f4")
MUTED = colors.HexColor("#5f6b76")
LOGO_WIDTH = 6.5 * cm
LOGO_HEIGHT = 2.6 * cm
LICENSE = "CC BY-SA 4.0"
TABLE_FONT_SIZE = 8.5
CELL_PADDING = 8


class PdfError(Exception):
    pass


def register_fonts() -> None:
    for name, filename in FONTS.items():
        path = FONT_DIR / filename
        if not path.exists():
            raise PdfError(f"font not found: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    for family in ("Body", "Sans"):
        registerFontFamily(
            family,
            normal=family,
            bold=f"{family}-Bold",
            italic=f"{family}-Italic",
            boldItalic=f"{family}-BoldItalic",
        )


def make_styles() -> dict[str, ParagraphStyle]:
    body = ParagraphStyle(
        "body", fontName="Body", fontSize=10.5, leading=15, textColor=INK,
        spaceAfter=7, alignment=TA_LEFT,
    )
    heading = dict(fontName="Sans-Bold", textColor=ACCENT, keepWithNext=1)
    return {
        "body": body,
        "cover_title": ParagraphStyle("cover_title", parent=body, fontName="Sans-Bold", textColor=ACCENT, fontSize=36, leading=42),
        "cover_course": ParagraphStyle("cover_course", parent=body, fontName="Sans", fontSize=15, leading=20),
        "cover_author": ParagraphStyle("cover_author", parent=body, fontName="Sans-Bold", fontSize=13, leading=17),
        "cover_date": ParagraphStyle("cover_date", parent=body, fontName="Sans", fontSize=12, leading=16, textColor=MUTED),
        "h1": ParagraphStyle("h1", parent=body, **heading, fontSize=24, leading=29, spaceAfter=12),
        "h2": ParagraphStyle("h2", parent=body, **heading, fontSize=15, leading=19, spaceBefore=16, spaceAfter=6),
        "h3": ParagraphStyle("h3", parent=body, **heading, fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=4),
        "item": ParagraphStyle("item", parent=body, leftIndent=22, bulletIndent=2, spaceAfter=4, bulletFontName="Body"),
        "quote": ParagraphStyle("quote", parent=body, fontSize=10, leading=14.5, spaceAfter=0),
        "cell": ParagraphStyle("cell", parent=body, fontName="Sans", fontSize=TABLE_FONT_SIZE, leading=11, spaceAfter=0),
        "head": ParagraphStyle("head", parent=body, fontName="Sans-Bold", fontSize=TABLE_FONT_SIZE, leading=11, spaceAfter=0),
    }


def smart_quotes(text: str) -> str:
    text = re.sub(r'(^|[\s(\[*])"', "\\1\u201c", text)
    text = text.replace('"', "\u201d")
    text = re.sub(r"(^|[\s(\[*\u201c])'", "\\1\u2018", text)
    return text.replace("'", "\u2019")


def inline(text: str) -> str:
    """Markdown inside a line of text -> ReportLab's paragraph markup."""
    stash: list[str] = []

    def keep(markup: str) -> str:
        stash.append(markup)
        return f"\x00{len(stash) - 1}\x00"

    def escape(value: str) -> str:
        return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def link(url: str, label: str) -> str:
        return f'{keep(f"""<a href="{escape(url)}" color="#1b4f72">""")}{label}{keep("</a>")}'

    text = re.sub(r"`([^`]+)`", lambda m: keep(f'<font face="Mono">{escape(m.group(1))}</font>'), text)
    text = re.sub(r"<(https?://[^>\s]+)>", lambda m: keep(link(m.group(1), escape(m.group(1)))), text)
    text = smart_quotes(escape(text))
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: link(m.group(2), m.group(1)), text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<![*\w])\*(?![\s*])(.+?)(?<![\s*])\*(?![*\w])", r"<i>\1</i>", text)
    # Stashed links hold stashed tags, so restore until none are left.
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)
    return text


def plain(markup: str) -> str:
    return re.sub(r"<[^>]+>", "", markup).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")


def column_widths(rows: list[list[str]]) -> list[float]:
    """The way browsers size tables: no column narrower than its longest word,
    and the remaining space goes to the columns with the most text."""
    def width(text: str, bold: bool) -> float:
        return stringWidth(text, "Sans-Bold" if bold else "Sans", TABLE_FONT_SIZE)

    count = len(rows[0])
    smallest = [0.0] * count
    natural = [0.0] * count
    for index, row in enumerate(rows):
        for column, cell in enumerate(row):
            text = plain(cell)
            bold = index == 0
            longest_word = max((width(word, bold) for word in text.split()), default=0)
            smallest[column] = max(smallest[column], longest_word + CELL_PADDING)
            natural[column] = max(natural[column], width(text, bold) + CELL_PADDING)
    if sum(smallest) >= TEXT_WIDTH:
        return [w * TEXT_WIDTH / sum(smallest) for w in smallest]
    if sum(natural) <= TEXT_WIDTH:
        return [w * TEXT_WIDTH / sum(natural) for w in natural]
    spare = TEXT_WIDTH - sum(smallest)
    extra = [n - s for n, s in zip(natural, smallest)]
    return [s + spare * e / sum(extra) for s, e in zip(smallest, extra)]


def make_table(lines: list[str], styles: dict[str, ParagraphStyle]) -> Table:
    rows = [[inline(cell.strip()) for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) < 2 or not all(re.fullmatch(r":?-+:?", plain(c)) for c in rows[1]):
        raise PdfError(f"not a Markdown table: {lines[0]}")
    rows = [rows[0]] + rows[2:]
    if any(len(row) != len(rows[0]) for row in rows):
        raise PdfError(f"table rows have different lengths: {lines[0]}")
    cells = [
        [Paragraph(cell, styles["head" if number == 0 else "cell"]) for cell in row]
        for number, row in enumerate(rows)
    ]
    table = Table(cells, colWidths=column_widths(rows), repeatRows=1, hAlign="LEFT", spaceBefore=4, spaceAfter=11)
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), SHADE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def make_quote(text: str, styles: dict[str, ParagraphStyle]) -> Table:
    quote = Table([[Paragraph(inline(text), styles["quote"])]], colWidths=[TEXT_WIDTH - 12], spaceBefore=2, spaceAfter=9)
    quote.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return quote


def parse(markdown: str, styles: dict[str, ParagraphStyle]) -> list:
    story: list = []
    lines = markdown.split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        heading = re.match(r"(#{1,3}) (.+)", line)
        bullet = re.match(r"- (.+)", line)
        number = re.match(r"(\d+)\. (.+)", line)
        if not line.strip():
            index += 1
        elif heading:
            story.append(Paragraph(inline(heading.group(2)), styles[f"h{len(heading.group(1))}"]))
            index += 1
        elif line.strip() == "---":
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=8))
            index += 1
        elif bullet:
            story.append(Paragraph(inline(bullet.group(1)), styles["item"], bulletText="\u2022"))
            index += 1
        elif number:
            story.append(Paragraph(inline(number.group(2)), styles["item"], bulletText=f"{number.group(1)}."))
            index += 1
        elif line.startswith("> "):
            story.append(make_quote(line[2:], styles))
            index += 1
        elif line.startswith("|"):
            start = index
            while index < len(lines) and lines[index].startswith("|"):
                index += 1
            story.append(KeepTogether(make_table(lines[start:index], styles)))
        else:
            story.append(Paragraph(inline(line), styles["body"]))
            index += 1
    return story


class Document(SimpleDocTemplate):
    """Adds a PDF bookmark for every section."""

    def afterFlowable(self, flowable) -> None:
        if not isinstance(flowable, Paragraph) or flowable.style.name not in ("h2", "h3"):
            return
        self._bookmarks = getattr(self, "_bookmarks", 0) + 1
        key = f"section-{self._bookmarks}"
        self.canv.bookmarkPage(key)
        level = 0 if flowable.style.name == "h2" else 1
        self.canv.addOutlineEntry(plain(flowable.text), key, level=level, closed=True)


def draw_cover(canvas, title: str, cover: dict, styles: dict[str, ParagraphStyle]) -> None:
    width, height = A4
    logo = cover.get("logo")
    if logo:
        canvas.drawImage(
            str(logo), width - MARGIN - LOGO_WIDTH, height - MARGIN - LOGO_HEIGHT,
            LOGO_WIDTH, LOGO_HEIGHT, preserveAspectRatio=True, anchor="ne", mask="auto",
        )

    def line(text: str, style: ParagraphStyle, top: float) -> float:
        paragraph = Paragraph(text, style)
        _, used = paragraph.wrapOn(canvas, TEXT_WIDTH, height)
        paragraph.drawOn(canvas, MARGIN, top - used)
        return top - used

    bottom = line(inline(title), styles["cover_title"], height * 0.66)
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(2)
    canvas.line(MARGIN, bottom - 16, MARGIN + 3 * cm, bottom - 16)
    bottom = line(inline(cover["course"]), styles["cover_course"], bottom - 32)
    bottom = line(inline(cover["author"]), styles["cover_author"], bottom - 44)
    line(inline(cover["date"]), styles["cover_date"], bottom - 6)
    canvas.setFont("Sans", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, 1.2 * cm, LICENSE)


def render(markdown: str, cover: dict) -> bytes:
    """The built article, with a front page, as the bytes of a PDF."""
    register_fonts()
    title = re.search(r"^# (.+)$", markdown, re.MULTILINE)
    if not title:
        raise PdfError("the article has no # title")
    title_text = plain(inline(title.group(1)))
    # The front page carries the title, so the article doesn't repeat it.
    body = markdown[:title.start()] + markdown[title.end():]
    styles = make_styles()

    def footer(canvas, document) -> None:
        canvas.saveState()
        canvas.setFont("Sans", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, 1.2 * cm, f"{title_text}  \u00b7  {LICENSE}")
        canvas.drawRightString(A4[0] - MARGIN, 1.2 * cm, str(document.page))
        canvas.restoreState()

    raw = io.BytesIO()
    document = Document(
        raw, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title=title_text, author=cover["author"], subject="Course notes", invariant=1,
    )
    story = [Spacer(1, 1), PageBreak()] + parse(body, styles)
    document.build(
        story,
        onFirstPage=lambda canvas, _: draw_cover(canvas, title_text, cover, styles),
        onLaterPages=footer,
    )
    return raw.getvalue()
