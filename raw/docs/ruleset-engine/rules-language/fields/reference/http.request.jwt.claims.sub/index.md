---
description: The `sub` (subject) claim identifies the principal that is the subject of the JWT.
title: http.request.jwt.claims.sub
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.jwt.claims.sub

`http.request.jwt.claims.sub``Map<Array<String>>`

The `sub` (subject) claim identifies the principal that is the subject of the JWT.

The claims in a JWT are normally statements about the subject. For details, refer to the [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) in RFC 7519.

Requires a Cloudflare Enterprise plan with a paid add-on.

For more information on validating JSON Web Tokens, refer to [JSON Web Tokens Validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) in the API Shield documentation.

Categories:
- Request
- JWT validation
