---
description: Remove Appliances from your account.
title: Remove appliances
image: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/og.png?v=b815deaf542b182a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Remove appliances

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When adding or removing Cloudflare One Appliances (formerly Magic WAN Connectors), you need to be aware of the difference between the physical device and its profile.

- The physical device is the hardware at your site.
- The profile contains the configuration that allows the device to connect to Cloudflare, including your WANs, LANs, traffic steering, and LAN policies.

You can have more than one Cloudflare One Appliance in one profile if you initially enabled high availability during the configuration of the profile. If you did not enable high availability, you need to delete the profile associated with a site before adding a new Cloudflare One Appliance.

## Remove a profile

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to **Appliances** > **Profiles**.
3. Find the profile that you want to edit > select the three dots next to it > **Delete**.

## Remove a physical device

To remove a Cloudflare One Appliance from your account:

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Appliances**.
3. Find the Cloudflare One Appliance that you want to delete > select the three dots next to it > **Delete**.
