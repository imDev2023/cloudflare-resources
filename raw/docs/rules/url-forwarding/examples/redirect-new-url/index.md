---
description: Create a redirect rule to redirect visitors from `/contact-us/` to the page's new path `/contacts/`.
title: Redirect visitors to a new page URL
image: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/og.png?v=dc5be0e05cb23d87
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Redirect visitors to a new page URL

Create a redirect rule to redirect visitors from `/contact-us/` to the page's new path `/contacts/`.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example static redirect for zone `example.com` will redirect visitors requesting the `/contact-us/` page to the new page URL `/contacts/`.

**When incoming requests match**

- **Field:** *URI Path*
- **Operator:** *equals*
- **Value:** `/contact-us/`

If you are using the Expression Editor, enter the following expression:  
`http.request.uri.path eq "/contact-us/"`

**Then**

- **Type:** *Static*
- **URL:** `/contacts/`
- **Status code:** *301*
- **Preserve query string:** Enabled

For example, the redirect rule would perform the following redirects:

| Request URL | Target URL | Status code |
| --- | --- | --- |
| `example.com/contact-us/` | `example.com/contacts/` | `301` |
| `example.com/contact-us/?state=TX` | `example.com/contacts/?state=TX` | `301` |
| `example.com/team/` | (unchanged) | n/a |
