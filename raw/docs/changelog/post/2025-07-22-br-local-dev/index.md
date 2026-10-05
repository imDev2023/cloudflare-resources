---
description: You can now use local development with Browser Rendering
title: Browser Rendering now supports local development
image: https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/og.png?v=34e83c53c0207ae5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 22, 2025

## Browser Rendering now supports local development

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run your Browser Rendering locally using `npx wrangler dev`, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.

Get started with this [example guide](https://developers.cloudflare.com/browser-run/how-to/deploy-worker/) that shows how to use Cloudflare's [fork of Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/) (you can also use [Playwright](https://developers.cloudflare.com/browser-run/playwright/)) to take screenshots of webpages and store the results in [Workers KV](https://developers.cloudflare.com/kv/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/#page","headline":"Browser Rendering now supports local development","description":"You can now use local development with Browser Rendering","url":"https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/og.png?v=34e83c53c0207ae5","dateModified":"2025-07-22","datePublished":"2025-07-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
