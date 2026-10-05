---
description: We've released a new REST API in open beta.
title: New REST API is in open beta!
image: https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/og.png?v=8d6a2f2c607f1596
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 27, 2025

## New REST API is in open beta!

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've released a new REST API for [Browser Rendering](https://developers.cloudflare.com/browser-run/) in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.

With the **REST API** you can:

- **Capture screenshots** – Use `/screenshot` to take a screenshot of a webpage from provided URL or HTML.
- **Generate PDFs** – Use `/pdf` to convert web pages into PDFs.
- **Extract HTML content** – Use `/content` to retrieve the full HTML from a page. **Snapshot (HTML + Screenshot)** – Use `/snapshot` to capture both the page's HTML and a screenshot in one request
- **Scrape Web Elements** – Use `/scrape` to extract specific elements from a page.

For example, to capture a screenshot:

*Screenshot examplebash*

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/screenshot' \
  -H 'Authorization: Bearer <apiToken>' \
  -H 'Content-Type: application/json' \
  -d '{
    "html": "Hello World!",
    "screenshotOptions": {
      "type": "webp",
      "omitBackground": true
    }
  }' \
  --output "screenshot.webp"
```

Learn more in our [documentation](https://developers.cloudflare.com/browser-run/quick-actions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/#page","headline":"New REST API is in open beta!","description":"We've released a new REST API in open beta.","url":"https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/og.png?v=8d6a2f2c607f1596","dateModified":"2025-02-27","datePublished":"2025-02-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
