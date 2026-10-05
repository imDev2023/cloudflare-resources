---
description: The `Cookie` HTTP header associated with a request represented as a Map (associative array).
title: http.request.cookies
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.cookies

`http.request.cookies``Map<Array<String>>`

The `Cookie` HTTP header associated with a request represented as a Map (associative array).

Requires a Cloudflare Pro, Business, or Enterprise plan.

The cookie names are URL decoded. If two cookies have the same name after decoding, their value arrays are merged.

The cookie values are not pre-processed and retain the original case used in the request.

Example value:

```txt
{ "app": ["test"] }
```

Example usage:

```txt
any(http.request.cookies["app"][*] == "test")
```

Categories:
- Request
- Headers
