---
description: Workflows now provides additional context inside step.do() callbacks and supports returning ReadableStream to handle larger step outputs.
title: Additional step context and ReadableStream support now available in Workflows step.do()
image: https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/og.png?v=1206e5c283976a7c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2026

## Additional step context and ReadableStream support now available in Workflows step.do()

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) now provides additional context inside `step.do()` callbacks and supports returning `ReadableStream` to handle larger step outputs.

#### Step context properties

The `step.do()` callback receives a context object with new properties [alongside](https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/) `attempt`:

- **`step.name`** — The name passed to `step.do()`
- **`step.count`** — How many times a step with that name has been invoked in this instance (1-indexed)
  - Useful when running the same step in a loop.
- **`config`** — The resolved step configuration, including `timeout` and `retries` with defaults applied

```ts
type ResolvedStepConfig = {
	retries: {
		limit: number;
		delay: WorkflowDelayDuration | number;
		backoff?: "constant" | "linear" | "exponential";
	};
	timeout: WorkflowTimeoutDuration | number;
};

type WorkflowStepContext = {
	step: {
		name: string;
		count: number;
	};
	attempt: number;
	config: ResolvedStepConfig;
};
```

#### ReadableStream support in `step.do()`

Steps can now return a `ReadableStream` directly. Although non-stream step outputs are [limited to 1 MiB](https://developers.cloudflare.com/workflows/reference/limits/), streamed outputs support much larger payloads.

```ts
const largePayload = await step.do("fetch-large-file", async () => {
	const object = await env.MY_BUCKET.get("large-file.bin");
	return object.body;
});
```

Note that streamed outputs are still considered part of the Workflow instance storage limit.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/#page","headline":"Additional step context and ReadableStream support now available in Workflows step.do()","description":"Workflows now provides additional context inside step.do() callbacks and supports returning ReadableStream to handle larger step outputs.","url":"https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/og.png?v=1206e5c283976a7c","dateModified":"2026-04-21","datePublished":"2026-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
