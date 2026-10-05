---
description: Restrict access to your Web3 gateway with WAF custom rules.
title: Restrict gateway access
image: https://developers.cloudflare.com/web3/how-to/restrict-gateway-access/og.png?v=5ca0e1e6b831371c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/web3/llms.txt  
> Use this file to discover all available pages before exploring further.

# Restrict gateway access

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/web3/how-to/restrict-gateway-access/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you are using a [Web3 gateway](https://developers.cloudflare.com/web3/about/) for internal application calls, you may want to restrict gateway access to specific backend services.

You can achieve this goal by [creating general Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) to block normal traffic and then [creating service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/) to allow access by your backend service.
