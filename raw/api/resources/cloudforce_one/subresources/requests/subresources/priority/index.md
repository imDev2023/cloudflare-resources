---
title: Priority
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Requests](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Priority

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