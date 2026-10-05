---
description: The names of the headers in the HTTP response.
title: http.response.headers.names
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.response.headers.names

`http.response.headers.names``Array<String>`

The names of the headers in the HTTP response.

The names are not pre-processed and retain the original case used in the response.

The order of header names is not guaranteed but will match [`http.response.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/).

Duplicate headers are listed multiple times.

- **Decoding**: No decoding performed
- **Whitespace**: Preserved
- **Non-ASCII**: Preserved

**Note**: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Example value:

```txt
["content-type"]
```

Example usage:

```txt
any(http.response.headers.names[*] == "content-type")
```

Categories:
- Response
- Headers
