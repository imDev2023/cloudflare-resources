---
description: Configure scoped or unscoped client-side resource alerts to get notified about relevant client-side changes on your zones.
title: Configure an alert
image: https://developers.cloudflare.com/client-side-security/alerts/configure/og.png?v=642483007d445d62
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/client-side-security/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configure an alert

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/client-side-security/alerts/configure/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To configure an alert:

1. In the Cloudflare dashboard, go to the **Notifications** page. [Go to **Notifications** ↗](https://dash.cloudflare.com/?to=/:account/notifications)
2. Choose **Add** and then select **Client-side security (formerly Page Shield)** in the **Product** dropdown.
3. Select an [alert type](https://developers.cloudflare.com/client-side-security/alerts/alert-types/).
4. Enter the notification name and description.
5. (Optional) If you are a customer with Client-Side Security Advanced, you can [define the zones for which you want to filter alerts](https://developers.cloudflare.com/client-side-security/alerts/#scoped-alerts) in **Rules of these zones**. This option requires that you define [content security rules](https://developers.cloudflare.com/client-side-security/rules/) in the selected zones.
6. Select one or more notification destinations (notification email, webhooks, and connected notification services).
7. Select **Create**.

## Manage alerts

To edit, delete, or disable an alert, go to the **Notifications** page.

[Go to **Notifications** ↗](https://dash.cloudflare.com/?to=/:account/notifications)
