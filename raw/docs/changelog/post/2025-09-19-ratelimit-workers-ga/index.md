---
description: Workers Rate Limiting is now Generally Available
title: Rate Limiting in Workers is now GA
image: https://developers.cloudflare.com/changelog/post/2025-09-19-ratelimit-workers-ga/og.png?v=b43a8e23a1ce0264
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 19, 2025

## Rate Limiting in Workers is now GA

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-19-ratelimit-workers-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Rate Limiting within Cloudflare Workers](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) is now Generally Available (GA).

The `ratelimit` binding is now stable and recommended for all production workloads. Existing deployments using the unsafe binding will continue to function to allow for a smooth transition.

For more details, refer to [Workers Rate Limiting](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-19-ratelimit-workers-ga/#page","headline":"Rate Limiting in Workers is now GA","description":"Workers Rate Limiting is now Generally Available","url":"https://developers.cloudflare.com/changelog/post/2025-09-19-ratelimit-workers-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-19-ratelimit-workers-ga/og.png?v=b43a8e23a1ce0264","dateModified":"2025-09-19","datePublished":"2025-09-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
