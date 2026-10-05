---
title: Configuration
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Token Validation](https://developers.cloudflare.com/api/resources/token_validation)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Configuration

##### [List token validation configurations](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/list)

GET/zones/{zone\_id}/token\_validation/config

##### [Get a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/get)

GET/zones/{zone\_id}/token\_validation/config/{config\_id}

##### [Create a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/create)

POST/zones/{zone\_id}/token\_validation/config

##### [Edit a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/edit)

PATCH/zones/{zone\_id}/token\_validation/config/{config\_id}

##### [Delete a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/delete)

DELETE/zones/{zone\_id}/token\_validation/config/{config\_id}

##### ModelsExpand Collapse

<details>

<summary>

TokenConfig object {id, created\_at, credentials, 5 more }

</summary>

id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

credentials: object {keys }

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

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%200">Link to this property</a>

"RS384"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%201">Link to this property</a>

"RS512"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%202">Link to this property</a>

"PS256"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%203">Link to this property</a>

"PS384"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%204">Link to this property</a>

"PS512"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alg">Link to this property</a>

e: string

RSA exponent

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20e">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kid">Link to this property</a>

kty: "RSA"

Key Type

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kty">Link to this property</a>

n: string

RSA modulus

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20n">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyEcEs256 object {alg, crv, kid, 3 more }

JSON representation of an ES256 key

</summary>

alg: "ES256"

Algorithm

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20alg">Link to this property</a>

crv: "P-256"

Curve

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20crv">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kid">Link to this property</a>

kty: "EC"

Key Type

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kty">Link to this property</a>

x: string

X EC coordinate

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20x">Link to this property</a>

y: string

Y EC coordinate

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20y">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

APIShieldCredentialsJWTKeyEcEs384 object {alg, crv, kid, 3 more }

JSON representation of an ES384 key

</summary>

alg: "ES384"

Algorithm

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20alg">Link to this property</a>

crv: "P-384"

Curve

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20crv">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20kid">Link to this property</a>

kty: "EC"

Key Type

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20kty">Link to this property</a>

x: string

X EC coordinate

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20x">Link to this property</a>

y: string

Y EC coordinate

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20y">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

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

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%200">Link to this property</a>

"HS384"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%201">Link to this property</a>

"HS512"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20alg">Link to this property</a>

kid: string

Key ID

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20kid">Link to this property</a>

kty: "oct"

Key Type

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20kty">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials%20%3E%20(property)%20keys">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20credentials">Link to this property</a>

description: string

maxLength500

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

title: string

maxLength50

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

token\_sources: array of string

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20token_sources">Link to this property</a>

token\_type: "JWT"

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)%20%3E%20(property)%20token_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20token_validation.configuration%20%3E%20(model)%20token_config%20%3E%20(schema)>)

<details>

<summary>

ConfigurationEditResponse object {id, description, title, token\_sources }

</summary>

id: optional string

UUID.

maxLength36

minLength36

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

maxLength500

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_edit_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

title: optional string

maxLength50

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_edit_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

token\_sources: optional array of string

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_edit_response%20%3E%20(schema)%20%3E%20(property)%20token_sources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_edit_response%20%3E%20(schema)>)

<details>

<summary>

ConfigurationDeleteResponse object {id }

</summary>

id: optional string

UUID.

maxLength36

minLength36

<a href="#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20token_validation.configuration%20%3E%20(model)%20configuration_delete_response%20%3E%20(schema)>)

#### ConfigurationCredentials

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