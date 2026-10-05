---
description: Filter the Durable Objects metrics charts to a single object by its ID or name.
title: Filter Durable Objects metrics by object ID or name
image: https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/og.png?v=de9fb566e87c210f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 12, 2026

## Filter Durable Objects metrics by object ID or name

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now filter the **Metrics** tab for a Durable Objects namespace by an individual Durable Object's [ID](https://developers.cloudflare.com/durable-objects/api/id/) or [name](https://developers.cloudflare.com/durable-objects/api/id/#name) in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.

[Go to **Durable Objects** ↗](https://dash.cloudflare.com/?to=/:account/workers/durable-objects) ![The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2936,height=1482,format=webp/_astro/durable-objects-metrics-dashboard.BFZTyhWU.png)

Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.

Metrics are powered by the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/), so standard analytics behavior such as ingestion delay and [sampling](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/) applies.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/#page","headline":"Filter Durable Objects metrics by object ID or name","description":"Filter the Durable Objects metrics charts to a single object by its ID or name.","url":"https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/og.png?v=de9fb566e87c210f","dateModified":"2026-06-12","datePublished":"2026-06-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
