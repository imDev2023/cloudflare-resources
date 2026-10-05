---
description: Workers no longer have an explicit limit on subrequests per invocation, allowing for more fetch and service calls.
title: Workers are no longer limited to 1000 subrequests
image: https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/og.png?v=77d894fac67ee974
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 11, 2026

## Workers are no longer limited to 1000 subrequests

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more `fetch()` calls or requests to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as open websockets on [Durable Objects](https://developers.cloudflare.com/durable-objects) or long-running [Workflows](https://developers.cloudflare.com/workflows), as these could often exceed this limit and error.

By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this limit can be increased up to 10 million by setting the new `subrequests` limit in your Wrangler configuration file.

```jsonc
{
	"limits": {
		"subrequests": 50000,
	},
}
```

```toml
[limits]
subrequests = 50_000
```

Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.

To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.

```jsonc
{
	"limits": {
		"subrequests": 10,
		"cpu_ms": 1000,
	},
}
```

```toml
[limits]
subrequests = 10
cpu_ms = 1_000
```

For more information, refer to the [Wrangler configuration documentation for limits](https://developers.cloudflare.com/workers/wrangler/configuration/#limits) and [subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/#page","headline":"Workers are no longer limited to 1000 subrequests","description":"Workers no longer have an explicit limit on subrequests per invocation, allowing for more fetch and service calls.","url":"https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/og.png?v=77d894fac67ee974","dateModified":"2026-02-11","datePublished":"2026-02-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
