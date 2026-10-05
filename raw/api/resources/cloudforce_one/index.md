---
title: Cloudforce One
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Cloudforce One

#### Cloudforce OneBinary Storage

##### [Retrieves a file from Binary Storage](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/binary_storage/methods/get)

GET/accounts/{account\_id}/cloudforce-one/binary/{hash}

##### [Posts a file to Binary Storage](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/binary_storage/methods/create)

POST/accounts/{account\_id}/cloudforce-one/binary

##### ModelsExpand Collapse

<details>

<summary>

BinaryStorageCreateResponse object {content\_type, md5, sha1, sha256 }

</summary>

content\_type: string

<a href="#(resource)%20cloudforce_one.binary_storage%20%3E%20(model)%20binary_storage_create_response%20%3E%20(schema)%20%3E%20(property)%20content_type">Link to this property</a>

md5: string

<a href="#(resource)%20cloudforce_one.binary_storage%20%3E%20(model)%20binary_storage_create_response%20%3E%20(schema)%20%3E%20(property)%20md5">Link to this property</a>

sha1: string

<a href="#(resource)%20cloudforce_one.binary_storage%20%3E%20(model)%20binary_storage_create_response%20%3E%20(schema)%20%3E%20(property)%20sha1">Link to this property</a>

sha256: string

<a href="#(resource)%20cloudforce_one.binary_storage%20%3E%20(model)%20binary_storage_create_response%20%3E%20(schema)%20%3E%20(property)%20sha256">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.binary_storage%20%3E%20(model)%20binary_storage_create_response%20%3E%20(schema)>)

#### Cloudforce OneRequests

##### [List Requests](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/list)

POST/accounts/{account\_id}/cloudforce-one/requests

##### [Get a Request](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/get)

GET/accounts/{account\_id}/cloudforce-one/requests/{request\_id}

##### [Create a New Request.](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/create)

POST/accounts/{account\_id}/cloudforce-one/requests/new

##### [Update a Request](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/requests/{request\_id}

##### [Delete a Request](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/requests/{request\_id}

##### [Get Request Quota](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/quota)

GET/accounts/{account\_id}/cloudforce-one/requests/quota

##### [Get Request Types](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/types)

GET/accounts/{account\_id}/cloudforce-one/requests/types

##### [Get Request Priority, Status, and TLP constants](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/constants)

GET/accounts/{account\_id}/cloudforce-one/requests/constants

##### ModelsExpand Collapse

<details>

<summary>

Item object {id, content, created, 10 more }

</summary>

id: string

UUID.

maxLength36

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

content: string

Request content.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20content">Link to this property</a>

created: string

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

priority: string

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

request: string

Requested information from request.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20request">Link to this property</a>

summary: string

Brief description of the request.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20summary">Link to this property</a>

<details>

<summary>

tlp: "clear"or "amber"or "amber-strict"or 2 more

The CISA defined Traffic Light Protocol (TLP).

</summary>

One of the following:

"clear"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"red"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

updated: string

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

completed: optional string

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20completed">Link to this property</a>

message\_tokens: optional number

Tokens for the request messages.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20message_tokens">Link to this property</a>

readable\_id: optional string

Readable Request ID.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20readable_id">Link to this property</a>

<details>

<summary>

status: optional "open"or "accepted"or "reported"or 3 more

Request Status.

</summary>

One of the following:

"open"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"accepted"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"reported"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"approved"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"completed"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"declined"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

tokens: optional number

Tokens for the request.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)%20%3E%20(property)%20tokens">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20item%20%3E%20(schema)>)

<details>

<summary>

ListItem object {id, created, priority, 9 more }

</summary>

id: string

UUID.

maxLength36

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

Request creation time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

<details>

<summary>

priority: "routine"or "high"or "urgent"

</summary>

One of the following:

"routine"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20priority%20%3E%20(member)%200">Link to this property</a>

"high"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20priority%20%3E%20(member)%201">Link to this property</a>

"urgent"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20priority%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

request: string

Requested information from request.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20request">Link to this property</a>

summary: string

Brief description of the request.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20summary">Link to this property</a>

<details>

<summary>

tlp: "clear"or "amber"or "amber-strict"or 2 more

The CISA defined Traffic Light Protocol (TLP).

</summary>

One of the following:

"clear"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"red"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

updated: string

Request last updated time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

completed: optional string

Request completion time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20completed">Link to this property</a>

message\_tokens: optional number

Tokens for the request messages.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20message_tokens">Link to this property</a>

readable\_id: optional string

Readable Request ID.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20readable_id">Link to this property</a>

<details>

<summary>

status: optional "open"or "accepted"or "reported"or 3 more

Request Status.

</summary>

One of the following:

"open"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"accepted"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"reported"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"approved"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"completed"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"declined"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

tokens: optional number

Tokens for the request.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)%20%3E%20(property)%20tokens">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20list_item%20%3E%20(schema)>)

<details>

<summary>

Quota object {anniversary\_date, quarter\_anniversary\_date, quota, remaining }

</summary>

anniversary\_date: optional string

Anniversary date is when annual quota limit is refreshed.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20quota%20%3E%20(schema)%20%3E%20(property)%20anniversary_date">Link to this property</a>

quarter\_anniversary\_date: optional string

Quarter anniversary date is when quota limit is refreshed each quarter.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20quota%20%3E%20(schema)%20%3E%20(property)%20quarter_anniversary_date">Link to this property</a>

quota: optional number

Tokens for the quarter.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20quota%20%3E%20(schema)%20%3E%20(property)%20quota">Link to this property</a>

remaining: optional number

Tokens remaining for the quarter.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20quota%20%3E%20(schema)%20%3E%20(property)%20remaining">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20quota%20%3E%20(schema)>)

<details>

<summary>

RequestConstants object {priority, status, tlp }

</summary>

<details>

<summary>

priority: optional array of "routine"or "high"or "urgent"

</summary>

One of the following:

"routine"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20priority%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"high"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20priority%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"urgent"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20priority%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

<details>

<summary>

status: optional array of "open"or "accepted"or "reported"or 3 more

</summary>

One of the following:

"open"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"accepted"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"reported"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"approved"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"completed"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"declined"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

tlp: optional array of "clear"or "amber"or "amber-strict"or 2 more

</summary>

One of the following:

"clear"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"red"

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_constants%20%3E%20(schema)>)

RequestTypes = array of string

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_types%20%3E%20(schema)>)

<details>

<summary>

RequestDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_delete_response%20%3E%20(schema)>)

RequestTypesResponse = string

Request Types.

[Link to this property](<#(resource)%20cloudforce_one.requests%20%3E%20(model)%20request_types_response%20%3E%20(schema)>)

#### Cloudforce OneRequestsMessage

##### [List Request Messages](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/get)

POST/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/message

##### [Create a New Request Message](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/create)

POST/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/message/new

##### [Update a Request Message](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/message/{message\_id}

##### [Delete a Request Message](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/message/{message\_id}

##### ModelsExpand Collapse

<details>

<summary>

Message object {id, author, content, 3 more }

</summary>

id: number

Message ID.

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

author: string

Author of message.

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20author">Link to this property</a>

content: string

Content of message.

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20content">Link to this property</a>

is\_follow\_on\_request: boolean

Whether the message is a follow-on request.

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20is_follow_on_request">Link to this property</a>

updated: string

Defines the message last updated time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

created: optional string

Defines the message creation time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message%20%3E%20(schema)>)

<details>

<summary>

MessageDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.message%20%3E%20(model)%20message_delete_response%20%3E%20(schema)>)

#### Cloudforce OneRequestsPriority

##### [Get a Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/get)

GET/accounts/{account\_id}/cloudforce-one/requests/priority/{priority\_id}

##### [Create a New Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/create)

POST/accounts/{account\_id}/cloudforce-one/requests/priority/new

##### [Update a Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/requests/priority/{priority\_id}

