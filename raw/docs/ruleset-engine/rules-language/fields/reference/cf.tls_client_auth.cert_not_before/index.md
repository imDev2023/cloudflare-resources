---
description: The mTLS client certificate is not valid before this date.
title: cf.tls_client_auth.cert_not_before
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_not\_before

`cf.tls_client_auth.cert_not_before``String`

The mTLS client certificate is not valid before this date.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"Mar 21 13:35:00 2022 GMT"
```

Categories:
- Request
- mTLS
