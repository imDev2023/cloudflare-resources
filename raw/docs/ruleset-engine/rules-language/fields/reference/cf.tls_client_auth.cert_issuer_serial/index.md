---
description: Serial number of the direct issuer of the mTLS client certificate.
title: cf.tls_client_auth.cert_issuer_serial
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_issuer\_serial

`cf.tls_client_auth.cert_issuer_serial``String`

Serial number of the direct issuer of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"2688201DBA77402EA87118876F2E1B24CF8B0395"
```

Categories:
- Request
- mTLS
