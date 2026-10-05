---
description: The millisecond when Cloudflare received the request, between 0–999.
title: http.request.timestamp.msec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.timestamp.msec

`http.request.timestamp.msec``Integer`

The millisecond when Cloudflare received the request, between 0–999.

To obtain the complete timestamp, use both [`http.request.timestamp.sec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/) and [`http.request.timestamp.msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/) fields.

Example value:

```txt
857
```

Categories:
- Request
