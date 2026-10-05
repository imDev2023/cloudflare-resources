---
description: Browser Run browser bindings now support typed session management, outbound Worker routing, and DevTools methods.
title: Browser Run adds session and DevTools methods to browser bindings
image: https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/og.png?v=c3488f2c0b73b3ef
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 21, 2026

## Browser Run adds session and DevTools methods to browser bindings

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) browser bindings now provide typed methods for session management and DevTools operations. You can acquire a session, connect a browser client, create Live View URLs, manage targets, and close sessions without constructing HTTP requests.

The new `acquire()` and `launch()` methods also accept [`outboundByHost`](https://developers.cloudflare.com/browser-run/features/outbound-workers/). This lets you route requests for selected hostnames through another Worker, including a Worker that adds authentication or reaches a private service.

```js
const connection = await env.BROWSER.launch({
	outboundByHost: {
		"private.example.test": env.OUTBOUND,
	},
});
```

```ts
const connection = await env.BROWSER.launch({
	outboundByHost: {
		"private.example.test": env.OUTBOUND,
	},
});
```

Use `connectSession(sessionId)` when you need to acquire and connect in separate steps. The method returns a session-pinned `webSocket` Fetcher for a CDP client.

The binding also includes session methods for Live View, active sessions, session history, limits, session details, and cleanup. The nested `devtools` binding provides typed methods for browser version information, protocol descriptions, and target operations such as listing, creating, activating, and closing targets.

Refer to the [Browser binding API documentation](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/) for method signatures and the [outbound Worker feature guide](https://developers.cloudflare.com/browser-run/features/outbound-workers/) for routing examples.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/#page","headline":"Browser Run adds session and DevTools methods to browser bindings","description":"Browser Run browser bindings now support typed session management, outbound Worker routing, and DevTools methods.","url":"https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/og.png?v=c3488f2c0b73b3ef","dateModified":"2026-09-21","datePublished":"2026-09-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
