---
description: HTTP and NetFlows traffic charts on Cloudflare Radar now show daily data for 1-3 month views and weekly data for 6+ month views, replacing the previous coarser defaults.
title: Finer-grained chart granularity on Cloudflare Radar for longer time ranges
image: https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/og.png?v=852292f1814af26a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 5, 2026

## Finer-grained chart granularity on Cloudflare Radar for longer time ranges

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now provides finer-grained traffic charts for longer time ranges. Previously, selecting a 1-3 month view on HTTP and NetFlows charts defaulted to weekly aggregation, which was too coarse to surface meaningful trends. Views longer than 3 months defaulted to monthly aggregation, returning as few as 7 data points for a 6-month range.

The new defaults are:

- **1-3 months**: daily granularity (7x more data points)
- **Longer than 3 months** (HTTP and NetFlows): weekly granularity (4x more data points)

For example, a 12-week traffic view previously showed weekly data:

![Traffic trends chart with weekly granularity for a 12-week view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/traffic-granularity-12w-before.OlJmS6Ts.png)

The same view now shows daily data:

![Traffic trends chart with daily granularity for a 12-week view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/traffic-granularity-12w-after.DL8mxwQ3.png)

Similarly, a 1-year HTTP traffic view that previously showed just 12 monthly data points now provides 52 weekly data points.

Visit [Cloudflare Radar ↗︎](https://radar.cloudflare.com/?dateRange=12w#traffic-trends) to explore the new granular views.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/#page","headline":"Finer-grained chart granularity on Cloudflare Radar for longer time ranges","description":"HTTP and NetFlows traffic charts on Cloudflare Radar now show daily data for 1-3 month views and weekly data for 6+ month views, replacing the previous coarser defaults.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/og.png?v=852292f1814af26a","dateModified":"2026-06-05","datePublished":"2026-06-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
