---
description: Custom Dashboards can now chart Workers Observability logs and traces alongside analytics and Log Explorer data.
title: Workers Observability logs and traces in Custom Dashboards
image: https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/og.png?v=751d0508f8ec4ac2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## Workers Observability logs and traces in Custom Dashboards

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now build Custom Dashboards charts from Workers Observability data. Two new datasets, **Workers Observability — Logs** and **Workers Observability — Traces (OTel)**, let you chart Worker invocations, log levels, errors, CPU and wall time, span counts, and durations next to HTTP traffic, security events, and other analytics datasets.

This gives you one dashboard for an application that spans Cloudflare's network and your Workers. For example, you can put request volume, WAF blocks, and Worker error rates on the same view, filter all three by time range, and spot whether a spike in errors lines up with a change in traffic.

The datasets are available for every Worker in your account that has [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) turned on. Custom Dashboards also now allow up to 100 dashboards for every account.

To get started, refer to [Workers Observability data in Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/#workers-observability-data).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/#page","headline":"Workers Observability logs and traces in Custom Dashboards","description":"Custom Dashboards can now chart Workers Observability logs and traces alongside analytics and Log Explorer data.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/og.png?v=751d0508f8ec4ac2","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
