---
title: Pagerduty
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Alerting](https://developers.cloudflare.com/api/resources/alerting)

[Destinations](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Pagerduty

##### [List PagerDuty services](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/get)

GET/accounts/{account\_id}/alerting/v3/destinations/pagerduty

##### [Create PagerDuty integration token](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/create)

POST/accounts/{account\_id}/alerting/v3/destinations/pagerduty/connect

##### [Delete PagerDuty Services](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/delete)

DELETE/accounts/{account\_id}/alerting/v3/destinations/pagerduty

##### [Connect PagerDuty](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/link)

GET/accounts/{account\_id}/alerting/v3/destinations/pagerduty/connect/{token\_id}

##### ModelsExpand Collapse

<details>

<summary>

Pagerduty object {id, name }

</summary>

id: optional string

UUID

maxLength32

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

The name of the pagerduty service.

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty%20%3E%20(schema)>)

<details>

<summary>

PagerdutyCreateResponse object {id }

</summary>

id: optional string

token in form of UUID

maxLength32

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_create_response%20%3E%20(schema)>)

<details>

<summary>

PagerdutyDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {message, code }

</summary>

message: string

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

code: optional number

minimum1000

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

</details>

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {message, code }

</summary>

message: string

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

code: optional number

minimum1000

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

</details>

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_delete_response%20%3E%20(schema)>)

<details>

<summary>

PagerdutyLinkResponse object {id }

</summary>

id: optional string

UUID

maxLength32

<a href="#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_link_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.pagerduty%20%3E%20(model)%20pagerduty_link_response%20%3E%20(schema)>)