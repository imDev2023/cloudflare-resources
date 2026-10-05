---
description: The raw full URI as received by the web server without any transformation.
title: raw.http.request.full_uri
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# raw.http.request.full\_uri

`raw.http.request.full_uri``String`

The raw full URI as received by the web server without any transformation.

The value will not include the `#fragment` part, which is not sent to web servers.

This is the raw field version of the [`http.request.full_uri`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.full_uri/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

**Note**: This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.

Categories:
- Request
- URI
- Raw fields
