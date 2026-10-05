---
description: The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate in a legacy format.
title: cf.tls_client_auth.cert_issuer_dn_legacy
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_issuer\_dn\_legacy

`cf.tls_client_auth.cert_issuer_dn_legacy``String`

The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate in a legacy format.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"/C=US/ST=Texas/L=Austin/O=Access Testing/OU=TX/CN=Access Testing CA"
```

Categories:
- Request
- mTLS
