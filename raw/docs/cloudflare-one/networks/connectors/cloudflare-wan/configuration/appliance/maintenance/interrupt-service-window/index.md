---
description: Learn how to set up when Connector can update its systems.
title: Interrupt window
image: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/og.png?v=860cb9ce4b51904c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Interrupt window

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Interrupt window defines when Cloudflare One Appliance (formerly Magic WAN Connector) can update its systems. When Cloudflare One Appliance is updating, this may result in an interruption to existing connections. Set up a time window that minimizes disruption to your sites.

1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), and go to **Networking** > **Connectors**.
2. In **Appliances** > **Appliances**, select the Cloudflare One Appliance for which you want to set up the update window > **Edit**.
3. In **Interrupt window**, select the most appropriate time for the Cloudflare One Appliance to update its systems:
   - **Timezone**: Select the time zone for the Cloudflare One Appliance to update.
   - **Start time**: Choose an hour for the Cloudflare One Appliance to start updating. Cloudflare recommends you choose an hour when there is minimal activity in your network, to avoid potential disruptions.
   - **Duration**: Duration indicates the time window during which the Cloudflare One Appliance is scheduled to update. For example, if you configure your Cloudflare One Appliance to update at `22:00` and specify a **Duration** of `4 hours`, the Cloudflare One Appliance will attempt to update within the four-hour period following `22:00`.
