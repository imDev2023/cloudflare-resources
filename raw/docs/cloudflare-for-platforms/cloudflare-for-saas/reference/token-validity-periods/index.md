---
description: DCV token expiration periods by certificate authority for TXT validation.
title: Token validity periods
image: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/og.png?v=c01fe50d5b613565
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-for-platforms/llms.txt  
> Use this file to discover all available pages before exploring further.

# Token validity periods

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you perform [TXT](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/) domain control validation, you will need to share these tokens with your customers.

However, these tokens expire after a certain amount of time, depending on your chosen certificate authority.

| Certificate authority | Token validity |
| --- | --- |
| Let's Encrypt | 7 days |
| Google Trust Services | 14 days |
| SSL.com | 14 days |

Caution

Tokens may also become invalid upon validation failure. For more details, refer to [Domain control validation flow](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/#dcv-tokens).
