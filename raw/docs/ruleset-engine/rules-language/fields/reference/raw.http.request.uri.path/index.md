---
description: The raw URI path of the request without any transformation.
title: raw.http.request.uri.path
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# raw.http.request.uri.path

`raw.http.request.uri.path``String`

The raw URI path of the request without any transformation.

This is the raw field version of the [`http.request.uri.path`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

**Note**: This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.

Categories:
- Request
- URI
- Raw fields
