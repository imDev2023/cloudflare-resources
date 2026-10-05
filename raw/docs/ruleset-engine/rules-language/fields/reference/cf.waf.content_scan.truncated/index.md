---
description: Indicates whether the request body exceeded the size limit for content scanning and was truncated before scanning.
title: cf.waf.content_scan.truncated
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.content\_scan.truncated

`cf.waf.content_scan.truncated``Boolean`

Indicates whether the request body exceeded the size limit for content scanning and was truncated before scanning.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

When this field is true, the scan results may be incomplete. Refer to [Size limit](https://developers.cloudflare.com/waf/detections/malicious-uploads/#size-limit).

Example usage:

```txt
# Block requests to a specific endpoint whose content was not fully scanned
cf.waf.content_scan.truncated and http.request.uri.path eq "/upload"
```

Categories:
- Request
