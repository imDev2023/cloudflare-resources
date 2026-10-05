---
title: SSO
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[IAM](https://developers.cloudflare.com/api/resources/iam)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# SSO

##### [Get all SSO connectors](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/list)

GET/accounts/{account\_id}/sso\_connectors

##### [Get single SSO connector](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/get)

GET/accounts/{account\_id}/sso\_connectors/{sso\_connector\_id}

##### [Initialize new SSO connector](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/create)

POST/accounts/{account\_id}/sso\_connectors

##### [Update SSO connector state](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/update)

PATCH/accounts/{account\_id}/sso\_connectors/{sso\_connector\_id}

##### [Delete SSO connector](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/delete)

DELETE/accounts/{account\_id}/sso\_connectors/{sso\_connector\_id}

##### [Begin SSO connector verification](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/begin_verification)

POST/accounts/{account\_id}/sso\_connectors/{sso\_connector\_id}/begin\_verification

##### ModelsExpand Collapse

<details>

<summary>

SSOListResponse object {id, created\_on, email\_domain, 4 more }

</summary>

id: optional string

SSO Connector identifier tag.

maxLength32

minLength32

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: optional string

Timestamp for the creation of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

email\_domain: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20email_domain">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

updated\_on: optional string

Timestamp for the last update of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_on">Link to this property</a>

use\_fedramp\_language: optional boolean

Controls the display of FedRAMP language to the user during SSO login

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20use_fedramp_language">Link to this property</a>

<details>

<summary>

verification: optional object {code, status }

</summary>

code: optional string

DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20code">Link to this property</a>

<details>

<summary>

status: optional "awaiting"or "pending"or "failed"or "verified"

The status of the verification code from the verification process.

</summary>

One of the following:

"awaiting"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"verified"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)%20%3E%20(property)%20verification">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.sso%20%3E%20(model)%20sso_list_response%20%3E%20(schema)>)

<details>

<summary>

SSOGetResponse object {id, created\_on, email\_domain, 4 more }

</summary>

id: optional string

SSO Connector identifier tag.

maxLength32

minLength32

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: optional string

Timestamp for the creation of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

email\_domain: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20email_domain">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

updated\_on: optional string

Timestamp for the last update of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_on">Link to this property</a>

use\_fedramp\_language: optional boolean

Controls the display of FedRAMP language to the user during SSO login

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20use_fedramp_language">Link to this property</a>

<details>

<summary>

verification: optional object {code, status }

</summary>

code: optional string

DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20code">Link to this property</a>

<details>

<summary>

status: optional "awaiting"or "pending"or "failed"or "verified"

The status of the verification code from the verification process.

</summary>

One of the following:

"awaiting"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"verified"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)%20%3E%20(property)%20verification">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.sso%20%3E%20(model)%20sso_get_response%20%3E%20(schema)>)

<details>

<summary>

SSOCreateResponse object {id, created\_on, email\_domain, 4 more }

</summary>

id: optional string

SSO Connector identifier tag.

maxLength32

minLength32

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: optional string

Timestamp for the creation of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

email\_domain: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20email_domain">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

updated\_on: optional string

Timestamp for the last update of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_on">Link to this property</a>

use\_fedramp\_language: optional boolean

Controls the display of FedRAMP language to the user during SSO login

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20use_fedramp_language">Link to this property</a>

<details>

<summary>

verification: optional object {code, status }

</summary>

code: optional string

DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20code">Link to this property</a>

<details>

<summary>

status: optional "awaiting"or "pending"or "failed"or "verified"

The status of the verification code from the verification process.

</summary>

One of the following:

"awaiting"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"verified"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)%20%3E%20(property)%20verification">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.sso%20%3E%20(model)%20sso_create_response%20%3E%20(schema)>)

<details>

<summary>

SSOUpdateResponse object {id, created\_on, email\_domain, 4 more }

</summary>

id: optional string

SSO Connector identifier tag.

maxLength32

minLength32

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: optional string

Timestamp for the creation of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

email\_domain: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20email_domain">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

updated\_on: optional string

Timestamp for the last update of the SSO connector

formatdate-time

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_on">Link to this property</a>

use\_fedramp\_language: optional boolean

Controls the display of FedRAMP language to the user during SSO login

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20use_fedramp_language">Link to this property</a>

<details>

<summary>

verification: optional object {code, status }

</summary>

code: optional string

DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20code">Link to this property</a>

<details>

<summary>

status: optional "awaiting"or "pending"or "failed"or "verified"

The status of the verification code from the verification process.

</summary>

One of the following:

"awaiting"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"verified"

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)%20%3E%20(property)%20verification">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.sso%20%3E%20(model)%20sso_update_response%20%3E%20(schema)>)

<details>

<summary>

SSODeleteResponse object {id }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.sso%20%3E%20(model)%20sso_delete_response%20%3E%20(schema)>)

<details>

<summary>

SSOBeginVerificationResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20iam.sso%20%3E%20(model)%20sso_begin_verification_response%20%3E%20(schema)>)