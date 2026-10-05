---
title: Evaluations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AI Gateway](https://developers.cloudflare.com/api/resources/ai_gateway)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Evaluations

##### [List evaluations (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/list)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/evaluations

##### [Get an evaluation (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/get)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/evaluations/{id}

##### [Create an evaluation (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/create)

POST/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/evaluations

##### [Delete an evaluation (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/delete)

DELETE/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/evaluations/{id}

##### ModelsExpand Collapse

<details>

<summary>

EvaluationListResponse object {id, created\_at, datasets, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

datasets: array of object {id, account\_id, account\_tag, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_id">Link to this property</a>

account\_tag: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_tag">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

enable: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20enable">Link to this property</a>

<details>

<summary>

filters: array of object {key, operator, value }

</summary>

<details>

<summary>

key: "created\_at"or "request\_content\_type"or "response\_content\_type"or 10 more

</summary>

One of the following:

"created\_at"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%200">Link to this property</a>

"request\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%201">Link to this property</a>

"response\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%202">Link to this property</a>

"success"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%203">Link to this property</a>

"cached"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%204">Link to this property</a>

"provider"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%205">Link to this property</a>

"model"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%206">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%207">Link to this property</a>

"tokens"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%208">Link to this property</a>

"tokens\_in"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%209">Link to this property</a>

"tokens\_out"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2010">Link to this property</a>

"duration"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2011">Link to this property</a>

"feedback"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operator: "eq"or "contains"or "lt"or "gt"

</summary>

One of the following:

"eq"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"contains"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"lt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"gt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

value: array of stringor numberor boolean

</summary>

One of the following:

string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

processed: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20processed">Link to this property</a>

<details>

<summary>

results: array of object {id, created\_at, evaluation\_id, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

evaluation\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_id">Link to this property</a>

evaluation\_type\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_type_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

result: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

status: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

status\_description: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status_description">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_list_response%20%3E%20(schema)>)

<details>

<summary>

EvaluationGetResponse object {id, created\_at, datasets, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

datasets: array of object {id, account\_id, account\_tag, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_id">Link to this property</a>

account\_tag: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_tag">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

enable: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20enable">Link to this property</a>

<details>

<summary>

filters: array of object {key, operator, value }

</summary>

<details>

<summary>

key: "created\_at"or "request\_content\_type"or "response\_content\_type"or 10 more

</summary>

One of the following:

"created\_at"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%200">Link to this property</a>

"request\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%201">Link to this property</a>

"response\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%202">Link to this property</a>

"success"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%203">Link to this property</a>

"cached"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%204">Link to this property</a>

"provider"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%205">Link to this property</a>

"model"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%206">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%207">Link to this property</a>

"tokens"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%208">Link to this property</a>

"tokens\_in"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%209">Link to this property</a>

"tokens\_out"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2010">Link to this property</a>

"duration"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2011">Link to this property</a>

"feedback"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operator: "eq"or "contains"or "lt"or "gt"

</summary>

One of the following:

"eq"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"contains"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"lt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"gt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

value: array of stringor numberor boolean

</summary>

One of the following:

string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20datasets">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

processed: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20processed">Link to this property</a>

<details>

<summary>

results: array of object {id, created\_at, evaluation\_id, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

evaluation\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_id">Link to this property</a>

evaluation\_type\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_type_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

result: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

status: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

status\_description: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status_description">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_get_response%20%3E%20(schema)>)

<details>

<summary>

EvaluationCreateResponse object {id, created\_at, datasets, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

datasets: array of object {id, account\_id, account\_tag, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_id">Link to this property</a>

account\_tag: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_tag">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

enable: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20enable">Link to this property</a>

<details>

<summary>

filters: array of object {key, operator, value }

</summary>

<details>

<summary>

key: "created\_at"or "request\_content\_type"or "response\_content\_type"or 10 more

</summary>

One of the following:

"created\_at"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%200">Link to this property</a>

"request\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%201">Link to this property</a>

"response\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%202">Link to this property</a>

"success"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%203">Link to this property</a>

"cached"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%204">Link to this property</a>

"provider"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%205">Link to this property</a>

"model"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%206">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%207">Link to this property</a>

"tokens"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%208">Link to this property</a>

"tokens\_in"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%209">Link to this property</a>

"tokens\_out"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2010">Link to this property</a>

"duration"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2011">Link to this property</a>

"feedback"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operator: "eq"or "contains"or "lt"or "gt"

</summary>

One of the following:

"eq"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"contains"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"lt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"gt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

value: array of stringor numberor boolean

</summary>

One of the following:

string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20datasets">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

processed: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20processed">Link to this property</a>

<details>

<summary>

results: array of object {id, created\_at, evaluation\_id, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

evaluation\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_id">Link to this property</a>

evaluation\_type\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_type_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

result: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

status: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

status\_description: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status_description">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_create_response%20%3E%20(schema)>)

<details>

<summary>

EvaluationDeleteResponse object {id, created\_at, datasets, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

datasets: array of object {id, account\_id, account\_tag, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_id">Link to this property</a>

account\_tag: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20account_tag">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

enable: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20enable">Link to this property</a>

<details>

<summary>

filters: array of object {key, operator, value }

</summary>

<details>

<summary>

key: "created\_at"or "request\_content\_type"or "response\_content\_type"or 10 more

</summary>

One of the following:

"created\_at"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%200">Link to this property</a>

"request\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%201">Link to this property</a>

"response\_content\_type"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%202">Link to this property</a>

"success"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%203">Link to this property</a>

"cached"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%204">Link to this property</a>

"provider"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%205">Link to this property</a>

"model"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%206">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%207">Link to this property</a>

"tokens"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%208">Link to this property</a>

"tokens\_in"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%209">Link to this property</a>

"tokens\_out"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2010">Link to this property</a>

"duration"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2011">Link to this property</a>

"feedback"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operator: "eq"or "contains"or "lt"or "gt"

</summary>

One of the following:

"eq"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"contains"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"lt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"gt"

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

value: array of stringor numberor boolean

</summary>

One of the following:

string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20filters">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20datasets">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

processed: boolean

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20processed">Link to this property</a>

<details>

<summary>

results: array of object {id, created\_at, evaluation\_id, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

evaluation\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_id">Link to this property</a>

evaluation\_type\_id: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20evaluation_type_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

result: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

status: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

status\_description: string

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20status_description">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

total\_logs: number

<a href="#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)%20%3E%20(property)%20total_logs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.evaluations%20%3E%20(model)%20evaluation_delete_response%20%3E%20(schema)>)