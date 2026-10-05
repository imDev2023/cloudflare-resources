---
description: The value of the 32-byte random value provided by the client in a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake), encoded in Base64.
title: cf.tls_client_random
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_random

`cf.tls_client_random``String`

The value of the 32-byte random value provided by the client in a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake), encoded in Base64.

For more details, refer to [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2).

Example value:

```txt
"YWJjZA=="
```

Categories:
- Request
- SSL/TLS
