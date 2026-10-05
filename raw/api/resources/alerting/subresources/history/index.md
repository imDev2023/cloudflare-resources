---
title: History
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Alerting](https://developers.cloudflare.com/api/resources/alerting)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# History

##### [List History](https://developers.cloudflare.com/api/resources/alerting/subresources/history/methods/list)

GET/accounts/{account\_id}/alerting/v3/history

##### ModelsExpand Collapse

<details>

<summary>

History object {id, alert\_body, alert\_type, 6 more }

</summary>

id: optional string

UUID

maxLength32

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

alert\_body: optional string

Message body included in the notification sent.

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20alert_body">Link to this property</a>

alert\_type: optional string

Type of notification that has been dispatched.

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20alert_type">Link to this property</a>

description: optional string

Description of the notification policy (if present).

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

mechanism: optional string

The mechanism to which the notification has been dispatched.

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20mechanism">Link to this property</a>

<details>

<summary>

mechanism\_type: optional "email"or "pagerduty"or "webhook"

The type of mechanism to which the notification has been dispatched. This can be email/pagerduty/webhook based on the mechanism configured.

</summary>

One of the following:

"email"

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20mechanism_type%20%3E%20(member)%200">Link to this property</a>

"pagerduty"

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20mechanism_type%20%3E%20(member)%201">Link to this property</a>

"webhook"

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20mechanism_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20mechanism_type">Link to this property</a>

name: optional string

Name of the policy.

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

policy\_id: optional string

The unique identifier of a notification policy

maxLength32

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20policy_id">Link to this property</a>

sent: optional string

Timestamp of when the notification was dispatched in ISO 8601 format.

formatdate-time

<a href="#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)%20%3E%20(property)%20sent">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.history%20%3E%20(model)%20history%20%3E%20(schema)>)