---
description: Connect to Cloudflare WAN with Network Interconnect.
title: Network Interconnect (CNI)
image: https://developers.cloudflare.com/cloudflare-wan/network-interconnect/og.png?v=d301aad9dd2fd976
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Network Interconnect (CNI)

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/network-interconnect/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare WAN (formerly Magic WAN) typically connects to Cloudflare through IPsec or GRE tunnels over the public Internet. Cloudflare Network Interconnect (CNI) is an alternative that provides a private, dedicated link — useful when you need lower latency, more consistent throughput, or want to avoid public Internet transit entirely.

Cloudflare Network Interconnect (CNI) provides a private, dedicated connection between your network and Cloudflare — bypassing the public Internet entirely. This is useful when you need consistent latency, higher throughput, or an additional layer of security that public Internet paths cannot guarantee.

With CNI, you get the same Cloudflare network services (firewall, routing, traffic management) applied to your traffic, but over a connection that does not traverse shared Internet infrastructure.

For more information about Network Interconnect, refer to the [Cloudflare Network Interconnect documentation](https://developers.cloudflare.com/network-interconnect/).

Run \<code>traceroute\</code>

If you connect through [GRE](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/), [IPsec](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/), [CNI](https://developers.cloudflare.com/network-interconnect/), or [WARP](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) and want to run `traceroute` to an endpoint behind a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), you need to change some settings.

Refer to [Run `traceroute`](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/traceroute/) for more information.
