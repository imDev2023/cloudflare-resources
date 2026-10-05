---
description: The SHA-1 fingerprint of TLS client extensions, encoded in Base64 using big-endian format.
title: cf.tls_client_extensions_sha1
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_extensions\_sha1

`cf.tls_client_extensions_sha1``String`

The SHA-1 fingerprint of TLS client extensions, encoded in Base64 using big-endian format.

For the little-endian version of this field, refer to [`cf.tls_client_extensions_sha1_le`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_extensions_sha1_le/).

Example value:

```txt
"OWFiM2I5ZDc0YWI0YWYzZmFkMGU0ZjhlYjhiYmVkMjgxNTU5YTU2Mg=="
```

Categories:
- Request
- SSL/TLS
