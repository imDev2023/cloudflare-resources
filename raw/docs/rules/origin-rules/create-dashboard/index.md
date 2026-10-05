---
description: Create origin rules in the Cloudflare dashboard.
title: Create an origin rule in the dashboard
image: https://developers.cloudflare.com/rules/origin-rules/create-dashboard/og.png?v=9d89164c92d2dc20
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Create an origin rule in the dashboard

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/origin-rules/create-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

1. In the Cloudflare dashboard, go to the Rules **Overview** page. [Go to **Overview** ↗](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)
2. Select **Create rule** > **Origin Rule**.
3. (Optional) Select one of the rule templates that address common use cases. Then, review and adjust the proposed rule configuration.
4. Enter a descriptive name for the rule in **Rule name**.
5. Under **When incoming requests match**, define the [rule expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/).
6. Under **Set origin parameters**, define the [origin rule settings](https://developers.cloudflare.com/rules/origin-rules/features/) you wish to change for requests matching the rule expression.
7. To save and deploy your rule, select **Deploy**. If you are not ready to deploy your rule, select **Save as Draft**.

   If you are matching a hostname in your rule expression, you may be prompted to create a proxied DNS record for that hostname. Refer to [Troubleshooting](https://developers.cloudflare.com/rules/reference/troubleshooting/#this-rule-may-not-apply-to-your-traffic) for more information.
