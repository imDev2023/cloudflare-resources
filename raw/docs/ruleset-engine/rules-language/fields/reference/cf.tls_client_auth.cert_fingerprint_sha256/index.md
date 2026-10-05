---
description: The SHA-256 fingerprint of the mTLS client certificate.
title: cf.tls_client_auth.cert_fingerprint_sha256
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_fingerprint\_sha256

`cf.tls_client_auth.cert_fingerprint_sha256``String`

The SHA-256 fingerprint of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"af363dc85bc942a892d3cee9796190fdb36d89cd588a4f1cb17c74a943439714"
```

Categories:
- Request
- mTLS