##### [Delete a Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/requests/priority/{priority\_id}

##### [Get Priority Intelligence Requirement Quota](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/quota)

GET/accounts/{account\_id}/cloudforce-one/requests/priority/quota

##### ModelsExpand Collapse

Label = string

[Link to this property](<#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20label%20%3E%20(schema)>)

<details>

<summary>

Priority object {id, created, labels, 4 more }

</summary>

id: string

UUID.

maxLength36

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

Priority creation time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

labels: array of <a href="https://developers.cloudflare.com/api/resources/cloudforce_one#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20label%20%3E%20(schema)">Label</a>

List of labels.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

priority: number

Priority.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

requirement: string

Requirement.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20requirement">Link to this property</a>

<details>

<summary>

tlp: "clear"or "amber"or "amber-strict"or 2 more

The CISA defined Traffic Light Protocol (TLP).

</summary>

One of the following:

"clear"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"red"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

updated: string

Priority last updated time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority%20%3E%20(schema)>)

<details>

<summary>

PriorityEdit object {labels, priority, requirement, tlp }

</summary>

labels: array of <a href="https://developers.cloudflare.com/api/resources/cloudforce_one#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20label%20%3E%20(schema)">Label</a>

List of labels.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20labels">Link to this property</a>

priority: number

Priority.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

requirement: string

Requirement.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20requirement">Link to this property</a>

<details>

<summary>

tlp: "clear"or "amber"or "amber-strict"or 2 more

The CISA defined Traffic Light Protocol (TLP).

</summary>

One of the following:

"clear"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"red"

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_edit%20%3E%20(schema)>)

<details>

<summary>

PriorityDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.priority%20%3E%20(model)%20priority_delete_response%20%3E%20(schema)>)

#### Cloudforce OneRequestsAssets

##### [Get a Request Asset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/get)

GET/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/asset/{asset\_id}

##### [List Request Assets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/create)

POST/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/asset

##### [Update a Request Asset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/asset/{asset\_id}

##### [Delete a Request Asset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/requests/{request\_id}/asset/{asset\_id}

##### ModelsExpand Collapse

<details>

<summary>

AssetGetResponse object {id, name, created, 2 more }

</summary>

id: number

Asset ID.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: string

Asset name.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

created: optional string

Defines the asset creation time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

description: optional string

Asset description.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

file\_type: optional string

Asset file type.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_get_response%20%3E%20(schema)%20%3E%20(property)%20file_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_get_response%20%3E%20(schema)>)

<details>

<summary>

AssetCreateResponse object {id, name, created, 2 more }

</summary>

id: number

Asset ID.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: string

Asset name.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

created: optional string

Defines the asset creation time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

description: optional string

Asset description.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

file\_type: optional string

Asset file type.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)%20%3E%20(property)%20file_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)>)

<details>

<summary>

AssetUpdateResponse object {id, name, created, 2 more }

</summary>

id: number

Asset ID.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: string

Asset name.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

created: optional string

Defines the asset creation time.

formatdate-time

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_update_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

description: optional string

Asset description.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

file\_type: optional string

Asset file type.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_update_response%20%3E%20(schema)%20%3E%20(property)%20file_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_update_response%20%3E%20(schema)>)

<details>

<summary>

AssetDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.requests.assets%20%3E%20(model)%20asset_delete_response%20%3E%20(schema)>)

#### Cloudforce OneScans

#### Cloudforce OneScansResults

##### [Get the Latest Scan Result](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/results/methods/get)

GET/accounts/{account\_id}/cloudforce-one/scans/results/{config\_id}

##### ModelsExpand Collapse

<details>

<summary>

ScanResult object {number, proto, status }

</summary>

number: optional number

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)%20%3E%20(property)%20number">Link to this property</a>

proto: optional string

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)%20%3E%20(property)%20proto">Link to this property</a>

status: optional string

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)>)

<details>

<summary>

ResultGetResponse object {"1.1.1.1" }

</summary>

<details>

<summary>

"1.1.1.1": array of <a href="https://developers.cloudflare.com/api/resources/cloudforce_one#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)">ScanResult</a> { number, proto, status }

</summary>

number: optional number

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)%20%3E%20(property)%20number">Link to this property</a>

proto: optional string

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)%20%3E%20(property)%20proto">Link to this property</a>

status: optional string

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20scan_result%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20result_get_response%20%3E%20(schema)%20%3E%20(property)%201.1.1.1">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.scans.results%20%3E%20(model)%20result_get_response%20%3E%20(schema)>)

#### Cloudforce OneScansConfig

##### [List Scan Configs](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/list)

GET/accounts/{account\_id}/cloudforce-one/scans/config

##### [Create a new Scan Config](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/create)

POST/accounts/{account\_id}/cloudforce-one/scans/config

##### [Update an existing Scan Config](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/scans/config/{config\_id}

##### [Delete a Scan Config](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/scans/config/{config\_id}

##### ModelsExpand Collapse

<details>

<summary>

ConfigListResponse object {id, account\_id, frequency, 2 more }

</summary>

id: string

Defines the Config ID.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_list_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

frequency: number

Defines the number of days between each scan (0 = One-off scan).

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_list_response%20%3E%20(schema)%20%3E%20(property)%20frequency">Link to this property</a>

ips: array of string

Defines a list of IP addresses or CIDR blocks to scan. The maximum number of total IP addresses allowed is 5000.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_list_response%20%3E%20(schema)%20%3E%20(property)%20ips">Link to this property</a>

ports: array of string

Defines a list of ports to scan. Valid values are:“default”, “all”, or a comma-separated list of ports or range of ports (e.g. \[“1-80”, “443”]). “default” scans the 100 most commonly open ports.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_list_response%20%3E%20(schema)%20%3E%20(property)%20ports">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_list_response%20%3E%20(schema)>)

<details>

<summary>

ConfigCreateResponse object {id, account\_id, frequency, 2 more }

</summary>

id: string

Defines the Config ID.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

frequency: number

Defines the number of days between each scan (0 = One-off scan).

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20frequency">Link to this property</a>

ips: array of string

Defines a list of IP addresses or CIDR blocks to scan. The maximum number of total IP addresses allowed is 5000.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20ips">Link to this property</a>

ports: array of string

Defines a list of ports to scan. Valid values are:“default”, “all”, or a comma-separated list of ports or range of ports (e.g. \[“1-80”, “443”]). “default” scans the 100 most commonly open ports.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20ports">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)>)

<details>

<summary>

ConfigEditResponse object {id, account\_id, frequency, 2 more }

</summary>

id: string

Defines the Config ID.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_edit_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

frequency: number

Defines the number of days between each scan (0 = One-off scan).

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_edit_response%20%3E%20(schema)%20%3E%20(property)%20frequency">Link to this property</a>

ips: array of string

Defines a list of IP addresses or CIDR blocks to scan. The maximum number of total IP addresses allowed is 5000.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_edit_response%20%3E%20(schema)%20%3E%20(property)%20ips">Link to this property</a>

ports: array of string

Defines a list of ports to scan. Valid values are:“default”, “all”, or a comma-separated list of ports or range of ports (e.g. \[“1-80”, “443”]). “default” scans the 100 most commonly open ports.

<a href="#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_edit_response%20%3E%20(schema)%20%3E%20(property)%20ports">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_edit_response%20%3E%20(schema)>)

ConfigDeleteResponse = unknown

[Link to this property](<#(resource)%20cloudforce_one.scans.config%20%3E%20(model)%20config_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat Events

##### [Filter and list events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events

##### [Reads an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/get)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/{event\_id}

##### [Creates a new event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/create

##### [Updates an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/events/{event\_id}

##### [Creates bulk events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/bulk_create)

POST/accounts/{account\_id}/cloudforce-one/events/create/bulk

##### [Creates bulk DOS event with relationships and indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/bulk_create_relationships)

Deprecated

POST/accounts/{account\_id}/cloudforce-one/events/create/bulk/relationships

##### ModelsExpand Collapse

<details>

<summary>

ThreatEventListResponse = array of object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_list_response%20%3E%20(schema)>)

