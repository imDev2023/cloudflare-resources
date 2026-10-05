---
description: Configure rules with advanced settings.
title: Configurations
image: https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/og.png?v=254f2e713194e777
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configurations

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Both Custom and Managed Lists are located in the account settings. Refer to [Features by plan type](https://developers.cloudflare.com/learning-paths/application-security/lists/features/) for more information on plan eligibility.

## Custom Lists

Using a Custom List is an alternative to creating individual Firewall rules with long lists of IP addresses or other types of identifiers. They are easier to read and update, especially when they are used across many security rules. Lists are often used in conjunction with in-house or third party security feeds.

## Managed Lists

The following lists are managed by the Cloudflare team and are regularly updated.

| Display name | Name in expressions | Description |
| --- | --- | --- |
| Cloudflare Open Proxies | `cf.open_proxies` | IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity. |
| Cloudflare Anonymizers | `cf.anonymizer` | IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes). |
| Cloudflare VPNs | `cf.vpn` | IP addresses of known VPN servers. |
| Cloudflare Malware | `cf.malware` | IP addresses of known sources of malware. |
| Cloudflare Botnets, Command and Control Servers | `cf.botnetcc` | IP addresses of known botnet command-and-control servers. |

  

## Creating a rule

Refer to [Use lists in expressions](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/) to learn how to invoke a Managed List.
