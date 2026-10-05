---
description: How Cloudflare Network Firewall protects your network traffic.
title: About
image: https://developers.cloudflare.com/cloudflare-network-firewall/about/og.png?v=9de2ec79f3c29195
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-network-firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# About

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/about/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Review the content below to learn more about concepts related to Cloudflare Network Firewall (formerly Magic Firewall).

Important

When using Cloudflare Network Firewall alongside other Cloudflare services that proxy traffic (for example, CDN and Spectrum), be aware of the following:

- Firewall rules that block traffic based on source IP address may not work as intended because rules are evaluated after Cloudflare terminates the incoming TCP connections.
- You must allow [Cloudflare IP addresses ↗︎](https://www.cloudflare.com/ips/).
- When using Cloudflare Network Firewall, fragmented packets are reassembled into complete packets before they are inspected. As a result, you cannot create firewall rules for fragments.

- [Analytics](https://developers.cloudflare.com/cloudflare-network-firewall/about/analytics/)
- [IDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/)
- [List types](https://developers.cloudflare.com/cloudflare-network-firewall/about/list-types/)
- [Protocol validation rules](https://developers.cloudflare.com/cloudflare-network-firewall/about/protocol-validation-rules/)
- [Ruleset logic](https://developers.cloudflare.com/cloudflare-network-firewall/about/ruleset-logic/)
- [Traffic types](https://developers.cloudflare.com/cloudflare-network-firewall/about/traffic-types/)
- [Unified Routing behavior changes](https://developers.cloudflare.com/cloudflare-network-firewall/about/unified-routing-changes/)