<details>

<summary>

ThreatEventGetResponse object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_get_response%20%3E%20(schema)>)

<details>

<summary>

ThreatEventCreateResponse object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_create_response%20%3E%20(schema)>)

<details>

<summary>

ThreatEventEditResponse object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_edit_response%20%3E%20(schema)>)

<details>

<summary>

ThreatEventBulkCreateResponse object {createdEventsCount, createdTagsCount, errorCount, 4 more }

Detailed result of bulk event creation with auto-tag management

</summary>

createdEventsCount: number

Number of events created

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createdEventsCount">Link to this property</a>

createdTagsCount: number

Number of new tags created in SoT

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createdTagsCount">Link to this property</a>

errorCount: number

Number of errors encountered

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20errorCount">Link to this property</a>

queuedIndicatorsCount: number

Number of indicators queued for async processing

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20queuedIndicatorsCount">Link to this property</a>

createBulkEventsRequestId: optional string

Correlation ID for async indicator processing

formatuuid

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createBulkEventsRequestId">Link to this property</a>

<details>

<summary>

createdEvents: optional array of object {eventIndex, shardId, uuid }

Array of created events with UUIDs and shard locations. Only present when includeCreatedEvents=true

</summary>

eventIndex: number

Original index in the input data array

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createdEvents%20%3E%20(items)%20%3E%20(property)%20eventIndex">Link to this property</a>

shardId: string

Dataset ID of the shard where the event was created

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createdEvents%20%3E%20(items)%20%3E%20(property)%20shardId">Link to this property</a>

uuid: string

UUID of the created event

formatuuid

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createdEvents%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20createdEvents">Link to this property</a>

<details>

<summary>

errors: optional array of object {error, eventIndex }

Array of error details

</summary>

error: string

Error message

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

eventIndex: number

Index of the event that caused the error

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20eventIndex">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_response%20%3E%20(schema)>)

<details>

<summary>

ThreatEventBulkCreateRelationshipsResponse object {createdEventsCount, createdIndicatorsCount, createdRelationshipsCount, 2 more }

Result of bulk relationship creation operation

</summary>

createdEventsCount: number

Number of events created

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20createdEventsCount">Link to this property</a>

createdIndicatorsCount: number

Number of indicators created

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20createdIndicatorsCount">Link to this property</a>

createdRelationshipsCount: number

Number of relationships created

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20createdRelationshipsCount">Link to this property</a>

errorCount: number

Number of errors encountered

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20errorCount">Link to this property</a>

<details>

<summary>

errors: optional array of object {error, eventIndex }

Array of error details

</summary>

error: string

Error message

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

eventIndex: number

Index of the event that caused the error

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20eventIndex">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events%20%3E%20(model)%20threat_event_bulk_create_relationships_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsAggregate

##### [Aggregate events by single or multiple columns with optional date filtering](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/aggregate/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/aggregate

##### ModelsExpand Collapse

<details>

<summary>

AggregateListResponse object {aggregateBy, aggregations, total, dateRange }

</summary>

aggregateBy: string

Column(s) that were aggregated by

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregateBy">Link to this property</a>

<details>

<summary>

aggregations: array of object {count, date }

Array of aggregation results with dynamic fields based on aggregateBy columns

</summary>

count: number

Number of events for this aggregation

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

date: optional string

Date (if groupByDate is true)

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations%20%3E%20(items)%20%3E%20(property)%20date">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations">Link to this property</a>

total: number

Total number of events in the aggregation

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20total">Link to this property</a>

<details>

<summary>

dateRange: optional object {endDate, startDate }

Date range used for filtering

</summary>

endDate: optional string

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20dateRange%20%3E%20(property)%20endDate">Link to this property</a>

startDate: optional string

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20dateRange%20%3E%20(property)%20startDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20dateRange">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsGraphql

##### [GraphQL endpoint for event aggregation](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/graphql/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/graphql

##### ModelsExpand Collapse

<details>

<summary>

GraphqlCreateResponse object {data, errors }

</summary>

data: optional unknown

<a href="#(resource)%20cloudforce_one.threat_events.graphql%20%3E%20(model)%20graphql_create_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

errors: optional array of unknown

<a href="#(resource)%20cloudforce_one.threat_events.graphql%20%3E%20(model)%20graphql_create_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.graphql%20%3E%20(model)%20graphql_create_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsGraph

##### [Query graph neighborhood from R2 Data Catalog](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/graph/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/graph

##### ModelsExpand Collapse

<details>

<summary>

GraphListResponse object {edges, node, nodes }

</summary>

<details>

<summary>

edges: array of object {id, relationshipType, source, 5 more }

</summary>

id: string

Deterministic composite edge id (source→target:relationshipType)

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

relationshipType: string

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20relationshipType">Link to this property</a>

source: string

Compact id of the source node (type:uuid)

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

sourceId: string

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20sourceId">Link to this property</a>

sourceType: string

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20sourceType">Link to this property</a>

target: string

Compact id of the target node (type:uuid)

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20target">Link to this property</a>

targetId: string

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20targetId">Link to this property</a>

targetType: string

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges%20%3E%20(items)%20%3E%20(property)%20targetType">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20edges">Link to this property</a>

node: map\[unknown]

Focal node object (legacy single-seed). Null when unavailable.

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20node">Link to this property</a>

nodes: array of map\[unknown]

<a href="#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)%20%3E%20(property)%20nodes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.graph%20%3E%20(model)%20graph_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsQueries

##### [List all saved event queries](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/queries

##### [Create a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/queries/create

##### [Read a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/queries/{query\_id}

##### [Update a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/events/queries/{query\_id}

##### [Delete a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/events/queries/{query\_id}

##### ModelsExpand Collapse

<details>

<summary>

QueryListResponse = array of object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)>)

<details>

<summary>

QueryCreateResponse object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)>)

<details>

<summary>

QueryGetResponse object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)>)

<details>

<summary>

QueryEditResponse object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsRelationships

##### [Filter and list events related to specific event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/relationships/methods/list)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/{event\_id}/relationships

##### ModelsExpand Collapse

<details>

<summary>

RelationshipListResponse = array of object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsIndicators

##### [Lists indicators across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {properties, type }

</summary>

<details>

<summary>

properties: object {completeness, indicators, pagination }

</summary>

<details>

<summary>

completeness: object {properties, type }

</summary>

<details>

<summary>

properties: object {complete, failedDatasets, failedShards, warnings }

</summary>

<details>

<summary>

complete: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20complete%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20complete">Link to this property</a>

<details>

<summary>

failedDatasets: object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets">Link to this property</a>

<details>

<summary>

failedShards: object {items, type }

</summary>

<details>

<summary>

items: object {properties, type }

</summary>

<details>

<summary>

properties: object {datasetId, shardId }

</summary>

<details>

<summary>

datasetId: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20datasetId%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

shardId: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20shardId%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20shardId">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards">Link to this property</a>

<details>

<summary>

warnings: object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness">Link to this property</a>

<details>

<summary>

indicators: object {items, type }

</summary>

<details>

<summary>

