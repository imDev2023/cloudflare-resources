---
description: Traceroutes in Zero Trust networking.
title: Traceroutes
image: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/traceroutes/og.png?v=d4263d5e20cd3a9c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Traceroutes

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/traceroutes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can run traceroutes to analyze the hop-by-hop Internet path and latency between Cloudflare's network and your network.

To run a traceroute from a specific Cloudflare data center to your network:

1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) > **Insights**.
2. Go to **Network health** > **WAN connector health**.
3. Find the tunnel for the traceroute.
4. Select the three dots > **Traceroute details**.

You can access detailed data from the traceroute, including:

- Time to live (TTL) and host
- Autonomous system (AS) number
- [Packets ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) sent in the traceroute
- Average, minimum, and maximum latency
- Standard deviation of latency
