---
description: Indicates whether the HTTP request contains too many headers.
title: http.request.headers.truncated
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.headers.truncated

`http.request.headers.truncated``Boolean`

Indicates whether the HTTP request contains too many headers.

When `true`, [`http.request.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/), [`http.request.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/), and [`http.request.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/) may not contain all of the headers sent in the HTTP request.

Categories:
- Request
- Headers
