---
title: Labels
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[API Gateway](https://developers.cloudflare.com/api/resources/api_gateway)

[Operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Labels

##### [Replace labels on a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/update)

PUT/zones/{zone\_id}/api\_gateway/operations/{operation\_id}/labels

##### [Attach labels to a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/create)

POST/zones/{zone\_id}/api\_gateway/operations/{operation\_id}/labels

##### [Remove labels from a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/delete)

DELETE/zones/{zone\_id}/api\_gateway/operations/{operation\_id}/labels

##### [Replace labels on web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/bulk_update)

PUT/zones/{zone\_id}/api\_gateway/operations/labels

##### [Attach labels to web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/bulk_create)

POST/zones/{zone\_id}/api\_gateway/operations/labels

##### [Remove labels from web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/bulk_delete)

DELETE/zones/{zone\_id}/api\_gateway/operations/labels

##### ModelsExpand Collapse

<details>

<summary>

LabelUpdateResponse object {endpoint, host, last\_updated, 3 more }

</summary>

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <a href="https://developers.cloudflare.com/rules/normalization/how-it-works/">https://developers.cloudflare.com/rules/normalization/how-it-works/</a>.

formaturi-template

maxLength4096

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

host: string

RFC3986-compliant host.

formathostname

maxLength255

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

<details>

<summary>

method: "GET"or "POST"or "HEAD"or 6 more

The HTTP method used to access the endpoint.

</summary>

One of the following:

"GET"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"POST"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

"HEAD"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%202">Link to this property</a>

"OPTIONS"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%203">Link to this property</a>

"PUT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%204">Link to this property</a>

"DELETE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%205">Link to this property</a>

"CONNECT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%206">Link to this property</a>

"PATCH"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%207">Link to this property</a>

"TRACE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

operation\_id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20operation_id">Link to this property</a>

<details>

<summary>

labels: optional array of object {created\_at, description, last\_updated, 3 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_update_response%20%3E%20(schema)>)

<details>

<summary>

LabelCreateResponse object {endpoint, host, last\_updated, 3 more }

</summary>

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <a href="https://developers.cloudflare.com/rules/normalization/how-it-works/">https://developers.cloudflare.com/rules/normalization/how-it-works/</a>.

formaturi-template

maxLength4096

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

host: string

RFC3986-compliant host.

formathostname

maxLength255

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

<details>

<summary>

method: "GET"or "POST"or "HEAD"or 6 more

The HTTP method used to access the endpoint.

</summary>

One of the following:

"GET"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"POST"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

"HEAD"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%202">Link to this property</a>

"OPTIONS"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%203">Link to this property</a>

"PUT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%204">Link to this property</a>

"DELETE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%205">Link to this property</a>

"CONNECT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%206">Link to this property</a>

"PATCH"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%207">Link to this property</a>

"TRACE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

operation\_id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20operation_id">Link to this property</a>

<details>

<summary>

labels: optional array of object {created\_at, description, last\_updated, 3 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_create_response%20%3E%20(schema)>)

<details>

<summary>

LabelDeleteResponse object {endpoint, host, last\_updated, 3 more }

</summary>

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <a href="https://developers.cloudflare.com/rules/normalization/how-it-works/">https://developers.cloudflare.com/rules/normalization/how-it-works/</a>.

formaturi-template

maxLength4096

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

host: string

RFC3986-compliant host.

formathostname

maxLength255

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

<details>

<summary>

method: "GET"or "POST"or "HEAD"or 6 more

The HTTP method used to access the endpoint.

</summary>

One of the following:

"GET"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"POST"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

"HEAD"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%202">Link to this property</a>

"OPTIONS"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%203">Link to this property</a>

"PUT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%204">Link to this property</a>

"DELETE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%205">Link to this property</a>

"CONNECT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%206">Link to this property</a>

"PATCH"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%207">Link to this property</a>

"TRACE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

operation\_id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20operation_id">Link to this property</a>

<details>

<summary>

labels: optional array of object {created\_at, description, last\_updated, 3 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_delete_response%20%3E%20(schema)>)

<details>

<summary>

LabelBulkUpdateResponse object {endpoint, host, last\_updated, 3 more }

</summary>

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <a href="https://developers.cloudflare.com/rules/normalization/how-it-works/">https://developers.cloudflare.com/rules/normalization/how-it-works/</a>.

formaturi-template

maxLength4096

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

host: string

RFC3986-compliant host.

formathostname

maxLength255

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

<details>

<summary>

method: "GET"or "POST"or "HEAD"or 6 more

The HTTP method used to access the endpoint.

</summary>

One of the following:

"GET"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"POST"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

"HEAD"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%202">Link to this property</a>

"OPTIONS"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%203">Link to this property</a>

"PUT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%204">Link to this property</a>

"DELETE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%205">Link to this property</a>

"CONNECT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%206">Link to this property</a>

"PATCH"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%207">Link to this property</a>

"TRACE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

operation\_id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20operation_id">Link to this property</a>

<details>

<summary>

labels: optional array of object {created\_at, description, last\_updated, 3 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_update_response%20%3E%20(schema)>)

<details>

<summary>

LabelBulkCreateResponse object {endpoint, host, last\_updated, 3 more }

</summary>

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <a href="https://developers.cloudflare.com/rules/normalization/how-it-works/">https://developers.cloudflare.com/rules/normalization/how-it-works/</a>.

formaturi-template

maxLength4096

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

host: string

RFC3986-compliant host.

formathostname

maxLength255

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

<details>

<summary>

method: "GET"or "POST"or "HEAD"or 6 more

The HTTP method used to access the endpoint.

</summary>

One of the following:

"GET"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"POST"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

"HEAD"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%202">Link to this property</a>

"OPTIONS"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%203">Link to this property</a>

"PUT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%204">Link to this property</a>

"DELETE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%205">Link to this property</a>

"CONNECT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%206">Link to this property</a>

"PATCH"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%207">Link to this property</a>

"TRACE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

operation\_id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20operation_id">Link to this property</a>

<details>

<summary>

labels: optional array of object {created\_at, description, last\_updated, 3 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_create_response%20%3E%20(schema)>)

<details>

<summary>

LabelBulkDeleteResponse object {endpoint, host, last\_updated, 3 more }

</summary>

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <a href="https://developers.cloudflare.com/rules/normalization/how-it-works/">https://developers.cloudflare.com/rules/normalization/how-it-works/</a>.

formaturi-template

maxLength4096

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

host: string

RFC3986-compliant host.

formathostname

maxLength255

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

<details>

<summary>

method: "GET"or "POST"or "HEAD"or 6 more

The HTTP method used to access the endpoint.

</summary>

One of the following:

"GET"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"POST"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

"HEAD"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%202">Link to this property</a>

"OPTIONS"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%203">Link to this property</a>

"PUT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%204">Link to this property</a>

"DELETE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%205">Link to this property</a>

"CONNECT"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%206">Link to this property</a>

"PATCH"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%207">Link to this property</a>

"TRACE"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

operation\_id: string

UUID.

maxLength36

minLength36

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20operation_id">Link to this property</a>

<details>

<summary>

labels: optional array of object {created\_at, description, last\_updated, 3 more }

</summary>

created\_at: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

description: string

The description of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

last\_updated: string

formatdate-time

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20last_updated">Link to this property</a>

metadata: unknown

Metadata for the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: string

The name of the label

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: "user"or "managed"

- <code>user</code> - label is owned by the user
- <code>managed</code> - label is owned by cloudflare

</summary>

One of the following:

"user"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"managed"

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

</details>

[Link to this property](<#(resource)%20api_gateway.operations.labels%20%3E%20(model)%20label_bulk_delete_response%20%3E%20(schema)>)