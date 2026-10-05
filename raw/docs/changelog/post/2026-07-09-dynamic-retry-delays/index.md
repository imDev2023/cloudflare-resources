---
description: Workflows step retries now support delay functions, so you can change the next retry delay based on the failed attempt and error.
title: Workflows now supports delay functions when retrying
image: https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/og.png?v=958f92fe47880a7d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 9, 2026

## Workflows now supports delay functions when retrying

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

With [Workflows](https://developers.cloudflare.com/workflows/), you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as `constant`, `linear`, or `exponential`.

Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to `retries.delay` and calculate the next delay from the failed attempt and thrown error.

This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a `Retry-After` value in its error messaging.

```js
await step.do(
	"sync customer",
	{
		retries: {
			limit: 5,
			delay: ({ ctx, error }) => {
				if (error.message.includes("rate limit")) {
					return `${ctx.attempt * 30} seconds`;
				}

				return "10 seconds";
			},
		},
	},
	async () => {
		await syncCustomer();
	},
);
```

```ts
await step.do(
	"sync customer",
	{
		retries: {
			limit: 5,
			delay: ({ ctx, error }) => {
				if (error.message.includes("rate limit")) {
					return `${ctx.attempt * 30} seconds`;
				}

				return "10 seconds";
			},
		},
	},
	async () => {
		await syncCustomer();
	},
);
```

Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to [Sleeping and retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/#page","headline":"Workflows now supports delay functions when retrying","description":"Workflows step retries now support delay functions, so you can change the next retry delay based on the failed attempt and error.","url":"https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/og.png?v=958f92fe47880a7d","dateModified":"2026-07-09","datePublished":"2026-07-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
