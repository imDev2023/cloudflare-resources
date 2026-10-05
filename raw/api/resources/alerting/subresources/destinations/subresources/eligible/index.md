---
title: Eligible
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Alerting](https://developers.cloudflare.com/api/resources/alerting)

[Destinations](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Eligible

##### [Get delivery mechanism eligibility](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/eligible/methods/get)

GET/accounts/{account\_id}/alerting/v3/destinations/eligible

##### ModelsExpand Collapse

<details>

<summary>

EligibleGetResponse = map\[array of object {eligible, ready, type } ]

</summary>

eligible: optional boolean

Determines whether or not the account is eligible for the delivery mechanism.

<a href="#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(items)%20%3E%20(property)%20eligible">Link to this property</a>

ready: optional boolean

Beta flag. Users can create a policy with a mechanism that is not ready, but we cannot guarantee successful delivery of notifications.

<a href="#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(items)%20%3E%20(property)%20ready">Link to this property</a>

<details>

<summary>

type: optional "email"or "pagerduty"or "webhook"

Determines type of delivery mechanism.

</summary>

One of the following:

"email"

<a href="#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"pagerduty"

<a href="#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"webhook"

<a href="#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20alerting.destinations.eligible%20%3E%20(model)%20eligible_get_response%20%3E%20(schema)>)