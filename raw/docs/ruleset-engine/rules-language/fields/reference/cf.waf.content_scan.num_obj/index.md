---
description: The number of content objects detected in the request (zero or greater).
title: cf.waf.content_scan.num_obj
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.content\_scan.num\_obj

`cf.waf.content_scan.num_obj``Integer`

The number of content objects detected in the request (zero or greater).

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:

```txt
# Check if requests to a specific endpoint contain more than two content objects
cf.waf.content_scan.num_obj > 2 and http.request.uri.path eq "/upload"
```

Categories:
- Request
