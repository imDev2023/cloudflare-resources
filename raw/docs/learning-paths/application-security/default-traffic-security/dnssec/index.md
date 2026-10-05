---
description: Sign your zone with DNSSEC for DNS security.
title: DNSSEC
image: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/dnssec/og.png?v=d173ef1a2e5d5411
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# DNSSEC

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/dnssec/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

DNS Security Extensions (DNSSEC) adds an extra layer of authentication to DNS, ensuring requests are not routed to a spoofed domain.

For additional background on DNSSEC, visit the [Cloudflare Learning Center ↗︎](https://www.cloudflare.com/learning/dns/dns-security/).

When you [enable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/), Cloudflare signs your zone, publishes your public signing keys, and generates your **DS** record.

Note:

Cloudflare automatically adds **DS** records for domains using Cloudflare Registrar or those using `.ch` and `.cz` top-level domains.
