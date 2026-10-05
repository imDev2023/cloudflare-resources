---
description: Enable user roles for Network Firewall management.
title: Enable user roles
image: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/og.png?v=39c6807a8367a0e1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-network-firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enable user roles

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can determine which users have, or do not have, configuration edit access for Magic products, including Magic Transit, Cloudflare WAN (formerly Magic WAN), and Cloudflare Network Firewall.

For example, if multiple teams manage different Cloudflare products on the same account, you can provide select users with edit access and other users with read-only access.

## Assign permissions

1. Go to the **Members** page. [Go to **Members** ↗](https://dash.cloudflare.com/?to=/:account/members)
2. Under **Members**, enter an existing user's name and select **Search**.
3. Expand the menu at the end of the user row.
4. From the list, locate **Network Services (Magic)**.
5. Select one of two options:
   - **Network Services (Magic)** - Enables users to view and edit Magic configurations.
   - **Network Services (Magic, Read-Only)** - Enables users to view but not modify Magic configurations.
