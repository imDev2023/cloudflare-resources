---
description: Explicit placement hints for legacy cloud infrastructure.
title: New Placement Hints for Workers
image: https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/og.png?v=6adc7aef4e43f5e0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 22, 2026

## New Placement Hints for Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure Workers to run close to infrastructure in legacy cloud regions to minimize latency to existing services and databases. This is most useful when your Worker makes multiple round trips.

To [set a placement hint](https://developers.cloudflare.com/workers/configuration/placement/#configure-explicit-placement-hints), set the `placement.region` property in your Wrangler configuration file:

```jsonc
{
	"placement": {
		"region": "aws:us-east-1",
	},
}
```

```toml
[placement]
region = "aws:us-east-1"
```

Placement hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers. Workers run in the [Cloudflare data center ↗︎](https://www.cloudflare.com/network/) with the lowest latency to the specified cloud region.

If your existing infrastructure is not in these cloud providers, expose it to placement probes with `placement.host` for layer 4 checks or `placement.hostname` for layer 7 checks. These probes are designed to locate single-homed infrastructure and are not suitable for anycasted or multicasted resources.

```jsonc
{
	"placement": {
		"host": "my_database_host.com:5432",
	},
}
```

```toml
[placement]
host = "my_database_host.com:5432"
```

```jsonc
{
	"placement": {
		"hostname": "my_api_server.com",
	},
}
```

```toml
[placement]
hostname = "my_api_server.com"
```

This is an extension of [Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/#enable-smart-placement), which automatically places your Workers closer to back-end APIs based on measured latency. When you do not know the location of your back-end APIs or have multiple back-end APIs, set `mode: "smart"`:

```jsonc
{
	"placement": {
		"mode": "smart",
	},
}
```

```toml
[placement]
mode = "smart"
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/#page","headline":"New Placement Hints for Workers","description":"Explicit placement hints for legacy cloud infrastructure.","url":"https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/og.png?v=6adc7aef4e43f5e0","dateModified":"2026-01-22","datePublished":"2026-01-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
