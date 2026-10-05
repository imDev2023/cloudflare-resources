---
description: Load balancing analytics now graphs traffic served by the fallback pool as its own series, so you can tell health-based routing apart from last-resort routing.
title: See fallback pool traffic separately in load balancing analytics
image: https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/og.png?v=a2bc16d1195fc2bc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## See fallback pool traffic separately in load balancing analytics

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Load balancing analytics now shows traffic served by your [fallback pool](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#fallback-pools) separately from traffic routed to the same pool by normal steering.

Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.

Fallback traffic is now labeled with the pool name followed by `(Fallback)`. A pool named `eu-west`, for example, is shown as `eu-west (Fallback)`. This label appears as its own entry in:

- **Requests over time**, as a separate series in the chart.
- **Pool distribution**, as a separate segment.
- **Top endpoints**, as a separate card for the pool.

The **Latency** view and the health event **Logs** are unchanged.

To see this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same breakdown appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

Refer to [load balancing analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to learn more.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/#page","headline":"See fallback pool traffic separately in load balancing analytics","description":"Load balancing analytics now graphs traffic served by the fallback pool as its own series, so you can tell health-based routing apart from last-resort routing.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/og.png?v=a2bc16d1195fc2bc","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
