---
description: Create a redirect rule to forward HTTPS requests from the root (also known as the “apex” or “naked” domain) to the WWW subdomain.
title: Redirect from root to WWW
image: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/og.png?v=3bb142c170fab23f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Redirect from root to WWW

Create a redirect rule to forward HTTPS requests from the root (also known as the “apex” or “naked” domain) to the WWW subdomain.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example creates a redirect rule that forwards HTTPS requests from the root domain (`example.com`) to the WWW subdomain (`www.example.com`), while retaining the original path and query string.

**When incoming requests match**

- **Wildcard pattern**
  - **Request URL**: `https://example.com/*`

**Then**

- **Target URL**: `https://www.example.com/${1}`
- **Status code**: *301*
- **Preserve query string**: Enabled

This rule ensures that only HTTPS requests from the root domain are redirected to the WWW subdomain, leaving other requests (such as HTTP or requests to other subdomains) unchanged.

For example, the redirect rule would perform the following redirects:

| Request URL | Target URL | Status code |
| --- | --- | --- |
| `https://example.com/products/` | `https://www.example.com/products/` | `301` |
| `https://store.example.com/products/` | (unchanged) | n/a |
| `https://example.com/admin/?logged_out=true` | `https://www.example.com/admin/?logged_out=true` | `301` |
| `http://example.com/?all_items=true` | (unchanged) | n/a |
| `http://www.example.com/admin/` | (unchanged) | n/a |

Make sure to replace `example.com` with your actual hostname before deploying your rule.
