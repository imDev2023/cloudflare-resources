---
description: The names of the headers in the HTTP request.
title: http.request.headers.names
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.headers.names

`http.request.headers.names``Array<String>`

The names of the headers in the HTTP request.

The names are not pre-processed and retain the original case used in the request.

The order of header names is not guaranteed but will match [`http.request.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/).

Duplicate headers are listed multiple times.

- **Decoding**: No decoding performed
- **Whitespace**: Preserved
- **Non-ASCII**: Preserved

When the HTTP request contains too many headers, this field may not contain the names of all of the headers sent in the HTTP request. In this situation, the [`http.request.headers.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/) field will be set to `true`.

**Note**: In HTTP/2, the names of HTTP headers are always in lowercase. Recent versions of the `curl` tool [enable HTTP/2 by default](https://curl.se/docs/manpage.html#--http2) for HTTPS connections.

Example value:

```txt
["content-type"]
```

Example usage:

```txt
any(http.request.headers.names[*] == "content-type")
```

Categories:
- Request
- Headers
