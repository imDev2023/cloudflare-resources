---
description: The mTLS client certificate encoded as a Structured Fields Byte Sequence per [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440).
title: cf.tls_client_auth.cert_rfc9440
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_rfc9440

`cf.tls_client_auth.cert_rfc9440``String`

The mTLS client certificate encoded as a Structured Fields Byte Sequence per [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440).

Contains the DER-encoded, Base64-wrapped client leaf certificate formatted as an [RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440#name-client-cert-http-header-fie) `Client-Cert` HTTP header value. The value is a Structured Fields Byte Sequence (the Base64 data prefixed and suffixed by `:`).

This field is populated regardless of the certificate validation result. Before using this value, verify the certificate status by checking [`cf.tls_client_auth.cert_verified`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/) and [`cf.tls_client_auth.cert_revoked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/).

Returns `""` if no client certificate was presented or if the encoded value exceeds the 10 KiB size limit. Refer to [`cf.tls_client_auth.cert_rfc9440_too_large`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440_too_large/) to distinguish between these cases.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
":MIIBqDCCAU6g......:"
```

Categories:
- Request
- mTLS
