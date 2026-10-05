---
description: Best practices for configuring the Network Firewall.
title: Best practices
image: https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/og.png?v=5b14221fed016293
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-network-firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# Best practices

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, Cloudflare Network Firewall (formerly Magic Firewall) permits all ingress traffic that has passed through Cloudflare's core DDoS mitigations. To proactively mitigate attacks and minimize your attack surface and leakage of attack traffic into your environment, we recommend implementing your Cloudflare Network Firewall rules using the following guidelines.

The best approach is to replicate your current ingress perimeter firewall rules in Network Firewall. If you are unable to export your current perimeter firewall rules, contact your Implementation Manager for help translating the rules into Cloudflare Network Firewall rules.

- [Minimal ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/minimal-ruleset/)
- [Extended ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/extended-ruleset/)
- [Magic Transit egress](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/magic-transit-egress/)
