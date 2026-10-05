---
description: How Best practices works in Gateway.
title: Best practices
image: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/og.png?v=7cc188f2cbe2feef
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Best practices

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, Cloudflare Network Firewall allows all incoming (ingress) traffic that has passed through Cloudflare's core DDoS mitigations. To reduce your exposure to attacks and prevent unwanted traffic from reaching your network, configure rules using the following guidelines.

If you are setting up firewall rules for the first time, start with the [Minimal ruleset](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/minimal-ruleset/). If you have existing on-premises or edge firewall rules, the best approach is to replicate those rules in Network Firewall. If you are unable to export your current firewall rules, contact your Cloudflare Implementation Manager for help translating the rules into Network Firewall rules.

- [Minimal ruleset](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/minimal-ruleset/)
- [Extended ruleset](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/extended-ruleset/)
- [Magic Transit egress](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/magic-transit-egress/)
