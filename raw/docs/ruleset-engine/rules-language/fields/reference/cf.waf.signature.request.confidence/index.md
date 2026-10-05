---
description: An array of confidence values associated with attack signatures that matched the request.
title: cf.waf.signature.request.confidence
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.signature.request.confidence

`cf.waf.signature.request.confidence``Array<String>`

An array of confidence values associated with attack signatures that matched the request.

Supported values are `high` and `low`.

Available to customers with [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.

Example value:

```txt
["high"]
```

Example usage:

```txt
any(cf.waf.signature.request.confidence[*] eq "high")
```

Categories:
- Request
