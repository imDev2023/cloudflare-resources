---
description: Learn about verify local connectivity in this guide.
title: Verify local connectivity
image: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-verify-local-connectivity/og.png?v=1d8a93134420870d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Verify local connectivity

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-verify-local-connectivity/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To verify that your DNS traffic is sent to Gateway:

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Traffic settings**.
2. Under **Log traffic activity**, enable activity logging for all DNS logs.
3. On your device, open a browser and go to any website.
4. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights** > **Logs** > **DNS**.
5. Make sure DNS queries from your device appear.
