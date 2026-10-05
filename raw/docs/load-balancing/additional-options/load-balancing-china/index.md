---
description: Use Load Balancing with the China Network.
title: Load Balancing with the China Network
image: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/og.png?v=a0093b5caf2ad1e2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/load-balancing/llms.txt  
> Use this file to discover all available pages before exploring further.

# Load Balancing with the China Network

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Prerequisites

To enable load balancers to be deployed to the [China Network](https://developers.cloudflare.com/china-network/), your zone will need to meet the following two criteria:

1. A valid [ICP license](https://developers.cloudflare.com/china-network/concepts/icp/) for the zone in question.
2. The zone must be provisioned with access to the China Network.

Once these two criteria are met, any newly created load balancer will be automatically deployed to the China Network. When choosing a region for a pool's health checks, `China` is now available to be selected in both the dashboard and API.

You can also create a load balancer by sending a `POST` request to the following endpoint. To deploy to the China Network with the API, the `networks` array in the API call must contain `jdcloud` as a value in addition to `cloudflare`. Refer to the [Cloudflare API documentation](https://developers.cloudflare.com/api/resources/load_balancers/methods/create/) for details on the required fields and their formats.

```bash
https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers
```

## Limitations

Load balancers deployed to the China Network currently have the following limitations:

- Only cookie-based session affinity is supported.
- Private network off-ramps (Tunnel, GRE, IPsec) are not supported.
- Private Network Load Balancing is not available on the China Network.
