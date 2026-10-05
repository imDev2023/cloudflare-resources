---
description: Detect and block requests with invalid headers.
title: Browser Integrity
image: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/browser-integrity/og.png?v=31602b9e9e949886
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Browser Integrity

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/browser-integrity/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's Browser Integrity Check (BIC) looks for common HTTP headers abused most commonly by spammers and denies access to your page.

It also challenges visitors without a user agent or with a non-standard user agent such as commonly used by abusive bots, crawlers, or visitors.

[BIC is enabled by default](https://developers.cloudflare.com/waf/tools/browser-integrity-check/).
