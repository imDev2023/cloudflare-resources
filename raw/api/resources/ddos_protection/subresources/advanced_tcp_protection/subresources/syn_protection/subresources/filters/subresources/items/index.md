---
title: Items
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[DDoS Protection](https://developers.cloudflare.com/api/resources/ddos_protection)

[Advanced TCP Protection](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection)

[SYN Protection](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection)

[Filters](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Items

##### [Get SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/subresources/items/methods/get)

GET/accounts/{account\_id}/magic/advanced\_tcp\_protection/configs/syn\_protection/filters/{filter\_id}

##### [Update SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/subresources/items/methods/edit)

PATCH/accounts/{account\_id}/magic/advanced\_tcp\_protection/configs/syn\_protection/filters/{filter\_id}

##### [Delete SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/subresources/items/methods/delete)

DELETE/accounts/{account\_id}/magic/advanced\_tcp\_protection/configs/syn\_protection/filters/{filter\_id}

##### ModelsExpand Collapse

<details>

<summary>

ItemGetResponse object {id, created\_on, expression, 2 more }

</summary>

id: string

The unique ID of the expression filter.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

The creation timestamp of the expression filter.

formatdate-time

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

expression: string

The filter expression.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_get_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

mode: string

The filter’s mode. Must be one of ‘enabled’, ‘disabled’, ‘monitoring’.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_get_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

modified\_on: string

The last modification timestamp of the expression filter.

formatdate-time

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_get_response%20%3E%20(schema)>)

<details>

<summary>

ItemEditResponse object {id, created\_on, expression, 2 more }

</summary>

id: string

The unique ID of the expression filter.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

The creation timestamp of the expression filter.

formatdate-time

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

expression: string

The filter expression.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_edit_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

mode: string

The filter’s mode. Must be one of ‘enabled’, ‘disabled’, ‘monitoring’.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

modified\_on: string

The last modification timestamp of the expression filter.

formatdate-time

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_edit_response%20%3E%20(schema)>)

<details>

<summary>

ItemDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ddos_protection.advanced_tcp_protection.syn_protection.filters.items%20%3E%20(model)%20item_delete_response%20%3E%20(schema)>)