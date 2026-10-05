---
description: D1's Worker API request latency decreases by 40-60%.
title: 40-60% Faster D1 Worker API Requests
image: https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/og.png?v=a9e9106f28f8fe68
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 7, 2025

## 40-60% Faster D1 Worker API Requests

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Users making [D1](https://developers.cloudflare.com/d1/) requests via the [Workers API](https://developers.cloudflare.com/d1/worker-api/) can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.

![D1 Worker API latency](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4437,height=1754,format=webp/_astro/faster-d1-worker-api.4S7VSUdP.png)

*p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement.*

This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 [location hints](https://developers.cloudflare.com/d1/configuration/data-location/#provide-a-location-hint) can be used to influence the geographic location of a database.

For more details on how D1 removed redundant round trips, see the D1 specific release note [entry](https://developers.cloudflare.com/d1/platform/release-notes/#2025-01-07).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/#page","headline":"40-60% Faster D1 Worker API Requests","description":"D1's Worker API request latency decreases by 40-60%.","url":"https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/og.png?v=a9e9106f28f8fe68","dateModified":"2025-01-07","datePublished":"2025-01-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
