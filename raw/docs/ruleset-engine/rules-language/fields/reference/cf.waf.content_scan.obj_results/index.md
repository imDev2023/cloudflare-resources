---
description: An array of scan results in the order the content objects were detected in the request.
title: cf.waf.content_scan.obj_results
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.content\_scan.obj\_results

`cf.waf.content_scan.obj_results``Array<String>`

An array of scan results in the order the content objects were detected in the request.

The possible values are: `clean`, `suspicious`, `infected`, and `not scanned`.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Example usage:

```txt
# Check if requests to a specific endpoint contain any suspicious or infected content objects
any(cf.waf.content_scan.obj_results[*] in {"suspicious" "infected"}) and http.request.uri.path eq "/upload"
```

Categories:
- Request
