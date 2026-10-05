---
description: Learn how to set up when Cloudflare One Appliance can update its systems.
title: Interrupt window
image: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/og.png?v=0e9156f8a28b8c6f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Interrupt window

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Interrupt window defines when Cloudflare One Appliance (formerly Magic WAN Connector) can update its systems. When Cloudflare One Appliance is updating, this may result in an interruption to existing connections. Set up a time window that minimizes disruption to your sites.

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Appliances**.
3. Find the Cloudflare One Appliance you want to set up the update window for > **Edit**.
4. In **Interrupt window**, select the most appropriate time for the Cloudflare One Appliance to update its systems:
   - **Timezone**: Select the time zone for the Cloudflare One Appliance to update.
   - **Start time**: Choose an hour for the Cloudflare One Appliance to start updating. Cloudflare recommends you choose an hour when there is minimal activity in your network, to avoid potential disruptions.
   - **Duration**: Duration indicates the time window during which the Cloudflare One Appliance is scheduled to update. For example, if you configure your Cloudflare One Appliance to update at `22:00` and specify a **Duration** of `4 hours`, the Cloudflare One Appliance will attempt to update within the four-hour period following `22:00`.
