---
description: Visual overview of Smart Shield features and their role in origin protection.
title: Network diagram
image: https://developers.cloudflare.com/smart-shield/concepts/network-diagram/og.png?v=f94b2984ede06d82
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/smart-shield/llms.txt  
> Use this file to discover all available pages before exploring further.

# Network diagram

Last updated May 4, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/smart-shield/concepts/network-diagram/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The diagram below shows how requests flow through the Cloudflare network when Smart Shield is active, and where each feature applies along that path.

![Network diagram of requests being processed with all Smart Shield features](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=5596,height=4759,format=webp/_astro/network-diagram.PeUYDGK_.png)

Requests from visitors first reach a nearby lower-tier data center. For static (cacheable) content, the lower-tier checks its local cache. On a cache miss, the request moves to an upper-tier data center — selected by [Smart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/) based on lowest latency to your origin. If [Regional Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/) is configured, a regional hub is checked before the upper-tier. Persistent storage through [Cache Reserve](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/) provides a final cache layer before requesting content from your origin.

For dynamic (non-cacheable) requests, [Argo Smart Routing](https://developers.cloudflare.com/smart-shield/configuration/argo/) finds the fastest network path to your origin. Between Cloudflare's upper-tier data centers and your origin, [connection reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/) packages multiple requests into a single connection, reducing the total number of connections your origin handles.

[Health Checks](https://developers.cloudflare.com/smart-shield/configuration/health-checks/) run from multiple data centers to monitor whether your origin is online and responsive. [Dedicated CDN Egress IPs](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/) provide reserved IP addresses for traffic from Cloudflare to your origin, allowing you to restrict your origin firewall to a small allowlist.
