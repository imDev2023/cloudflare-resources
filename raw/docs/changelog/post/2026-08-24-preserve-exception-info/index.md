---
description: Log events now preserve the name, message, and stack of exceptions passed to console methods.
title: Preserve exception details in console logs
image: https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/og.png?v=7736349cbb6945fc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 24, 2026

## Preserve exception details in console logs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.

For example, your Worker can catch and log an exception:

```js
try {
	throw new Error("Deliberately created exception");
} catch (error) {
	console.error("caught exception:", error);
}
```

```ts
try {
	throw new Error("Deliberately created exception");
} catch (error) {
	console.error("caught exception:", error);
}
```

If you use [Workers Observability](https://developers.cloudflare.com/workers/observability/), your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:

![Workers Observability log entry showing a caught exception and its stack trace](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=212,format=webp/_astro/2026-08-24-error-info.Be4rAN4i.png)

The exception's stack trace appears directly in the log message.

If you send telemetry to a [Tail Worker](https://developers.cloudflare.com/workers/observability/logs/tail-workers/), the Tail Worker now receives a log entry with an `errorInfo` array:

```json
{
	"message": ["Request failed:", "RangeError: Value out of range"],
	"errorInfo": [
		null,
		{
			"name": "RangeError",
			"message": "Value out of range",
			"stack": "RangeError: Value out of range\n    at ..."
		}
	],
	"level": "error",
	"timestamp": 1784851200000
}
```

Each `errorInfo` item corresponds to the console argument at the same index in `message`. Arguments that are not exceptions have a `null` entry.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/#page","headline":"Preserve exception details in console logs","description":"Log events now preserve the name, message, and stack of exceptions passed to console methods.","url":"https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/og.png?v=7736349cbb6945fc","dateModified":"2026-08-24","datePublished":"2026-08-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
