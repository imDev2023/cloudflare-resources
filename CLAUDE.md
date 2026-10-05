# Cloudflare knowledge base

This repository is the canonical knowledge base on Cloudflare's developer platform and network products; `README.md` is the index.

## Rules for editing

- `raw/` is scraped source material; refresh it with the scripts in `scripts/`, never hand-edit it.
- The synthesized files (`build/`, `protect-connect/`, and the top-level `*.md`) state only what the sources say, cite source URLs, and flag contradictions between sources instead of picking a side.
- Put each full sentence on its own line, and use plain ASCII hyphens, never em or en dashes.
- Date every snapshot of something that moves (prices, limits, versions, beta or GA status, counts).
- When a refresh changes `raw/`, update the synthesized files that cover the changed pages, and the "Known stale or broken things" list in `README.md`.
- Never commit API keys; the scripts read them from the environment.
