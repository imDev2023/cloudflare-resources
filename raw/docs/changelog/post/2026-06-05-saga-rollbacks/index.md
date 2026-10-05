---
description: Workflows now lets you attach rollback handlers to step.do(), inspect rollback outcomes, and query rollback events in analytics.
title: Rollback support now available in Workflows
image: https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/og.png?v=d3485f3046d8068c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 5, 2026

## Rollback support now available in Workflows

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) now supports saga-style rollbacks, allowing you to add compensating logic to each `step.do()` in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse `step-start` order.

This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level `catch`, you can keep each compensating action next to the step it undoes.

Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.

```js
await step.do(
	"provision resource",
	async () => {
		const resource = await provisionResource();
		return { resourceId: resource.id };
	},
	{
		rollback: async ({ output }) => {
			const { resourceId } = output;
			await deleteResource(resourceId);
		},
		rollbackConfig: {
			retries: { limit: 3, delay: "15 seconds", backoff: "linear" },
			timeout: "2 minutes",
		},
	},
);
```

```ts
await step.do(
	"provision resource",
	async () => {
		const resource = await provisionResource();
		return { resourceId: resource.id };
	},
	{
		rollback: async ({ output }) => {
			const { resourceId } = output as { resourceId: string };
			await deleteResource(resourceId);
		},
		rollbackConfig: {
			retries: { limit: 3, delay: "15 seconds", backoff: "linear" },
			timeout: "2 minutes",
		},
	},
);
```

Refer to [rollback options](https://developers.cloudflare.com/workflows/build/workers-api/#rollback-options) to learn more.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/#page","headline":"Rollback support now available in Workflows","description":"Workflows now lets you attach rollback handlers to step.do(), inspect rollback outcomes, and query rollback events in analytics.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/og.png?v=d3485f3046d8068c","dateModified":"2026-06-05","datePublished":"2026-06-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
