---
description: Browser Run guardrails restrict HTTP and HTTPS requests by hostname.
title: Control which hostnames Browser Run sessions can access
image: https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/og.png?v=94e2dce4c14afce2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 14, 2026

## Control which hostnames Browser Run sessions can access

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now supports [guardrails](https://developers.cloudflare.com/browser-run/features/guardrails/), which limit a browser session's HTTP and HTTPS requests to permitted hostnames.

Use guardrails when you need to:

- Keep a browser workflow limited to a specific website and its subdomains.
- Load only known third-party APIs, scripts, images, and fonts.
- Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.

Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named `MYBROWSER`, pass `guardrails` when launching Puppeteer:

```js
import puppeteer from "@cloudflare/puppeteer";

export async function startGuardedSession(env) {
	return puppeteer.launch(env.MYBROWSER, {
		guardrails: {
			allowedDomains: ["example.com", "*.example.com"],
		},
	});
}
```

```ts
import puppeteer from "@cloudflare/puppeteer";

interface Env {
	MYBROWSER: Fetcher;
}

export async function startGuardedSession(env: Env) {
	return puppeteer.launch(env.MYBROWSER, {
		guardrails: {
			allowedDomains: ["example.com", "*.example.com"],
		},
	});
}
```

In addition to session guardrails, Browser Run now supports a read-only mode for [Live View](https://developers.cloudflare.com/browser-run/features/live-view/). Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.

To create a read-only link, set `{ mode: "readonly" }` when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.

Refer to the [guardrails documentation](https://developers.cloudflare.com/browser-run/features/guardrails/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/#page","headline":"Control which hostnames Browser Run sessions can access","description":"Browser Run guardrails restrict HTTP and HTTPS requests by hostname.","url":"https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/og.png?v=94e2dce4c14afce2","dateModified":"2026-09-14","datePublished":"2026-09-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
