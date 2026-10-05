---
title: Tags
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workers For Platforms](https://developers.cloudflare.com/api/resources/workers_for_platforms)

[Dispatch](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch)

[Namespaces](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces)

[Scripts](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Tags

##### [List Workers for Platforms Script Tags](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/methods/list)

GET/accounts/{account\_id}/workers/dispatch/namespaces/{dispatch\_namespace}/scripts/{script\_name}/tags

##### [Replace Workers for Platforms Script Tags](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/methods/update)

PUT/accounts/{account\_id}/workers/dispatch/namespaces/{dispatch\_namespace}/scripts/{script\_name}/tags

##### [Delete Workers for Platforms Script Tag](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/methods/delete)

DELETE/accounts/{account\_id}/workers/dispatch/namespaces/{dispatch\_namespace}/scripts/{script\_name}/tags/{tag}

##### ModelsExpand Collapse

TagListResponse = string

[Link to this property](<#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)>)

TagUpdateResponse = string

[Link to this property](<#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_update_response%20%3E%20(schema)>)

<details>

<summary>

TagDeleteResponse = object {errors, messages, result, success } or object {errors, messages, success, result }

</summary>

One of the following:

<details>

<summary>

WorkersTagsKVResponse object {errors, messages, result, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20messages">Link to this property</a>

result: map\[string]

Tags associated with the Worker, as a key/value object. Each complete UTF-8 encoded tag (the key plus <code>=</code> and the value when the value is non-empty) must not exceed 1024 bytes.

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20result">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersAPIResponseNullResult object {errors, messages, success, result }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20success">Link to this property</a>

result: optional unknown

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20result">Link to this property</a>

</details>

<a href="#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers_for_platforms.dispatch.namespaces.scripts.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)>)