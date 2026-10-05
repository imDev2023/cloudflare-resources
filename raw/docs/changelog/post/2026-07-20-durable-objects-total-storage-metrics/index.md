---
description: Track total SQLite storage usage over time for a Durable Object namespace in the Cloudflare dashboard.
title: View total SQLite storage for Durable Object namespaces
image: https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/og.png?v=ff04a60c33f84d76
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 20, 2026

## View total SQLite storage for Durable Object namespaces

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new **Total storage** chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.

![The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1436,height=846,format=webp/_astro/durable-objects-total-storage.Cr_F72Yz.png) [Go to **Durable Objects** ↗](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/#total-storage).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/#page","headline":"View total SQLite storage for Durable Object namespaces","description":"Track total SQLite storage usage over time for a Durable Object namespace in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/og.png?v=ff04a60c33f84d76","dateModified":"2026-07-20","datePublished":"2026-07-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