items: object {createdAt, indicatorType, sources, 8 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20indicatorType">Link to this property</a>

<details>

<summary>

sources: array of object {resourceId, resourceType, system, title }

RSS article sources from which this indicator was extracted.

</summary>

resourceId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceId">Link to this property</a>

resourceType: "article"

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceType">Link to this property</a>

system: "threat-signals"

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20system">Link to this property</a>

title: string

Threat Signals article title; null for historical provenance without a stored title.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {properties, type }

</summary>

<details>

<summary>

properties: object {count, cursor, has\_more, 4 more }

</summary>

<details>

<summary>

count: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20count%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

cursor: object {description, nullable, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor%20%3E%20(property)%20description">Link to this property</a>

nullable: boolean

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor%20%3E%20(property)%20nullable">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor">Link to this property</a>

<details>

<summary>

has\_more: object {description, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20has_more%20%3E%20(property)%20description">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20has_more%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20has_more">Link to this property</a>

<details>

<summary>

page: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20page%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20page">Link to this property</a>

<details>

<summary>

per\_page: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20per_page%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

total\_count: object {description, nullable, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count%20%3E%20(property)%20description">Link to this property</a>

nullable: boolean

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count%20%3E%20(property)%20nullable">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count">Link to this property</a>

<details>

<summary>

total\_count\_is\_exact: object {description, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count_is_exact%20%3E%20(property)%20description">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count_is_exact%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsIndicatorsAggregate

##### [Aggregate indicators by column(s)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/aggregate/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/indicators/aggregate

##### ModelsExpand Collapse

<details>

<summary>

AggregateListResponse object {aggregateBy, aggregations, failedDatasets, total }

</summary>

aggregateBy: string

Column(s) that were aggregated by

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregateBy">Link to this property</a>

<details>

<summary>

aggregations: array of object {count }

Array of aggregation results with dynamic fields based on aggregateBy columns

</summary>

count: number

Number of indicators for this aggregation

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations">Link to this property</a>

failedDatasets: number

Number of datasets whose aggregation failed and were excluded from the result

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20failedDatasets">Link to this property</a>

total: number

Total count in the aggregation: indicator rows when measure=indicators, or linked-event rows when measure=relationships

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20total">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsIndicatorsTypes

##### [Lists indicator types across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/types/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/indicator-types

##### ModelsExpand Collapse

<details>

<summary>

TypeListResponse object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsIndicatorsBy Dataset

##### [Lists indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/methods/list)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/indicators

##### [Reads an indicator](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/indicators/{indicator\_id}

##### ModelsExpand Collapse

<details>

<summary>

ByDatasetListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {createdAt, indicatorType, sources, 8 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

<details>

<summary>

sources: array of object {resourceId, resourceType, system, title }

RSS article sources from which this indicator was extracted.

</summary>

resourceId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceId">Link to this property</a>

resourceType: "article"

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceType">Link to this property</a>

system: "threat-signals"

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20system">Link to this property</a>

title: string

Threat Signals article title; null for historical provenance without a stored title.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)>)

<details>

<summary>

ByDatasetGetResponse object {createdAt, indicatorType, updatedAt, 7 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20indicatorType">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsIndicatorsBy DatasetTags

##### [List mirrored tags for an indicator dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/subresources/tags/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/indicators/tags

##### ModelsExpand Collapse

TagListResponse = array of unknown

Array of mirror tag rows

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.by_dataset.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsAttackers

##### [Lists attackers across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/attackers/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/attackers

##### ModelsExpand Collapse

<details>

<summary>

AttackerListResponse object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.attackers%20%3E%20(model)%20attacker_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.attackers%20%3E%20(model)%20attacker_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.attackers%20%3E%20(model)%20attacker_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.attackers%20%3E%20(model)%20attacker_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsCategories

##### [Lists categories across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/categories

##### [Reads a category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/get)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/categories/{category\_id}

##### [Creates a new category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/categories/create

##### [Updates a category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/edit)

Deprecated

PATCH/accounts/{account\_id}/cloudforce-one/events/categories/{category\_id}

##### [Deletes a category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/delete)

Deprecated

DELETE/accounts/{account\_id}/cloudforce-one/events/categories/{category\_id}

##### ModelsExpand Collapse

<details>

<summary>

CategoryListResponse = array of object {killChain, name, uuid, 3 more }

</summary>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20killChain">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

mitreAttack: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreCapec">Link to this property</a>

shortname: optional string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20shortname">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)>)

<details>

<summary>

CategoryGetResponse object {killChain, name, uuid, 3 more }

</summary>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

mitreAttack: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

shortname: optional string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)%20%3E%20(property)%20shortname">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_get_response%20%3E%20(schema)>)

<details>

<summary>

CategoryCreateResponse object {killChain, name, uuid, 3 more }

</summary>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

mitreAttack: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

shortname: optional string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20shortname">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)>)

<details>

<summary>

CategoryEditResponse object {killChain, name, uuid, 3 more }

</summary>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

mitreAttack: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

shortname: optional string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20shortname">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)>)

<details>

<summary>

CategoryDeleteResponse object {uuid }

</summary>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.categories%20%3E%20(model)%20category_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsCategoriesCatalog

##### [Lists categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/subresources/catalog/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/categories/catalog

##### ModelsExpand Collapse

<details>

<summary>

CatalogListResponse = array of object {killChain, name, uuid, 3 more }

</summary>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20killChain">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

mitreAttack: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreCapec">Link to this property</a>

shortname: optional string

<a href="#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20shortname">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.categories.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsCountries

##### [Retrieves countries information for all countries](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/countries/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/countries

##### ModelsExpand Collapse

<details>

<summary>

CountryListResponse = array of object {result, success }

</summary>

<details>

<summary>

result: array of object {alpha2, alpha3, name }

</summary>

alpha2: string

<a href="#(resource)%20cloudforce_one.threat_events.countries%20%3E%20(model)%20country_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20result%20%3E%20(items)%20%3E%20(property)%20alpha2">Link to this property</a>

alpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.countries%20%3E%20(model)%20country_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20result%20%3E%20(items)%20%3E%20(property)%20alpha3">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.countries%20%3E%20(model)%20country_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20result%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.countries%20%3E%20(model)%20country_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

success: string

<a href="#(resource)%20cloudforce_one.threat_events.countries%20%3E%20(model)%20country_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.countries%20%3E%20(model)%20country_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsCrons

#### Cloudforce OneThreat EventsDatasets

##### [Lists all datasets in an account](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/dataset

##### [Reads a dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}

##### [Creates a dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/dataset/create

##### [Updates an existing dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}

##### [Delete a dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}

##### [Reads raw data for an event by UUID](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/raw)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/raw/{dataset\_id}/{event\_id}

##### ModelsExpand Collapse

<details>

<summary>

DatasetListResponse = array of object {indicatorWriteMode, isAnalytics, isPublic, 3 more }

</summary>

<details>

<summary>

indicatorWriteMode: "read\_only"or "create\_only"or "full"

Effective indicator mutation capability after account/dataset authorization and dataset storage capability are applied. API Gateway method permissions are separate and must also allow the requested operation.

</summary>

One of the following:

"read\_only"

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorWriteMode%20%3E%20(member)%200">Link to this property</a>

"create\_only"

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorWriteMode%20%3E%20(member)%201">Link to this property</a>

"full"

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorWriteMode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorWriteMode">Link to this property</a>

isAnalytics: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20isAnalytics">Link to this property</a>

isPublic: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20isPublic">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

deletedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20deletedAt">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)>)

<details>

<summary>

DatasetGetResponse object {isAnalytics, isPublic, name, uuid }

</summary>

isAnalytics: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20isAnalytics">Link to this property</a>

isPublic: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20isPublic">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_get_response%20%3E%20(schema)>)

<details>

<summary>

DatasetCreateResponse object {isAnalytics, isPublic, name, uuid }

</summary>

isAnalytics: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_create_response%20%3E%20(schema)%20%3E%20(property)%20isAnalytics">Link to this property</a>

isPublic: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_create_response%20%3E%20(schema)%20%3E%20(property)%20isPublic">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_create_response%20%3E%20(schema)>)

<details>

<summary>

DatasetEditResponse object {isAnalytics, isPublic, name, uuid }

</summary>

isAnalytics: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_edit_response%20%3E%20(schema)%20%3E%20(property)%20isAnalytics">Link to this property</a>

isPublic: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_edit_response%20%3E%20(schema)%20%3E%20(property)%20isPublic">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_edit_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_edit_response%20%3E%20(schema)>)

<details>

<summary>

DatasetDeleteResponse object {name, uuid }

</summary>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_delete_response%20%3E%20(schema)>)

<details>

<summary>

DatasetRawResponse object {id, accountId, created, 3 more }

</summary>

id: number

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

accountId: number

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)%20%3E%20(property)%20accountId">Link to this property</a>

created: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

data: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

source: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets%20%3E%20(model)%20dataset_raw_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsDatasetsHealth

#### Cloudforce OneThreat EventsDatasetsEvents

##### [Reads an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/subresources/events/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/events/{event\_id}

##### ModelsExpand Collapse

<details>

<summary>

EventGetResponse object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.datasets.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsRaw

##### [Reads data for a raw event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/raw/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/{event\_id}/raw/{raw\_id}

##### [Updates a raw event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/raw/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/events/{event\_id}/raw/{raw\_id}

##### ModelsExpand Collapse

<details>

<summary>

RawGetResponse object {id, accountId, created, 3 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

accountId: number

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20accountId">Link to this property</a>

created: string

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

data: unknown

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

source: string

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)>)

<details>

<summary>

RawEditResponse object {id, data }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

data: unknown

<a href="#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_edit_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.raw%20%3E%20(model)%20raw_edit_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsRelate

##### [Removes an event reference](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/relate/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/events/relate/{event\_id}

##### ModelsExpand Collapse

<details>

<summary>

RelateDeleteResponse object {success }

</summary>

success: boolean

<a href="#(resource)%20cloudforce_one.threat_events.relate%20%3E%20(model)%20relate_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.relate%20%3E%20(model)%20relate_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTags

##### [Lists all tags (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/tags

##### [Creates a new tag](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/tags/create

##### [Updates a tag (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/events/tags/{tag\_uuid}

##### [Deletes a tag (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/events/tags/{tag\_uuid}

##### ModelsExpand Collapse

<details>

<summary>

TagListResponse object {pagination, tags }

</summary>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

<details>

<summary>

tags: array of object {uuid, value, activeDuration, 34 more }

</summary>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

activeDuration: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration">Link to this property</a>

<details>

<summary>

activeDuration\_annotated: optional object {value, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20activeDuration_annotated">Link to this property</a>

actorCategory: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory">Link to this property</a>

<details>

<summary>

actorCategory\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20actorCategory_annotated">Link to this property</a>

<details>

<summary>

aliases: optional array of object {value, confidence, tlp }

Structured aliases ({ value, confidence 1-10, tlp }). Public: returned to all accounts with per-entry TLP filtering (entries with tlp: purple are removed for non-CFONE accounts).

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliases">Link to this property</a>

aliasGroupNames: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliasGroupNames">Link to this property</a>

aliasGroupNamesInternal: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20aliasGroupNamesInternal">Link to this property</a>

attributionOrganization: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization">Link to this property</a>

<details>

<summary>

attributionOrganization\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20attributionOrganization_annotated">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

categoryUuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryUuid">Link to this property</a>

confidence: optional number

Overall tag confidence (1-10).

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

dateOfDiscovery: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20dateOfDiscovery">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

externalReferenceLinks: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferenceLinks">Link to this property</a>

<details>

<summary>

externalReferences: optional array of object {url, description }

Structured external references ({ url, description }). Public: returned to all accounts.

</summary>

url: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences">Link to this property</a>

<details>

<summary>

externalReferences\_annotated: optional array of object {value, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20externalReferences_annotated">Link to this property</a>

<details>

<summary>

internalAliases: optional array of object {value, confidence, tlp }

Owner-private structured aliases ({ value, confidence 1-10, tlp }). Returned to the owning account and omitted from shared-catalog non-owner responses.

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalAliases">Link to this property</a>

internalDescription: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20internalDescription">Link to this property</a>

lastSeen: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20lastSeen">Link to this property</a>

motive: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive">Link to this property</a>

<details>

<summary>

motive\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20motive_annotated">Link to this property</a>

opsecLevel: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel">Link to this property</a>

<details>

<summary>

opsecLevel\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20opsecLevel_annotated">Link to this property</a>

originCountryISO: optional string

ISO country code (alpha-2 or alpha-3). Normalized to uppercase on read. Null when stored value is blank/whitespace.

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO">Link to this property</a>

<details>

<summary>

originCountryISO\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20originCountryISO_annotated">Link to this property</a>

priority: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

<details>

<summary>

priority\_annotated: optional object {value, tlp }

</summary>

value: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20priority_annotated">Link to this property</a>

properties: optional map\[unknown]

Parsed custom field values. Null when the tag has no custom fields.

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

sophisticationLevel: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel">Link to this property</a>

<details>

<summary>

sophisticationLevel\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20sophisticationLevel_annotated">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

Tag-level TLP handling marking.

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

updatedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

version: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)>)

<details>

<summary>

TagCreateResponse object {uuid, value, activeDuration, 34 more }

</summary>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

activeDuration: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration">Link to this property</a>

<details>

<summary>

activeDuration\_annotated: optional object {value, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated">Link to this property</a>

actorCategory: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory">Link to this property</a>

<details>

<summary>

actorCategory\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated">Link to this property</a>

<details>

<summary>

aliases: optional array of object {value, confidence, tlp }

Structured aliases ({ value, confidence 1-10, tlp }). Public: returned to all accounts with per-entry TLP filtering (entries with tlp: purple are removed for non-CFONE accounts).

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliases">Link to this property</a>

aliasGroupNames: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliasGroupNames">Link to this property</a>

aliasGroupNamesInternal: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20aliasGroupNamesInternal">Link to this property</a>

attributionOrganization: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization">Link to this property</a>

<details>

<summary>

attributionOrganization\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20categoryName">Link to this property</a>

categoryUuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20categoryUuid">Link to this property</a>

confidence: optional number

Overall tag confidence (1-10).

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20confidence">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

dateOfDiscovery: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20dateOfDiscovery">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

externalReferenceLinks: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferenceLinks">Link to this property</a>

<details>

<summary>

externalReferences: optional array of object {url, description }

Structured external references ({ url, description }). Public: returned to all accounts.

</summary>

url: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences">Link to this property</a>

<details>

<summary>

externalReferences\_annotated: optional array of object {value, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated">Link to this property</a>

<details>

<summary>

internalAliases: optional array of object {value, confidence, tlp }

Owner-private structured aliases ({ value, confidence 1-10, tlp }). Returned to the owning account and omitted from shared-catalog non-owner responses.

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases">Link to this property</a>

internalDescription: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20internalDescription">Link to this property</a>

lastSeen: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20lastSeen">Link to this property</a>

motive: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive">Link to this property</a>

<details>

<summary>

motive\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated">Link to this property</a>

opsecLevel: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel">Link to this property</a>

<details>

<summary>

opsecLevel\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated">Link to this property</a>

originCountryISO: optional string

ISO country code (alpha-2 or alpha-3). Normalized to uppercase on read. Null when stored value is blank/whitespace.

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO">Link to this property</a>

<details>

<summary>

originCountryISO\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated">Link to this property</a>

priority: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

<details>

<summary>

priority\_annotated: optional object {value, tlp }

</summary>

value: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated">Link to this property</a>

properties: optional map\[unknown]

Parsed custom field values. Null when the tag has no custom fields.

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20properties">Link to this property</a>

sophisticationLevel: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel">Link to this property</a>

<details>

<summary>

sophisticationLevel\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

Tag-level TLP handling marking.

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

updatedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

version: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)>)

<details>

<summary>

TagEditResponse object {uuid, value, activeDuration, 34 more }

</summary>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

activeDuration: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration">Link to this property</a>

<details>

<summary>

activeDuration\_annotated: optional object {value, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20activeDuration_annotated">Link to this property</a>

actorCategory: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory">Link to this property</a>

<details>

<summary>

actorCategory\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20actorCategory_annotated">Link to this property</a>

<details>

<summary>

aliases: optional array of object {value, confidence, tlp }

Structured aliases ({ value, confidence 1-10, tlp }). Public: returned to all accounts with per-entry TLP filtering (entries with tlp: purple are removed for non-CFONE accounts).

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliases">Link to this property</a>

aliasGroupNames: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliasGroupNames">Link to this property</a>

aliasGroupNamesInternal: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20aliasGroupNamesInternal">Link to this property</a>

attributionOrganization: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization">Link to this property</a>

<details>

<summary>

attributionOrganization\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20attributionOrganization_annotated">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20categoryName">Link to this property</a>

categoryUuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20categoryUuid">Link to this property</a>

confidence: optional number

Overall tag confidence (1-10).

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20confidence">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

dateOfDiscovery: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20dateOfDiscovery">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

externalReferenceLinks: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferenceLinks">Link to this property</a>

<details>

<summary>

externalReferences: optional array of object {url, description }

Structured external references ({ url, description }). Public: returned to all accounts.

</summary>

url: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences">Link to this property</a>

<details>

<summary>

externalReferences\_annotated: optional array of object {value, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20externalReferences_annotated">Link to this property</a>

<details>

<summary>

internalAliases: optional array of object {value, confidence, tlp }

Owner-private structured aliases ({ value, confidence 1-10, tlp }). Returned to the owning account and omitted from shared-catalog non-owner responses.

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

maximum10

minimum1

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalAliases">Link to this property</a>

internalDescription: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20internalDescription">Link to this property</a>

lastSeen: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20lastSeen">Link to this property</a>

motive: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive">Link to this property</a>

<details>

<summary>

motive\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20motive_annotated">Link to this property</a>

opsecLevel: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel">Link to this property</a>

<details>

<summary>

opsecLevel\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20opsecLevel_annotated">Link to this property</a>

originCountryISO: optional string

ISO country code (alpha-2 or alpha-3). Normalized to uppercase on read. Null when stored value is blank/whitespace.

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO">Link to this property</a>

<details>

<summary>

originCountryISO\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20originCountryISO_annotated">Link to this property</a>

priority: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

<details>

<summary>

priority\_annotated: optional object {value, tlp }

</summary>

value: number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority_annotated">Link to this property</a>

properties: optional map\[unknown]

Parsed custom field values. Null when the tag has no custom fields.

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20properties">Link to this property</a>

sophisticationLevel: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel">Link to this property</a>

<details>

<summary>

sophisticationLevel\_annotated: optional object {value, confidence, tlp }

</summary>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20value">Link to this property</a>

confidence: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20confidence">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20sophisticationLevel_annotated">Link to this property</a>

<details>

<summary>

tlp: optional "red"or "amber"or "amber-strict"or 4 more

Tag-level TLP handling marking.

</summary>

One of the following:

"red"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%200">Link to this property</a>

"amber"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%201">Link to this property</a>

"amber-strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%202">Link to this property</a>

"green"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%203">Link to this property</a>

"clear"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%204">Link to this property</a>

"purple"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%205">Link to this property</a>

"amber+strict"

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

updatedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

version: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_edit_response%20%3E%20(schema)>)

<details>

<summary>

TagDeleteResponse object {uuid }

</summary>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTagsCategories

##### [Lists all tag categories (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/tags/categories

##### [Creates a new tag category (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/tags/categories/create

##### [Updates a tag category (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/edit)

Deprecated

PATCH/accounts/{account\_id}/cloudforce-one/events/tags/categories/{category\_uuid}

##### [Deletes a tag category (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/delete)

Deprecated

DELETE/accounts/{account\_id}/cloudforce-one/events/tags/categories/{category\_uuid}

##### ModelsExpand Collapse

<details>

<summary>

CategoryListResponse object {categories }

</summary>

<details>

<summary>

categories: array of object {name, uuid, createdAt, 3 more }

</summary>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

schema: optional array of object {key, kind, allowedValues, 11 more }

Parsed FieldDefinition\[] defining custom fields for this category, or null if none.

</summary>

key: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

kind: "string"or "number"or "enum"or 3 more

</summary>

One of the following:

"string"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

"enum"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%202">Link to this property</a>

"date"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%203">Link to this property</a>

"array"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%204">Link to this property</a>

"object"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

allowedValues: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20allowedValues">Link to this property</a>

<details>

<summary>

annotations: optional object {confidence, tlp }

</summary>

confidence: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations%20%3E%20(property)%20confidence">Link to this property</a>

tlp: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations">Link to this property</a>

deprecated: optional boolean

Marks a field as unavailable for new values while retaining its definition for historical values.

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20deprecated">Link to this property</a>

deprecatedValues: optional array of string

Enum values unavailable for new writes but retained in allowedValues for historical display.

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20deprecatedValues">Link to this property</a>

element: optional unknown

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20element">Link to this property</a>

<details>

<summary>

enforcement: optional "error"or "warn"or "off"

</summary>

One of the following:

"error"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%200">Link to this property</a>

"warn"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%201">Link to this property</a>

"off"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement">Link to this property</a>

<details>

<summary>

format: optional "date"or "url"or "duration"or "country"

</summary>

One of the following:

"date"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"url"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"duration"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"country"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format">Link to this property</a>

label: optional string

maxLength128

minLength1

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

maxLength: optional number

exclusiveMinimum

minimum0

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20maxLength">Link to this property</a>

<details>

<summary>

numberConstraint: optional object {integer, max, min }

</summary>

integer: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20integer">Link to this property</a>

max: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20max">Link to this property</a>

min: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint">Link to this property</a>

properties: optional map\[unknown]

Map of property key to FieldDefinition for object fields. Required when kind is ‘object’. See FieldDefinition (recursive).

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

required: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20required">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20schema">Link to this property</a>

updatedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)>)

