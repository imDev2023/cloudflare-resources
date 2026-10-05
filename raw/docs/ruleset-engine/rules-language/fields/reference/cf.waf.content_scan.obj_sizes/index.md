---
description: An array of file sizes in bytes, in the order the content objects were detected in the request.
title: cf.waf.content_scan.obj_sizes
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.content\_scan.obj\_sizes

`cf.waf.content_scan.obj_sizes``Array<Integer>`

An array of file sizes in bytes, in the order the content objects were detected in the request.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:

```txt
# Check if requests to a specific endpoint contain any content objects larger than 500 KB (512,000 bytes)
any(cf.waf.content_scan.obj_sizes[*] > 512000) and http.request.uri.path eq "/upload"
```

Categories:
- Request
