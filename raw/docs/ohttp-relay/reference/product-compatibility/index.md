---
description: Cloudflare products that are and are not compatible with Cloudflare OHTTP Relay, including API Shield, Cache, and WAF.
title: Product compatibility
image: https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/og.png?v=496f9b822fad9830
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ohttp-relay/llms.txt  
> Use this file to discover all available pages before exploring further.

# Product compatibility

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When [using Cloudflare OHTTP Relay (formerly Privacy Gateway)](https://developers.cloudflare.com/ohttp-relay/get-started/), the majority of Cloudflare products will be compatible with your application.

However, the following products are not compatible:

- [API Shield](https://developers.cloudflare.com/api-shield/): [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/) and [API discovery](https://developers.cloudflare.com/api-shield/security/api-discovery/) are not possible since Cloudflare cannot see the request URLs.
- [Cache](https://developers.cloudflare.com/cache/): Caching of application content is no longer possible since each between client and gateway is end-to-end encrypted.
- [WAF](https://developers.cloudflare.com/waf/): Rules implemented based on request content are not supported since Cloudflare cannot see the request or response content.
