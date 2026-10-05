---
description: A new cfWorker timing metric helps isolate Worker execution time from origin latency in the Server-Timing header.
title: New cfWorker metric in Server-Timing header
image: https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/og.png?v=6a6ea5f3ac43c582
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 18, 2026

## New cfWorker metric in Server-Timing header

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Server-Timing header now includes a new `cfWorker` metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.

Previously, Worker execution time was included in the `edge` metric, making it harder to identify true edge performance. The new `cfWorker` metric provides this visibility:

| Metric | Description |
| --- | --- |
| `edge` | Total time spent on the Cloudflare edge, including Worker execution |
| `origin` | Time spent fetching from the origin server |
| `cfWorker` | Time spent in Worker execution, including subrequests but excluding origin fetch time |

#### Example response

```txt
Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7
```

In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.

#### Availability

The `cfWorker` metric is enabled by default if you have [Real User Monitoring (RUM)](https://developers.cloudflare.com/web-analytics/) enabled. Otherwise, you can enable it using [Rules](https://developers.cloudflare.com/rules/).

This metric is particularly useful for:

- **Performance debugging**: Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.
- **Optimization targeting**: Identify which component of your request path needs optimization.
- **Real User Monitoring (RUM)**: Access detailed timing breakdowns directly from response headers for client-side analytics.

For more information about Server-Timing headers, refer to the [W3C Server Timing specification ↗︎](https://www.w3.org/TR/server-timing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/#page","headline":"New cfWorker metric in Server-Timing header","description":"A new cfWorker timing metric helps isolate Worker execution time from origin latency in the Server-Timing header.","url":"https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/og.png?v=6a6ea5f3ac43c582","dateModified":"2026-02-18","datePublished":"2026-02-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
