---
description: An array containing up to 10 Refs for attack signatures that matched the request.
title: cf.waf.signature.request.refs
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.signature.request.refs

`cf.waf.signature.request.refs``Array<String>`

An array containing up to 10 Refs for attack signatures that matched the request.

Each Ref is the same value as the corresponding Cloudflare Managed Rules public Rule ID.

Available to customers with [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.

Example value:

```txt
["d68f8101f6e14e25aefcaea69c530a29"]
```

Example usage:

```txt
any(cf.waf.signature.request.refs[*] eq "d68f8101f6e14e25aefcaea69c530a29")
```

Categories:
- Request
