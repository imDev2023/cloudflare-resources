---
description: Cloudflare Mesh connects your services and devices with post-quantum encrypted mesh networking. Route traffic privately between servers, laptops, and phones without VPNs or bastion hosts.
title: Introducing Cloudflare Mesh
image: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/og.png?v=0aa49fe65041f8f4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 14, 2026

## Introducing Cloudflare Mesh

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) is now available ([blog post ↗︎](https://blog.cloudflare.com/mesh/)). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.

![Cloudflare Mesh network map showing nodes and devices connected through Cloudflare](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2070,height=875,format=webp/_astro/mesh-network-map.CED6jNHK.gif)

#### What Cloudflare Mesh does

- Assigns a private [Mesh IP](https://developers.cloudflare.com/mesh/concepts/#mesh-ips) to every enrolled device and node.
- Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.
- Supports [CIDR routes](https://developers.cloudflare.com/mesh/features/routes/) for subnet routing through Mesh nodes.
- Supports [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) with active-passive replicas for nodes with routes.
- All traffic flows through Cloudflare, so [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/), [device posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/), and access rules apply to every connection.

#### What changed

- **WARP Connector** is now **Cloudflare Mesh**. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.
- **Peer-to-peer connectivity** is now called **Mesh connectivity** and is part of the Cloudflare Mesh documentation.
- **Mesh node limit** increased from 10 to **50 per account**.
- New [dashboard experience ↗︎](https://dash.cloudflare.com/?to=/:account/mesh) at **Networking** > **Mesh** with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.

#### Get started

Refer to the [Cloudflare Mesh documentation](https://developers.cloudflare.com/mesh/) to set up your first Mesh network.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/#page","headline":"Introducing Cloudflare Mesh","description":"Cloudflare Mesh connects your services and devices with post-quantum encrypted mesh networking. Route traffic privately between servers, laptops, and phones without VPNs or bastion hosts.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/og.png?v=0aa49fe65041f8f4","dateModified":"2026-04-14","datePublished":"2026-04-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
