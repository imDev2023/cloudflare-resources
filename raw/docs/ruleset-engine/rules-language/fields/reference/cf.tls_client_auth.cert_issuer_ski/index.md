---
description: The Subject Key Identifier (SKI) of the direct issuer of the mTLS client certificate.
title: cf.tls_client_auth.cert_issuer_ski
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_issuer\_ski

`cf.tls_client_auth.cert_issuer_ski``String`

The Subject Key Identifier (SKI) of the direct issuer of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"8204924CF49D471E855862706D889F58F6B784D3"
```

Categories:
- Request
- mTLS
