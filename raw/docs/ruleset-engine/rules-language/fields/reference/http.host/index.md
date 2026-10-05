---
description: The hostname used in the full request URI.
title: http.host
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.host

`http.host``String`

The hostname used in the full request URI.

The `http.host` field contains the `Host` header from the original client request.

If you have configured [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/) that change the hostname, this change is not reflected in the `http.host` value seen by other rule phases (such as custom rules, cache rules, or transform rules) or [Cloudflare Workers](https://developers.cloudflare.com/workers/). All rule phases and Workers evaluate against the original, unmodified host.

Example value:

```txt
"www.example.org"
```

Categories:
- Request
- URI
