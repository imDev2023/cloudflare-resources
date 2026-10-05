---
description: Pre-built lists managed by Cloudflare for use in rule expressions.
title: Managed Lists
image: https://developers.cloudflare.com/waf/tools/lists/managed-lists/og.png?v=0237e6080a90e97a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Managed Lists

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/tools/lists/managed-lists/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare provides Managed Lists you can use in rule expressions. These lists are regularly updated.

Note

This feature requires an Enterprise plan.

## Managed IP Lists

Use Managed IP Lists to access Cloudflare's IP threat intelligence.

Cloudflare provides the following Managed IP Lists:

| Display name | Name in expressions | Description |
| --- | --- | --- |
| Cloudflare Open Proxies | `cf.open_proxies` | IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity. |
| Cloudflare Anonymizers | `cf.anonymizer` | IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes). |
| Cloudflare VPNs | `cf.vpn` | IP addresses of known VPN servers. |
| Cloudflare Malware | `cf.malware` | IP addresses of known sources of malware. |
| Cloudflare Botnets, Command and Control Servers | `cf.botnetcc` | IP addresses of known botnet command-and-control servers. |
