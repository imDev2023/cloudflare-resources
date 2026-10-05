---
description: Evaluate feature flags at the edge directly from Cloudflare Workers with Flagship, Cloudflare's native feature flag service.
title: Flagship now in public beta
image: https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/og.png?v=1b5a14448ed36ac2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 26, 2026

## Flagship now in public beta

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**[Flagship](https://developers.cloudflare.com/flagship/)** is now in public beta. Evaluate feature flags directly from Cloudflare Workers with no outbound HTTP calls, using globally distributed flag configuration backed by Workers KV and Durable Objects. Flagship supports typed flag values, targeting rules, percentage rollouts, audit history, and OpenFeature-compatible SDKs.

Evaluate a flag from a Worker in a few lines of code:

*src/index.jsjs*

```js
export default {
	async fetch(request, env) {
		const showNewCheckout = await env.FLAGS.getBooleanValue(
			"new-checkout",
			false,
		);

		return new Response(showNewCheckout ? "New checkout" : "Standard checkout");
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		const showNewCheckout = await env.FLAGS.getBooleanValue("new-checkout", false);

		return new Response(
			showNewCheckout ? "New checkout" : "Standard checkout",
		);
	},
} satisfies ExportedHandler<Env>;
```

Start creating flags from the Cloudflare dashboard today. Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/get-started/) to get started.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/#page","headline":"Flagship now in public beta","description":"Evaluate feature flags at the edge directly from Cloudflare Workers with Flagship, Cloudflare's native feature flag service.","url":"https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/og.png?v=1b5a14448ed36ac2","dateModified":"2026-05-26","datePublished":"2026-05-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
