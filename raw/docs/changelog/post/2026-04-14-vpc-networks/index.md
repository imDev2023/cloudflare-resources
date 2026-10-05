---
description: Workers can now access entire private networks through VPC Network bindings, with support for Cloudflare Tunnel and Cloudflare Mesh.
title: VPC Networks and Cloudflare Mesh support now in public beta
image: https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/og.png?v=a9e36dbdbd6619bb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 14, 2026

## VPC Networks and Cloudflare Mesh support now in public beta

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing [VPC Service](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/) bindings, which scope each binding to a specific host and port.

You can bind to a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) by `tunnel_id` to reach any service on the network where that tunnel is running, or bind to your [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) network using `cf1:network` to reach any Mesh node, client device, or subnet route in your account:

```jsonc
{
  "vpc_networks": [
    {
      "binding": "MESH",
      "network_id": "cf1:network",
      "remote": true
    }
  ]
}
```

```toml
[[vpc_networks]]
binding = "MESH"
network_id = "cf1:network"
remote = true
```

At runtime, `fetch()` routes through the network to reach the service at the IP and port you specify:

```js
const response = await env.MESH.fetch("http://10.0.1.50:8080/api/data");
```

For configuration options and examples, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and [Connect Workers to Cloudflare Mesh](https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/#page","headline":"VPC Networks and Cloudflare Mesh support now in public beta","description":"Workers can now access entire private networks through VPC Network bindings, with support for Cloudflare Tunnel and Cloudflare Mesh.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/og.png?v=a9e36dbdbd6619bb","dateModified":"2026-04-14","datePublished":"2026-04-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
