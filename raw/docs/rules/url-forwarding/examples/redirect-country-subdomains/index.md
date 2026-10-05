---
description: Create a redirect rule to redirect United Kingdom and France visitors from the `example.com` website's  root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.
title: Redirect local visitors to specific subdomains
image: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/og.png?v=9c7c484a5980c2e2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Redirect local visitors to specific subdomains

Create a redirect rule to redirect United Kingdom and France visitors from the `example.com` website's root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect United Kingdom and France visitors requesting the website's root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.

**When incoming requests match**

Using the Expression Editor:  
`(ip.src.country eq "GB" or ip.src.country eq "FR") and http.request.uri.path eq "/"`

**Then**

- **Type:** *Dynamic*
- **Expression:** `lower(concat("https://", ip.src.country, ".example.com"))`
- **Status code:** *301*

For example, the redirect rule would perform the following redirects:

| Visitor country | Request URL | Target URL | Status code |
| --- | --- | --- | --- |
| United Kingdom | `example.com` | `https://gb.example.com` | `301` |
| France | `example.com` | `https://fr.example.com` | `301` |
| United States | `example.com` | (unchanged) | n/a |
