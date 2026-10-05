---
description: Browser Run sessions now accept concurrent connections, so multiple Workers can share one browser.
title: Connect multiple clients to one Browser Run session
image: https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/og.png?v=0d0f196fad04b353
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 29, 2026

## Connect multiple clients to one Browser Run session

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) sessions now accept multiple concurrent connections. Before, a session accepted only one connection at a time, and other Workers had to wait until that connection closed. Now multiple Workers can connect to the same browser at the same time.

Each `puppeteer.connect()` call opens its own Chrome DevTools Protocol (CDP) connection. Create a separate browser context for each request to keep its pages, cookies, and storage apart from other clients.

```js
const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
const context = await browser.createBrowserContext();

try {
	const page = await context.newPage();
	await page.goto("https://example.com");
	// ...
} finally {
	await context.close();
	await browser.disconnect(); // keep the shared browser running
}
```

```ts
const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
const context = await browser.createBrowserContext();

try {
	const page = await context.newPage();
	await page.goto("https://example.com");
	// ...
} finally {
	await context.close();
	await browser.disconnect(); // keep the shared browser running
}
```

Sharing sessions means fewer new browsers to launch, less cold-start time, and fewer [concurrent browsers](https://developers.cloudflare.com/browser-run/limits/) counted against your limits.

Concurrent connections require `@cloudflare/puppeteer` version 1.1.0 or later.

Refer to [Reuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/) for a full example.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/#page","headline":"Connect multiple clients to one Browser Run session","description":"Browser Run sessions now accept concurrent connections, so multiple Workers can share one browser.","url":"https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/og.png?v=0d0f196fad04b353","dateModified":"2026-09-29","datePublished":"2026-09-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
