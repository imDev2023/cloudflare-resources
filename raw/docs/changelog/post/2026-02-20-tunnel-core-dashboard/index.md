---
description: Create and configure Tunnels for public applications, Workers VPC, and Load Balancing without leaving the Core Dashboard — now with native integrations and unified visibility.
title: Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard
image: https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/og.png?v=950d8af58e46aa02
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 20, 2026

## Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) is now available in the main Cloudflare Dashboard at [Networking > Tunnels ↗︎](https://dash.cloudflare.com/?to=/:account/tunnels), bringing first-class Tunnel management to developers using Tunnel for securing origin servers.

![Manage Tunnels in the Core Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=894,format=webp/_astro/tunnel-core-dashboard.BGPqaHfo.gif)

This new experience provides everything you need to manage Tunnels for [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), including:

- **Full Tunnel lifecycle management**: Create, configure, delete, and monitor all your Tunnels in one place.
- **Native integrations**: View Tunnels by name when configuring [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) and [Workers VPC](https://developers.cloudflare.com/workers-vpc/) — no more copy-pasting UUIDs.
- **Real-time visibility**: Monitor [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) and Tunnel [health status](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) directly in the dashboard.
- **Routing map**: Manage all ingress routes for your Tunnel, including [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/), [private CIDRs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/), and [Workers VPC services](https://developers.cloudflare.com/workers-vpc/), from a single interactive interface.

#### Choose the right dashboard for your use case

**Core Dashboard**: Navigate to [Networking > Tunnels ↗︎](https://dash.cloudflare.com/?to=/:account/tunnels) to manage Tunnels for:

- Securing origin servers and [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/) with CDN, WAF, Load Balancing, and DDoS protection
- Connecting [Workers to private services](https://developers.cloudflare.com/workers-vpc/) via Workers VPC

**Cloudflare One Dashboard**: Navigate to [Zero Trust > Networks > Connectors ↗︎](https://one.dash.cloudflare.com/?to=/:account/networks/connectors) to manage Tunnels for:

- Securing your public applications with [Zero Trust access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)
- Connecting users to [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/)
- Building a [private mesh network](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-networks)

Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.

#### Get started

New to Tunnel? Learn how to [get started with Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/) or explore advanced use cases like [securing SSH servers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/) or [running Tunnels in Kubernetes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/#page","headline":"Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard","description":"Create and configure Tunnels for public applications, Workers VPC, and Load Balancing without leaving the Core Dashboard — now with native integrations and unified visibility.","url":"https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/og.png?v=950d8af58e46aa02","dateModified":"2026-02-20","datePublished":"2026-02-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
