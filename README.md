# thefatalfive.com

Static site for **The Fatal Five**, Jeff Bourke's book and author platform.

## Live

- Production: https://thefatalfive.com (also www.thefatalfive.com)
- Deployed via Vercel, connected to this repo's `main` branch. Pushing to `main` redeploys production automatically.

## Structure

Plain HTML/CSS, no build tooling required to serve — every page is a static file.

```
index.html              Homepage (hero, framework, evidence, book, about, field notes, assessment, speaking)
assessment/index.html   Full 25-question Fatal Five Assessment (self-contained, do not rebuild)
drift-check/index.html  4-question quick Drift Check, embedded via iframe on the homepage (self-contained, do not rebuild)
corpus/index.html       The 65-case research corpus, published as a reference table
field-notes/            Field Notes index + individual case-file articles
assets/                 Images, shared stylesheet (assets/css/style.css)
build/                  Python scripts that generate index.html, corpus/index.html, and the field-notes pages.
                         Edit these and re-run (python3 build_index.py etc. from the build/ directory) rather than
                         hand-editing the generated HTML, so content stays consistent site-wide.
```

## Content rules (do not violate)

- **Only these figures may appear anywhere on the site:** 65 disasters, 175 years (1849–2024), 190,000+ lives.
  No percentages (96%/88%/80%/76%/72%, etc.) outside the Corpus page, and only there once the formal
  dual-coder pattern-coding protocol is complete and the figures are labeled "preliminary."
- Book title is **The Fatal Five** (subtitle: *The Warning Signs Behind Every Disaster — and How to Read Them
  Before Yours*) — not "Beyond the Wreckage" (the old working title).
- No photographs of real disasters anywhere on the site.
- The assessment (`/assessment`) and drift check (`/drift-check`) are finished, self-contained tools — don't
  rebuild or restyle them; if content changes, edit them directly.

## Local development

```bash
python3 -m http.server 8080
# visit http://localhost:8080
```

## Regenerating a page

```bash
cd build
python3 build_index.py       # regenerates index.html
python3 build_corpus.py      # regenerates corpus/index.html from the case CSV
python3 build_field_notes.py # regenerates field-notes/index.html + article pages
```
