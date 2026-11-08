# What Is Open Source Software?

Course material for the lecture *Developing open-source web software: What is open-source software?* It has two parts, built from the same numbers:

- **The article**, `build/what-is-open-source.md`: course notes that go deeper than the slides, for students who will write about open source. It goes alongside Chapter 2 of the Drupal site-building book (`../developing-open-sourced-web-software-with-drupal/manuscript/02-open-source-and-the-drupal-community.md`).
- **The handout**, `build/what-is-open-source.pdf`: the same article as an A4 PDF, to give to students. It isn't kept in Git: build it yourself (see [Building](#building)).
- **The deck**, `build/what-is-open-source.pptx`: the lecture slides in English, with English speaker notes. It's the original Icelandic course deck, translated and updated.

The numbers that go out of date (versions, market shares, counts) aren't typed into either of them. They live in `data/numbers.yml`, each with its source, and a script fetches the current ones from those sources. Update the numbers, build, and the article and the deck are both current.

## License

The article, the slides and the speaker notes are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license](LICENSE) (CC BY-SA 4.0), like the Drupal site-building book. You may share and adapt them, also commercially, as long as you credit the author and share your changes under the same license.

The Reykjavík University logo on the handout's front page isn't covered by this license. It belongs to Reykjavík University, and it isn't in this repository.

## Layout

```
data/numbers.yml          every number, its source, and how to fetch it
data/cover.yml            the PDF's front page: course, author, date, logo
assets/                   the logo for the front page (not in Git)
manuscript/               the article, with {{ placeholders }} for the numbers
slides/template.pptx      the deck, with {{ placeholders }} in the tables
slides/notes.md           the speaker notes, one "## Slide N" section per slide
tools/update_numbers.py   fetches the current numbers into data/numbers.yml
tools/build.py            fills in the placeholders, and writes build/
tools/build_pdf.py        lays out the article as a PDF (used by build.py)
build/                    generated: don't edit, rebuild
BACKLOG.md                open items and ideas
LICENSE                   CC BY-SA 4.0
```

## Setup

Once, to install the Python libraries the tools use (python-pptx, PyYAML and ReportLab):

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Updating the numbers

```bash
.venv/bin/python tools/update_numbers.py --dry-run   # see what changed, write nothing
.venv/bin/python tools/update_numbers.py             # write the new numbers
.venv/bin/python tools/build.py                      # rebuild the article and the deck
```

The update script prints every number, with a `*` in front of the ones that changed, and a `?` in front of any it couldn't fetch (the old value stays; check those by hand). It also sets `checked:` to today's date, which the article and the deck show as "Numbers checked on ...". At the end, it lists the numbers that have no automatic source, with a link to check them by hand.

To update only some numbers: `.venv/bin/python tools/update_numbers.py drupal php`.

If GitHub refuses requests (it allows 60 an hour without logging in), set `GITHUB_TOKEN`.

### Where the numbers come from

| Numbers | Source |
|---|---|
| Versions of npm packages (Bootstrap, Angular, React) | registry.npmjs.org |
| Versions of Python packages (Django, django CMS) | pypi.org |
| Umbraco | api.nuget.org |
| Shotcut, Spring, OpenWGA | GitHub releases and tags |
| Brave | versions.brave.com (Brave's Release channel; GitHub also lists Nightly and Beta builds) |
| Joomla, Drupal | endoflife.date |
| WordPress, PHP, Linux, GIMP, VLC, LibreOffice, .NET, Symfony, OpenCms | each project's own website or API |
| Shares of all websites and of CMS websites | W3Techs's page for each CMS |
| Modules on drupal.org | drupal.org's API |
| Websites in the world; Drupal's next release | by hand (see `data/numbers.yml`) |

### Adding a number

1. Add an entry to `data/numbers.yml`, with `value`, `label`, `source`, and a `fetch` section (the comment at the top of the file lists the fetch methods). Leave `fetch` out if the number needs a person.
2. Run `.venv/bin/python tools/update_numbers.py <name> --dry-run` to see that it's fetched right.
3. Use it as `{{ name }}` in the article, the deck or the notes.

## Building

```bash
.venv/bin/python tools/build.py           # build build/
.venv/bin/python tools/build.py --check   # fail if build/ is out of date
```

The PDF and the logo aren't in Git. After a fresh clone, get the logo from Reykjavík University, save it as `assets/ru-logo.png`, and run the build. Without the logo, the build warns and leaves that corner of the front page empty. `--check` reports the PDF as out of date until you've built it once.

The build:

- fills every `{{ placeholder }}` from `data/numbers.yml`, and stops on one it doesn't know;
- removes Obsidian comments, `%% like this %%`, from the article (notes to yourself);
- puts the speaker notes from `slides/notes.md` into the deck;
- lays out the article as an A4 PDF, with a front page from `data/cover.yml`, using the fonts that come with macOS (Georgia, Arial and Courier New), embedded in the file;
- writes the deck with fixed timestamps, so building the same input twice gives the same file.

## Editing

- **The article:** edit `manuscript/what-is-open-source.md`, in any Markdown editor.
- **The speaker notes:** edit `slides/notes.md`. Paragraphs are separated by blank lines; a line starting with `- ` is a paragraph of its own. Notes typed into the deck itself are overwritten by the build.
- **The slides:** open `slides/template.pptx` in PowerPoint, Keynote or Google Slides, edit, and save it back as `slides/template.pptx` (from Google Slides: **File** > **Download** > **Microsoft PowerPoint (.pptx)**). Keep the placeholders. Type each one in one go, in one formatting: if the build says a placeholder is "split across runs", the formatting changes halfway through it, so delete it and retype it.

## Getting the deck into Google Slides

Upload `build/what-is-open-source.pptx` to Google Drive, and open it with Google Slides (or, in an existing deck, **File** > **Import slides**). After you update the numbers, upload the new build again. A Google Slides deck can't be rebuilt in place from the template, so to keep one deck and its link, import the updated slides into it and delete the old ones.

## Sources

- The original deck, in Icelandic, on Google Drive: <https://docs.google.com/presentation/d/1AqtqdLWEZplWBDGiOifoMl4mrIFO2t35T53SGMOU5LM/edit>. This project doesn't change it.
- Chapter 2 of the Drupal site-building book, for the licenses and the history.