<details>

<summary>

CategoryCreateResponse object {name, uuid, createdAt, 3 more }

</summary>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

schema: optional array of object {key, kind, allowedValues, 11 more }

Parsed FieldDefinition\[] defining custom fields for this category, or null if none.

</summary>

key: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

kind: "string"or "number"or "enum"or 3 more

</summary>

One of the following:

"string"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

"enum"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%202">Link to this property</a>

"date"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%203">Link to this property</a>

"array"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%204">Link to this property</a>

"object"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

allowedValues: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20allowedValues">Link to this property</a>

<details>

<summary>

annotations: optional object {confidence, tlp }

</summary>

confidence: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations%20%3E%20(property)%20confidence">Link to this property</a>

tlp: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations">Link to this property</a>

deprecated: optional boolean

Marks a field as unavailable for new values while retaining its definition for historical values.

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20deprecated">Link to this property</a>

deprecatedValues: optional array of string

Enum values unavailable for new writes but retained in allowedValues for historical display.

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20deprecatedValues">Link to this property</a>

element: optional unknown

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20element">Link to this property</a>

<details>

<summary>

enforcement: optional "error"or "warn"or "off"

</summary>

One of the following:

"error"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%200">Link to this property</a>

"warn"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%201">Link to this property</a>

"off"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement">Link to this property</a>

