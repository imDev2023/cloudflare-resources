---
description: Prevent a Durable Object alarm from retrying when ctx.abort() resets the object.
title: Prevent Durable Object alarm retries when using `ctx.abort()`
image: https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/og.png?v=25e43d5dd7218bb6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## Prevent Durable Object alarm retries when using \`ctx.abort()\`

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, an alarm interrupted by `ctx.abort()` retries after the Durable Object resets. Pass `{ retryAlarm: false }` when the alarm should stop instead:

*src/index.jsjs*

```js
import { DurableObject } from "cloudflare:workers";

export class CleanupTask extends DurableObject {
	async alarm() {
		await this.ctx.storage.deleteAll();

		this.ctx.abort("Cleanup complete", { retryAlarm: false });
	}
}
```

*src/index.tsts*

```ts
import { DurableObject } from "cloudflare:workers";

export class CleanupTask extends DurableObject {
	async alarm(): Promise<void> {
		await this.ctx.storage.deleteAll();

		this.ctx.abort("Cleanup complete", { retryAlarm: false });
	}
}
```

For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.

Alarms can run concurrently with other requests to the same Durable Object. If another request calls `ctx.abort()` while an alarm is running, the `retryAlarm` option on that call also controls whether the alarm retries.

The default retry prevents an unrelated request from permanently canceling the alarm. Set `retryAlarm: false` on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to `ctx.abort()` keep retrying alarms.

For local development, `retryAlarm` requires Wrangler 4.126.0 or later.

For more information, refer to [`ctx.abort()`](https://developers.cloudflare.com/durable-objects/api/state/#abort).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/#page","headline":"Prevent Durable Object alarm retries when using `ctx.abort()`","description":"Prevent a Durable Object alarm from retrying when ctx.abort() resets the object.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/og.png?v=25e43d5dd7218bb6","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
