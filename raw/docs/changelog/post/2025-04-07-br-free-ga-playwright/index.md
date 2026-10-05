---
description: Browser Rendering updates - free tier and REST API GA with new endpoints
title: Browser Rendering REST API is Generally Available, with new endpoints and a free tier
image: https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/og.png?v=571cce1e57e80053
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## Browser Rendering REST API is Generally Available, with new endpoints and a free tier

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’re excited to announce Browser Rendering is now available on the [Workers Free plan ↗︎](https://www.cloudflare.com/plans/developer-platform/), making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.

The Browser Rendering **[REST API](https://developers.cloudflare.com/browser-run/quick-actions/) is now Generally Available**, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:

- **Extract structured data** – Use `/json` to retrieve structured data from a webpage.
- **Retrieve links** – Use `/links` to pull all links from a webpage.
- **Convert to Markdown** – Use `/markdown` to convert webpage content into Markdown format.

For example, to fetch the Markdown representation of a webpage:

*Markdown examplebash*

```bash
curl -X 'POST' 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/markdown' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <apiToken>' \
  -d '{
    "url": "https://example.com"
  }'
```

For the full list of endpoints, check out our [REST API documentation](https://developers.cloudflare.com/browser-run/quick-actions/). You can also interact with Browser Rendering via the [Cloudflare TypeScript SDK ↗︎](https://github.com/cloudflare/cloudflare-typescript).

We also recently landed support for [Playwright](https://developers.cloudflare.com/browser-run/playwright/) in Browser Rendering for browser automation from Cloudflare [Workers](https://developers.cloudflare.com/workers/), in addition to [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/), giving you more flexibility to test across different browser environments.

Visit the [Browser Rendering docs](https://developers.cloudflare.com/browser-run/) to learn more about how to use headless browsers in your applications.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/#page","headline":"Browser Rendering REST API is Generally Available, with new endpoints and a free tier","description":"Browser Rendering updates - free tier and REST API GA with new endpoints","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/og.png?v=571cce1e57e80053","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
