---
description: Secure Internet traffic and SaaS apps.
title: Build DNS security policies
image: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/og.png?v=41b68f7c471f77e7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Build DNS security policies

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

DNS security is an important, wide-reaching, and early action in the lifecycle of a request. Cloudflare operates one of the world's largest and fastest public DNS resolvers. Your users' public DNS requests will be resolved by that same resolution engine -- whether they are connecting from a network pointing its resolvers to Cloudflare or an endpoint running the Cloudflare One Client.

## Objectives

By the end of this module, you will be able to:

- Create your first Gateway DNS policy.
- Build an allow or block list for use in firewall policies.
- Onboard networks to Gateway to filter DNS queries.
