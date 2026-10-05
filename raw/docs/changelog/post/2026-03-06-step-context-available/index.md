---
description: Cloudflare Workflows, our durable execution engine, now supports step context in production &amp; local development
title: Workflow steps now expose retry attempt number via step context
image: https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/og.png?v=3b6760637a166648
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 6, 2026

## Workflow steps now expose retry attempt number via step context

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Workflows allows you to configure specific retry logic for each step in your workflow execution. Now, you can access **which** retry attempt is currently executing for calls to `step.do()`:

```ts
await step.do("my-step", async (ctx) => {
	// ctx.attempt is 1 on first try, 2 on first retry, etc.
	console.log(`Attempt ${ctx.attempt}`);
});
```

You can use the step context for improved logging & observability, progressive backoff, or conditional logic in your workflow definition.

Note that the current attempt number is 1-indexed. For more information on retry behavior, refer to [Sleeping and Retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/#page","headline":"Workflow steps now expose retry attempt number via step context","description":"Cloudflare Workflows, our durable execution engine, now supports step context in production & local development","url":"https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/og.png?v=3b6760637a166648","dateModified":"2026-03-06","datePublished":"2026-03-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
