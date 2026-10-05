---
description: Simplified Python package management in Python Workers using Pywrangler
title: Easy Python package management with Pywrangler
image: https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/og.png?v=6954b3ae0ea21b96
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 8, 2025

## Easy Python package management with Pywrangler

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are introducing a brand new tool called Pywrangler, which simplifies package management in Python Workers by automatically installing Workers-compatible Python packages into your project.

With Pywrangler, you specify your Worker's Python dependencies in your `pyproject.toml` file:

```toml
[project]
name = "python-beautifulsoup-worker"
version = "0.1.0"
description = "A simple Worker using beautifulsoup4"
requires-python = ">=3.12"
dependencies = [
    "beautifulsoup4"
]

[dependency-groups]
dev = [
  "workers-py",
  "workers-runtime-sdk"
]
```

You can then develop and deploy your Worker using the following commands:

```bash
uv run pywrangler dev
uv run pywrangler deploy
```

Pywrangler automatically downloads and vendors the necessary packages for your Worker, and these packages are bundled with the Worker when you deploy.

Consult the [Python packages documentation](https://developers.cloudflare.com/workers/languages/python/packages/) for full details on Pywrangler and Python package management in Workers.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/#page","headline":"Easy Python package management with Pywrangler","description":"Simplified Python package management in Python Workers using Pywrangler","url":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/og.png?v=6954b3ae0ea21b96","dateModified":"2025-12-08","datePublished":"2025-12-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
