---
description: Run screenshots, PDFs, data extraction, and AI extraction against a live browser from the dashboard, then copy the generated code.
title: Browser Run adds a Playground to the Cloudflare dashboard
image: https://developers.cloudflare.com/changelog/post/2026-07-31-br-dashboard-playground/og.png?v=067e1984c7b7d880
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 31, 2026

## Browser Run adds a Playground to the Cloudflare dashboard

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-31-br-dashboard-playground/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now includes a Playground in the Cloudflare dashboard. Use it to try Quick Actions against a live browser without creating a Worker, installing an SDK, or deploying code first.

The Playground helps you test a target URL or raw HTML input, tune viewport and page-load settings, preview the output, and copy working code for the same request.

![Browser Run Playground in the Cloudflare dashboard showing a generated screenshot preview and output settings](https://developers.cloudflare.com/images/browser-run/playground.png)

With the Playground, you can:

- Capture visuals as [screenshots](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/) or [PDFs](https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/).
- Generate multiple output formats in one request with the [snapshot endpoint](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/).
- Extract [HTML](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/), [Markdown](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/), [links](https://developers.cloudflare.com/browser-run/quick-actions/links-endpoint/), or [scraped data](https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/).
- Extract [structured data with AI](https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/) using a prompt and optional JSON Schema.

You can also configure desktop, laptop, tablet, mobile, or custom viewport sizes, set browser scale, choose page-load conditions, set timeouts, and wait for selectors before running a request.

Select **Show Code** to generate the same request as cURL, TypeScript SDK, Python, or Workers Binding code. For example, a screenshot request can be copied as a Workers Binding call:

```ts
interface Env {
	BROWSER: BrowserRun;
}

export default {
	async fetch(request, env): Promise<Response> {
		return await env.BROWSER.quickAction("screenshot", {
			url: "https://developers.cloudflare.com",
			viewport: {
				width: 1920,
				height: 1080,
			},
		});
	},
} satisfies ExportedHandler<Env>;
```

Requests made in the Playground incur [Browser Run charges](https://developers.cloudflare.com/browser-run/pricing/). AI extraction also incurs Workers AI charges.

To try the Playground, go to **Browser Run** in the Cloudflare dashboard and select **Playground**.

[Go to **Browser Run** ↗](https://dash.cloudflare.com/?to=/:account/workers/browser-run)

For more information, refer to the [Quick Actions documentation](https://developers.cloudflare.com/browser-run/quick-actions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-31-br-dashboard-playground/#page","headline":"Browser Run adds a Playground to the Cloudflare dashboard","description":"Run screenshots, PDFs, data extraction, and AI extraction against a live browser from the dashboard, then copy the generated code.","url":"https://developers.cloudflare.com/changelog/post/2026-07-31-br-dashboard-playground/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-31-br-dashboard-playground/og.png?v=067e1984c7b7d880","dateModified":"2026-07-31","datePublished":"2026-07-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
