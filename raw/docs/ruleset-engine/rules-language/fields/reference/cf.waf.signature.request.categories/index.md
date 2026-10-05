---
description: An array of categories associated with attack signatures that matched the request.
title: cf.waf.signature.request.categories
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.signature.request.categories

`cf.waf.signature.request.categories``Array<String>`

An array of categories associated with attack signatures that matched the request.

Available to customers with [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) in Security Analytics and Custom Rules.

Contact your Cloudflare account team to request Early Access.

Example value:

```txt
["sqli", "cve-2025-55182"]
```

Example usage:

```txt
any(cf.waf.signature.request.categories[*] eq "sqli")
```

Categories:
- Request
