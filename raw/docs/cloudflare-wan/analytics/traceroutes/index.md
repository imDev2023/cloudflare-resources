---
description: Run traceroutes across your WAN network.
title: Traceroutes
image: https://developers.cloudflare.com/cloudflare-wan/analytics/traceroutes/og.png?v=4e7ceb0943c0986e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Traceroutes

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/analytics/traceroutes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can run traceroutes to analyze the hop-by-hop Internet path and latency between Cloudflare's network and your network.

To run a traceroute from a specific Cloudflare data center to your network:

1. Go to the **Network health** page.

[Go to **Network health** ↗](https://dash.cloudflare.com/?to=/:account/networking-insights/health)

2. Select **Connector health**.
3. Select the tunnel for the traceroute.
4. Select the three dots > **Traceroute details**.

You can access detailed data from the traceroute, including:

- Time to live (TTL) and host
- Autonomous system (AS) number
- [Packets ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) sent in the traceroute
- Average, minimum, and maximum latency
- Standard deviation of latency
