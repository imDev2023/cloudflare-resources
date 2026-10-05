---
description: Developers can now use the Playwright library for browser automation with Browser Rendering
title: Playwright for Browser Rendering now available
image: https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/og.png?v=c17e2f6e105a354b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 4, 2025

## Playwright for Browser Rendering now available

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to share that you can now use Playwright's browser automation [capabilities ↗︎](https://playwright.dev/docs/api/class-playwright) from Cloudflare [Workers](https://developers.cloudflare.com/workers/).

[Playwright ↗︎](https://playwright.dev/) is an open-source package developed by Microsoft that can do browser automation tasks; it's commonly used to write software tests, debug applications, create screenshots, and crawl pages. Like [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/), we [forked ↗︎](https://github.com/cloudflare/playwright) Playwright and modified it to be compatible with Cloudflare Workers and [Browser Rendering](https://developers.cloudflare.com/browser-run/).

Below is an example of how to use Playwright with Browser Rendering to test a TODO application using assertions:

*Assertion examplets*

```ts
import { launch, type BrowserWorker } from "@cloudflare/playwright";
import { expect } from "@cloudflare/playwright/test";

interface Env {
	MYBROWSER: BrowserWorker;
}

export default {
	async fetch(request: Request, env: Env) {
		const browser = await launch(env.MYBROWSER);
		const page = await browser.newPage();

		await page.goto("https://demo.playwright.dev/todomvc");

		const TODO_ITEMS = [
			"buy some cheese",
			"feed the cat",
			"book a doctors appointment",
		];

		const newTodo = page.getByPlaceholder("What needs to be done?");
		for (const item of TODO_ITEMS) {
			await newTodo.fill(item);
			await newTodo.press("Enter");
		}

		await expect(page.getByTestId("todo-title")).toHaveCount(TODO_ITEMS.length);

		await Promise.all(
			TODO_ITEMS.map((value, index) =>
				expect(page.getByTestId("todo-title").nth(index)).toHaveText(value),
			),
		);
	},
};
```

Playwright is available as an npm package at [`@cloudflare/playwright` ↗︎](https://www.npmjs.com/package/@cloudflare/playwright) and the code is at [GitHub ↗︎](https://github.com/cloudflare/playwright).

Learn more in our [documentation](https://developers.cloudflare.com/browser-run/playwright/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/#page","headline":"Playwright for Browser Rendering now available","description":"Developers can now use the Playwright library for browser automation with Browser Rendering","url":"https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/og.png?v=c17e2f6e105a354b","dateModified":"2025-04-04","datePublished":"2025-04-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
