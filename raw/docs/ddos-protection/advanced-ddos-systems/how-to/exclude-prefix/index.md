---
description: Exclude a prefix or prefix subset from Advanced DDoS Protection monitoring.
title: Exclude a prefix
image: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/og.png?v=5905699c6d7e1ada
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# Exclude a prefix

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To exclude a prefix or a prefix subset from Advanced DDoS Protection:

1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page. [Go to **DDoS Managed Rules** ↗](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
2. Go to **Advanced Protection**.
3. [Add the prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/) you previously onboarded to Magic Transit to Advanced TCP Protection.
4. [Add the prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/) (or subset) you wish to exclude as a new, separate prefix in Advanced TCP Protection.
5. For the prefix you added in the previous step, select **Exclude Subset** in the **Enrolled Prefixes** list.

Note

Prefixes or subsets added as *Excluded* will not be protected by Advanced TCP Protection.