<details>

<summary>

format: optional "date"or "url"or "duration"or "country"

</summary>

One of the following:

"date"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"url"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"duration"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"country"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format">Link to this property</a>

label: optional string

maxLength128

minLength1

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

maxLength: optional number

exclusiveMinimum

minimum0

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20maxLength">Link to this property</a>

<details>

<summary>

numberConstraint: optional object {integer, max, min }

</summary>

integer: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20integer">Link to this property</a>

max: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20max">Link to this property</a>

min: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint">Link to this property</a>

properties: optional map\[unknown]

Map of property key to FieldDefinition for object fields. Required when kind is ‘object’. See FieldDefinition (recursive).

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

required: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20required">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20schema">Link to this property</a>

updatedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_create_response%20%3E%20(schema)>)

<details>

<summary>

CategoryEditResponse object {name, uuid, createdAt, 3 more }

</summary>

name: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

description: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

schema: optional array of object {key, kind, allowedValues, 11 more }

Parsed FieldDefinition\[] defining custom fields for this category, or null if none.

</summary>

key: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

kind: "string"or "number"or "enum"or 3 more

</summary>

One of the following:

"string"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

"enum"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%202">Link to this property</a>

"date"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%203">Link to this property</a>

"array"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%204">Link to this property</a>

"object"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

