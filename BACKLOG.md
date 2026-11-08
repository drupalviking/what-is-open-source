# Backlog

## To do

- **Slide 9: link the source.** The quote is from the Icelandic Government Offices' (Stjórnarráð Íslands) website; the notes name it, but there's no link yet. (The translation is checked.)
- **Visual check of the built deck.** Not done yet: no renderer was available when the deck was built (Keynote hung on a dialog). Open `build/what-is-open-source.pptx`, and check slides 10, 13 and 15, where the tables have new text. The cells were shortened to keep their original line counts, but that's an estimate.
- **Upload the deck to Google Slides**, next to the original Icelandic deck.
- **Drupal 12.** When it's released (planned for the week of 7 December 2026), empty `drupal_next` in `data/numbers.yml`, and change the Drupal cell on slide 13 (and the table in the article) from `{{ drupal }} ({{ drupal_next }})` to `{{ drupal }}`. endoflife.date will then report 12.0.x.
- **A fetchable source for the number of websites.** `websites_total` is from Forbes (February 2023), and has to be checked by hand. Netcraft's monthly Web Server Survey would be a current, citable source.
- **Slide 15 has no source line.** Add one (the projects' own release pages), like slides 10 and 13.
- **Version control.** This folder isn't a Git repository yet. Decide whether it gets its own repository, or moves into the book's teachers' kit (`slides/` in the book's repository), where the Preface says the teachers' kit lives.
- **A license line on the title slide**, "CC BY-SA 4.0", if you want the deck to carry it too (the article and the README do).
- **The validator.** The pptx skill's `validate.py` needs Python 3.10 or later, and this machine has 3.9, so the built deck hasn't been schema-validated. The build opens and saves it with python-pptx, which catches most structural problems.

## Ideas

- Run `tools/update_numbers.py` on a schedule (a monthly GitHub Action, once this is in Git), and open a pull request when numbers change.
- An Icelandic build from the same numbers: an Icelandic `notes.md` and template, so the Icelandic course gets updated numbers too.
- A Spanish version, to match the book.
- Slides for the deeper topics the article has and the deck doesn't: the grey zone (open core, source-available and the forks it caused), Heartbleed, Log4Shell and the xz backdoor, and the .NET and React license stories.
- A slide comparing free software and open source side by side (the four freedoms next to the ten points), since students mix them up.
