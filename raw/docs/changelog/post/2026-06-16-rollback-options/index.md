---
description: Workflows rollback handlers now receive the original step context, and rollbackConfig is limited to retry and timeout settings.
title: Workflows rollback handlers now include step context
image: https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/og.png?v=29f6046d37f3a3b4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 23, 2026

## Workflows rollback handlers now include step context

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original [step context](https://developers.cloudflare.com/workflows/build/step-context/) via a `ctx` object for the step being rolled back. This includes `ctx.step.name`, `ctx.step.count`, `ctx.attempt`, and the step `config` with defaults applied.

The [step configuration](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig) includes the retry and timeout settings used for that step, so you can customize your step recovery logic according to those fields.

```ts
await step.do(
	"create charge",
	async () => {
		const charge = await createCharge();
		return { chargeId: charge.id };
	},
	{
		rollback: async ({ ctx, output, error }) => {
			// `output` is the value returned by the step being rolled back.
			const { chargeId } = output as { chargeId: string };
			await refundCharge(chargeId, {
				// `ctx` is the original step context, including step name, count, attempt, and config.
				reason: `${ctx.step.name}: ${error.message}`,
			});
		},
		rollbackConfig: {
			// `rollbackConfig` controls retries and timeout for the rollback handler.
			retries: { limit: 3, delay: "30 seconds", backoff: "linear" },
			timeout: "5 minutes",
		},
	},
);
```

Refer to [rollback options](https://developers.cloudflare.com/workflows/build/workers-api/#rollback-options) to learn more.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/#page","headline":"Workflows rollback handlers now include step context","description":"Workflows rollback handlers now receive the original step context, and rollbackConfig is limited to retry and timeout settings.","url":"https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/og.png?v=29f6046d37f3a3b4","dateModified":"2026-06-23","datePublished":"2026-06-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
