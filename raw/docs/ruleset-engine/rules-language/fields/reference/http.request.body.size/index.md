---
description: The total size of the HTTP request body (in bytes).
title: http.request.body.size
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.body.size

`http.request.body.size``Number`

The total size of the HTTP request body (in bytes).

This field may have a value larger than the one returned by `len(http.request.body.raw)`, since the [`http.request.body.raw`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/) field only considers the request body up to a maximum size that varies according to your Cloudflare plan.

Requires a Cloudflare Enterprise plan.

Categories:
- Request
- Body
