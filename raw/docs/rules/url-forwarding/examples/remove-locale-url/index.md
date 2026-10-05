---
description: Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.
title: Remove locale from URL path
image: https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/og.png?v=f0e8ae7373978a7e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Remove locale from URL path

Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect visitors from an old URL format that included the locale (for example, `/en-us/<page_name>`) to the new format `/<page_name>`.

**When incoming requests match**

- **Field:** *URI Path*
- **Operator:** *matches regex*
- **Value:** `^/[A-Za-z]{2}-[A-Za-z]{2}/`

If you are using the Expression Editor, enter the following expression:  
`http.request.uri.path matches "^/[A-Za-z]{2}-[A-Za-z]{2}/"`

**Then**

- **Type:** *Dynamic*
- **Expression:** `regex_replace(http.request.uri.path, "^/[A-Za-z]{2}-[A-Za-z]{2}/(.*)", "/${1}")`
- **Status code:** *301*
- **Preserve query string:** Enabled

The function [`regex_replace()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#regex_replace) allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using `${<num>}` in the replacement string, where `<num>` is the number of the capture group.

For example, the redirect rule would perform the following redirects:

| Request URL | Target URL | Status code |
| --- | --- | --- |
| `example.com/en-us/meet-our-team` | `example.com/meet-our-team` | `301` |
| `example.com/pt-BR/meet-our-team` | `example.com/meet-our-team` | `301` |
| `example.com/en-us/calendar?view=month` | `example.com/calendar?view=month` | `301` |
| `example.com/meet-our-team` | (unchanged) | n/a |
| `example.com/robots.txt` | (unchanged) | n/a |
