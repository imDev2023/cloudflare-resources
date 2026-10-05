---
title: OAuth Clients
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[IAM](https://developers.cloudflare.com/api/resources/iam)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# OAuth Clients

##### [List OAuth Clients](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/list)

GET/accounts/{account\_id}/oauth\_clients

##### [OAuth Client Details](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/get)

GET/accounts/{account\_id}/oauth\_clients/{oauth\_client\_id}

##### [Create OAuth Client](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/create)

POST/accounts/{account\_id}/oauth\_clients

##### [Update OAuth Client](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/update)

PATCH/accounts/{account\_id}/oauth\_clients/{oauth\_client\_id}

##### [Delete OAuth Client](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/delete)

DELETE/accounts/{account\_id}/oauth\_clients/{oauth\_client\_id}

##### [Rotate OAuth Client Secret](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/rotate_secret)

POST/accounts/{account\_id}/oauth\_clients/{oauth\_client\_id}/rotate\_secret

##### [Delete Rotated OAuth Client Secret](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/delete_rotated_secret)

DELETE/accounts/{account\_id}/oauth\_clients/{oauth\_client\_id}/rotate\_secret

##### ModelsExpand Collapse

<details>

<summary>

OAuthClientListResponse object {client\_id, visibility, allowed\_cors\_origins, 17 more }

Fields shared by OAuth client responses and create/update requests.

</summary>

client\_id: string

The unique identifier for an OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_id">Link to this property</a>

<details>

<summary>

visibility: "public"or "private"

Visibility of the OAuth client.

</summary>

One of the following:

"public"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%200">Link to this property</a>

"private"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20visibility">Link to this property</a>

allowed\_cors\_origins: optional array of string

Array of allowed CORS origins.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_cors_origins">Link to this property</a>

client\_name: optional string

Human-readable name of the OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_name">Link to this property</a>

client\_uri: optional string

URL of the home page of the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri">Link to this property</a>

<details>

<summary>

client\_uri\_verification: optional object {status, text }

Client URI domain control verification state.

</summary>

<details>

<summary>

status: optional "pending"or "in\_progress"or "verified"or "failed"

Current verification status for the client URI host.

</summary>

One of the following:

"pending"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"in\_progress"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"verified"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failed"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status">Link to this property</a>

text: optional string

Exact TXT record value that must be added to DNS to prove ownership of the client URI host.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification">Link to this property</a>

created\_at: optional string

Timestamp when the OAuth client was created.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

grant\_types: optional array of "authorization\_code"or "refresh\_token"

Array of OAuth grant types the client is allowed to use. <code>authorization_code</code> is required; <code>refresh_token</code> may be included optionally.

</summary>

One of the following:

"authorization\_code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"refresh\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20grant_types">Link to this property</a>

has\_rotated\_secret: optional boolean

Indicates whether the client has a rotated secret that has not yet been deleted.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20has_rotated_secret">Link to this property</a>

logo\_uri: optional string

URL of the client’s logo.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20logo_uri">Link to this property</a>

optional\_scopes: optional array of string

Scopes that the authorizing user may decline during consent. Each value must also appear in <code>scopes</code>. The scopes <code>openid</code>, <code>offline</code>, and <code>offline_access</code> cannot be optional.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20optional_scopes">Link to this property</a>

policy\_uri: optional string

URL that points to a privacy policy document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20policy_uri">Link to this property</a>

post\_logout\_redirect\_uris: optional array of string

Array of allowed post-logout redirect URIs.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20post_logout_redirect_uris">Link to this property</a>

promoted\_at: optional string

Timestamp when the OAuth client was promoted to public visibility.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20promoted_at">Link to this property</a>

redirect\_uris: optional array of string

Array of allowed redirect URIs for the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20redirect_uris">Link to this property</a>

<details>

<summary>

response\_types: optional array of "token"or "id\_token"or "code"

Array of OAuth response types the client is allowed to use.

</summary>

One of the following:

"token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"id\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20response_types">Link to this property</a>

scopes: optional array of string

Array of OAuth scopes the client is allowed to request. Colon-delimited scopes are not accepted. Dot-delimited scopes are validated against available OAuth API scopes; simple identity scopes are allowed. Protocol scopes <code>offline_access</code> and <code>openid</code> are added or removed automatically based on <code>grant_types</code> and <code>response_types</code>.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20scopes">Link to this property</a>

<details>

<summary>

token\_endpoint\_auth\_method: optional "none"or "client\_secret\_basic"or "client\_secret\_post"

The authentication method the client uses at the token endpoint.

</summary>

One of the following:

"none"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%200">Link to this property</a>

"client\_secret\_basic"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%201">Link to this property</a>

"client\_secret\_post"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

tos\_uri: optional string

URL that points to a terms of service document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20tos_uri">Link to this property</a>

updated\_at: optional string

Timestamp when the OAuth client was last updated.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_list_response%20%3E%20(schema)>)

