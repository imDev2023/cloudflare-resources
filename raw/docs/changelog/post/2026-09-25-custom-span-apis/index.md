---
description: Create spans without changing the active context, annotate the current span from anywhere, record exceptions, and set multiple attributes at once.
title: Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs
image: https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/og.png?v=abe6a40cac4b876d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2026

## Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) in Workers now support more of the OpenTelemetry span API, so you can instrument more of your code and record errors directly on your spans.

- **`tracing.startSpan(name)`** creates a span without making it the active span, and returns it. Other spans do not nest under it. Call `span.end()` when the operation is complete.
- **`tracing.getActiveSpan()`** returns the currently active span. Use it to annotate the current span from helper functions and libraries without passing the span object through your code. Outside any custom span, it returns the invocation's root span.
- **`span.recordException(exception)`** records an exception event on a span. It accepts an `Error`, a string, or an object with a `code`, `name`, or `message`.
- **`span.setAttributes(attributes)`** sets multiple attributes at once. `setAttribute()` and `setAttributes()` now return the span, so you can chain calls.

*src/index.jsjs*

```js
import { tracing } from "cloudflare:workers";

export default {
	async fetch(request, env) {
		const user = await authenticate(request, env);

		// Annotate the invocation's root span
		tracing.getActiveSpan()?.setAttributes({
			"user.id": user.id,
			"user.plan": user.plan,
		});

		const span = tracing.startSpan("load-profile");
		try {
			return Response.json(await loadProfile(env, user.id));
		} catch (err) {
			span.recordException(err);
			throw err;
		} finally {
			span.end();
		}
	},
};
```

*src/index.tsts*

```ts
import { tracing } from "cloudflare:workers";

export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		const user = await authenticate(request, env);

		// Annotate the invocation's root span
		tracing.getActiveSpan()?.setAttributes({
			"user.id": user.id,
			"user.plan": user.plan,
		});

		const span = tracing.startSpan("load-profile");
		try {
			return Response.json(await loadProfile(env, user.id));
		} catch (err) {
			span.recordException(err as Error);
			throw err;
		} finally {
			span.end();
		}
	},
};
```

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/#page","headline":"Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs","description":"Create spans without changing the active context, annotate the current span from anywhere, record exceptions, and set multiple attributes at once.","url":"https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/og.png?v=abe6a40cac4b876d","dateModified":"2026-09-25","datePublished":"2026-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
