---
title: Recommendations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[SSL](https://developers.cloudflare.com/api/resources/ssl)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Recommendations

##### [SSL/TLS Recommendation](https://developers.cloudflare.com/api/resources/ssl/subresources/recommendations/methods/get)

Deprecated

GET/zones/{zone\_id}/ssl/recommendation

##### ModelsExpand Collapse

<details>

<summary>

RecommendationGetResponse object {id, editable, modified\_on, 2 more }

</summary>

id: string

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether this setting can be updated or not.

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

value: "auto"or "custom"

Current setting of the automatic SSL/TLS.

</summary>

One of the following:

"auto"

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

next\_scheduled\_scan: optional string

Next time this zone will be scanned by the Automatic SSL/TLS.

formatdate-time

<a href="#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)%20%3E%20(property)%20next_scheduled_scan">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.recommendations%20%3E%20(model)%20recommendation_get_response%20%3E%20(schema)>)