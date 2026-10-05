---
description: Generic Global Tiered Cache now hashes content within a region's data centers to reduce duplication and increase cache efficiency.
title: Regionalized Generic Tiered Cache for higher hit ratios
image: https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/og.png?v=52a3538d4f253a8e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 19, 2024

## Regionalized Generic Tiered Cache for higher hit ratios

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now achieve higher cache hit ratios with [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache). Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.

#### How it works

Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:

- Same content always routes to the same upper-tier data center within a region.
- Eliminates redundant copies across multiple upper-tier caches.
- Increases the likelihood of cache HITs for the same content.

#### Example

A popular image requested from multiple edge locations in a region:

- **Before**: Cached at 3-4 different upper-tier data centers
- **After**: Cached at 1 designated upper-tier data center
- **Result**: 3-4x fewer cache MISSes, reducing origin load and improving performance

#### Get started

To get started, enable [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache) on your zone.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/#page","headline":"Regionalized Generic Tiered Cache for higher hit ratios","description":"Generic Global Tiered Cache now hashes content within a region's data centers to reduce duplication and increase cache efficiency.","url":"https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/og.png?v=52a3538d4f253a8e","dateModified":"2024-07-19","datePublished":"2024-07-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
