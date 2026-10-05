---
description: The HTTP response headers represented as a Map (or associative array).
title: http.response.headers
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.response.headers

`http.response.headers``Map<Array<String>>`

The HTTP response headers represented as a Map (or associative array).

When there are repeating headers, the array includes them in the order they appear in the response. The keys convert to lowercase.

- **Decoding**: No decoding performed
- **Whitespace**: Preserved
- **Non-ASCII**: Preserved

**Note**: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Example value:

```txt
{"server": ["nginx"]}
```

Example usage:

```txt
any(http.response.headers["server"][*] == "nginx")
```

Categories:
- Response
- Headers
