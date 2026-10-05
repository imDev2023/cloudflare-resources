---
description: Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.
title: Redirect requests for a domain to a new domain
image: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/og.png?v=9505264070c109e3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Redirect requests for a domain to a new domain

Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In this example, an old website was discontinued and replaced by a new one in a different domain. The functionality is different, and all URLs should now point to the root of the new domain. The same applies to any subdomains of the old domain.

[Create a redirect rule](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-dashboard/) with the following configuration:

**When incoming requests match**

- **Wildcard pattern**
  - **Request URL**: `http*://*example.com/*`

**Then**

- **Target URL**: `https://example.net/`
- **Status code:** *301*

For example, the redirect rule would perform the following redirects:

| Request URL | Target URL | Status code |
| --- | --- | --- |
| `http://example.com/` | `https://example.net/` | `301` |
| `https://example.com/` | `https://example.net/` | `301` |
| `https://subdomain.example.com/` | `https://example.net/` | `301` |
| `https://example.com/my/path/to/page.htm` | `https://example.net/` | `301` |
| `https://example.com/search?q=term` | `https://example.net/` | `301` |
