---
description: Block requests with suspicious HTTP headers using Browser Integrity Check.
title: Browser Integrity Check
image: https://developers.cloudflare.com/waf/tools/browser-integrity-check/og.png?v=7e62226e196098b4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Browser Integrity Check

Last updated Aug 3, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/tools/browser-integrity-check/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's Browser Integrity Check (BIC) looks for common HTTP headers abused most commonly by spammers and denies access to your page.

It also challenges visitors without a user agent or with a non-standard user agent such as commonly used by abusive bots, crawlers, or visitors.

Browser Integrity Check is enabled by default.

## Disable Browser Integrity Check

### Disable globally

To disable BIC globally for your zone:

1. In the Cloudflare dashboard, go to the Security **Settings** page. [Go to **Settings** ↗](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
2. (Optional) Filter by **DDoS attacks**.
3. Turn off **Browser integrity check**.

### Disable selectively

To disable BIC selectively, you can skip Browser Integrity Check using a [custom rule with a skip action](https://developers.cloudflare.com/waf/custom-rules/skip/).

Also, use a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/) to selectively enable or disable this feature for certain sections of your website using a filter expression (such as a matching hostname or request URL path).
