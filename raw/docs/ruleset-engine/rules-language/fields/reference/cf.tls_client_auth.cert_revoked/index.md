---
description: Indicates whether the mTLS client presented a valid but revoked client certificate.
title: cf.tls_client_auth.cert_revoked
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_revoked

`cf.tls_client_auth.cert_revoked``Boolean`

Indicates whether the mTLS client presented a valid but revoked client certificate.

When `true`, the [`cf.tls_client_auth.cert_verified`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/) field is also `true`.

This field defaults to `false` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Categories:
- Request
- mTLS
