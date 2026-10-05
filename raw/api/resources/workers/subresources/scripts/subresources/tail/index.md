---
title: Tail
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workers](https://developers.cloudflare.com/api/resources/workers)

[Scripts](https://developers.cloudflare.com/api/resources/workers/subresources/scripts)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Tail

##### [List Worker Tails](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/tails

##### [Start Worker Tail](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/create)

POST/accounts/{account\_id}/workers/scripts/{script\_name}/tails

##### [Delete Worker Tail](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/delete)

DELETE/accounts/{account\_id}/workers/scripts/{script\_name}/tails/{id}

##### ModelsExpand Collapse

<details>

<summary>

ConsumerScript object {service, environment, namespace }

A reference to a script that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)>)

<details>

<summary>

TailGetResponse object {id, expires\_at, url }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expires\_at: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

url: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)>)

<details>

<summary>

TailCreateResponse object {id, expires\_at, url }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expires\_at: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

url: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)>)

<details>

<summary>

TailDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)>)