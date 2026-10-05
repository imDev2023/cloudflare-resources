---
description: Browser Run's /snapshot endpoint now accepts a formats parameter to return Markdown and the accessibility tree alongside HTML and screenshots.
title: New formats parameter for the Browser Run /snapshot endpoint
image: https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/og.png?v=fcd8b905f002ebaf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 11, 2026

## New formats parameter for the Browser Run /snapshot endpoint

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/)'s [`/snapshot` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) now supports a `formats` parameter that lets you return multiple page formats in a single API call. Previously, `/snapshot` returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.

These formats are particularly useful for AI agent workflows:

- Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.
- The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.

The following example returns a screenshot, Markdown, and the accessibility tree in one call:

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/snapshot' \
  -H 'Authorization: Bearer <apiToken>' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com/",
    "formats": ["screenshot", "markdown", "accessibilityTree"]
  }'
```

```typescript
import Cloudflare from "cloudflare";

const client = new Cloudflare({
	apiToken: process.env["CLOUDFLARE_API_TOKEN"],
});

const snapshot = await client.browserRendering.snapshot.create({
	account_id: process.env["CLOUDFLARE_ACCOUNT_ID"],
	url: "https://example.com/",
	formats: ["screenshot", "markdown", "accessibilityTree"],
});

console.log(snapshot.markdown);
console.log(snapshot.accessibilityTree);
```

```typescript
interface Env {
	BROWSER: BrowserRun;
}

export default {
	async fetch(request, env): Promise<Response> {
		return await env.BROWSER.quickAction("snapshot", {
			url: "https://example.com/",
			formats: ["screenshot", "markdown", "accessibilityTree"],
		});
	},
} satisfies ExportedHandler<Env>;
```

You must request at least two formats. If you only need one, use the respective single-format endpoint such as [`/screenshot`](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/) or [`/markdown`](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/).

Refer to the [`/snapshot` documentation](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) for the full list of accepted values.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/#page","headline":"New formats parameter for the Browser Run /snapshot endpoint","description":"Browser Run's /snapshot endpoint now accepts a formats parameter to return Markdown and the accessibility tree alongside HTML and screenshots.","url":"https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/og.png?v=fcd8b905f002ebaf","dateModified":"2026-06-11","datePublished":"2026-06-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
