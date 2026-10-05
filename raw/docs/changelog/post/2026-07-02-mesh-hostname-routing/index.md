---
description: Route traffic to a Cloudflare Mesh node by hostname instead of IP.
title: Hostname routing for Cloudflare Mesh
image: https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/og.png?v=00692aeab6279a14
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 2, 2026

## Hostname routing for Cloudflare Mesh

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now add [hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Cloudflare Mesh node, in addition to CIDR routes.

1. [Client device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

   Requests `wiki.internal.local`
2. DNS query↓
3. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

   Returns a token IP, then rewrites the destination to the real private IP. `172.64.128.0/20`
4. [Hostname route](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes)↓
5. [Mesh node](https://developers.cloudflare.com/mesh/)

   Forwards traffic to the host on the local network
6. ↓
7. Private host

   `wiki.internal.local` · `10.0.0.50`

Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:

- **Private hostname** (for example, `wiki.internal.local`) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.
- **Public hostname** (for example, `www.example.com`) — route that hostname's traffic through the node and egress via the node's public IP.

[Go to **Mesh** ↗](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, prerequisites, and DNS options, refer to [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/#page","headline":"Hostname routing for Cloudflare Mesh","description":"Route traffic to a Cloudflare Mesh node by hostname instead of IP.","url":"https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/og.png?v=00692aeab6279a14","dateModified":"2026-07-02","datePublished":"2026-07-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
