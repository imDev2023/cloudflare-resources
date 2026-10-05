---
description: Browser Rendering birthday week announcements
title: Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits
image: https://developers.cloudflare.com/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/og.png?v=5dc07553377271bb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2025

## Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’re shipping three updates to Browser Rendering:

- Playwright support is now Generally Available and synced with [Playwright v1.55 ↗︎](https://playwright.dev/docs/release-notes#version-155), giving you a stable foundation for critical automation and AI-agent workflows.
- We’re also adding [Stagehand support (Beta)](https://developers.cloudflare.com/browser-run/stagehand/) so you can combine code with natural language instructions to build more resilient automations.
- Finally, we’ve tripled [limits](https://developers.cloudflare.com/browser-run/limits/#workers-paid) for paid plans across both the [REST API](https://developers.cloudflare.com/browser-run/quick-actions/) and [Browser Sessions](https://developers.cloudflare.com/browser-run/#integration-methods) to help you scale.

To get started with Stagehand, refer to the [Stagehand](https://developers.cloudflare.com/browser-run/stagehand/) example that uses Stagehand and [Workers AI](https://developers.cloudflare.com/workers-ai/) to search for a movie on this [example movie directory ↗︎](https://demo.playwright.dev/movies), extract its details using natural language (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.

*Stagehand examplets*

```ts
const stagehand = new Stagehand({
	env: "LOCAL",
	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },
	llmClient: new WorkersAIClient(env.AI),
	verbose: 1,
});

await stagehand.init();
const page = stagehand.page;

await page.goto("https://demo.playwright.dev/movies");

// if search is a multi-step action, stagehand will return an array of actions it needs to act on
const actions = await page.observe('Search for "Furiosa"');
for (const action of actions) await page.act(action);

await page.act("Click the search result");

// normal playwright functions work as expected
await page.waitForSelector(".info-wrapper .cast");

let movieInfo = await page.extract({
	instruction: "Extract movie information",
	schema: z.object({
		title: z.string(),
		year: z.number(),
		rating: z.number(),
		genres: z.array(z.string()),
		duration: z.number().describe("Duration in minutes"),
	}),
});

await stagehand.close();
```

![Stagehand video](https://developers.cloudflare.com/images/browser-run/speedystagehand.gif)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/#page","headline":"Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits","description":"Browser Rendering birthday week announcements","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/og.png?v=5dc07553377271bb","dateModified":"2025-09-25","datePublished":"2025-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
