---
description: The `aud` (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.
title: http.request.jwt.claims.aud.names
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# http.request.jwt.claims.aud.names

`http.request.jwt.claims.aud.names``Array<String>`

The `aud` (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.

Each principal intended to process the JWT must identify itself with a value in the audience claim. In the general case, the `aud` value is an array of case-sensitive strings, each containing a `StringOrURI` value. For details, refer to the [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) in RFC 7519.

Requires a Cloudflare Enterprise plan with a paid add-on.

For more information on validating JSON Web Tokens, refer to [JSON Web Tokens Validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) in the API Shield documentation.

Categories:
- Request
- JWT validation
