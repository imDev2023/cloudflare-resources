---
description: Create a redirect rule to redirect requests for the administration area of `store.example.com` to HTTPS, keeping the original path and query string.
title: Redirect admin area requests to HTTPS
image: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/og.png?v=31f3ec7e25aa57f4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Redirect admin area requests to HTTPS

Create a redirect rule to redirect requests for the administration area of `store.example.com` to HTTPS, keeping the original path and query string.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect requests for the administration area of a specific subdomain (`store.example.com`) to HTTPS, keeping the original path and query string.

**When incoming requests match**

- **Wildcard pattern**
  - **Request URL**: `http://store.example.com/admin*`

**Then**

- **Target URL**: `https://store.example.com/admin${1}`
- **Status code:** *301*
- **Preserve query string:** Enabled

For example, the redirect rule would perform the following redirects:

| Request URL | Target URL | Status code |
| --- | --- | --- |
| `http://store.example.com/admin/products/` | `https://store.example.com/admin/products/` | `301` |
| `https://store.example.com/admin/products/` | (unchanged) | n/a |
| `http://store.example.com/admin/?logged_out=true` | `https://store.example.com/admin/?logged_out=true` | `301` |
| `http://store.example.com/?all_items=true` | (unchanged) | n/a |
| `http://example.com/admin/` | (unchanged) | n/a |
