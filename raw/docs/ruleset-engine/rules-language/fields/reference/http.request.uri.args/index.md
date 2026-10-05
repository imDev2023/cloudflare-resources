---
description: The HTTP URI arguments associated with a request represented as a Map (associative array).
title: http.request.uri.args
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.uri.args

`http.request.uri.args``Map<Array<String>>`

The HTTP URI arguments associated with a request represented as a Map (associative array).

When an argument repeats, the array contains multiple items in the order they appear in the request.

The values are not pre-processed and retain the original case used in the request.

- **Decoding**: No decoding performed
- **Non-ASCII**: Preserved

Example value:

```txt
{"search": ["red+apples"]}
```

Example usage:

```txt
any(http.request.uri.args["search"][*] == "red+apples")
```

Categories:
- Request
- URI
