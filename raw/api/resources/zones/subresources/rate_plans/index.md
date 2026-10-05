---
title: Rate Plans
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zones](https://developers.cloudflare.com/api/resources/zones)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Rate Plans

##### [List Available Rate Plans](https://developers.cloudflare.com/api/resources/zones/subresources/rate_plans/methods/get)

GET/zones/{zone\_id}/available\_rate\_plans

##### ModelsExpand Collapse

<details>

<summary>

RatePlanGetResponse object {id, components, currency, 3 more }

</summary>

id: optional string

Plan identifier tag.

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

components: optional array of object {default, name, unit\_price }

Array of available components values for the plan.

</summary>

default: optional number

The default amount allocated.

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20default">Link to this property</a>

<details>

<summary>

name: optional "zones"or "page\_rules"or "dedicated\_certificates"or "dedicated\_certificates\_custom"

The unique component.

</summary>

One of the following:

"zones"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%200">Link to this property</a>

"page\_rules"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%201">Link to this property</a>

"dedicated\_certificates"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%202">Link to this property</a>

"dedicated\_certificates\_custom"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

unit\_price: optional number

The unit price of the component.

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components%20%3E%20(items)%20%3E%20(property)%20unit_price">Link to this property</a>

</details>

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20components">Link to this property</a>

currency: optional string

The monetary unit in which pricing information is displayed.

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20currency">Link to this property</a>

duration: optional number

The duration of the plan subscription.

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20duration">Link to this property</a>

<details>

<summary>

frequency: optional "weekly"or "monthly"or "quarterly"or "yearly"

The frequency at which you will be billed for this plan.

</summary>

One of the following:

"weekly"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20frequency%20%3E%20(member)%200">Link to this property</a>

"monthly"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20frequency%20%3E%20(member)%201">Link to this property</a>

"quarterly"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20frequency%20%3E%20(member)%202">Link to this property</a>

"yearly"

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20frequency%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20frequency">Link to this property</a>

name: optional string

The plan name.

maxLength80

<a href="#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zones.rate_plans%20%3E%20(model)%20rate_plan_get_response%20%3E%20(schema)>)