<details>

<summary>

OAuthClientGetResponse object {client\_id, visibility, allowed\_cors\_origins, 17 more }

Fields shared by OAuth client responses and create/update requests.

</summary>

client\_id: string

The unique identifier for an OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_id">Link to this property</a>

<details>

<summary>

visibility: "public"or "private"

Visibility of the OAuth client.

</summary>

One of the following:

"public"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%200">Link to this property</a>

"private"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20visibility">Link to this property</a>

allowed\_cors\_origins: optional array of string

Array of allowed CORS origins.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_cors_origins">Link to this property</a>

client\_name: optional string

Human-readable name of the OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_name">Link to this property</a>

client\_uri: optional string

URL of the home page of the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri">Link to this property</a>

<details>

<summary>

client\_uri\_verification: optional object {status, text }

Client URI domain control verification state.

</summary>

<details>

<summary>

status: optional "pending"or "in\_progress"or "verified"or "failed"

Current verification status for the client URI host.

</summary>

One of the following:

"pending"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"in\_progress"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"verified"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failed"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status">Link to this property</a>

text: optional string

Exact TXT record value that must be added to DNS to prove ownership of the client URI host.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification">Link to this property</a>

created\_at: optional string

Timestamp when the OAuth client was created.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

grant\_types: optional array of "authorization\_code"or "refresh\_token"

Array of OAuth grant types the client is allowed to use. <code>authorization_code</code> is required; <code>refresh_token</code> may be included optionally.

</summary>

One of the following:

"authorization\_code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"refresh\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20grant_types">Link to this property</a>

has\_rotated\_secret: optional boolean

Indicates whether the client has a rotated secret that has not yet been deleted.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20has_rotated_secret">Link to this property</a>

logo\_uri: optional string

URL of the client’s logo.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20logo_uri">Link to this property</a>

optional\_scopes: optional array of string

Scopes that the authorizing user may decline during consent. Each value must also appear in <code>scopes</code>. The scopes <code>openid</code>, <code>offline</code>, and <code>offline_access</code> cannot be optional.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20optional_scopes">Link to this property</a>

policy\_uri: optional string

URL that points to a privacy policy document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20policy_uri">Link to this property</a>

post\_logout\_redirect\_uris: optional array of string

Array of allowed post-logout redirect URIs.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20post_logout_redirect_uris">Link to this property</a>

promoted\_at: optional string

Timestamp when the OAuth client was promoted to public visibility.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20promoted_at">Link to this property</a>

redirect\_uris: optional array of string

Array of allowed redirect URIs for the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20redirect_uris">Link to this property</a>

<details>

<summary>

response\_types: optional array of "token"or "id\_token"or "code"

Array of OAuth response types the client is allowed to use.

</summary>

One of the following:

"token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"id\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20response_types">Link to this property</a>

scopes: optional array of string

Array of OAuth scopes the client is allowed to request. Colon-delimited scopes are not accepted. Dot-delimited scopes are validated against available OAuth API scopes; simple identity scopes are allowed. Protocol scopes <code>offline_access</code> and <code>openid</code> are added or removed automatically based on <code>grant_types</code> and <code>response_types</code>.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20scopes">Link to this property</a>

<details>

<summary>

token\_endpoint\_auth\_method: optional "none"or "client\_secret\_basic"or "client\_secret\_post"

The authentication method the client uses at the token endpoint.

</summary>

One of the following:

"none"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%200">Link to this property</a>

"client\_secret\_basic"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%201">Link to this property</a>

"client\_secret\_post"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

