---
description: Troubleshoot common alert configuration errors.
title: Common errors
image: https://developers.cloudflare.com/notifications/reference/common-errors/og.png?v=9b00279b3a712300
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/notifications/llms.txt  
> Use this file to discover all available pages before exploring further.

# Common errors

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/notifications/reference/common-errors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Webhook test failed with status code 400 Bad Request

This error can occur when you try to configure a webhook that is not currently supported, such as setting up a PagerDuty webhook. PagerDuty needs to be configured under [connected services](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/), not as a webhook.

## Deleted users are still receiving alerts

When you remove a user from your account via **Manage Account** > **Members** in the Cloudflare dashboard, their email address is not removed from existing alerts. You need to remove their email address by [editing the alert](https://developers.cloudflare.com/notifications/get-started/#manage-alerts).
