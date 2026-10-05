---
title: Regional Tiered Cache
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cache](https://developers.cloudflare.com/api/resources/cache)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Regional Tiered Cache

##### [Get Regional Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/regional_tiered_cache/methods/get)

GET/zones/{zone\_id}/cache/regional\_tiered\_cache

##### [Change Regional Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/regional_tiered_cache/methods/edit)

PATCH/zones/{zone\_id}/cache/regional\_tiered\_cache

##### ModelsExpand Collapse

RegionalTieredCache = "tc\_regional"

The identifier of the caching setting.

[Link to this property](<#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache%20%3E%20(schema)>)

<details>

<summary>

RegionalTieredCacheGetResponse object {id, editable, value, modified\_on }

</summary>

id: <a href="https://developers.cloudflare.com/api/resources/cache#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache%20%3E%20(schema)">RegionalTieredCache</a>

The identifier of the caching setting.

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Regional Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_get_response%20%3E%20(schema)>)

<details>

<summary>

RegionalTieredCacheEditResponse object {id, editable, value, modified\_on }

</summary>

id: <a href="https://developers.cloudflare.com/api/resources/cache#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache%20%3E%20(schema)">RegionalTieredCache</a>

The identifier of the caching setting.

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Regional Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.regional_tiered_cache%20%3E%20(model)%20regional_tiered_cache_edit_response%20%3E%20(schema)>)