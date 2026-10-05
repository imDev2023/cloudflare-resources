---
description: Actions available in custom load balancing rules.
title: Actions
image: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/og.png?v=cf508f5bb5f495fe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/load-balancing/llms.txt  
> Use this file to discover all available pages before exploring further.

# Actions

Last updated Sep 10, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Add **actions** to customize how your load balancer responds to certain HTTP requests.

Each load balancing rule includes one or more actions.

## Supported Actions

This table lists the actions available for Load Balancing rules. For a walkthrough, refer to [Create Load Balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/).

| Action | Options | Description |
| --- | --- | --- |
| *Fixed response* | *N/A* | Respond to the request with an HTTP status code and an optional message. |
| *Override* | *Session affinity* | Set the [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/) for the request. You can customize cookie behavior and session time-to-live (TTL). |
| *Override* | *Load balancer TTL* | Customize the load balancer session time-to-live (TTL). |
| *Override* | *Steering policy* | Update the [steering policy](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/) associated with your load balancer. |
| *Override* | *Fallback pool* | Update the [fallback pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/#off---failover) associated with your load balancer. |
| *Override* | *Pools* | Update the [pools](https://developers.cloudflare.com/load-balancing/pools/) associated with your load balancer. |
| *Override* | *Region pools* | Update the [region pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/) associated with your load balancer. |
| *Override* | *Country pools* | Update the [country pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/) associated with your load balancer. |
| *Override* | *Terminates* | Stop processing Load Balancing rules and apply the current load balancing logic to the request. |
