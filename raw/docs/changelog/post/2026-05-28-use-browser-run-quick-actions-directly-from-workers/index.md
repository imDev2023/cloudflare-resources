---
description: Call Browser Run Quick Actions from your Worker using the new quickAction() binding method, with no API tokens or external HTTP requests required.
title: Use Browser Run Quick Actions directly from Workers
image: https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/og.png?v=e6f645e90fa71717
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2026

## Use Browser Run Quick Actions directly from Workers

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now call [Browser Run Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) directly from a [Cloudflare Worker](https://developers.cloudflare.com/workers/) using the `quickAction()` method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.

With the `quickAction()` method you can:

- [Capture screenshots](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/) from URLs or HTML
- [Generate PDFs](https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/) with custom styling, headers, and footers
- [Extract HTML content](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/) from fully rendered pages
- [Convert pages to Markdown](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/)
- [Extract structured JSON](https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/) using AI
- [Scrape elements](https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/) with CSS selectors
- [Get all links](https://developers.cloudflare.com/browser-run/quick-actions/links-endpoint/) from a page
- [Capture snapshots](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) (HTML + screenshot in one request)

To get started, add a browser binding to your Wrangler configuration:

```jsonc
{
  "compatibility_date": "2026-03-24",
  "browser": {
    "binding": "BROWSER"
  }
}
```

```toml
compatibility_date = "2026-03-24"

[browser]
binding = "BROWSER"
```

Then call any Quick Action directly from your Worker. For example, to capture a screenshot:

```js
const screenshot = await env.BROWSER.quickAction("screenshot", {
	url: "https://www.cloudflare.com/",
});
```

```ts
const screenshot = await env.BROWSER.quickAction("screenshot", {
  url: "https://www.cloudflare.com/",
});
```

The `quickAction()` method requires a compatibility date of `2026-03-24` or later.

For setup instructions and the full list of available actions, refer to [Browser Run Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/#page","headline":"Use Browser Run Quick Actions directly from Workers","description":"Call Browser Run Quick Actions from your Worker using the new quickAction() binding method, with no API tokens or external HTTP requests required.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/og.png?v=e6f645e90fa71717","dateModified":"2026-05-28","datePublished":"2026-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
