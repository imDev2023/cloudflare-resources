---
description: Create a URL rewrite rule (part of Transform Rules) to normalize encoded forward slashes (`%2F`) in the request path to standard slashes (`/`).
title: Normalize encoded slashes in URL path
image: https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/og.png?v=0597d9af2d8690ae
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Normalize encoded slashes in URL path

Create a URL rewrite rule (part of Transform Rules) to normalize encoded forward slashes (`%2F`) in the request path to standard slashes (`/`).

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Different web servers and applications handle encoded forward slashes (`%2F`) in URLs differently. Cloudflare follows [RFC 3986 ↗︎](https://datatracker.ietf.org/doc/html/rfc3986), which specifies that `%2F` **should not** be automatically normalized to `/` because `/` is a reserved character in URLs, and decoding it might change the intended meaning of the path.

However, many origin servers **do** automatically decode `%2F` into `/` when processing requests. If your origin server behaves this way, you may want to apply the same normalization at Cloudflare’s edge to ensure consistency in request handling, rule evaluation, and logging.

## How to normalize `%2F`

To normalize encoded forward slashes (`%2F`) to standard slashes (`/`) in the request path before [subsequent](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/) rule evaluation, create a new URL rewrite rule and define a dynamic URL path rewrite using [`url_decode()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#url_decode) function:

Text in **Expression Editor**:

```txt
(lower(raw.http.request.full_uri) wildcard "*%2f*")
```

Text after **Path** > **Rewrite to** > *Dynamic*:

```txt
url_decode(http.request.uri.path)
```

This transformation ensures that `%2F` is always treated as `/` in the request path. This is particularly useful when setting up rules that depend on URL path matching, as it prevents discrepancies caused by differing normalization behaviors.
