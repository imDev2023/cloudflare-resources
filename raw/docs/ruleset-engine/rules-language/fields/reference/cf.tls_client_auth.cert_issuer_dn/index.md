---
description: The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate.
title: cf.tls_client_auth.cert_issuer_dn
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_issuer\_dn

`cf.tls_client_auth.cert_issuer_dn``String`

The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"CN=Access Testing CA,OU=TX,O=Access Testing,L=Austin,ST=Texas,C=US"
```

Categories:
- Request
- mTLS
