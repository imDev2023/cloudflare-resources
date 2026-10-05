---
description: Allowlist trusted IP addresses or prefixes to exclude them from Advanced DDoS Protection.
title: Add an IP or prefix to the allowlist
image: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/og.png?v=b9a3a83217ee1f89
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add an IP or prefix to the allowlist

Last updated Jun 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To add an IP address or prefix to the Advanced DDoS Protection [allowlist](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#allowlist):

1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page. [Go to **DDoS Managed Rules** ↗](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
2. Go to **Advanced Protection**.
3. Under **General settings** > **Allowlist**, select **Edit**.
4. Enter a prefix and (optionally) a description in **Prefix** and **Description**, respectively.
5. To exclude the current prefix from the allowlist instead of including it, uncheck the **Enabled** checkbox. 6. Select **Add**.

Allowlists support approximately 200 IP addresses in a single expression for a rule.

Important

Prefixes in the allowlist will be vulnerable to IP spoofing attacks. If an attacker can guess the source IP addresses you have allowlisted, their packets will be allowlisted.
