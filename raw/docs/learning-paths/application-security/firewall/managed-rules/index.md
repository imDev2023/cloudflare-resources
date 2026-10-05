---
description: Deploy WAF managed rulesets for threat protection.
title: Managed Rules
image: https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/og.png?v=fe7424de91fc02cf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Managed Rules

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare provides pre-configured managed rulesets that protect against web application exploits such as the following:

- Zero-day vulnerabilities
- Top-10 attack techniques
- Use of stolen/leaked credentials
- Extraction of sensitive data

Managed rulesets are [regularly updated](https://developers.cloudflare.com/waf/change-log/). Each rule has a default action that varies according to the severity of the rule. You can adjust the behavior of specific rules, choosing from several possible actions.

Rules of managed rulesets have associated tags (such as `wordpress`) that allow you to search for a specific group of rules and configure them in bulk.

## Rulesets

By default, Cloudflare offers the following rulesets:

- [Cloudflare Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/)
- [Cloudflare OWASP Core Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/)
- [Cloudflare Exposed Credentials Check Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/)
