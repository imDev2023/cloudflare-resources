---
description: Read the jurisdiction of a Durable Object from within the object itself.
title: Access Durable Object jurisdiction via `ctx.id.jurisdiction`
image: https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/og.png?v=c6ad0134933c9f86
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 26, 2026

## Access Durable Object jurisdiction via \`ctx.id.jurisdiction\`

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`ctx.id.jurisdiction` inside a Durable Object now reports the [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction) the object was created in — for example `"eu"` when accessed through `env.MY_DURABLE_OBJECT.jurisdiction("eu")` — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve `jurisdiction`, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#jurisdiction).

```js
export class RegionalRoom extends DurableObject {
	async fetch(request) {
		// "eu" when accessed through env.MY_DURABLE_OBJECT.jurisdiction("eu")
		const region = this.ctx.id.jurisdiction;
		return new Response(`Hello from ${region ?? "the default region"}!`);
	}
}

// Worker
export default {
	async fetch(request, env) {
		const stub = env.MY_DURABLE_OBJECT.jurisdiction("eu").getByName("general");
		return stub.fetch(request);
	},
};
```

`ctx.id.jurisdiction` is `undefined` for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have `jurisdiction` stored; to backfill the value, reschedule the alarm from a `fetch()` or RPC handler.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/#page","headline":"Access Durable Object jurisdiction via `ctx.id.jurisdiction`","description":"Read the jurisdiction of a Durable Object from within the object itself.","url":"https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/og.png?v=c6ad0134933c9f86","dateModified":"2026-03-26","datePublished":"2026-03-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
