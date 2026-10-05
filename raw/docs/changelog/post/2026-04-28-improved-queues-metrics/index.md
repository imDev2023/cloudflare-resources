---
description: Cloudflare Queues metrics now include realtime backlog size (in count &amp; bytes) and oldest message timestamp
title: Realtime backlog metrics now available for Queues
image: https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/og.png?v=041711224ffeddd8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 28, 2026

## Realtime backlog metrics now available for Queues

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Queues](https://developers.cloudflare.com/queues/), Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:

- **`backlog_count`** — the number of unacknowledged messages in the queue
- **`backlog_bytes`** — the total size of those messages in bytes
- **`oldest_message_timestamp_ms`** — the timestamp of the oldest unacknowledged message

The following endpoints also now include a `metadata.metrics` object on the result field after successful message consumption:

- `/accounts/{account_id}/queues/{queue_id}/messages/pull`
- `/accounts/{account_id}/queues/{queue_id}/messages`
- `/accounts/{account_id}/queues/{queue_id}/messages/batch`

#### Javascript APIs

Call `env.QUEUE.metrics()` to get realtime backlog metrics:

```ts
const {
	backlogCount, // number
	backlogBytes, // number
	oldestMessageTimestamp, // Date | undefined
} = await env.QUEUE.metrics();
```

`env.QUEUE.send()` and `env.QUEUE.sendBatch()` also now return a metrics object on the response.

You can also query these fields via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) or view realtime backlog on the [dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/queues).

![Queues realtime backlog](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1402,height=494,format=webp/_astro/2026-04-28-queues-metrics.BYi0hgrD.png)

For more information, refer to [Queues metrics](https://developers.cloudflare.com/queues/observability/metrics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/#page","headline":"Realtime backlog metrics now available for Queues","description":"Cloudflare Queues metrics now include realtime backlog size (in count & bytes) and oldest message timestamp","url":"https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/og.png?v=041711224ffeddd8","dateModified":"2026-04-28","datePublished":"2026-04-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
