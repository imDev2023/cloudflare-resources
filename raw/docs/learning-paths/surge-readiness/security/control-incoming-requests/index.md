---
description: Filter incoming requests with WAF rules.
title: Control incoming requests
image: https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/og.png?v=cda05aef0d2e4e23
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Control incoming requests

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Use [Custom rules](https://developers.cloudflare.com/waf/custom-rules/) to allow you to control incoming traffic by filtering requests to a zone. They work as customized web application firewall (WAF) rules that you can use to perform actions like Block or Managed Challenge on incoming requests.

Use WAF [Managed Rules](https://developers.cloudflare.com/waf/managed-rules/) to apply custom criteria for all incoming HTTP requests.

## Understand hosting plan limits

Cloudflare offsets most of the load to your website via caching and request filtering, but some traffic will still pass through to your origin. Knowing the limits of your hosting plan can help prevent a bottleneck from your host.

Once you are aware of your plan limits, you can use [Rate Limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) to restrict how many times a requesting entity can make a request to your website.

To help you define the best rate limiting setting for your use case, refer to [How Cloudflare determines the request rate](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/).

## Security models

- Positive Security policy: Allow specific requests and deny everything else.
- Negative Security policy: Block specific requests and allow everything else.

## Actions

- Log: Test rule effectiveness before committing to a more severe action.
- Allow: Allow matching requests to access the site.
- Block: Block matching requests from accessing the site.
- Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before proceeding.
- Interactive Challenge: Visitors will be shown an interactive challenge before proceeding.
