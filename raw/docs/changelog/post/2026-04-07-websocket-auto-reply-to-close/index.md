---
description: The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer, matching standard WebSocket behavior.
title: WebSockets now automatically reply to Close frames
image: https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/og.png?v=06f7e8c0065f4d0a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2026

## WebSockets now automatically reply to Close frames

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer. The `readyState` transitions to `CLOSED` before the `close` event fires. This matches the [WebSocket specification ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event) and standard browser behavior.

This change is enabled by default for Workers using compatibility dates on or after `2026-04-07` (via the [`web_socket_auto_reply_to_close`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close) compatibility flag). Existing code that manually calls `close()` inside the `close` event handler will continue to work — the call is silently ignored when the WebSocket is already closed.

```js
const [client, server] = Object.values(new WebSocketPair());
server.accept();

server.addEventListener("close", (event) => {
	// readyState is already CLOSED — no need to call server.close().
	console.log(server.readyState); // WebSocket.CLOSED
	console.log(event.code); // 1000
	console.log(event.wasClean); // true
});
```

#### Half-open mode for WebSocket proxying

The automatic close behavior can interfere with WebSocket proxying, where a Worker sits between a client and a backend and needs to coordinate the close on both sides independently. To support this use case, pass `{ allowHalfOpen: true }` to `accept()`:

```js
const [client, server] = Object.values(new WebSocketPair());

server.accept({ allowHalfOpen: true });

server.addEventListener("close", (event) => {
	// readyState is still CLOSING here, giving you time
	// to coordinate the close on the other side.
	console.log(server.readyState); // WebSocket.CLOSING

	// Manually close when ready.
	server.close(event.code, "done");
});
```

For more information, refer to [WebSockets Close behavior](https://developers.cloudflare.com/workers/runtime-apis/websockets/#close-behavior).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/#page","headline":"WebSockets now automatically reply to Close frames","description":"The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer, matching standard WebSocket behavior.","url":"https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/og.png?v=06f7e8c0065f4d0a","dateModified":"2026-04-07","datePublished":"2026-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
