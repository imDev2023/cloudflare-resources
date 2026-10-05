---
description: Set up alerts via email, webhooks, or PagerDuty.
title: Configure alerts
image: https://developers.cloudflare.com/notifications/get-started/og.png?v=c4455bad2494d8e0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/notifications/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configure alerts

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/notifications/get-started/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This guide covers creating and managing alerts from the Cloudflare dashboard. For a full list of available alert types, refer to [Available alerts](https://developers.cloudflare.com/notifications/notification-available/).

## Permissions

To create an alert, you need one of the following:

- **Super Administrator** or **Administrator** role in the dashboard
- **Account edit** role (allows creating any alert type)
- An API token with the [Notifications Read/Write permission](https://developers.cloudflare.com/fundamentals/api/reference/permissions/)

Some alert types are only available on Professional, Business, or Enterprise plans, or require a specific Cloudflare product.

## Create an alert

1. In the Cloudflare dashboard, go to **Alerts** > **Overview**. [Go to **Alerts** ↗](https://dash.cloudflare.com/?to=/:account/notifications)
2. Select **Create an Alert**.
3. Choose the alert type you want to create and select **Select**.
4. Name the alert.
5. Add one or more delivery destinations (email, webhook, or PagerDuty).
6. (Optional) Configure any additional options, such as specific domains or services to monitor.
7. Select **Create**.

## Manage alerts

Once created, each alert has an action menu (⋯) with the following options:

- **Edit** — modify the alert name, delivery destinations, or configuration.
- **Disable / Enable** — toggle the alert on or off.
- **Test** — send a test alert with sample data to verify delivery.
- **Mute** — temporarily suppress the alert for a preset duration (**1h**, **12h**, **24h**) or a custom time range. Muted alerts still appear in [Alert history](https://developers.cloudflare.com/notifications/notification-history/) and are marked as silenced.
- **Delete** — permanently remove the alert.

## Manage silences

You can view, edit, or delete existing silences from **Alerts** > **Silences**.

[Go to **Alerts** ↗](https://dash.cloudflare.com/?to=/:account/notifications)
