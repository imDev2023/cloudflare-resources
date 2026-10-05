---
description: Serial number of the mTLS client certificate.
title: cf.tls_client_auth.cert_serial
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_serial

`cf.tls_client_auth.cert_serial``String`

Serial number of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"527E0F20A20EA2A4146C78390F34CE7AF0878CA4"
```

Categories:
- Request
- mTLS
