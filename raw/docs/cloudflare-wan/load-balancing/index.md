---
description: Load balance traffic across WAN tunnel endpoints.
title: Load Balancing
image: https://developers.cloudflare.com/cloudflare-wan/load-balancing/og.png?v=dc192e07558887ab
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Load Balancing

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/load-balancing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If your network has multiple paths to the same destination — for example, redundant tunnels to a data center — you can use Cloudflare Load Balancing to distribute traffic across those paths. This prevents any single path from becoming a bottleneck and allows traffic to fail over automatically if a path goes down.

Cloudflare WAN (formerly Magic WAN) uses Private Network Load Balancing, which balances traffic across your private network endpoints. It supports both on-ramping (traffic entering Cloudflare's network) and off-ramping (traffic exiting to your sites).

Refer to [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) for more information about the feature and how to set it up. Before using this feature, [enable Load Balancing](https://developers.cloudflare.com/load-balancing/).
