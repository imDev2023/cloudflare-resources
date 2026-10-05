---
description: Regenerate Cloudflare API token secrets to rotate credentials and maintain account security.
title: Roll tokens
image: https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/og.png?v=2494fa0d8284674c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/fundamentals/llms.txt  
> Use this file to discover all available pages before exploring further.

# Roll tokens

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the [scannable format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which allows credential scanning tools to detect leaked tokens.

To roll your API token:

1. Go to **My Profile** > **API Tokens**. [Go to **API Tokens** ↗](https://dash.cloudflare.com/profile/api-tokens)
2. Next to the API token you want to roll, select the **three dot icon** > **Roll**.
3. Select **Confirm** to generate a new API token.
