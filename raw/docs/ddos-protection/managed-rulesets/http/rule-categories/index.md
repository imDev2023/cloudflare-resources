---
description: Categories of rules in the HTTP DDoS Attack Protection managed ruleset.
title: Rule categories
image: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/og.png?v=f523352a78064e41
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# Rule categories

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The main categories (or tags) of HTTP DDoS Attack Protection managed rules are the following:

| Name | Description |
| --- | --- |
| `botnets` | Rules for requests from known botnets, with very high accuracy and low risk of false positives. It is recommended that you keep these rules enabled. |
| `unusual-requests` | Rules for requests with suspicious characteristics that are not usually seen in legitimate traffic. |
| `advanced` | Rules related to features available to Advanced DDoS Protection customers, such as [Adaptive DDoS Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/). |
| `generic` | Rules for detecting and mitigating floods of requests. These rules are useful for mitigating attacks that have no known signatures, but they may also trigger on unusually high volumes of legitimate traffic. To reduce the risk of false positives, their request per second (rps) activation threshold is higher. These rules either rate-limit or challenge traffic by default, but you can override them to block traffic if necessary. |
| `read-only` | Highly targeted rules for mitigating DDoS attacks with a high confidence rate. These rules are read-only — you cannot override their sensitivity level or action. |
| `test` | Rules used for testing the detection, mitigation, and alerting capabilities of Cloudflare's DDoS protection products. |
