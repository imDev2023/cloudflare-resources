---
description: Available URL normalization types and configuration settings.
title: URL normalization settings
image: https://developers.cloudflare.com/rules/normalization/settings/og.png?v=6730d09818a77043
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# URL normalization settings

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/normalization/settings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare dashboard provides the following settings to manage URL normalization:

## Normalization type

Default value: *RFC-3986*

Selects the type of normalization to perform:

- *RFC-3986* – Applies URL normalization strictly according to [RFC 3986 ↗︎](https://datatracker.ietf.org/doc/html/rfc3986).
- *Cloudflare* – In addition to what is defined in RFC 3986, applies [extra URL normalization techniques](https://developers.cloudflare.com/rules/normalization/how-it-works/#cloudflare-normalization).

## Normalize incoming URLs

Default value: *On*

Configures the URLs of all incoming traffic to Cloudflare:

- When enabled, all incoming URLs are normalized before they pass to subsequent Cloudflare features that can receive a URL as input, such as Page Rules, WAF custom rules, Workers, and Access.
- When disabled, incoming URLs are not normalized before passing to subsequent Cloudflare features.

## Normalize URLs to origin

Default value: *Off*

Configures URLs sent to the origin:

- When enabled, requests sent to the origin are normalized.
- When disabled, requests sent to the origin are not modified.

You can only view and enable this option when **Normalize incoming URLs** is enabled.

For examples of how these settings affect URL normalization, refer to the [URL normalization examples](https://developers.cloudflare.com/rules/normalization/examples/).
