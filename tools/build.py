#!/usr/bin/env python3
"""Builds the article and the deck from their sources into build/.

  manuscript/*.md                     -> build/*.md and build/*.pdf
  slides/template.pptx + notes.md     -> build/what-is-open-source.pptx

What the build does:

  - Fills every {{ placeholder }} from data/numbers.yml. {{ checked }} is the
    date the numbers were last fetched, as "4 November 2026". An unknown
    placeholder stops the build.
  - Removes Obsidian comments, %% like this %%, from the Markdown.
  - Removes all animations and slide transitions from the deck, including any
    that come in with a later edit of the template.
  - Puts the speaker notes from slides/notes.md (one "## Slide N" section per
    slide) into the deck, replacing whatever notes the template has.
  - Writes the deck with fixed timestamps, so the same input always gives the
    same file, and Git only sees a change when something really changed.

A placeholder in the deck has to sit inside one run of text (one stretch of
the same formatting). If you type one in PowerPoint or Google Slides and the
build says it is "split", retype the whole placeholder in one go, without
changing the formatting halfway.

Usage:
  .venv/bin/python tools/build.py           build build/
  .venv/bin/python tools/build.py --check   fail if build/ is out of date
"""

from __future__ import annotations

import datetime
import io
import re
import sys
import zipfile
from pathlib import Path

import yaml
from pptx import Presentation
from pptx.oxml.ns import qn

from build_pdf import PdfError, render

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
DECK = "what-is-open-source.pptx"
PLACEHOLDER = re.compile(r"\{\{\s*([a-z0-9_]+)\s*\}\}")
COMMENT = re.compile(r"%%.*?%%", re.DOTALL)


class BuildError(Exception):
    pass


def load_numbers() -> dict[str, str]:
    data = yaml.safe_load((ROOT / "data" / "numbers.yml").read_text())
    values = {key: str(entry["value"]) for key, entry in data["numbers"].items()}
    checked = datetime.date.fromisoformat(str(data["checked"]))
    values["checked"] = f"{checked.day} {checked:%B %Y}"
    return values


def load_cover() -> dict:
    """data/cover.yml, with the date written out and the logo as a path (or None)."""
    cover = yaml.safe_load((ROOT / "data" / "cover.yml").read_text())
    date = datetime.date.fromisoformat(str(cover["date"]))
    cover["date"] = f"{date.day} {date:%B %Y}"
    logo = ROOT / cover["logo"]
    if logo.suffix.lower() not in (".png", ".jpg", ".jpeg"):
        raise BuildError(f"data/cover.yml: the logo has to be a PNG or JPEG: {cover['logo']}")
    if not logo.exists():
        print(f"warning: no logo on the front page, {cover['logo']} is missing", file=sys.stderr)
        logo = None
    cover["logo"] = logo
    return cover


def fill(text: str, values: dict[str, str], where: str) -> str:
    def replace(match: re.Match) -> str:
        if match.group(1) not in values:
            raise BuildError(f"{where}: unknown placeholder {match.group(0)}")
        return values[match.group(1)]
    return PLACEHOLDER.sub(replace, text)


def build_markdown(source: Path, values: dict[str, str]) -> str:
    text = COMMENT.sub("", source.read_text())
    text = fill(text, values, source.relative_to(ROOT).as_posix())
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"


def read_notes(values: dict[str, str]) -> dict[int, list[str]]:
    """slides/notes.md -> {slide number: [paragraphs]}."""
    source = ROOT / "slides" / "notes.md"
    notes: dict[int, list[str]] = {}
    current = None
    for line in source.read_text().split("\n"):
        heading = re.match(r"## Slide (\d+)\s*$", line)
        if heading:
            current = notes.setdefault(int(heading.group(1)), [])
            current.append("")
        elif current is not None:
            current.append(line)
    for number, lines in notes.items():
        paragraphs, buffer = [], []
        for line in lines + [""]:
            if line.startswith("- "):
                if buffer:
                    paragraphs.append(" ".join(buffer))
                buffer = [line[2:]]
            elif line.strip():
                buffer.append(line.strip())
            elif buffer:
                paragraphs.append(" ".join(buffer))
                buffer = []
        notes[number] = [fill(p, values, f"slides/notes.md, slide {number}") for p in paragraphs]
    return notes


def text_frames(shapes):
    for shape in shapes:
        if shape.shape_type == 6:  # a group
            yield from text_frames(shape.shapes)
        if shape.has_text_frame:
            yield shape.text_frame
        if getattr(shape, "has_table", False) and shape.has_table:
            for row in shape.table.rows:
                for cell in row.cells:
                    yield cell.text_frame


def build_deck(values: dict[str, str]) -> bytes:
    template = ROOT / "slides" / "template.pptx"
    deck = Presentation(str(template))
    notes = read_notes(values)
    if notes and max(notes) > len(deck.slides):
        raise BuildError(f"slides/notes.md has notes for slide {max(notes)}, but the deck has {len(deck.slides)} slides")
    for number, slide in enumerate(deck.slides, start=1):
        for tag in ("p:timing", "p:transition"):
            for element in slide._element.findall(qn(tag)):
                slide._element.remove(element)
        for frame in text_frames(slide.shapes):
            for paragraph in frame.paragraphs:
                for run in paragraph.runs:
                    if "{{" in run.text:
                        run.text = fill(run.text, values, f"slide {number}")
                if "{{" in "".join(r.text for r in paragraph.runs):
                    raise BuildError(f"slide {number}: placeholder split across runs in '{''.join(r.text for r in paragraph.runs)}'")
        paragraphs = notes.get(number, [])
        if paragraphs or slide.has_notes_slide:
            frame = slide.notes_slide.notes_text_frame
            frame.text = "\n".join(paragraphs)
    raw = io.BytesIO()
    deck.save(raw)
    # Same input, same bytes: rewrite the ZIP with fixed timestamps and order.
    stable = io.BytesIO()
    with zipfile.ZipFile(raw) as source, zipfile.ZipFile(stable, "w", zipfile.ZIP_DEFLATED) as target:
        names = source.namelist()
        names.sort(key=lambda n: (n != "[Content_Types].xml", n))
        for name in names:
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            target.writestr(info, source.read(name))
    return stable.getvalue()


def main() -> int:
    check = "--check" in sys.argv
    try:
        values = load_numbers()
        cover = load_cover()
        outputs: dict[str, bytes] = {}
        for source in sorted((ROOT / "manuscript").glob("*.md")):
            article = build_markdown(source, values)
            outputs[source.name] = article.encode()
            outputs[source.with_suffix(".pdf").name] = render(article, cover)
        outputs[DECK] = build_deck(values)
    except (BuildError, PdfError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    stale = []
    BUILD.mkdir(exist_ok=True)
    for name, content in outputs.items():
        target = BUILD / name
        if target.exists() and target.read_bytes() == content:
            continue
        if check:
            stale.append(name)
        else:
            target.write_bytes(content)
            print(f"built build/{name}")
    for target in sorted(BUILD.glob("*")):
        if target.is_file() and target.name not in outputs and target.suffix in (".md", ".pdf", ".pptx"):
            if check:
                stale.append(target.name)
            else:
                target.unlink()
                print(f"removed build/{target.name}")
    if stale:
        print("out of date: " + ", ".join(stale), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
