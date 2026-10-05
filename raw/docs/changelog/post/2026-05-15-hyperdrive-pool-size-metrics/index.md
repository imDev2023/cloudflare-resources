---
description: Hyperdrive configurations now export connection pool size metrics via GraphQL and a new dashboard chart.
title: Hyperdrive exposes database connection pool size metrics
image: https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/og.png?v=6c89eac9a3f06627
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 15, 2026

## Hyperdrive exposes database connection pool size metrics

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/), you can see `waitingClients`, `currentPoolSize`, `availablePoolSlots`, and `maxPoolSize` for each of your configurations.

A new **Pool connections** chart has been added to the **Metrics** tab of each Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com). You can use the location selector to drill down into specific locations hosting your connection pool by airport code.

![Hyperdrive pool size metrics chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2604,height=890,format=webp/_astro/hyperdrive-pool-size-metrics-chart.DZxLTFgB.png)

The chart shows:

- **Waiting clients**: Client requests waiting for an available connection.
- **Open connections**: Active connections to your database.
- **Pool size maximum**: Your configured origin connection limit.

Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to [increase your Hyperdrive connection limit](https://developers.cloudflare.com/hyperdrive/platform/limits/#request-a-limit-increase).

#### Pool size metrics

The `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/) exposes the following key connection pool metrics for each Hyperdrive configuration:

Under `avg`:

- **`currentPoolSize`** — Average number of connections currently open in the pool.
- **`availablePoolSlots`** — Average number of pool connections available for checkout.
- **`waitingClients`** — Average number of clients waiting for a connection from the pool.

Under `max`:

- **`maxPoolSize`** — Configured maximum size of the connection pool.
- **`currentPoolSize`** — Peak number of connections open in the pool.
- **`waitingClients`** — Peak number of clients waiting for a connection from the pool.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/hyperdrive/observability/metrics/) and [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/#page","headline":"Hyperdrive exposes database connection pool size metrics","description":"Hyperdrive configurations now export connection pool size metrics via GraphQL and a new dashboard chart.","url":"https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/og.png?v=6c89eac9a3f06627","dateModified":"2026-05-15","datePublished":"2026-05-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