allowedValues: optional array of string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20allowedValues">Link to this property</a>

<details>

<summary>

annotations: optional object {confidence, tlp }

</summary>

confidence: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations%20%3E%20(property)%20confidence">Link to this property</a>

tlp: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20annotations">Link to this property</a>

deprecated: optional boolean

Marks a field as unavailable for new values while retaining its definition for historical values.

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20deprecated">Link to this property</a>

deprecatedValues: optional array of string

Enum values unavailable for new writes but retained in allowedValues for historical display.

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20deprecatedValues">Link to this property</a>

element: optional unknown

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20element">Link to this property</a>

<details>

<summary>

enforcement: optional "error"or "warn"or "off"

</summary>

One of the following:

"error"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%200">Link to this property</a>

"warn"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%201">Link to this property</a>

"off"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20enforcement">Link to this property</a>

<details>

<summary>

format: optional "date"or "url"or "duration"or "country"

</summary>

One of the following:

"date"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"url"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"duration"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"country"

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20format">Link to this property</a>

label: optional string

maxLength128

minLength1

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

maxLength: optional number

exclusiveMinimum

minimum0

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20maxLength">Link to this property</a>

<details>

<summary>

numberConstraint: optional object {integer, max, min }

</summary>

integer: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20integer">Link to this property</a>

max: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20max">Link to this property</a>

min: optional number

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20numberConstraint">Link to this property</a>

properties: optional map\[unknown]

Map of property key to FieldDefinition for object fields. Required when kind is ‘object’. See FieldDefinition (recursive).

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

required: optional boolean

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(items)%20%3E%20(property)%20required">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20schema">Link to this property</a>

updatedAt: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_edit_response%20%3E%20(schema)>)

<details>

<summary>

CategoryDeleteResponse object {uuid }

</summary>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.categories%20%3E%20(model)%20category_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTagsIndicators

##### [List indicators related to a tag](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/tags/{tag\_uuid}/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {createdAt, indicatorType, updatedAt, 7 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTagsIndicatorsBy Dataset

##### [List indicators related to a tag within a dataset (deprecated)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/indicators/subresources/by_dataset/methods/list)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/tags/{tag\_uuid}/indicators

##### ModelsExpand Collapse

<details>

<summary>

ByDatasetListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {createdAt, indicatorType, updatedAt, 7 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsEvent Tags

##### [Adds a tag to an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/event_tags/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/event\_tag/{event\_id}/create

##### [Removes a tag from an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/event_tags/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/events/event\_tag/{event\_id}

##### ModelsExpand Collapse

<details>

<summary>

EventTagCreateResponse object {success }

</summary>

success: boolean

<a href="#(resource)%20cloudforce_one.threat_events.event_tags%20%3E%20(model)%20event_tag_create_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.event_tags%20%3E%20(model)%20event_tag_create_response%20%3E%20(schema)>)

<details>

<summary>

EventTagDeleteResponse object {success }

</summary>

success: boolean

<a href="#(resource)%20cloudforce_one.threat_events.event_tags%20%3E%20(model)%20event_tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.event_tags%20%3E%20(model)%20event_tag_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTarget Industries

##### [Lists target industries across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/target_industries/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/targetIndustries

##### ModelsExpand Collapse

<details>

<summary>

TargetIndustryListResponse object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.target_industries%20%3E%20(model)%20target_industry_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.target_industries%20%3E%20(model)%20target_industry_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.target_industries%20%3E%20(model)%20target_industry_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.target_industries%20%3E%20(model)%20target_industry_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTarget IndustriesBy Dataset

##### [Lists all target industries for a specific dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/target_industries/subresources/by_dataset/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/targetIndustries

##### ModelsExpand Collapse

<details>

<summary>

ByDatasetListResponse object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.target_industries.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.target_industries.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.target_industries.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.target_industries.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsTarget IndustriesCatalog

##### [Lists all target industries from industry map catalog](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/target_industries/subresources/catalog/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/targetIndustries/catalog

##### ModelsExpand Collapse

<details>

<summary>

CatalogListResponse object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.target_industries.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.target_industries.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.target_industries.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.target_industries.catalog%20%3E%20(model)%20catalog_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat EventsInsights

#### Cloudforce OneThreat Signals

Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

## Prerequisites

1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.

#### Cloudforce OneThreat SignalsSearch

##### [Search Threat Signals articles using AI Search](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/search/methods/search)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/search

##### ModelsExpand Collapse

<details>

<summary>

SearchSearchResponse object {count, results }

</summary>

count: number

Number of unique article candidates returned in this response. Equal to results.length.

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

results: array of object {article\_id, dataset\_id, event\_id, 3 more }

</summary>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20article_id">Link to this property</a>

dataset\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

event\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20event_id">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

score: number

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

text: string

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsCategories

##### [List Threat Signals feed categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/categories/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/categories

##### ModelsExpand Collapse

<details>

<summary>

CategoryListResponse object {categories }

</summary>

<details>

<summary>

categories: array of object {id, description, name }

</summary>

id: string

Wire value accepted by the feed <code>category_id</code> field.

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

description: string

Plain-language description of the category.

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

name: string

Human-readable display label.

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsFeeds

##### [List Threat Signals feeds](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds

##### [Create Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds

##### [Update Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}

##### [Delete Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}

##### [Trigger Threat Signals feed poll](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/poll)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/poll

##### ModelsExpand Collapse

<details>

<summary>

FeedListResponse object {count, feeds, page, 2 more }

</summary>

count: number

Number of feeds on this page.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

feeds: array of object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds">Link to this property</a>

page: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20per_page">Link to this property</a>

total\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)>)

<details>

<summary>

FeedCreateResponse object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)>)

<details>

<summary>

FeedEditResponse object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)>)

<details>

<summary>

FeedDeleteResponse object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)>)

<details>

<summary>

FeedPollResponse object {errors, feeds, triggered }

</summary>

errors: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

feeds: array of object {feed\_id, status, workflow\_id, feed\_enabled }

</summary>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

<details>

<summary>

status: "workflow\_created"or "error"

</summary>

One of the following:

"workflow\_created"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"error"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

workflow\_id: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20workflow_id">Link to this property</a>

feed\_enabled: optional boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20feed_enabled">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds">Link to this property</a>

triggered: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20triggered">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsFeedsRaw

##### [Get Threat Signals feed XML](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/raw/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}/raw

##### ModelsExpand Collapse

RawGetResponse = string

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsFeedsSkills

##### [Get Threat Signals feed skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/skills/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}/skills

##### [Set Threat Signals feed skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/skills/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}/skills

##### ModelsExpand Collapse

<details>

<summary>

SkillGetResponse object {feed\_id, skills }

</summary>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

<details>

<summary>

skills: array of object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)>)

<details>

<summary>

SkillUpdateResponse object {feed\_id, skills }

</summary>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

<details>

<summary>

skills: array of object {position, skill\_id }

</summary>

position: number

Zero-based pipeline position.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20position">Link to this property</a>

skill\_id: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20skill_id">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20skills">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsArticles

##### [List Threat Signals articles](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles

##### [Bulk update Threat Signals article read status](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/bulk_edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles

