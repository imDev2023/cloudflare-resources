---
description: You can now connect to R2 buckets, D1 databases, and other resources running on Cloudflare, while running your Worker's code locally, on your own machine.
title: Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development
image: https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/og.png?v=79c431d87c5ef5a7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 16, 2025

## Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Three months ago [we announced the public beta](https://developers.cloudflare.com/changelog/2025-06-18-remote-bindings-beta/) of [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) for local development. Now, we're excited to say that it's available for everyone in Wrangler, Vite, and Vitest without using an experimental flag!

With remote bindings, you can now connect to deployed resources like [R2 buckets](https://developers.cloudflare.com/r2/) and [D1 databases](https://developers.cloudflare.com/d1/) while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.

#### Example configuration

To enable remote bindings, add `"remote" : true` to each binding that you want to rely on a remote resource running on Cloudflare:

```jsonc
{
	"name": "my-worker",
	// Set this to today's date
	"compatibility_date": "2026-10-05",

	"r2_buckets": [
		{
			"bucket_name": "screenshots-bucket",
			"binding": "screenshots_bucket",
			"remote": true,
		},
	],
}
```

```toml
name = "my-worker"
# Set this to today's date
compatibility_date = "2026-10-05"

[[r2_buckets]]
bucket_name = "screenshots-bucket"
binding = "screenshots_bucket"
remote = true
```

When remote bindings are configured, your Worker **still executes locally**, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.

**You can [try out remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) for local development today with:**

- [Wrangler v4.37.0](https://developers.cloudflare.com/workers/wrangler/)
- The [Cloudflare Vite Plugin](https://developers.cloudflare.com/workers/vite-plugin/)
- The [Cloudflare Vitest Plugin](https://developers.cloudflare.com/workers/testing/vitest-integration/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/#page","headline":"Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development","description":"You can now connect to R2 buckets, D1 databases, and other resources running on Cloudflare, while running your Worker's code locally, on your own machine.","url":"https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/og.png?v=79c431d87c5ef5a7","dateModified":"2025-09-16","datePublished":"2025-09-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
