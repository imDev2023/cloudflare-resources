---
title: Lists
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Gateway](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Lists

##### [List Zero Trust lists](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/list)

GET/accounts/{account\_id}/gateway/lists

##### [Get Zero Trust list details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/get)

GET/accounts/{account\_id}/gateway/lists/{list\_id}

##### [Create Zero Trust list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/create)

POST/accounts/{account\_id}/gateway/lists

##### [Update Zero Trust list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/update)

PUT/accounts/{account\_id}/gateway/lists/{list\_id}

##### [Patch Zero Trust list.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/edit)

PATCH/accounts/{account\_id}/gateway/lists/{list\_id}

##### [Delete Zero Trust list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/delete)

DELETE/accounts/{account\_id}/gateway/lists/{list\_id}

##### ModelsExpand Collapse

<details>

<summary>

GatewayItem object {created\_at, description, value }

</summary>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

description: optional string

Provide the list item description (optional).

minimum0

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

value: optional string

Specify the item value.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)>)

<details>

<summary>

GatewayList object {id, count, created\_at, 5 more }

</summary>

id: optional string

Identify the API resource with a UUID.

maxLength36

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

count: optional number

Indicate the number of items in the list.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

description: optional string

Provide the list description.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

items: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)">GatewayItem</a> { created\_at, description, value }

Provide the list items.

</summary>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

description: optional string

Provide the list item description (optional).

minimum0

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

value: optional string

Specify the item value.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

name: optional string

Specify the list name.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: optional "SERIAL"or "URL"or "DOMAIN"or 6 more

Specify the list type.

</summary>

One of the following:

"SERIAL"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"URL"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"DOMAIN"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"EMAIL"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"IP"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"CATEGORY"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"LOCATION"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"DEVICE"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"AAGUID"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_list%20%3E%20(schema)>)

<details>

<summary>

ListCreateResponse object {id, created\_at, description, 4 more }

</summary>

id: optional string

Identify the API resource with a UUID.

maxLength36

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

description: optional string

Provide the list description.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

items: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)">GatewayItem</a> { created\_at, description, value }

Provide the list items.

</summary>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

description: optional string

Provide the list item description (optional).

minimum0

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

value: optional string

Specify the item value.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20gateway_item%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

name: optional string

Specify the list name.

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: optional "SERIAL"or "URL"or "DOMAIN"or 6 more

Specify the list type.

</summary>

One of the following:

"SERIAL"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"URL"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"DOMAIN"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"EMAIL"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"IP"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"CATEGORY"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"LOCATION"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"DEVICE"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"AAGUID"

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_create_response%20%3E%20(schema)>)

ListDeleteResponse = unknown

[Link to this property](<#(resource)%20zero_trust.gateway.lists%20%3E%20(model)%20list_delete_response%20%3E%20(schema)>)

#### ListsItems

##### [Get Zero Trust list items](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/subresources/items/methods/list)

GET/accounts/{account\_id}/gateway/lists/{list\_id}/items