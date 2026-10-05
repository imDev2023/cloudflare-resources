---
title: Webhooks
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Casb](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb)

[Posture](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Webhooks

##### [List webhook configurations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/list)

GET/accounts/{account\_id}/data-security/posture/webhooks

##### [Create a new webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/create)

POST/accounts/{account\_id}/data-security/posture/webhooks

##### [Get webhook configuration by ID](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/get)

GET/accounts/{account\_id}/data-security/posture/webhooks/{webhook\_id}

##### [Update an existing webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/update)

PUT/accounts/{account\_id}/data-security/posture/webhooks/{webhook\_id}

##### [Delete a webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/delete)

DELETE/accounts/{account\_id}/data-security/posture/webhooks/{webhook\_id}

##### [Test a webhook configuration before creating it](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/evaluate)

POST/accounts/{account\_id}/data-security/posture/webhooks/evaluate

##### [Test an existing webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/evaluate_existing)

POST/accounts/{account\_id}/data-security/posture/webhooks/{webhook\_id}/evaluate

##### ModelsExpand Collapse

<details>

<summary>

WebhookListResponse object {id, authentication\_type, created\_at, 6 more }

Webhook configuration for sending finding notifications.

</summary>

id: string

Unique identifier for the specific webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

authentication\_type: "Basic Auth"or "None"or "Bearer Auth"or 2 more

Type of authentication used for the webhook.

</summary>

One of the following:

"Basic Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%200">Link to this property</a>

"None"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%201">Link to this property</a>

"Bearer Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%202">Link to this property</a>

"Static Headers"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%203">Link to this property</a>

"HMAC-Signing"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type">Link to this property</a>

created\_at: string

Timestamp when the webhook configuration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

destination\_url: string

Target URL for the webhook configuration. Where resulting data will be sent.

formaturi

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20destination_url">Link to this property</a>

label: string

Account-specified display label for the webhook configuration.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

status: "enabled"or "disabled"

Current status of the webhook configuration. If disabled, data cannot be sent through this configuration.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

Timestamp when the webhook configuration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

version: number

Version number of the configuration.

formatuint32

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

headers: optional array of object {key, value }

List of header keys configured for this webhook. Values are not included for security reasons.

</summary>

key: optional string

Header key name (lowercase).

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

value: optional string

Header value. This field is never returned in API responses for security reasons.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)%20%3E%20(property)%20headers">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_list_response%20%3E%20(schema)>)

<details>

<summary>

WebhookCreateResponse object {id, authentication\_type, created\_at, 6 more }

Webhook configuration for sending finding notifications.

</summary>

id: string

Unique identifier for the specific webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

authentication\_type: "Basic Auth"or "None"or "Bearer Auth"or 2 more

Type of authentication used for the webhook.

</summary>

One of the following:

"Basic Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%200">Link to this property</a>

"None"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%201">Link to this property</a>

"Bearer Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%202">Link to this property</a>

"Static Headers"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%203">Link to this property</a>

"HMAC-Signing"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type">Link to this property</a>

created\_at: string

Timestamp when the webhook configuration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

destination\_url: string

Target URL for the webhook configuration. Where resulting data will be sent.

formaturi

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20destination_url">Link to this property</a>

label: string

Account-specified display label for the webhook configuration.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

status: "enabled"or "disabled"

Current status of the webhook configuration. If disabled, data cannot be sent through this configuration.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

Timestamp when the webhook configuration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

version: number

Version number of the configuration.

formatuint32

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

headers: optional array of object {key, value }

List of header keys configured for this webhook. Values are not included for security reasons.

</summary>

key: optional string

Header key name (lowercase).

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

value: optional string

Header value. This field is never returned in API responses for security reasons.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20headers">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)>)

<details>

<summary>

WebhookGetResponse object {id, authentication\_type, created\_at, 6 more }

Webhook configuration for sending finding notifications.

</summary>

id: string

Unique identifier for the specific webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

authentication\_type: "Basic Auth"or "None"or "Bearer Auth"or 2 more

Type of authentication used for the webhook.

</summary>

One of the following:

"Basic Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%200">Link to this property</a>

"None"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%201">Link to this property</a>

"Bearer Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%202">Link to this property</a>

"Static Headers"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%203">Link to this property</a>

"HMAC-Signing"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type">Link to this property</a>

created\_at: string

Timestamp when the webhook configuration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

destination\_url: string

Target URL for the webhook configuration. Where resulting data will be sent.

formaturi

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20destination_url">Link to this property</a>

label: string

Account-specified display label for the webhook configuration.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

status: "enabled"or "disabled"

Current status of the webhook configuration. If disabled, data cannot be sent through this configuration.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

Timestamp when the webhook configuration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

version: number

Version number of the configuration.

formatuint32

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

headers: optional array of object {key, value }

List of header keys configured for this webhook. Values are not included for security reasons.

</summary>

key: optional string

Header key name (lowercase).

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

value: optional string

Header value. This field is never returned in API responses for security reasons.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)%20%3E%20(property)%20headers">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_get_response%20%3E%20(schema)>)

<details>

<summary>

WebhookUpdateResponse object {id, authentication\_type, created\_at, 6 more }

Webhook configuration for sending finding notifications.

</summary>

id: string

