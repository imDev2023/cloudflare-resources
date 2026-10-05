---
description: Configure DDoS attack alert notifications.
title: Set up alerts
image: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts/og.png?v=2145053600e2f830
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Set up alerts

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Another part of preparing for DDoS attacks is knowing when your application is being attacked.

Cloudflare offers notifications for DDoS attacks, which you can set up on your account.

To set up a notification:

1. In the Cloudflare dashboard, go to the **Notifications** page. [Go to **Notifications** ↗](https://dash.cloudflare.com/?to=/:account/notifications)
2. Select **Add**.
3. Select one of the [available DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/#alert-types) depending on your plan and services:
   - HTTP DDoS Attack Alert
   - Layer 3/4 DDoS Attack Alert
   - Advanced HTTP DDoS Attack Alert
   - Advanced Layer 3/4 DDoS Attack Alert
4. Enter a notification name and (optionally) a description.
5. Configure a delivery method for the notification. The available delivery methods depend on your Cloudflare plan. For more information, refer to [Cloudflare Notifications](https://developers.cloudflare.com/notifications/).
6. If you are creating a notification for one of the advanced DDoS attack alerts, select **Next** and define the parameters that will filter the notifications you will receive.
7. Select **Save**.
