---
description: The Distinguished Name (DN) of the owner (or requester) of the mTLS client certificate in [RFC 2253](https://datatracker.ietf.org/doc/html/rfc2253) format.
title: cf.tls_client_auth.cert_subject_dn_rfc2253
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.tls\_client\_auth.cert\_subject\_dn\_rfc2253

`cf.tls_client_auth.cert_subject_dn_rfc2253``String`

The Distinguished Name (DN) of the owner (or requester) of the mTLS client certificate in [RFC 2253](https://datatracker.ietf.org/doc/html/rfc2253) format.

This field defaults to `""` if the connection does not use [mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/).

Example value:

```txt
"CN=James Royal,OU=Access Admins,O=Access,L=Austin,ST=Texas,C=US"
```

Categories:
- Request
- mTLS
