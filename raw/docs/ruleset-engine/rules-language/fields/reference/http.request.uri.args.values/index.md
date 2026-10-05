---
description: The values of arguments in the HTTP URI query string.
title: http.request.uri.args.values
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.uri.args.values

`http.request.uri.args.values``Array<String>`

The values of arguments in the HTTP URI query string.

The values are not pre-processed and retain the original case used in the request. They are in the same order as in the request.

Duplicated values are listed multiple times.

- **Decoding**: No decoding performed
- **Non-ASCII**: Preserved

Example value:

```txt
["red+apples"]
```

Example usage:

```txt
any(http.request.uri.args.values[*] == "red+apples")
```

Categories:
- Request
- URI