tos\_uri: optional string

URL that points to a terms of service document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20tos_uri">Link to this property</a>

updated\_at: optional string

Timestamp when the OAuth client was last updated.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_get_response%20%3E%20(schema)>)

<details>

<summary>

OAuthClientCreateResponse object {client\_id, visibility, allowed\_cors\_origins, 18 more }

Fields shared by OAuth client responses and create/update requests.

</summary>

client\_id: string

The unique identifier for an OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_id">Link to this property</a>

<details>

<summary>

visibility: "public"or "private"

Visibility of the OAuth client.

</summary>

One of the following:

"public"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%200">Link to this property</a>

"private"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20visibility">Link to this property</a>

allowed\_cors\_origins: optional array of string

Array of allowed CORS origins.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_cors_origins">Link to this property</a>

client\_name: optional string

Human-readable name of the OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_name">Link to this property</a>

client\_secret: optional string

The client secret. This is the only time the secret is returned in a response.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

client\_uri: optional string

URL of the home page of the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri">Link to this property</a>

<details>

<summary>

client\_uri\_verification: optional object {status, text }

Client URI domain control verification state.

</summary>

<details>

<summary>

status: optional "pending"or "in\_progress"or "verified"or "failed"

Current verification status for the client URI host.

</summary>

One of the following:

"pending"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"in\_progress"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"verified"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failed"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status">Link to this property</a>

text: optional string

Exact TXT record value that must be added to DNS to prove ownership of the client URI host.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification">Link to this property</a>

created\_at: optional string

Timestamp when the OAuth client was created.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

grant\_types: optional array of "authorization\_code"or "refresh\_token"

Array of OAuth grant types the client is allowed to use. <code>authorization_code</code> is required; <code>refresh_token</code> may be included optionally.

</summary>

One of the following:

"authorization\_code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"refresh\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20grant_types">Link to this property</a>

has\_rotated\_secret: optional boolean

Indicates whether the client has a rotated secret that has not yet been deleted.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20has_rotated_secret">Link to this property</a>

logo\_uri: optional string

URL of the client’s logo.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20logo_uri">Link to this property</a>

optional\_scopes: optional array of string

Scopes that the authorizing user may decline during consent. Each value must also appear in <code>scopes</code>. The scopes <code>openid</code>, <code>offline</code>, and <code>offline_access</code> cannot be optional.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20optional_scopes">Link to this property</a>

policy\_uri: optional string

URL that points to a privacy policy document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20policy_uri">Link to this property</a>

post\_logout\_redirect\_uris: optional array of string

Array of allowed post-logout redirect URIs.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20post_logout_redirect_uris">Link to this property</a>

promoted\_at: optional string

Timestamp when the OAuth client was promoted to public visibility.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20promoted_at">Link to this property</a>

redirect\_uris: optional array of string

Array of allowed redirect URIs for the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20redirect_uris">Link to this property</a>

<details>

<summary>

response\_types: optional array of "token"or "id\_token"or "code"

Array of OAuth response types the client is allowed to use.

</summary>

One of the following:

"token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"id\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20response_types">Link to this property</a>

scopes: optional array of string

Array of OAuth scopes the client is allowed to request. Colon-delimited scopes are not accepted. Dot-delimited scopes are validated against available OAuth API scopes; simple identity scopes are allowed. Protocol scopes <code>offline_access</code> and <code>openid</code> are added or removed automatically based on <code>grant_types</code> and <code>response_types</code>.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20scopes">Link to this property</a>

<details>

<summary>

token\_endpoint\_auth\_method: optional "none"or "client\_secret\_basic"or "client\_secret\_post"

The authentication method the client uses at the token endpoint.

</summary>

One of the following:

"none"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%200">Link to this property</a>

"client\_secret\_basic"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%201">Link to this property</a>

"client\_secret\_post"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

tos\_uri: optional string

URL that points to a terms of service document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20tos_uri">Link to this property</a>

updated\_at: optional string

Timestamp when the OAuth client was last updated.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_create_response%20%3E%20(schema)>)

<details>

<summary>

OAuthClientUpdateResponse object {client\_id, visibility, allowed\_cors\_origins, 17 more }

Fields shared by OAuth client responses and create/update requests.

</summary>

client\_id: string

