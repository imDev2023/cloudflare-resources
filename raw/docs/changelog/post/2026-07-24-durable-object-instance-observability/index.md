---
description: Correlate telemetry for specific Durable Object instances.
title: Filter Durable Object logs and traces by instance ID
image: https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/og.png?v=02b07c4a5397aa72
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 24, 2026

## Filter Durable Object logs and traces by instance ID

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) and [OpenTelemetry](https://developers.cloudflare.com/observability/export/opentelemetry/) spans for [Durable Object](https://developers.cloudflare.com/durable-objects/) requests include the Durable Object instance ID.

Use `$workers.durableObjectId` to filter logs for a specific instance. Root and child spans include the same ID in `cloudflare.durable_object.id`.

![Query Builder filtering traces by Durable Object instance ID](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2000,height=666,format=webp/_astro/2026-07-24-durable-object-trace-filter.DW-BwlKL.png)

Use these fields to isolate a specific instance and correlate its logs and traces.

For more information, refer to [Durable Objects metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/) and [Workers tracing spans and attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/#page","headline":"Filter Durable Object logs and traces by instance ID","description":"Correlate telemetry for specific Durable Object instances.","url":"https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/og.png?v=02b07c4a5397aa72","dateModified":"2026-07-24","datePublished":"2026-07-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
