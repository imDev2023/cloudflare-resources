---
description: A comprehensive guide to building effective Durable Objects applications.
title: New Best Practices guide for Durable Objects
image: https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/og.png?v=2f295f3d270c275a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 15, 2025

## New Best Practices guide for Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new [Rules of Durable Objects](https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/) guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.

Key guidance includes:

- **Design around your "atom" of coordination** — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.
- **Use SQLite storage with RPC methods** — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.
- **Understand input and output gates** — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use `blockConcurrencyWhile()`.
- **Leverage Hibernatable WebSockets** — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.

The [testing documentation](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/) has also been updated with modern patterns using `@cloudflare/vitest-pool-workers`, including examples for testing SQLite storage, alarms, and direct instance access:

*test/counter.test.jsjs*

```js
import { env, runDurableObjectAlarm } from "cloudflare:test";
import { it, expect } from "vitest";

it("can test Durable Objects with isolated storage", async () => {
	const stub = env.COUNTER.getByName("test");

	// Call RPC methods directly on the stub
	await stub.increment();
	expect(await stub.getCount()).toBe(1);

	// Trigger alarms immediately without waiting
	await runDurableObjectAlarm(stub);
});
```

*test/counter.test.tsts*

```ts
import { env, runDurableObjectAlarm } from "cloudflare:test";
import { it, expect } from "vitest";

it("can test Durable Objects with isolated storage", async () => {
	const stub = env.COUNTER.getByName("test");

	// Call RPC methods directly on the stub
	await stub.increment();
	expect(await stub.getCount()).toBe(1);

	// Trigger alarms immediately without waiting
	await runDurableObjectAlarm(stub);
});
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/#page","headline":"New Best Practices guide for Durable Objects","description":"A comprehensive guide to building effective Durable Objects applications.","url":"https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/og.png?v=2f295f3d270c275a","dateModified":"2025-12-15","datePublished":"2025-12-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
