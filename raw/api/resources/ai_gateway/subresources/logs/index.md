---
title: Logs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AI Gateway](https://developers.cloudflare.com/api/resources/ai_gateway)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Logs

##### [List Gateway Logs](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/list)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/logs

##### [Get Gateway Log Detail](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/get)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/logs/{id}

##### [Patch Gateway Log](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/edit)

PATCH/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/logs/{id}

##### [Delete Gateway Logs](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/delete)

DELETE/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/logs

##### [Get Gateway Log Request](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/request)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/logs/{id}/request

##### [Get Gateway Log Response](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/response)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/logs/{id}/response

##### ModelsExpand Collapse

<details>

<summary>

LogListResponse object {id, cached, created\_at, 16 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

cached: boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20cached">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

duration: number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20duration">Link to this property</a>

model: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20model">Link to this property</a>

path: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20path">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20provider">Link to this property</a>

success: boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

tokens\_in: number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20tokens_in">Link to this property</a>

tokens\_out: number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20tokens_out">Link to this property</a>

cost: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20cost">Link to this property</a>

custom\_cost: optional boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20custom_cost">Link to this property</a>

metadata: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

model\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20model_type">Link to this property</a>

request\_content\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20request_content_type">Link to this property</a>

request\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20request_type">Link to this property</a>

response\_content\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20response_content_type">Link to this property</a>

status\_code: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20status_code">Link to this property</a>

step: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20step">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)>)

<details>

<summary>

LogGetResponse object {id, cached, created\_at, 22 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

cached: boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20cached">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

duration: number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20duration">Link to this property</a>

model: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20model">Link to this property</a>

path: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20path">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20provider">Link to this property</a>

success: boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

tokens\_in: number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20tokens_in">Link to this property</a>

tokens\_out: number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20tokens_out">Link to this property</a>

cost: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20cost">Link to this property</a>

custom\_cost: optional boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_cost">Link to this property</a>

metadata: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

model\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20model_type">Link to this property</a>

request\_content\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20request_content_type">Link to this property</a>

request\_head: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20request_head">Link to this property</a>

request\_head\_complete: optional boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20request_head_complete">Link to this property</a>

request\_size: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20request_size">Link to this property</a>

request\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20request_type">Link to this property</a>

response\_content\_type: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20response_content_type">Link to this property</a>

response\_head: optional string

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20response_head">Link to this property</a>

response\_head\_complete: optional boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20response_head_complete">Link to this property</a>

response\_size: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20response_size">Link to this property</a>

status\_code: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20status_code">Link to this property</a>

step: optional number

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20step">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)>)

LogEditResponse = unknown

[Link to this property](<#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_edit_response%20%3E%20(schema)>)

<details>

<summary>

LogDeleteResponse object {success }

</summary>

success: boolean

<a href="#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_delete_response%20%3E%20(schema)>)

LogRequestResponse = unknown

[Link to this property](<#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_request_response%20%3E%20(schema)>)

LogResponseResponse = unknown

[Link to this property](<#(resource)%20ai_gateway.logs%20%3E%20(model)%20log_response_response%20%3E%20(schema)>)