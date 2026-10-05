---
description: The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's `Content-Type` header.
title: http.response.content_type.media_type
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.response.content\_type.media\_type

`http.response.content_type.media_type``String`

The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's `Content-Type` header.

The field value will not include parameters such as `charset`.

Example values:

| Content-Type header | Field value |
| --- | --- |
| `text/html` | `"text/html"` |
| `text/html; charset=utf-8` | `"text/html"` |
| `text/html+extra` | `"text/html+extra"` |
| `text/html+extra; charset=utf-8` | `"text/html+extra"` |
| `text/HTML` | `"text/html"` |
| `text/html; charset=utf-8; other=value` | `"text/html"` |

**Note**: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Categories:
- Response
- Headers
