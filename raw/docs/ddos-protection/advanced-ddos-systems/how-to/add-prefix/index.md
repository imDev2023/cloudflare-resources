---
description: Add an IP prefix to Advanced DDoS Protection for monitoring and mitigation.
title: Add a prefix
image: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/og.png?v=1def90251de3f213
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add a prefix

Last updated Jun 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To add a [prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#prefixes) to Advanced DDoS Protection:

1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page. [Go to **DDoS Managed Rules** ↗](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
2. Go to **Advanced Protection**.
3. Under **General settings** > **Prefixes**, select **Edit**.
4. Expand the **Add existing prefix** section and select **Add** next to the prefix you wish to add.  
    Alternatively, enter a prefix and (optionally) a description in **Prefix** and **Description**, respectively, and select **Add**.

Note

The **Add existing prefix** list will not display leased prefixes, but you can add them manually in the Cloudflare dashboard or [using the API](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/). You cannot add [delegated prefixes](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/) to Advanced TCP Protection.
