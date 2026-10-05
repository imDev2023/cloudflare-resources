---
description: The Workers runtime now exposes the WebSocket binaryType property and delivers binary frames as Blob by default, matching the WebSocket specification.
title: WebSocket binary messages now delivered as Blob by default
image: https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/og.png?v=3475fc0fa88eb35a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2026

## WebSocket binary messages now delivered as Blob by default

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Binary frames received on a `WebSocket` are now delivered to the `message` event as [`Blob` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Blob) objects by default. This matches the [WebSocket specification ↗︎](https://websockets.spec.whatwg.org/) and standard browser behavior. Previously, binary frames were always delivered as [`ArrayBuffer` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer). The [`binaryType`](https://developers.cloudflare.com/workers/runtime-apis/websockets/#binarytype) property on `WebSocket` controls the delivery type on a per-WebSocket basis.

This change has been active for Workers with compatibility dates on or after `2026-03-17`, via the [`websocket_standard_binary_type`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#websocket-standard-binary-type) compatibility flag. We should have documented this change when it shipped but didn't. We're sorry for the trouble that caused. If your Worker handles binary WebSocket messages and assumes `event.data` is an `ArrayBuffer`, the frames will arrive as `Blob` instead, and a naive `instanceof ArrayBuffer` check will silently drop every frame.

To opt back into `ArrayBuffer` delivery, assign `binaryType` before calling `accept()`. This works regardless of the compatibility flag:

```js
const resp = await fetch("https://example.com", {
	headers: { Upgrade: "websocket" },
});
const ws = resp.webSocket;

// Opt back into ArrayBuffer delivery for this WebSocket.
ws.binaryType = "arraybuffer";
ws.accept();

ws.addEventListener("message", (event) => {
	if (typeof event.data === "string") {
		// Text frame.
	} else {
		// event.data is an ArrayBuffer because we set binaryType above.
	}
});
```

If you are not ready to migrate and want to keep `ArrayBuffer` as the default for all WebSockets in your Worker, add the `no_websocket_standard_binary_type` flag to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

This change has no effect on the Durable Object hibernatable WebSocket [`webSocketMessage`](https://developers.cloudflare.com/durable-objects/best-practices/websockets/) handler, which continues to receive binary data as `ArrayBuffer`.

For more information, refer to [WebSockets binary messages](https://developers.cloudflare.com/workers/runtime-apis/websockets/#binary-messages).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/#page","headline":"WebSocket binary messages now delivered as Blob by default","description":"The Workers runtime now exposes the WebSocket binaryType property and delivers binary frames as Blob by default, matching the WebSocket specification.","url":"https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/og.png?v=3475fc0fa88eb35a","dateModified":"2026-04-21","datePublished":"2026-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
