---
title: Smart Tiered Cache
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cache](https://developers.cloudflare.com/api/resources/cache)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Smart Tiered Cache

##### [Get Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/get)

GET/zones/{zone\_id}/cache/tiered\_cache\_smart\_topology\_enable

##### [Create Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/create)

POST/zones/{zone\_id}/cache/tiered\_cache\_smart\_topology\_enable

##### [Patch Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/edit)

PATCH/zones/{zone\_id}/cache/tiered\_cache\_smart\_topology\_enable

##### [Delete Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/delete)

DELETE/zones/{zone\_id}/cache/tiered\_cache\_smart\_topology\_enable

##### ModelsExpand Collapse

<details>

<summary>

SmartTieredCacheGetResponse object {id, editable, value, modified\_on }

</summary>

id: "tiered\_cache\_smart\_topology\_enable"

The identifier of the caching setting.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Smart Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_get_response%20%3E%20(schema)>)

<details>

<summary>

SmartTieredCacheCreateResponse object {id, editable, value, modified\_on }

</summary>

id: "tiered\_cache\_smart\_topology\_enable"

The identifier of the caching setting.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Smart Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_create_response%20%3E%20(schema)>)

<details>

<summary>

SmartTieredCacheEditResponse object {id, editable, value, modified\_on }

</summary>

id: "tiered\_cache\_smart\_topology\_enable"

The identifier of the caching setting.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Smart Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_edit_response%20%3E%20(schema)>)

<details>

<summary>

SmartTieredCacheDeleteResponse object {id, editable, modified\_on }

</summary>

id: "tiered\_cache\_smart\_topology\_enable"

The identifier of the caching setting.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_delete_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.smart_tiered_cache%20%3E%20(model)%20smart_tiered_cache_delete_response%20%3E%20(schema)>)