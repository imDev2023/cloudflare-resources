---
description: The Browser Rendering REST API rate limit has been increased from 3 to 10 requests per second for Workers Paid plans.
title: "Browser Rendering: 3x higher REST API request rate"
image: https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/og.png?v=e1e9f9dfe73f6f00
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 4, 2026

## Browser Rendering: 3x higher REST API request rate

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Rendering](https://developers.cloudflare.com/browser-run/) REST API rate limits for Workers Paid plans have been increased from 3 requests per second (180/min) to **10 requests per second (600/min)**. No action is needed to benefit from the higher limit.

![Browser Rendering REST API rate limit increased from 3 to 10 requests per second](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=916,height=85,format=webp/_astro/rest-api-limit-increase.DJHY7xYF.png)

The [REST API](https://developers.cloudflare.com/browser-run/quick-actions/) lets you perform common browser tasks with a single API call, and you can now do it at a higher rate.

- [/content - Fetch HTML](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/)
- [/screenshot - Capture screenshot](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/)
- [/pdf - Render PDF](https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/)
- [/markdown - Extract Markdown from a webpage](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/)
- [/snapshot - Take a webpage snapshot](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/)
- [/scrape - Scrape HTML elements](https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/)
- [/json - Capture structured data using AI](https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/)
- [/links - Retrieve links from a webpage](https://developers.cloudflare.com/browser-run/quick-actions/links-endpoint/)

If you use the [Browser Sessions](https://developers.cloudflare.com/browser-run/#integration-methods) method, increases to concurrent browser and new browser limits are coming soon. Stay tuned.

For full details, refer to the [Browser Rendering limits page](https://developers.cloudflare.com/browser-run/limits/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/#page","headline":"Browser Rendering: 3x higher REST API request rate","description":"The Browser Rendering REST API rate limit has been increased from 3 to 10 requests per second for Workers Paid plans.","url":"https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/og.png?v=e1e9f9dfe73f6f00","dateModified":"2026-03-04","datePublished":"2026-03-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
