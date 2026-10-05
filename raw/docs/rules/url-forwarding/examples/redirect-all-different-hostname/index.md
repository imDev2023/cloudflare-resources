---
description: Create a redirect rule to redirect all requests for `smallshop.example.com` to a different hostname using HTTPS, keeping the original path and query string.
title: Redirect requests to a different hostname
image: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/og.png?v=25a02eca63d2f058
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Redirect requests to a different hostname

Create a redirect rule to redirect all requests for `smallshop.example.com` to a different hostname using HTTPS, keeping the original path and query string.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect will redirect all requests for `smallshop.example.com` to a different hostname `globalstore.example.net` using HTTPS, keeping the original path and query string.

**When incoming requests match**

- **Wildcard pattern**
  - **Request URL**: `http*://smallshop.example.com/*`

**Then**

- **Target URL**: `https://globalstore.example.net/${2}`
- **Status code:** *301*
- **Preserve query string:** Enabled

For example, the redirect rule would perform the following redirects:

| Request URL | Target URL | Status code |
| --- | --- | --- |
| `http://smallshop.example.com/` | `https://globalstore.example.net/` | `301` |
| `http://smallshop.example.com/admin/?logged_out=true` | `https://globalstore.example.net/admin/?logged_out=true` | `301` |
| `https://smallshop.example.com/?all_items=1` | `https://globalstore.example.net/?all_items=1` | `301` |
| `http://example.com/about/` | (unchanged) | n/a |
