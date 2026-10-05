---
description: Use Cloudflare as a secondary DNS provider.
title: Cloudflare as Secondary
image: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/og.png?v=8c4a0b046aff07a4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dns/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cloudflare as Secondary

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.

When you make edits in your primary DNS provider, those DNS records will be transferred from your primary DNS provider to Cloudflare via zone transfer using [AXFR ↗︎](https://datatracker.ietf.org/doc/html/rfc5936) or [IXFR ↗︎](https://datatracker.ietf.org/doc/html/rfc1995).

```
flowchart LR
accTitle: Cloudflare as Secondary DNS
A((Zone Admin)) --DNS record <br /> management--> B[Primary DNS <br /> provider]
B --Zone transfer--> C[Cloudflare <br /> DNS]
B & C <--DNS lookups--> D[Resolver] <--DNS lookups--> E((User))

```

## How to

- [Set up incoming zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/)
- Proxy traffic through Cloudflare with [Secondary DNS Override](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/)

## Availability

Secondary DNS is only available to Enterprise customers. For more details on activation and pricing, contact your account team.
