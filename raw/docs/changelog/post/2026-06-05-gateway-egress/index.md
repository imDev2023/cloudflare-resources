---
description: Workers using cf1:network now egress to the public Internet through Cloudflare Gateway — with policies enforced and DNS, HTTP, and Network logging.
title: Filter Workers' public Internet traffic using Gateway policies
image: https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/og.png?v=2e2cbf7c43a14718
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 5, 2026

## Filter Workers' public Internet traffic using Gateway policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers using a [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) binding with `network_id: "cf1:network"` now egress to public Internet destinations through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/). This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.

1. [Worker](https://developers.cloudflare.com/workers/)

   Calls `env.EGRESS.fetch()`
2. [VPC binding](https://developers.cloudflare.com/workers-vpc/)↓
3. [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

   Bind via [`cf1:network`](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/)
4. ↓
5. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

   Policies applied: [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/) [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)
6. ↓
7. ↗Public Internet

   Any public hostname or IP

[Gateway logsDNSHTTPNetwork](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)

What you get by default:

- **Visibility.** Worker egress shows up in Gateway [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) logs alongside your other traffic, so you can audit what your Workers are calling and when.
- **Enforcement.** Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.

```jsonc
{
	"vpc_networks": [
		{
			"binding": "EGRESS",
			"network_id": "cf1:network",
			"remote": true,
		},
	],
}
```

```toml
[[vpc_networks]]
binding = "EGRESS"
network_id = "cf1:network"
remote = true
```

```js
// Egress to a public destination — subject to your Gateway policies and logged
const response = await env.EGRESS.fetch("https://api.example.com/data");
```

```ts
// Egress to a public destination — subject to your Gateway policies and logged
const response = await env.EGRESS.fetch("https://api.example.com/data");
```

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/). For policy authoring, refer to [Cloudflare Gateway traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/#page","headline":"Filter Workers' public Internet traffic using Gateway policies","description":"Workers using cf1:network now egress to the public Internet through Cloudflare Gateway — with policies enforced and DNS, HTTP, and Network logging.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/og.png?v=2e2cbf7c43a14718","dateModified":"2026-06-05","datePublished":"2026-06-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
