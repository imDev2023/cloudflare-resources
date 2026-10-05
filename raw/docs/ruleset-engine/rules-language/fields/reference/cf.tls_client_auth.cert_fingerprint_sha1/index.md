---
description: The SHA-1 fingerprint of the mTLS client certificate.
title: cf.tls_client_auth.cert_fingerprint_sha1
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_fingerprint\_sha1

`cf.tls_client_auth.cert_fingerprint_sha1``String`

The SHA-1 fingerprint of the mTLS client certificate.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"933ad5282c560ae3f482a43ecd73bc9de878a190"
```

Categories:
- Request
- mTLS
