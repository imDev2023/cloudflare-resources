---
description: Pool sets combine geographic matching with location-specific steering policies, weights, pools, and fallback behavior.
title: Load Balancing now supports pool sets
image: https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/og.png?v=86096fd4224d7fe6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 31, 2026

## Load Balancing now supports pool sets

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.

Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.

For example, this pool set uses Dynamic Latency steering for traffic from Germany:

```json
{
	"pool_sets": [
		{
			"name": "germany-lowest-latency",
			"match": { "topology": { "countries": ["DE"] } },
			"overrides": {
				"pools": [
					"0930eec54a4c7ae6616985b79f678210",
					"c8b4f5a6d7e84910a2b3c4d5e6f70819"
				],
				"steering_policy": "dynamic_latency"
			}
		}
	]
}
```

Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.

For configuration details and more examples, refer to [Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/#page","headline":"Load Balancing now supports pool sets","description":"Pool sets combine geographic matching with location-specific steering policies, weights, pools, and fallback behavior.","url":"https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/og.png?v=86096fd4224d7fe6","dateModified":"2026-08-31","datePublished":"2026-08-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
