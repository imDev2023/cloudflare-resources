---
description: The mTLS client certificate is not valid after this date.
title: cf.tls_client_auth.cert_not_after
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_not\_after

`cf.tls_client_auth.cert_not_after``String`

The mTLS client certificate is not valid after this date.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"Mar 21 13:35:00 2023 GMT"
```

Categories:
- Request
- mTLS
