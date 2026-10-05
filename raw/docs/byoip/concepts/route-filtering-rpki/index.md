---
description: How route filtering and RPKI protect against route hijacking.
title: Route filtering and RPKI
image: https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/og.png?v=b413c76cacd35f5f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/byoip/llms.txt  
> Use this file to discover all available pages before exploring further.

# Route filtering and RPKI

Last updated Apr 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Network operators rely on [IRR records](https://developers.cloudflare.com/byoip/concepts/irr-entries/) to determine which autonomous systems (ASNs) are authorized to announce specific IP prefixes. Based on these records, operators configure filtering policies on their routers to block unauthorized announcements — a practice known as route filtering.

However, IRR records alone are not cryptographically verified, which means they can be inaccurate or outdated. Resource Public Key Infrastructure (RPKI) addresses this gap by adding cryptographic validation. With RPKI, the association between an IP prefix and its authorized ASN is signed and verifiable, allowing network operators to confirm that a route announcement is legitimate before accepting it.

When you register your prefix with one of the five Regional Internet Registries (RIRs)<sup>[1](#user-content-fn-1)</sup>, you can create a Route Origin Authorization (ROA) — a cryptographically signed object that declares which ASN is authorized to originate your prefix. ROAs are publicly verifiable, and you can check your prefixes using [Cloudflare's RPKI Portal ↗︎](https://rpki.cloudflare.com/?view=validator) or other sources such as [Routinator ↗︎](https://rpki-validator.ripe.net/ui/).

## Footnotes

1. AFRINIC, APNIC, ARIN, LACNIC, and RIPE. [↩](#user-content-fnref-1)
