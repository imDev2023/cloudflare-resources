---
description: VPC Network bindings using cf1:network now reach destinations connected through Cloudflare WAN on-ramps (GRE, IPsec, CNI), in addition to Cloudflare Mesh nodes and subnet or hostname routes announced through Cloudflare Tunnel or Mesh.
title: Reach Cloudflare WAN destinations from Workers VPC
image: https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/og.png?v=f0707f8ed3253151
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 21, 2026

## Reach Cloudflare WAN destinations from Workers VPC

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings with `network_id: "cf1:network"` to reach your full private network from Workers, including:

- [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes and client devices
- Subnet routes and hostname routes announced through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) or Cloudflare Mesh
- Destinations connected through [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) on-ramps — GRE, IPsec, and CNI

This means a single VPC Network binding can route Worker requests to private services regardless of how those services are connected to Cloudflare: through a Cloudflare Tunnel from a cloud VPC, a Mesh node on a private subnet, or a Cloudflare WAN on-ramp from your data center or branch site.

```jsonc
{
	"vpc_networks": [
		{
			"binding": "PRIVATE_NETWORK",
			"network_id": "cf1:network",
			"remote": true,
		},
	],
}
```

```toml
[[vpc_networks]]
binding = "PRIVATE_NETWORK"
network_id = "cf1:network"
remote = true
```

At runtime, the URL you pass to `fetch()` determines the destination:

```js
// Reach a service behind a Cloudflare WAN IPsec on-ramp
const response = await env.PRIVATE_NETWORK.fetch("http://10.50.0.100:8080/api");
```

Note

For destinations behind Cloudflare WAN on-ramps (GRE, IPsec, or CNI), your network must route the [Cloudflare source IP range](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/) back through the on-ramp so reply traffic returns to Cloudflare. Without this route, stateful flows will fail. This is part of standard Cloudflare WAN onboarding.

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/#page","headline":"Reach Cloudflare WAN destinations from Workers VPC","description":"VPC Network bindings using cf1:network now reach destinations connected through Cloudflare WAN on-ramps (GRE, IPsec, CNI), in addition to Cloudflare Mesh nodes and subnet or hostname routes announced through Cloudflare Tunnel or Mesh.","url":"https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/og.png?v=f0707f8ed3253151","dateModified":"2026-05-21","datePublished":"2026-05-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
