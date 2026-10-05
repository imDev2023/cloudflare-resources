---
description: Use the `cf.vary` request option to control cache variants for Workers subrequests that receive origin Vary responses.
title: Workers fetch requests now support cf.vary
image: https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/og.png?v=19d8ae0a562b3926
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 28, 2026

## Workers fetch requests now support cf.vary

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers `fetch()` requests now support the `cf.vary` request option. Use `cf.vary` to control how Cloudflare caches origin responses with a `Vary` header for a single subrequest.

*src/index.jsjs*

```js
export default {
	async fetch(request) {
		return fetch(request, {
			cf: {
				vary: {
					default: { action: "bypass" },
					headers: {
						accept: {
							action: "normalize",
							media_types: ["text/html", "application/json"],
						},
						"accept-language": {
							action: "normalize",
							languages: ["en", "fr", "de"],
						},
					},
				},
			},
		});
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request): Promise<Response> {
		return fetch(request, {
			cf: {
				vary: {
					default: { action: "bypass" },
					headers: {
						accept: {
							action: "normalize",
							media_types: ["text/html", "application/json"],
						},
						"accept-language": {
							action: "normalize",
							languages: ["en", "fr", "de"],
						},
					},
				},
			},
		});
	},
} satisfies ExportedHandler;
```

For more information, refer to [`cf.vary`](https://developers.cloudflare.com/workers/runtime-apis/request/#the-cfvary-property).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/#page","headline":"Workers fetch requests now support cf.vary","description":"Use the cf.vary request option to control cache variants for Workers subrequests that receive origin Vary responses.","url":"https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/og.png?v=19d8ae0a562b3926","dateModified":"2026-06-28","datePublished":"2026-06-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
