---
description: Debug and monitor your private network connections with per-service metrics, error breakdowns, and latency tracking.
title: Observability for Workers VPC Services
image: https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/og.png?v=92269284ded91aca
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 20, 2026

## Observability for Workers VPC Services

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Each VPC Service now has a **Metrics** tab so you can monitor connection health and debug failures without leaving the dashboard.

![Workers VPC Metrics dashboard showing connections, latency, and errors charts](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3336,height=3204,format=webp/_astro/2026-03-20-metrics-dashboard.6kfnbqQd.png)

- **Connections** — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).
- **Latency** — Track connection and DNS resolution latency trends.
- **Errors** — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.

You can also view and edit your VPC Service configuration, host details, and port assignments from the **Settings** tab.

For a full list of error codes and what they mean, refer to [Troubleshooting](https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/#page","headline":"Observability for Workers VPC Services","description":"Debug and monitor your private network connections with per-service metrics, error breakdowns, and latency tracking.","url":"https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/og.png?v=92269284ded91aca","dateModified":"2026-03-20","datePublished":"2026-03-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
