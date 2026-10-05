---
description: Use tracing.startActiveSpan() and span.end() to instrument operations that outlive a single callback, such as stream pipelines.
title: Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs
image: https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/og.png?v=b4fcc15affa3efee
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 28, 2026

## Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers runtime now provides built-in `tracing.startActiveSpan()` and `span.end()` APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed.

This augments the [existing API for writing custom spans](https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/), `tracing.enterSpan()`, which automatically ends a span when its callback is returned. With `startActiveSpan()`, the span remains open after the callback returns, and you call `span.end()` when the work is complete:

*src/index.jsjs*

```js
import { tracing } from "cloudflare:workers";

const encoder = new TextEncoder();

export default {
	fetch() {
		return tracing.startActiveSpan("stream-response", (span) => {
			let timer;

			const body = new ReadableStream({
				start(controller) {
					controller.enqueue(encoder.encode("Starting...\n"));

					timer = setTimeout(() => {
						controller.enqueue(encoder.encode("Complete.\n"));
						controller.close();

						span.setAttribute("stream.status", "complete");
						span.end();
					}, 1000);
				},

				cancel() {
					if (timer !== undefined) clearTimeout(timer);

					span.setAttribute("stream.status", "cancelled");
					span.end();
				},
			});

			return new Response(body, {
				headers: { "content-type": "text/plain" },
			});
		});
	},
};
```

*src/index.tsts*

```ts
import { tracing } from "cloudflare:workers";

const encoder = new TextEncoder();

export default {
	fetch(): Response {
		return tracing.startActiveSpan("stream-response", (span) => {
			let timer: ReturnType<typeof setTimeout> | undefined;

			const body = new ReadableStream<Uint8Array>({
				start(controller) {
					controller.enqueue(encoder.encode("Starting...\n"));

					timer = setTimeout(() => {
						controller.enqueue(encoder.encode("Complete.\n"));
						controller.close();

						span.setAttribute("stream.status", "complete");
						span.end();
					}, 1000);
				},

				cancel() {
					if (timer !== undefined) clearTimeout(timer);

					span.setAttribute("stream.status", "cancelled");
					span.end();
				},
			});

			return new Response(body, {
				headers: { "content-type": "text/plain" },
			});
		});
	},
};
```

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/#page","headline":"Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs","description":"Use tracing.startActiveSpan() and span.end() to instrument operations that outlive a single callback, such as stream pipelines.","url":"https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/og.png?v=b4fcc15affa3efee","dateModified":"2026-07-28","datePublished":"2026-07-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
