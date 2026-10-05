---
description: Remove a zone from your Cloudflare account.
title: Zone removal
image: https://developers.cloudflare.com/dns/zone-setups/removal/og.png?v=a982002297a04ec1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dns/llms.txt  
> Use this file to discover all available pages before exploring further.

# Zone removal

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dns/zone-setups/removal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If domains on Free zones remain in the [Pending](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/#pending) or [Moved](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/#moved) status for too long, Cloudflare automatically removes them from your account and the Cloudflare network. Refer to [zone statuses](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) for more details.

You can also [manually remove a domain](https://developers.cloudflare.com/fundamentals/manage-domains/remove-domain/) from Cloudflare.

If you need to re-add a domain to your account, follow the [regular onboarding flow](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/). Cloudflare will assign a new nameserver pair when you re-add the domain, so you must [update your registrar](https://developers.cloudflare.com/dns/nameservers/update-nameservers/) with the new nameservers. Refer to [nameserver assignment](https://developers.cloudflare.com/dns/nameservers/nameserver-options/#assignment-method) for details.

Purged zones

By default, your zone will be automatically purged seven days after the removal. In this case, even if you re-add the domain to the same Cloudflare account, none of the zone settings are expected to be restored. Refer to [zone statuses](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) for more details.
