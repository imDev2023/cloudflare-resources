---
description: How Notifications works in Zero Trust networking.
title: Notifications
image: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/og.png?v=d6a52aa95b07605c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Notifications

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Administrators can receive an alert when Cloudflare Tunnels in an account change their health or deployment status. Notifications can be delivered via email, webhook, and third-party services.

## Manage notifications

Tunnel notifications are configured on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/). For more information, refer to [Create a notification](https://developers.cloudflare.com/notifications/get-started/#create-an-alert).

## Available notifications

<details>

<summary>

Tunnel Creation or Deletion Event

</summary>

**Who is it for?**

Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

No action is needed.

</details>

<details>

<summary>

Tunnel Health Alert

</summary>

**Who is it for?**

Customers who want to be warned about changes in health status for their Cloudflare Tunnels.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

Monitor tunnel health over time and consider deploying <a href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas or load balancers</a>.

**Additional information**

Refer to <a href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">Tunnel status</a> to review the list of possible tunnel statuses (<code>Healthy</code>, <code>Inactive</code>, <code>Down</code> and <code>Degraded</code>).

</details>
