---
description: Gain instant visibility into Workers execution with automatic tracing and OpenTelemetry exports
title: Workers automatic tracing, now in open beta
image: https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/og.png?v=a7362fcadc2be41b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 7, 2025

## Workers automatic tracing, now in open beta

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enable automatic tracing on your Workers, giving you detailed metadata and timing information for every operation your Worker performs.

![Tracing example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1920,height=1080,format=webp/_astro/R2_Screenshot.DAnOidMq.png)

Tracing helps you identify performance bottlenecks, resolve errors, and understand how your Worker interacts with other services on the Workers platform. You can now answer questions like:

- Which calls are slowing down my application?
- Which queries to my database take the longest?
- What happened within a request that resulted in an error?

**You can now:**

- View traces alongside your logs in the Workers Observability dashboard
- Export traces (and correlated logs) to any [OTLP-compatible destination ↗︎](https://opentelemetry.io/docs/specs/otel/protocol/), such as [Honeycomb](https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/), [Sentry](https://developers.cloudflare.com/observability/export/opentelemetry/sentry/), or [Grafana](https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/), by configuring a tracing destination in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/destinations)
- Analyze and query across span attributes (operation type, status, duration, errors)

#### To get started, set:

```jsonc
{
	"observability": {
		"traces": {
			"enabled": true,
		},
	},
}
```

Note

In the future, Cloudflare plans to enable automatic tracing in addition to logs when you set `observability.enabled = true` in your Wrangler configuration.

While automatic tracing is in early beta, this setting will not enable tracing by default, and will only enable logs.

An updated [`compatibility_date`](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) will be required for this change to take effect.

#### Want to learn more?

- [Read the announcement ↗︎](https://blog.cloudflare.com/workers-tracing-now-in-open-beta/)
- [Check out the documentation](https://developers.cloudflare.com/workers/observability/traces/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/#page","headline":"Workers automatic tracing, now in open beta","description":"Gain instant visibility into Workers execution with automatic tracing and OpenTelemetry exports","url":"https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/og.png?v=a7362fcadc2be41b","dateModified":"2025-11-07","datePublished":"2025-11-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
