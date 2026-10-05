---
title: Token Validation
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Token Validation

#### Token ValidationConfiguration

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

#### Token ValidationConfigurationCredentials

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

#### Token ValidationRules

##### [List token validation rules](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/list)

GET/zones/{zone\_id}/token\_validation/rules

##### [Create a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/create)

POST/zones/{zone\_id}/token\_validation/rules

##### [Create token validation rules](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/bulk_create)

POST/zones/{zone\_id}/token\_validation/rules/bulk

##### [Edit token validation rules](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/bulk_edit)

PATCH/zones/{zone\_id}/token\_validation/rules/bulk

##### [Get a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/get)

GET/zones/{zone\_id}/token\_validation/rules/{rule\_id}

##### [Delete a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/delete)

DELETE/zones/{zone\_id}/token\_validation/rules/{rule\_id}

##### [Edit a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/edit)

PATCH/zones/{zone\_id}/token\_validation/rules/{rule\_id}

##### ModelsExpand Collapse

<details>

<summary>

TokenValidationRule object {action, description, enabled, 6 more }

A Token Validation rule that can enforce security policies using JWT Tokens.

</summary>

<details>

<summary>

action: "log"or "block"

Action to take on requests that match operations included in <code>selector</code> and fail <code>expression</code>.

</summary>

One of the following:

"log"

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

description: string

A human-readable description that gives more details than <code>title</code>.

maxLength500

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: boolean

Toggle rule on or off.

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

Rule expression. Requests that fail to match this expression will be subject to <code>action</code>.

For details on expressions, see the <a href="https://developers.cloudflare.com/api-shield/security/jwt-validation/">Cloudflare Docs</a>.

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

selector: object {exclude, include }

Select operations covered by this rule.

For details on selectors, see the <a href="https://developers.cloudflare.com/api-shield/security/jwt-validation/">Cloudflare Docs</a>.

</summary>

<details>

<summary>

exclude: optional array of object {operation\_ids }

Ignore operations that were otherwise included by <code>include</code>.

</summary>

operation\_ids: optional array of string

Excluded operation IDs.

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20selector%20%3E%20(property)%20exclude%20%3E%20(items)%20%3E%20(property)%20operation_ids">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20selector%20%3E%20(property)%20exclude">Link to this property</a>

<details>

<summary>

include: optional array of object {host }

Select all matching operations.

</summary>

host: optional array of string

Included hostnames.

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20selector%20%3E%20(property)%20include%20%3E%20(items)%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20selector%20%3E%20(property)%20include">Link to this property</a>

</details>

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20selector">Link to this property</a>

title: string

A human-readable name for the rule.

maxLength50

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

id: optional string

UUID.

maxLength36

minLength36

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

last\_updated: optional string

formatdate-time

<a href="#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

</details>

[Link to this property](<#(resource)%20token_validation.rules%20%3E%20(model)%20token_validation_rule%20%3E%20(schema)>)

RuleDeleteResponse = unknown

[Link to this property](<#(resource)%20token_validation.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)>)