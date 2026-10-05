---
description: The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.
title: http.request.timestamp.sec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.timestamp.sec

`http.request.timestamp.sec``Integer`

The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.

The field value is 10 digits long.

When validating HMAC tokens in an expression, pass this field as the `currentTimestamp` argument to the [`is_timed_hmac_valid_v0()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hmac-validation) validation function.

To obtain the timestamp milliseconds, use the [`http.request.timestamp.msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/) field.

Example value:

```txt
1484063137
```

Categories:
- Request
