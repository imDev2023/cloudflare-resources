---
description: Hyperdrive now caches queries in all Cloudflare locations decreasing cache hit latency by up to 90%
title: Up to 10x faster cached queries for Hyperdrive
image: https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/og.png?v=09583412ce099426
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 11, 2024

## Up to 10x faster cached queries for Hyperdrive

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.

When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.

This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.

![Hyperdrive edge caching improves average session duration for database queries](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1746,height=734,format=webp/_astro/hyperdrive-edge-caching-metrics.BR7svphB.png)

*P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.*

This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.

For more details on how Hyperdrive performs query caching, refer to the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/#page","headline":"Up to 10x faster cached queries for Hyperdrive","description":"Hyperdrive now caches queries in all Cloudflare locations decreasing cache hit latency by up to 90%","url":"https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/og.png?v=09583412ce099426","dateModified":"2024-12-11","datePublished":"2024-12-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
