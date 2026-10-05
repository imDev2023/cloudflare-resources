---
description: Set up webhooks to receive notifications when Cloudflare Images direct creator uploads succeed or fail.
title: Configure webhooks
image: https://developers.cloudflare.com/images/storage/upload-images/configure-webhooks/og.png?v=f39359d7b63e799f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configure webhooks

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/configure-webhooks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Webhooks are available on all plans. Accounts without a paid zone can configure up to 100 webhook destinations.

You can set up webhooks to receive notifications about your upload workflow. This will send an HTTP POST request to a specified endpoint when an image either successfully uploads or fails to upload.

Currently, webhooks are supported only for [direct creator uploads](https://developers.cloudflare.com/images/storage/upload-images/direct-creator-upload/).

To receive notifications for direct creator uploads:

1. In the Cloudflare dashboard, go to the **Notifications** pages. [Go to **Notifications** ↗](https://dash.cloudflare.com/?to=/:account/notifications)
2. Select **Destinations**.
3. From the Webhooks card, select **Create**.
4. Enter information for your webhook and select **Save and Test**. The new webhook will appear in the **Webhooks** card and can be attached to notifications.
5. Next, go to **Notifications** > **All Notifications** and select **Add**.
6. Under the list of products, locate **Images** and select **Select**.
7. Give your notification a name and optional description.
8. Under the **Webhooks** field, select the webhook that you recently created.
9. Select **Save**.
