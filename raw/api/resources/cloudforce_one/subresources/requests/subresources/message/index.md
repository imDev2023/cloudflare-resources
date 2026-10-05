---
title: Message
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Requests](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Message

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