---
description: Deploy Keyless SSL key servers with high availability.
title: High availability
image: https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/og.png?v=ad3bde2e14789538
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ssl/llms.txt  
> Use this file to discover all available pages before exploring further.

# High availability

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Keyless SSL server runs as a single binary with minimal dependencies and is designed to be robust and reliable. However, the network between your key server and Cloudflare may not be, which could prevent new TLS connections.

For this reason, we strongly recommend that you run at least two key servers in a high availability configuration behind a load balancer. Set up health checks for each key server on the configured TCP port—2407 by default and failover as necessary or round-robin between active (healthy) key servers.

From a network availability and performance perspective, advertise the IP address of your key server from multiple data centers (an anycast setup) so the Cloudflare global network can route to the closest key server via BGP. When you use anycast routing, you can also safely take a data center offline to perform maintenance.