The unique identifier for an OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_id">Link to this property</a>

<details>

<summary>

visibility: "public"or "private"

Visibility of the OAuth client.

</summary>

One of the following:

"public"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%200">Link to this property</a>

"private"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20visibility">Link to this property</a>

allowed\_cors\_origins: optional array of string

Array of allowed CORS origins.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20allowed_cors_origins">Link to this property</a>

client\_name: optional string

Human-readable name of the OAuth client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_name">Link to this property</a>

client\_uri: optional string

URL of the home page of the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri">Link to this property</a>

<details>

<summary>

client\_uri\_verification: optional object {status, text }

Client URI domain control verification state.

</summary>

<details>

<summary>

status: optional "pending"or "in\_progress"or "verified"or "failed"

Current verification status for the client URI host.

</summary>

One of the following:

"pending"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"in\_progress"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"verified"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failed"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20status">Link to this property</a>

text: optional string

Exact TXT record value that must be added to DNS to prove ownership of the client URI host.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20client_uri_verification">Link to this property</a>

created\_at: optional string

Timestamp when the OAuth client was created.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

grant\_types: optional array of "authorization\_code"or "refresh\_token"

Array of OAuth grant types the client is allowed to use. <code>authorization_code</code> is required; <code>refresh_token</code> may be included optionally.

</summary>

One of the following:

"authorization\_code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"refresh\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20grant_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20grant_types">Link to this property</a>

has\_rotated\_secret: optional boolean

Indicates whether the client has a rotated secret that has not yet been deleted.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20has_rotated_secret">Link to this property</a>

logo\_uri: optional string

URL of the client’s logo.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20logo_uri">Link to this property</a>

optional\_scopes: optional array of string

Scopes that the authorizing user may decline during consent. Each value must also appear in <code>scopes</code>. The scopes <code>openid</code>, <code>offline</code>, and <code>offline_access</code> cannot be optional.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20optional_scopes">Link to this property</a>

policy\_uri: optional string

URL that points to a privacy policy document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20policy_uri">Link to this property</a>

post\_logout\_redirect\_uris: optional array of string

Array of allowed post-logout redirect URIs.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20post_logout_redirect_uris">Link to this property</a>

promoted\_at: optional string

Timestamp when the OAuth client was promoted to public visibility.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20promoted_at">Link to this property</a>

redirect\_uris: optional array of string

Array of allowed redirect URIs for the client.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20redirect_uris">Link to this property</a>

<details>

<summary>

response\_types: optional array of "token"or "id\_token"or "code"

Array of OAuth response types the client is allowed to use.

</summary>

One of the following:

"token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"id\_token"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"code"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20response_types%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20response_types">Link to this property</a>

scopes: optional array of string

Array of OAuth scopes the client is allowed to request. Colon-delimited scopes are not accepted. Dot-delimited scopes are validated against available OAuth API scopes; simple identity scopes are allowed. Protocol scopes <code>offline_access</code> and <code>openid</code> are added or removed automatically based on <code>grant_types</code> and <code>response_types</code>.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20scopes">Link to this property</a>

<details>

<summary>

token\_endpoint\_auth\_method: optional "none"or "client\_secret\_basic"or "client\_secret\_post"

The authentication method the client uses at the token endpoint.

</summary>

One of the following:

"none"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%200">Link to this property</a>

"client\_secret\_basic"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%201">Link to this property</a>

"client\_secret\_post"

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

tos\_uri: optional string

URL that points to a terms of service document.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20tos_uri">Link to this property</a>

updated\_at: optional string

Timestamp when the OAuth client was last updated.

formatdate-time

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_update_response%20%3E%20(schema)>)

<details>

<summary>

OAuthClientDeleteResponse object {id }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_delete_response%20%3E%20(schema)>)

<details>

<summary>

OAuthClientRotateSecretResponse object {client\_secret }

</summary>

client\_secret: optional string

The new client secret.

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_rotate_secret_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_rotate_secret_response%20%3E%20(schema)>)

<details>

<summary>

OAuthClientDeleteRotatedSecretResponse object {id }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_delete_rotated_secret_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.oauth_clients%20%3E%20(model)%20oauth_client_delete_rotated_secret_response%20%3E%20(schema)>)