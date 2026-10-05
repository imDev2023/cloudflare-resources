---
description: Learn about create cipa policy in this guide.
title: Create CIPA policy
image: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/og.png?v=b2500901b8656e48
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Create CIPA policy

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Create CIPA policy

1. Go to **Traffic policies** > **Firewall policies**.
2. Create a policy to block using the CIPA filter:

   | Selector | Operator | Value | Action |
   | --- | --- | --- | --- |
   | Content Categories | in | *CIPA Filter* | Block |
3. In **Logs** > **Gateway** > **DNS**, verify that you see the blocked domain.

Your environment is now protected against all of the subcategories listed in [Configuration](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/#configuration).
