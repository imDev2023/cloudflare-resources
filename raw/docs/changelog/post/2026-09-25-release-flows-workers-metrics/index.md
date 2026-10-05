---
description: Workers Metrics charts now show all releases in the selected time range, including each traffic allocation change in a gradual deployment.
title: See every release and gradual deployment on Workers Metrics charts
image: https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/og.png?v=95cfd14864de56a2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2026

## See every release and gradual deployment on Workers Metrics charts

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/) charts now show every release in the selected time range, including the full progression of [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/). This makes it easier to correlate changes in memory, CPU time, errors, or latency with the code that was serving traffic.

![Memory usage chart showing a gradual deployment as a shaded rollout band](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-memory-usage.C5rkO7VY.png)

A gradual deployment appears as a single rollout across the chart, with shading that increases as more traffic moves to the new version. Hover over a rollout to see the previous and new versions, the rollout duration, and the traffic percentage configured at each step.

![Invocations chart showing traffic shifting from the previous version to the new version during a gradual deployment](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-invocations.BvQMAKnw.png)

Use these annotations to:

- **Find when a regression started** — See which traffic percentage was configured when errors, latency, CPU time, or wall time changed.
- **Compare rollout stages** — Check whether a metric changed as more traffic moved to the new version.
- **Confirm rollbacks** — Rollbacks appear as separate release events, so you can check whether metrics recovered after a rollback.

Direct deployments that send 100% of traffic to a single version still appear as individual markers. Nearby direct deployments are grouped to reduce visual clutter. Versions that are only uploaded, or only configured at 0%, do not appear on metrics charts.

To view release annotations, open the **Metrics** tab for your [Worker ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/#page","headline":"See every release and gradual deployment on Workers Metrics charts","description":"Workers Metrics charts now show all releases in the selected time range, including each traffic allocation change in a gradual deployment.","url":"https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/og.png?v=95cfd14864de56a2","dateModified":"2026-09-25","datePublished":"2026-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