Unique identifier for the specific webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

authentication\_type: "Basic Auth"or "None"or "Bearer Auth"or 2 more

Type of authentication used for the webhook.

</summary>

One of the following:

"Basic Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%200">Link to this property</a>

"None"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%201">Link to this property</a>

"Bearer Auth"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%202">Link to this property</a>

"Static Headers"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%203">Link to this property</a>

"HMAC-Signing"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_type">Link to this property</a>

created\_at: string

Timestamp when the webhook configuration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

destination\_url: string

Target URL for the webhook configuration. Where resulting data will be sent.

formaturi

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20destination_url">Link to this property</a>

label: string

Account-specified display label for the webhook configuration.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

status: "enabled"or "disabled"

Current status of the webhook configuration. If disabled, data cannot be sent through this configuration.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

Timestamp when the webhook configuration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

version: number

Version number of the configuration.

formatuint32

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

headers: optional array of object {key, value }

List of header keys configured for this webhook. Values are not included for security reasons.

</summary>

key: optional string

Header key name (lowercase).

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

value: optional string

Header value. This field is never returned in API responses for security reasons.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20headers">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)>)

<details>

<summary>

WebhookDeleteResponse object {errors, messages, success }

Common response structure for all API endpoints.

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

Error or message code.

minimum1000

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

Human-readable message.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

Link to relevant documentation.

formaturi

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

JSON pointer to the source of the error.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

Error or message code.

minimum1000

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

Human-readable message.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

Link to relevant documentation.

formaturi

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

JSON pointer to the source of the error.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: boolean

Whether the API call was successful.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)>)

<details>

<summary>

WebhookEvaluateResponse object {message, status\_code, success }

Response body for webhook evaluation test results.

</summary>

message: string

Human-readable message describing the test result.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

status\_code: number

HTTP status code returned by the webhook endpoint. 0 if connection failed.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_response%20%3E%20(schema)%20%3E%20(property)%20status_code">Link to this property</a>

success: boolean

Whether the webhook test was successful (received 2xx response).

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_response%20%3E%20(schema)>)

<details>

<summary>

WebhookEvaluateExistingResponse object {message, status\_code, success }

Response body for webhook evaluation test results.

</summary>

message: string

Human-readable message describing the test result.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_existing_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

status\_code: number

HTTP status code returned by the webhook endpoint. 0 if connection failed.

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_existing_response%20%3E%20(schema)%20%3E%20(property)%20status_code">Link to this property</a>

success: boolean

Whether the webhook test was successful (received 2xx response).

<a href="#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_existing_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks%20%3E%20(model)%20webhook_evaluate_existing_response%20%3E%20(schema)>)

#### WebhooksJobs

##### [Create webhook jobs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/subresources/jobs/methods/create)

POST/accounts/{account\_id}/data-security/posture/webhooks/jobs

##### ModelsExpand Collapse

<details>

<summary>

JobCreateResponse object {created, failed }

</summary>

<details>

<summary>

created: array of object {id, asset\_data, created\_at, 9 more }

Successfully created webhook jobs.

</summary>

id: string

Unique identifier for the webhook job.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

asset\_data: map\[unknown]

Asset data associated with this webhook job.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20asset_data">Link to this property</a>

created\_at: string

When the webhook job was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

integration\_id: string

ID of the integration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20integration_id">Link to this property</a>

last\_updated\_at: string

When the webhook job was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20last_updated_at">Link to this property</a>

<details>

<summary>

parameters: object {finding\_instance\_id }

Parameters for a webhook job.

</summary>

finding\_instance\_id: string

ID of the finding instance.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20parameters%20%3E%20(property)%20finding_instance_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20parameters">Link to this property</a>

<details>

<summary>

status: "pending"or "processing"or "completed"or "failed"

Status of a webhook job.

</summary>

One of the following:

"pending"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"completed"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

triggered\_by\_actor: "user"or "account\_token"

Type of actor that triggered the webhook job.

</summary>

One of the following:

"user"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_actor%20%3E%20(member)%200">Link to this property</a>

"account\_token"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_actor%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_actor">Link to this property</a>

triggered\_by\_id: string

ID of the actor that triggered the job.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_id">Link to this property</a>

webhook\_id: string

ID of the webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20webhook_id">Link to this property</a>

failure\_details: optional map\[unknown]

Additional details about the failure.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_details">Link to this property</a>

<details>

<summary>

failure\_reason: optional "Permission Denied"or "Integration Unavailable"or "Service Temporarily Unavailable"or "System Error"

Reason for webhook job failure.

</summary>

One of the following:

"Permission Denied"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%200">Link to this property</a>

"Integration Unavailable"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%201">Link to this property</a>

"Service Temporarily Unavailable"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%202">Link to this property</a>

"System Error"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

<details>

<summary>

failed: array of object {error, finding\_instance\_id, webhook\_id }

Failed webhook job creation attempts.

</summary>

error: string

Error message describing the failure.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

finding\_instance\_id: string

ID of the finding instance that failed to create a webhook job.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed%20%3E%20(items)%20%3E%20(property)%20finding_instance_id">Link to this property</a>

webhook\_id: string

ID of the webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed%20%3E%20(items)%20%3E%20(property)%20webhook_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)>)