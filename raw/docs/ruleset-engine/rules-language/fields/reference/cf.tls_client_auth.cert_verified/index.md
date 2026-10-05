---
description: Returns `true` when an mTLS client presents a valid client certificate.
title: cf.tls_client_auth.cert_verified
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_verified

`cf.tls_client_auth.cert_verified``Boolean`

Returns `true` when an mTLS client presents a valid client certificate.

Also returns `true` when a client presents a valid certificate that was revoked (refer to [`cf.tls_client_auth.cert_revoked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/)).

This field defaults to `false` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Categories:
- Request
- mTLS
