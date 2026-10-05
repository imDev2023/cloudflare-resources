---
description: The HTTP response headers without any transformation represented as a Map (or associative array).
title: raw.http.response.headers
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# raw.http.response.headers

`raw.http.response.headers``Map<Array<String>>`

The HTTP response headers without any transformation represented as a Map (or associative array).

This is the raw field version of the [`http.response.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers/) field. Raw fields, prefixed with `raw.`, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Example value:

```txt
{"server": ["nginx"]}
```

Example usage:

```txt
any(raw.http.response.headers["server"][*] == "nginx")
```

Categories:
- Response
- Headers
- Raw fields
