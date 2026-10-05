---
description: Connect to the Internal DNS Gateway resolver.
title: Connect to Gateway resolver
image: https://developers.cloudflare.com/dns/internal-dns/connectivity/og.png?v=a784affe3f64863d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dns/llms.txt  
> Use this file to discover all available pages before exploring further.

# Connect to Gateway resolver

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dns/internal-dns/connectivity/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To connect to Cloudflare Gateway resolver - which is [required to reach private resources in Internal DNS](https://developers.cloudflare.com/dns/internal-dns/#architecture-overview) - you can use the following options:

- DNS endpoints supported with [DNS locations](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/)
  - DNS over UDP/TCP port 53 (IPv4 or IPv6)
  - DNS over TLS
  - DNS over HTTPS
- [Proxy Auto-Configuration (PAC) files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/)
- [WARP device client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)
- [Clientless browser isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#filter-dns-queries)
- [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/)
