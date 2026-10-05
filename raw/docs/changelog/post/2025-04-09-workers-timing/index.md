---
description: Workers Observability tooling now shows CPU time and Wall time for a Workers Invocation.
title: CPU time and Wall time now published for Workers Invocations
image: https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/og.png?v=2df9acc045922ceb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 9, 2025

## CPU time and Wall time now published for Workers Invocations

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now observe and investigate the CPU time and Wall time for every Workers Invocations.

- For [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs), CPU time and Wall time are surfaced in the [Invocation Log](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)..
- For [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers), CPU time and Wall time are surfaced at the top level of the [Workers Trace Events object](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events).
- For [Workers Logpush](https://developers.cloudflare.com/workers/observability/logs/logpush), CPU and Wall time are surfaced at the top level of the [Workers Trace Events object](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events). All new jobs will have these new fields included by default. Existing jobs need to be updated to include CPU time and Wall time.

You can use a Workers Logs filter to search for logs where Wall time exceeds 100ms.

![Workers Logs Wall Time Filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=652,height=436,format=webp/_astro/2025-04-09-wall-time-filter.CT-VQyTS.png)

You can also use the Workers Observability [Query Builder ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/investigate) to find the median CPU time and median Wall time for all of your Workers.

![Query Builder filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2650,height=1318,format=webp/_astro/2025-04-09-query-builder.CaW9IZza.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/#page","headline":"CPU time and Wall time now published for Workers Invocations","description":"Workers Observability tooling now shows CPU time and Wall time for a Workers Invocation.","url":"https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/og.png?v=2df9acc045922ceb","dateModified":"2025-04-09","datePublished":"2025-04-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
