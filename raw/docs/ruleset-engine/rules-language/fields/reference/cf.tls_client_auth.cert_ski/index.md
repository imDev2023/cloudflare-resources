---
description: The Subject Key Identifier (SKI) of the mTLS client certificate.
title: cf.tls_client_auth.cert_ski
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_ski

`cf.tls_client_auth.cert_ski``String`

The Subject Key Identifier (SKI) of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"27846FAE6EAC4A8DAD9101B519CF1EB460242831"
```

Categories:
- Request
- mTLS
