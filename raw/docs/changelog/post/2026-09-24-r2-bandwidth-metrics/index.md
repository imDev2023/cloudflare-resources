---
description: View upload and download bandwidth usage across your buckets.
title: R2 bandwidth usage metrics
image: https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/og.png?v=25f07c150f749b19
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 24, 2026

## R2 bandwidth usage metrics

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

New [R2](https://developers.cloudflare.com/r2/) product-level **Metrics** page in the Cloudflare dashboard shows bandwidth usage. You can view usage across all buckets or per bucket.

[Go to **R2 Metrics** ↗](https://dash.cloudflare.com/?to=/:account/r2/metrics) ![R2 upload and download throughput across all buckets over 24 hours](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1443,height=747,format=webp/_astro/r2-bandwidth-metrics.9lTC-zY2.png)

Bandwidth throughput is split by object upload and download. The [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) exposes the same bandwidth usage metrics that power the dashboard for your queries and analytics.

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/#page","headline":"R2 bandwidth usage metrics","description":"View upload and download bandwidth usage across your buckets.","url":"https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/og.png?v=25f07c150f749b19","dateModified":"2026-09-24","datePublished":"2026-09-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
