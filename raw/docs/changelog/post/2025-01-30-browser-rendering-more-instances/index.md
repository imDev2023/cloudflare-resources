---
description: Browser Rendering now supports more concurrent browser sessions.
title: Increased Browser Rendering limits!
image: https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/og.png?v=761f7bab76a38acc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 30, 2025

## Increased Browser Rendering limits!

[Workers](https://developers.cloudflare.com/workers/) [Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Rendering](https://developers.cloudflare.com/browser-run/) now supports 10 concurrent browser instances per account *and* 10 new instances per minute, up from the previous limits of 2.

This allows you to launch more browser tasks from [Cloudflare Workers](https://developers.cloudflare.com/workers).

To manage concurrent browser sessions, you can use [Queues](https://developers.cloudflare.com/queues/) or [Workflows](https://developers.cloudflare.com/workflows/):

*index.jsjs*

```js
export default {
	async queue(batch, env) {
		for (const message of batch.messages) {
			const browser = await puppeteer.launch(env.BROWSER);
			const page = await browser.newPage();

			try {
				await page.goto(message.url, {
					waitUntil: message.waitUntil,
				});
				// Process page...
			} finally {
				await browser.close();
			}
		}
	},
};
```

*index.tsts*

```ts
interface QueueMessage {
	url: string;
	waitUntil: number;
}

export interface Env {
	BROWSER_QUEUE: Queue<QueueMessage>;
	BROWSER: Fetcher;
}

export default {
	async queue(batch: MessageBatch<QueueMessage>, env: Env): Promise<void> {
		for (const message of batch.messages) {
			const browser = await puppeteer.launch(env.BROWSER);
			const page = await browser.newPage();

			try {
				await page.goto(message.url, {
					waitUntil: message.waitUntil,
				});
				// Process page...
			} finally {
				await browser.close();
			}
		}
	},
};
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/#page","headline":"Increased Browser Rendering limits!","description":"Browser Rendering now supports more concurrent browser sessions.","url":"https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/og.png?v=761f7bab76a38acc","dateModified":"2025-01-30","datePublished":"2025-01-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
