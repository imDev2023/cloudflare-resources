---
description: In Orange-to-Orange (O2O) setups — where a SaaS provider uses Cloudflare for SaaS and their customer also has their own Cloudflare zone — the __cf_bm Bot Management cookie returned from the origin-facing Cloudflare zone can cause the eyeball-facing zone to bypass cache. This occurs because the Set-Cookie header in the response triggers Cloudflare's default behavior of not caching responses with Set-Cookie.
title: Bot Management cookie causes cache bypass in O2O setups
image: https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/og.png?v=a679315e8bda7705
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Bot Management cookie causes cache bypass in O2O setups

Last updated Jun 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [Orange-to-Orange (O2O)](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/) setups — where a SaaS provider uses [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) and their customer also has their own Cloudflare zone — the `__cf_bm` Bot Management cookie returned from the origin-facing Cloudflare zone can cause the eyeball-facing zone to bypass cache. This occurs because the `Set-Cookie` header in the response triggers Cloudflare's default behavior of not caching responses with `Set-Cookie`.

If you are seeing unexpectedly low cache hit rates in an O2O setup with Bot Management enabled, this may be the cause.
