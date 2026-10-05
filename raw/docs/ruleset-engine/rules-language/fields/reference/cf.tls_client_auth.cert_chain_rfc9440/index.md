---
description: The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440).
title: cf.tls_client_auth.cert_chain_rfc9440
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_chain\_rfc9440

`cf.tls_client_auth.cert_chain_rfc9440``String`

The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440).

Contains the DER-encoded, Base64-wrapped client certificate chain formatted as an [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440#name-client-cert-chain-http-head) `Client-Cert-Chain` HTTP header value. The value is a structured field list of byte sequences. The leaf certificate is not included in the chain (it is available in [`cf.tls_client_auth.cert_rfc9440`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/)). The chain reflects the certificates as sent by the client, without any reordering or validation.

This field is populated regardless of the certificate validation result. Before using this value, verify the certificate status by checking [`cf.tls_client_auth.cert_verified`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/) and [`cf.tls_client_auth.cert_revoked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/).

Returns `""` if the client did not send any intermediate certificates or if the encoded value exceeds the 16 KiB size limit. Refer to [`cf.tls_client_auth.cert_chain_rfc9440_too_large`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/) to distinguish between these cases.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
":MII.....=:, :MII....=:"
```

Categories:
- Request
- mTLS
