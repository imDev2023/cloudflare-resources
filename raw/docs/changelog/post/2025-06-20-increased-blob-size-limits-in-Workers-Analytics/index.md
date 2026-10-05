---
description: We’ve increased the total allowed size of blob fields per request from 5 KB to 16 KB in the Workers Analytics Engine.
title: Increased blob size limits in Workers Analytics Engine
image: https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/og.png?v=73ef8700bd960e4b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 20, 2025

## Increased blob size limits in Workers Analytics Engine

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve increased the total allowed size of [`blob`](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker) fields on data points written to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) from **5 KB to 16 KB**.

This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.

You can find full details on limits for queries, filters, payloads, and more [here in the Workers Analytics Engine limits documentation](https://developers.cloudflare.com/analytics/analytics-engine/limits/).

```js
export default {
	async fetch(request, env) {
		env.analyticsDataset.writeDataPoint({
			// The sum of all of the blob's sizes can now be 16 KB
			blobs: [
				// The URL of the request to the Worker
				request.url,
				// Some metadata about your application you'd like to store
				JSON.stringify(metadata),
				// The version of your Worker this datapoint was collected from
				env.versionMetadata.tag,
			],
			indexes: ["sample-index"],
		});
	},
};
```

*worker.tsts*

```ts
export default {
	async fetch(request, env) {
		env.analyticsDataset.writeDataPoint({
			// The sum of all of the blob's sizes can now be 16 KB
			blobs: [
				// The URL of the request to the Worker
				request.url,
				// Some metadata about your application you'd like to store
				JSON.stringify(metadata),
				// The version of your Worker this datapoint was collected from
				env.versionMetadata.tag,
			],
			indexes: ["sample-index"],
		});
	}
};
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/#page","headline":"Increased blob size limits in Workers Analytics Engine","description":"We’ve increased the total allowed size of blob fields per request from 5 KB to 16 KB in the Workers Analytics Engine.","url":"https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/og.png?v=73ef8700bd960e4b","dateModified":"2025-06-20","datePublished":"2025-06-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
