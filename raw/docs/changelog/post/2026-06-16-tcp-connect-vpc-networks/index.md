---
description: VPC Network bindings now support the connect() Socket API for raw TCP connections, in addition to HTTP traffic via fetch(). Workers can open TCP sockets to any private destination reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp.
title: TCP connections via connect() over VPC Networks
image: https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/og.png?v=9ef6b4a8ef064564
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 16, 2026

## TCP connections via connect() over VPC Networks

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now support the [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via `fetch()`.

This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "vpc_networks": [
    {
      "binding": "PRIVATE_NETWORK",
      "network_id": "cf1:network",
      "remote": true
    }
  ]
}
```

```toml
[[vpc_networks]]
binding = "PRIVATE_NETWORK"
network_id = "cf1:network"
remote = true
```

At runtime, use `connect()` on the binding to open a TCP socket to a private destination:

```ts
export default {
	async fetch(request: Request, env: Env) {
		// Open a TCP connection to a private Redis instance
		const socket = await env.PRIVATE_NETWORK.connect("10.0.1.50:6379");

		// Write a Redis PING command
		const writer = socket.writable.getWriter();
		await writer.write(new TextEncoder().encode("PING\r\n"));
		await writer.close();

		return new Response(socket.readable);
	},
};
```

Note

`connect()` over VPC Networks currently supports plaintext TCP only.

For more details, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and the [Workers Binding API](https://developers.cloudflare.com/workers-vpc/api/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/#page","headline":"TCP connections via connect() over VPC Networks","description":"VPC Network bindings now support the connect() Socket API for raw TCP connections, in addition to HTTP traffic via fetch(). Workers can open TCP sockets to any private destination reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp.","url":"https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/og.png?v=9ef6b4a8ef064564","dateModified":"2026-06-16","datePublished":"2026-06-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
