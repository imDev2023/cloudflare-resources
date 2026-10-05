---
description: Pywrangler, the CLI tool for managing Python Workers and packages, now runs natively on Windows.
title: Better Windows support for Python Workers
image: https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/og.png?v=ea06c2bba70403b5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 25, 2026

## Better Windows support for Python Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Pywrangler ↗︎](https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler), the CLI tool for managing Python Workers and packages, now supports Windows, allowing you to develop and deploy Python Workers from Windows environments. Previously, Pywrangler was only available on macOS and Linux.

You can install and use Pywrangler on Windows the same way you would on other platforms. [Specify your Worker's Python dependencies](https://developers.cloudflare.com/workers/languages/python/packages/) in your `pyproject.toml` file, then use the following commands to develop and deploy:

```bash
uvx --from workers-py pywrangler dev
uvx --from workers-py pywrangler deploy
```

All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.

#### Requirements

This feature requires the following minimum versions:

- `wrangler` >= 4.64.0
- `workers-py` >= 1.72.0
- `uv` >= 0.9.28

To upgrade `workers-py` (which includes Pywrangler) in your project, run:

```bash
uv tool upgrade workers-py
```

To upgrade `wrangler`, run:

```bash
npm install -g wrangler@latest
```

To upgrade `uv`, run:

```bash
uv self update
```

To get started with Python Workers on Windows, refer to the [Python packages documentation](https://developers.cloudflare.com/workers/languages/python/packages/) for full details on Pywrangler.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/#page","headline":"Better Windows support for Python Workers","description":"Pywrangler, the CLI tool for managing Python Workers and packages, now runs natively on Windows.","url":"https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/og.png?v=ea06c2bba70403b5","dateModified":"2026-02-25","datePublished":"2026-02-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
