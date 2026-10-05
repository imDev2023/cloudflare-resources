---
description: Returns `true` when an mTLS client presents a certificate (valid or not).
title: cf.tls_client_auth.cert_presented
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_presented

`cf.tls_client_auth.cert_presented``Boolean`

Returns `true` when an mTLS client presents a certificate (valid or not).

This field defaults to `false` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Categories:
- Request
- mTLS
