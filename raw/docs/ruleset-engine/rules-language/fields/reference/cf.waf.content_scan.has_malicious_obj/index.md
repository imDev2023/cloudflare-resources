---
description: Indicates whether the request contains at least one malicious content object.
title: cf.waf.content_scan.has_malicious_obj
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.content\_scan.has\_malicious\_obj

`cf.waf.content_scan.has_malicious_obj``Boolean`

Indicates whether the request contains at least one malicious content object.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:

```txt
# Check if requests to a specific endpoint include any malicious content objects
cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq "/upload"
```

Categories:
- Request
