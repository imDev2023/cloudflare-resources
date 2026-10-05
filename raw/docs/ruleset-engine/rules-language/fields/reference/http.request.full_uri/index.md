---
description: The full URI as received by the web server.
title: http.request.full_uri
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.full\_uri

`http.request.full_uri``String`

The full URI as received by the web server.

The value will not include the `#fragment` part, which is not sent to web servers.

Example value:

```txt
"https://www.example.org/articles/index?section=539061&expand=comments"
```

Categories:
- Request
- URI