##### [Get Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}

##### [Update Threat Signals article read status](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}

##### ModelsExpand Collapse

<details>

<summary>

ArticleListResponse object {articles, has\_more, next\_cursor, 2 more }

</summary>

<details>

<summary>

articles: array of object {id, dataset\_id, event\_id, 10 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

dataset\_id: string

Threat Events dataset identifier for the article redirect. Null when the account feeds dataset mapping is unavailable.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

event\_id: string

Threat Events event identifier associated with this article for a UI redirect. Null when no event has been linked.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20event_id">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

fetched\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20fetched_at">Link to this property</a>

link: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20link">Link to this property</a>

published\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20published_at">Link to this property</a>

read: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20read">Link to this property</a>

read\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20read_at">Link to this property</a>

summary: string

Persisted enrichment summary. Null until enrichment produces a summary.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20summary">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles">Link to this property</a>

has\_more: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20has_more">Link to this property</a>

next\_cursor: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20next_cursor">Link to this property</a>

total\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count">Link to this property</a>

total\_count\_is\_exact: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)>)

<details>

<summary>

ArticleBulkEditResponse object {updated\_count }

</summary>

updated\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_bulk_edit_response%20%3E%20(schema)>)

<details>

<summary>

ArticleGetResponse object {id, bullet\_points, content\_r2\_key, 16 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

bullet\_points: object {impact, what\_happened, who\_affected }

</summary>

impact: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20impact">Link to this property</a>

what\_happened: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20what_happened">Link to this property</a>

who\_affected: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20who_affected">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points">Link to this property</a>

content\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20content_r2_key">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

fetched\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20fetched_at">Link to this property</a>

<details>

<summary>

indicator\_extraction\_status: "in\_progress"or "complete"or "failed"or "unknown"

Progress of the article’s indicator extraction and IOC contextualization run. complete and failed are terminal; unknown means no run has been recorded.

</summary>

One of the following:

"in\_progress"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%200">Link to this property</a>

"complete"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%202">Link to this property</a>

"unknown"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status">Link to this property</a>

link: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20link">Link to this property</a>

metadata: map\[unknown]

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

published\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20published_at">Link to this property</a>

read: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20read">Link to this property</a>

read\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20read_at">Link to this property</a>

source\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20source_count">Link to this property</a>

summary: string

Persisted enrichment summary. Null until enrichment produces a summary.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20summary">Link to this property</a>

summary\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20summary_r2_key">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20skill_version">Link to this property</a>

tag\_skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)>)

<details>

<summary>

ArticleEditResponse object {id, bullet\_points, content\_r2\_key, 16 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

bullet\_points: object {impact, what\_happened, who\_affected }

</summary>

impact: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20impact">Link to this property</a>

what\_happened: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20what_happened">Link to this property</a>

who\_affected: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20who_affected">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points">Link to this property</a>

content\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20content_r2_key">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

fetched\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20fetched_at">Link to this property</a>

<details>

<summary>

indicator\_extraction\_status: "in\_progress"or "complete"or "failed"or "unknown"

Progress of the article’s indicator extraction and IOC contextualization run. complete and failed are terminal; unknown means no run has been recorded.

</summary>

One of the following:

"in\_progress"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%200">Link to this property</a>

"complete"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%202">Link to this property</a>

"unknown"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status">Link to this property</a>

link: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20link">Link to this property</a>

metadata: map\[unknown]

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

published\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20published_at">Link to this property</a>

read: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20read">Link to this property</a>

read\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20read_at">Link to this property</a>

source\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20source_count">Link to this property</a>

summary: string

Persisted enrichment summary. Null until enrichment produces a summary.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20summary">Link to this property</a>

summary\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20summary_r2_key">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20skill_version">Link to this property</a>

tag\_skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsArticlesContent

##### [Get Threat Signals article content](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/content/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/content

##### ModelsExpand Collapse

ContentGetResponse = string

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.content%20%3E%20(model)%20content_get_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsArticlesTags

##### [Add tag to Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tags

##### [Remove tag from Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tags/{tag\_id}

##### [Generate Threat Signals article AI tags](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/generate)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tag

##### ModelsExpand Collapse

<details>

<summary>

TagCreateResponse object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)>)

<details>

<summary>

TagDeleteResponse object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)>)

<details>

<summary>

TagGenerateResponse object {tag\_skill\_version, tags }

</summary>

tag\_skill\_version: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

Final hydrated assignment set; may be empty when no applicable tags are selected.

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsArticlesSkill Outputs

##### [Get Threat Signals article skill output](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/skill_outputs/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/skills/{skill\_id}/output

##### ModelsExpand Collapse

<details>

<summary>

SkillOutputGetResponse object {article\_id, custom\_skill\_version, output\_schema, 2 more }

</summary>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20article_id">Link to this property</a>

custom\_skill\_version: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_skill_version">Link to this property</a>

output\_schema: string

JSON-encoded output schema of the skill. Null when the skill no longer exists.

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

skill\_id: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20skill_id">Link to this property</a>

custom\_output: optional unknown

Skill output. Parsed JSON when the stored output is valid JSON, otherwise the raw string.

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_output">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsIndicators

##### [List Threat Signals article indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {id, article\_id, article\_title, 5 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20article_id">Link to this property</a>

article\_title: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20article_title">Link to this property</a>

dataset\_id: string

Threat Events dataset identifier for navigating from this indicator. Null when the account feeds dataset mapping is unavailable.

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {count, cursor, has\_more, 4 more }

</summary>

count: number

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20count">Link to this property</a>

cursor: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20cursor">Link to this property</a>

has\_more: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20has_more">Link to this property</a>

page: number

Ordinal of this cursor page; not a total-results offset.

minimum1

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

maximum100

minimum1

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20per_page">Link to this property</a>

total\_count: number

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count">Link to this property</a>

total\_count\_is\_exact: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsSkills

##### [List Threat Signals skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills

##### [Create Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills

##### [Get Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}

##### [Update Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}

##### [Delete Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}

##### ModelsExpand Collapse

<details>

<summary>

SkillListResponse object {count, custom\_skills\_available, page, 3 more }

</summary>

count: number

Number of skills on this page.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

custom\_skills\_available: boolean

Whether the authenticated account may access custom-skill capabilities under Stakeout’s Threat Signals access-mode policy. This is a policy availability indicator, not a row-existence indicator. False for threat\_signals\_only mode; true for entitled, allowlisted, cfone\_internal, and service modes.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20custom_skills_available">Link to this property</a>

page: number

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

skills: array of object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills">Link to this property</a>

total\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)>)

<details>

<summary>

SkillCreateResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)>)

<details>

<summary>

SkillGetResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)>)

<details>

<summary>

SkillEditResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)>)

<details>

<summary>

SkillDeleteResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)>)

#### Cloudforce OneThreat SignalsSkillsTag Categories

##### [Get Threat Signals skill tag categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/subresources/tag_categories/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}/tag-categories

##### [Replace Threat Signals skill tag categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/subresources/tag_categories/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}/tag-categories

##### ModelsExpand Collapse

<details>

<summary>

TagCategoryGetResponse object {category\_uuids, skill\_id }

</summary>

category\_uuids: array of string

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_get_response%20%3E%20(schema)%20%3E%20(property)%20category_uuids">Link to this property</a>

skill\_id: "default-tagging-skill"

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_get_response%20%3E%20(schema)%20%3E%20(property)%20skill_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_get_response%20%3E%20(schema)>)

<details>

<summary>

TagCategoryUpdateResponse object {category\_uuids, skill\_id }

</summary>

category\_uuids: array of string

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_update_response%20%3E%20(schema)%20%3E%20(property)%20category_uuids">Link to this property</a>

skill\_id: "default-tagging-skill"

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_update_response%20%3E%20(schema)%20%3E%20(property)%20skill_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_update_response%20%3E%20(schema)>)