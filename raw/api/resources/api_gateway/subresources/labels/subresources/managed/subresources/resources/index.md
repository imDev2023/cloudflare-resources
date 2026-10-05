---
title: Resources
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[API Gateway](https://developers.cloudflare.com/api/resources/api_gateway)

[Labels](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels)

[Managed](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/managed)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Resources

#### ResourcesOperation

##### [Replace operations attached to a managed label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/managed/subresources/resources/subresources/operation/methods/update)

PUT/zones/{zone\_id}/api\_gateway/labels/managed/{name}/resources/operation

##### ModelsExpand Collapse

<details>

<summary>

OperationUpdateResponse object {created\_at, description, last\_updated, 4 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

mapped\_resources: optional unknown

Provides counts of what resources are linked to this label

<a href="#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)%20%3E%20(property)%20mapped_resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.labels.managed.resources.operation%20%3E%20(model)%20operation_update_response%20%3E%20(schema)>)