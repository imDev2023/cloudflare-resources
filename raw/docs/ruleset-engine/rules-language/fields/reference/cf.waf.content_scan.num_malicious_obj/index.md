---
description: The number of malicious content objects detected in the request (zero or greater).
title: cf.waf.content_scan.num_malicious_obj
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.content\_scan.num\_malicious\_obj

`cf.waf.content_scan.num_malicious_obj``Integer`

The number of malicious content objects detected in the request (zero or greater).

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:

```txt
# Check if requests to a specific endpoint contain more than two malicious content objects
cf.waf.content_scan.num_malicious_obj > 2 and http.request.uri.path eq "/upload"
```

Categories:
- Request
