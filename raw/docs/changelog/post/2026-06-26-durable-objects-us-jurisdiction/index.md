---
description: Restrict Durable Objects to run and store data within the United States.
title: New `us` jurisdiction for Durable Objects
image: https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/og.png?v=9ea6fcb5c42befd5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 26, 2026

## New \`us\` jurisdiction for Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects now supports a `us` [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction), letting you create Durable Objects that only run and store data within the United States. Use the `us` jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.

Create a namespace restricted to the `us` jurisdiction the same way as any other jurisdiction:

```js
// Worker
export default {
	async fetch(request, env) {
		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction("us");
		const stub = usSubnamespace.getByName("general");
		return stub.fetch(request);
	},
};
```

Workers may still access Durable Objects constrained to the `us` jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.

For the full list of supported jurisdictions, refer to [Data location — Restrict Durable Objects to a jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/#page","headline":"New `us` jurisdiction for Durable Objects","description":"Restrict Durable Objects to run and store data within the United States.","url":"https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/og.png?v=9ea6fcb5c42befd5","dateModified":"2026-06-26","datePublished":"2026-06-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
