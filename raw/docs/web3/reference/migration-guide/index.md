---
description: Migrate from legacy Web3 gateways to the current setup.
title: Legacy gateway migration
image: https://developers.cloudflare.com/web3/reference/migration-guide/og.png?v=a4d4b36b2965fcbe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/web3/llms.txt  
> Use this file to discover all available pages before exploring further.

# Legacy gateway migration

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/web3/reference/migration-guide/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

As announced in [our blog post ↗︎](https://blog.cloudflare.com/ea-web3-gateways/), Cloudflare is deprecating legacy hostnames that point to our public gateway endpoints at `cloudflare-eth.com` and `cloudflare-ipfs.com`.

If you created a hostname pointing to these gateways during the [private beta ↗︎](https://blog.cloudflare.com/announcing-web3-gateways/), you should migrate to use our new Web3 gateways to avoid a disruption in service.

---

## Migration guide

The migration is a simple process.

First, create a [Cloudflare account](https://developers.cloudflare.com/fundamentals/account/create-account/).

Then create a new [Web3 custom gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway) with your existing hostname.

Alternatively, you could also create a [Web3 custom gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway) for a new hostname and then modify your application to use your newly created hostname ([IPFS](https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/) or [Ethereum](https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/)).
