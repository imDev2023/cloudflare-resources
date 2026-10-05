---
title: Credentials
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Token Validation](https://developers.cloudflare.com/api/resources/token_validation)

[Configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Credentials

##### [Replace token validation credentials](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/subresources/credentials/methods/update)

PUT/zones/{zone\_id}/token\_validation/config/{config\_id}/credentials

##### [Edit token validation credentials](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/subresources/credentials/methods/edit)

PATCH/zones/{zone\_id}/token\_validation/config/{config\_id}/credentials

##### ModelsExpand Collapse

<details>

<summary>

CredentialUpdateResponse object {keys }

</summary>

<details>

<summary>

keys: array of object {alg, e, kid, 2 more } or object {alg, crv, kid, 3 more } or object {alg, crv, kid, 3 more } or object {alg, kid, kty }

</summary>

One of the following:

<details>

<summary>

APIShieldCredentialsJWTKeyRSA object {alg, e, kid, 2 more }

JSON representation of an RSA key.

</summary>

<details>

<summary>

alg: "RS256"or "RS384"or "RS512"or 3 more

Algorithm

</summary>

One of the following:

"RS256"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%200">Link to this property</a>

"RS384"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%201">Link to this property</a>

"RS512"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%202">Link to this property</a>

"PS256"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%203">Link to this property</a>

"PS384"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%204">Link to this property</a>

"PS512"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg">Link to this property</a>

e: string

RSA exponent

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20e">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kid">Link to this property</a>

kty: "RSA"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kty">Link to this property</a>

n: string

RSA modulus

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20n">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyEcEs256 object {alg, crv, kid, 3 more }

JSON representation of an ES256 key

</summary>

alg: "ES256"

Algorithm

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20alg">Link to this property</a>

crv: "P-256"

Curve

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20crv">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kid">Link to this property</a>

kty: "EC"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kty">Link to this property</a>

x: string

X EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20x">Link to this property</a>

y: string

Y EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20y">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyEcEs384 object {alg, crv, kid, 3 more }

JSON representation of an ES384 key

</summary>

alg: "ES384"

Algorithm

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20alg">Link to this property</a>

crv: "P-384"

Curve

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20crv">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20kid">Link to this property</a>

kty: "EC"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20kty">Link to this property</a>

x: string

X EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20x">Link to this property</a>

y: string

Y EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20y">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyOctResponse object {alg, kid, kty }

JSON representation of a symmetric verification key in API responses (secret material is redacted).

</summary>

<details>

<summary>

alg: "HS256"or "HS384"or "HS512"

Algorithm

</summary>

One of the following:

"HS256"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%200">Link to this property</a>

"HS384"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%201">Link to this property</a>

"HS512"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20kid">Link to this property</a>

kty: "oct"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20kty">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)%20%3E%20(property)%20keys">Link to this property</a>

</details>

[Link to this property](<#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_update_response%20%3E%20(schema)>)

<details>

<summary>

CredentialEditResponse object {keys }

</summary>

<details>

<summary>

keys: array of object {alg, e, kid, 2 more } or object {alg, crv, kid, 3 more } or object {alg, crv, kid, 3 more } or object {alg, kid, kty }

</summary>

One of the following:

<details>

<summary>

APIShieldCredentialsJWTKeyRSA object {alg, e, kid, 2 more }

JSON representation of an RSA key.

</summary>

<details>

<summary>

alg: "RS256"or "RS384"or "RS512"or 3 more

Algorithm

</summary>

One of the following:

"RS256"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%200">Link to this property</a>

"RS384"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%201">Link to this property</a>

"RS512"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%202">Link to this property</a>

"PS256"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%203">Link to this property</a>

"PS384"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%204">Link to this property</a>

"PS512"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg">Link to this property</a>

e: string

RSA exponent

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20e">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kid">Link to this property</a>

kty: "RSA"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kty">Link to this property</a>

n: string

RSA modulus

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20n">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyEcEs256 object {alg, crv, kid, 3 more }

JSON representation of an ES256 key

</summary>

alg: "ES256"

Algorithm

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20alg">Link to this property</a>

crv: "P-256"

Curve

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20crv">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kid">Link to this property</a>

kty: "EC"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kty">Link to this property</a>

x: string

X EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20x">Link to this property</a>

y: string

Y EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20y">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyEcEs384 object {alg, crv, kid, 3 more }

JSON representation of an ES384 key

</summary>

alg: "ES384"

Algorithm

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20alg">Link to this property</a>

crv: "P-384"

Curve

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20crv">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20kid">Link to this property</a>

kty: "EC"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20kty">Link to this property</a>

x: string

X EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20x">Link to this property</a>

y: string

Y EC coordinate

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20y">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyOctResponse object {alg, kid, kty }

JSON representation of a symmetric verification key in API responses (secret material is redacted).

</summary>

<details>

<summary>

alg: "HS256"or "HS384"or "HS512"

Algorithm

</summary>

One of the following:

"HS256"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%200">Link to this property</a>

"HS384"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%201">Link to this property</a>

"HS512"

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20kid">Link to this property</a>

kty: "oct"

Key Type

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20kty">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)%20%3E%20(property)%20keys">Link to this property</a>

</details>

[Link to this property](<#(resource)%20token_validation.configuration.credentials%20%3E%20(model)%20credential_edit_response%20%3E%20(schema)>)