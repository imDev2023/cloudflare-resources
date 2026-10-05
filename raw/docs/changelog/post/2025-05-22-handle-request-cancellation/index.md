---
description: Workers can now add event listeners on Request.signal and perform tasks when the request is cancelled by the client
title: Handle incoming request cancellation in Workers with Request.signal
image: https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/og.png?v=c8fc198a40f9c64d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 22, 2025

## Handle incoming request cancellation in Workers with Request.signal

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In Cloudflare Workers, you can now attach an event listener to [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) objects, using the [`signal` property ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Request/signal). This allows you to perform tasks when the request to your Worker is canceled by the client. To use this feature, you must set the [`enable_request_signal`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests) compatibility flag.

You can use a listener to perform cleanup tasks or write to logs before your Worker's invocation ends. For example, if you run the Worker below, and then abort the request from the client, a log will be written:

*index.jsjs*

```js
export default {
	async fetch(request, env, ctx) {
		// This sets up an event listener that will be called if the client disconnects from your
		// worker.
		request.signal.addEventListener("abort", () => {
			console.log("The request was aborted!");
		});

		const { readable, writable } = new IdentityTransformStream();
		sendPing(writable);
		return new Response(readable, {
			headers: { "Content-Type": "text/plain" },
		});
	},
};

async function sendPing(writable) {
	const writer = writable.getWriter();
	const enc = new TextEncoder();

	for (;;) {
		// Send 'ping' every second to keep the connection alive
		await writer.write(enc.encode("ping\r\n"));
		await scheduler.wait(1000);
	}
}
```

*index.tsts*

```ts
export default {
  async fetch(request, env, ctx): Promise<Response> {
    // This sets up an event listener that will be called if the client disconnects from your
    // worker.
    request.signal.addEventListener('abort', () => {
      console.log('The request was aborted!');
    });

    const { readable, writable } = new IdentityTransformStream();
    sendPing(writable);
    return new Response(readable, { headers: { 'Content-Type': 'text/plain' } });
  },
} satisfies ExportedHandler<Env>;

async function sendPing(writable: WritableStream): Promise<void> {
	const writer = writable.getWriter();
	const enc = new TextEncoder();

	for (;;) {
		// Send 'ping' every second to keep the connection alive
		await writer.write(enc.encode('ping\r\n'));
		await scheduler.wait(1000);
	}
}
```

For more information see the [`Request` documentation](https://developers.cloudflare.com/workers/runtime-apis/request).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/#page","headline":"Handle incoming request cancellation in Workers with Request.signal","description":"Workers can now add event listeners on Request.signal and perform tasks when the request is cancelled by the client","url":"https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/og.png?v=c8fc198a40f9c64d","dateModified":"2025-05-22","datePublished":"2025-05-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
