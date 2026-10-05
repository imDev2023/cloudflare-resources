---
title: Webhooks
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Alerting](https://developers.cloudflare.com/api/resources/alerting)

[Destinations](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Webhooks

##### [List webhooks](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/list)

GET/accounts/{account\_id}/alerting/v3/destinations/webhooks

##### [Get a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/get)

GET/accounts/{account\_id}/alerting/v3/destinations/webhooks/{webhook\_id}

##### [Create a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/create)

POST/accounts/{account\_id}/alerting/v3/destinations/webhooks

##### [Update a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/update)

PUT/accounts/{account\_id}/alerting/v3/destinations/webhooks/{webhook\_id}

##### [Delete a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/delete)

DELETE/accounts/{account\_id}/alerting/v3/destinations/webhooks/{webhook\_id}

##### ModelsExpand Collapse

<details>

<summary>

Webhooks object {id, created\_at, last\_failure, 5 more }

</summary>

id: optional string

The unique identifier of a webhook

maxLength32

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

Timestamp of when the webhook destination was created.

formatdate-time

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

last\_failure: optional string

Timestamp of the last time an attempt to dispatch a notification to this webhook failed.

formatdate-time

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20last_failure">Link to this property</a>

last\_success: optional string

Timestamp of the last time Cloudflare was able to successfully dispatch a notification using this webhook.

formatdate-time

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20last_success">Link to this property</a>

name: optional string

The name of the webhook destination. This will be included in the request body when you receive a webhook notification.

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

secret: optional string

Optional secret that will be passed in the <code>cf-webhook-auth</code> header when dispatching generic webhook notifications or formatted for supported destinations. Secrets are not returned in any API response body.

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20secret">Link to this property</a>

<details>

<summary>

type: optional "datadog"or "discord"or "feishu"or 5 more

Type of webhook endpoint.

</summary>

One of the following:

"datadog"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"discord"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"feishu"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"gchat"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"generic"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"opsgenie"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"slack"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"splunk"

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

url: optional string

The POST endpoint to call when dispatching a notification.

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhooks%20%3E%20(schema)>)

<details>

<summary>

WebhookCreateResponse object {id }

</summary>

id: optional string

UUID

maxLength32

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_create_response%20%3E%20(schema)>)

<details>

<summary>

WebhookUpdateResponse object {id }

</summary>

id: optional string

UUID

maxLength32

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_update_response%20%3E%20(schema)>)

<details>

<summary>

WebhookDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {message, code }

</summary>

message: string

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

code: optional number

minimum1000

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

</details>

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {message, code }

</summary>

message: string

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

code: optional number

minimum1000

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

</details>

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful

<a href="#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.webhooks%20%3E%20(model)%20webhook_delete_response%20%3E%20(schema)>)