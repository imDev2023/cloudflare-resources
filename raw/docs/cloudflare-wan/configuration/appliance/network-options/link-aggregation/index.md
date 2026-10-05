---
description: Bundle physical LAN ports into a single logical interface for redundancy and bandwidth.
title: Configure link aggregation groups
image: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/og.png?v=c6f554f5a2fa4746
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configure link aggregation groups

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can bundle multiple physical LAN ports on a Cloudflare One Appliance into a single logical port called a Link Aggregation Group (LAG). This increases LAN bandwidth and provides redundancy. If a member port fails, traffic automatically shifts to the remaining ports in under one second.

Note

Your appliance must be running OS version 2026.2.0 or later. This version deploys automatically.

The following guide assumes you have already created a site and configured your Cloudflare One Appliance. For instructions, refer to [Configure hardware Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/) or [Configure virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

## Create a LAG

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Profiles**.
3. Select the Cloudflare One Appliance you want to configure > **Edit**.
4. Go to the **Appliances** tab.
5. In **Link aggregation groups (LAGs)**, select **Create A LAG**.
6. Select the LAN ports you want to bundle. You can add up to six ports per LAG. All ports must be the same type and speed.
7. Select **Save**.

## Assign a LAN to a LAG

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Profiles**.
3. Select the Cloudflare One Appliance you want to edit > **Edit**.
4. Go to **Network Configuration** > **LAN configuration**.
5. Select or create a LAN > **Edit**.
6. In **Interface** > **Interface type**, select **Aggregate** as your LAG instead of a single port.
7. Select **Save**.

## Monitor LAG status

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Profiles**.
3. Select the Cloudflare One Appliance > **Edit**.
4. Go to the **Appliances** tab.

The page displays each configured LAG and the status of its member ports.

## Delete a LAG

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Profiles**.
3. Select the Cloudflare One Appliance > **Edit**.
4. Go to the **Appliances** tab.
5. Next to the LAG you want to delete, select the three-dot menu > **Delete**.
6. Select **Delete**.
