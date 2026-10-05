---
description: Durable Objects now supports two new location hints for Northeast and Southeast Asia-Pacific, giving you finer-grained control within the `apac` region.
title: "New Asia-Pacific location hints: apac-ne and apac-se"
image: https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/og.png?v=21b7ecc7ecb7005d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2026

## New Asia-Pacific location hints: apac-ne and apac-se

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects now supports two new location hints for Asia-Pacific: `apac-ne` (Northeast Asia-Pacific) and `apac-se` (Southeast Asia-Pacific). Use `apac-ne` or `apac-se` when you want finer-grained placement within Asia-Pacific rather than the broader `apac` hint.

Use the new hints the same way as any other `locationHint`:

```js
// Northeast Asia-Pacific (Japan, Korea, etc.)
const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: "apac-ne" });

// Southeast Asia-Pacific (Singapore, Indonesia, etc.)
const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: "apac-se" });
```

If your users are spread across all of Asia-Pacific, the existing `apac` hint remains the right choice. Only reach for `apac-ne` or `apac-se` when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.

As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.

For the full list of supported hints, refer to [Data location — Provide a location hint](https://developers.cloudflare.com/durable-objects/reference/data-location/#provide-a-location-hint).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/#page","headline":"New Asia-Pacific location hints: apac-ne and apac-se","description":"Durable Objects now supports two new location hints for Northeast and Southeast Asia-Pacific, giving you finer-grained control within the apac region.","url":"https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/og.png?v=21b7ecc7ecb7005d","dateModified":"2026-06-19","datePublished":"2026-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
