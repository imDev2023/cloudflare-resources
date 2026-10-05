---
description: Distribute requests randomly across origins.
title: Random
image: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/random-origin-steering/og.png?v=431fdf646fe82d0d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/load-balancing/llms.txt  
> Use this file to discover all available pages before exploring further.

# Random

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/random-origin-steering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Random steering** sends requests to endpoints purely based on [endpoint weights](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights). Distributes traffic more accurately, but may cause requests from the same IP to hit different endpoints.
