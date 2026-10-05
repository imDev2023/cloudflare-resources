---
description: Control how traffic is distributed across pools and origins.
title: Traffic steering
image: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/og.png?v=235cf4fba340cc16
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/load-balancing/llms.txt  
> Use this file to discover all available pages before exploring further.

# Traffic steering

Last updated Sep 10, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When requests come to your load balancer, it distributes them across your pools and endpoints according to four factors:

1. [Pool and endpoint health](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/): Traffic decisions start with which pools and endpoints are available and should receive traffic.
2. [Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/): The preferred way to define new API-managed location routing. A matched pool set can replace pool selection and provide its own steering policy, weights, and fallback pool.
3. [Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/): Policies set on your [load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/) that route traffic to attached and available pools.
4. [Local traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/): These are policies set on each [pool](https://developers.cloudflare.com/load-balancing/pools/) that route traffic to available endpoints within the pool.

When a pool or endpoint becomes unhealthy, your load balancer and pools redistribute traffic according to these same policies.
