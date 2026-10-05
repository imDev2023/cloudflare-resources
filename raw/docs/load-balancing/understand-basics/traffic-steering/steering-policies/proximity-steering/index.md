---
description: Route traffic to the nearest pool by geographic proximity.
title: Proximity
image: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/og.png?v=b895d9873fb4450e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/load-balancing/llms.txt  
> Use this file to discover all available pages before exploring further.

# Proximity

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Proximity steering** routes visitors or internal services to the closest physical data center.

To use proximity steering on a load balancer, you first need to add GPS coordinates to each pool.

## When to add proximity steering

- For new pools, add GPS coordinates when you create a pool.
- For existing pools, add GPS coordinates when [managing pools](https://developers.cloudflare.com/load-balancing/pools/create-pool/#edit-a-pool) or in the **Add Traffic steering** step of [creating a load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/).

## How to add proximity steering

To add coordinates when creating or editing a pool:

1. Click the *Configure coordinates for Proximity Steering* dropdown.
2. Enter the latitude and longitude or drag a marker on the map.
3. Select **Save**.

Warning:

For accurate proximity steering, add GPS coordinates to all pools within the same load balancer.
