---
description: Enable the Web Application Firewall.
title: Enable WAF
image: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/enable-waf/og.png?v=17b616810d8b4f5b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enable WAF

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/enable-waf/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Once you [proxy your DNS records](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/), you should enable rulesets for Cloudflare's [Web Application Firewall (WAF)](https://developers.cloudflare.com/waf/).

The available rulesets depend on your zone's plan, but all customers have access at least to the Cloudflare Free Managed Ruleset, which provides mitigations against high and wide-impacting vulnerabilities.

For more details and potential customizations, refer to [Managed rulesets](https://developers.cloudflare.com/waf/managed-rules/).
