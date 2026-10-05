---
title: Dynamic Routing
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AI Gateway](https://developers.cloudflare.com/api/resources/ai_gateway)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Dynamic Routing

##### [List dynamic routes](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/list)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes

##### [Get a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/get)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}

##### [Create a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/create)

POST/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes

##### [Rename a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/update)

PATCH/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}

##### [Delete a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/delete)

DELETE/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}

##### [List dynamic route deployments](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/list_deployments)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}/deployments

##### [Deploy a dynamic route version](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/create_deployment)

POST/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}/deployments

##### [List dynamic route versions](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/list_versions)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}/versions

##### [Create a dynamic route version](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/create_version)

POST/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}/versions

##### [Get a dynamic route version](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/get_version)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/routes/{id}/versions/{version\_id}

##### ModelsExpand Collapse

<details>

<summary>

DynamicRoutingListResponse object {data, success }

</summary>

<details>

<summary>

data: object {order\_by, order\_by\_direction, page, 2 more }

</summary>

order\_by: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20order_by">Link to this property</a>

order\_by\_direction: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20order_by_direction">Link to this property</a>

page: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

routes: array of object {id, account\_tag, created\_at, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_tag: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20account_tag">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

deployment: object {created\_at, deployment\_id, version\_id }

</summary>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20deployment%20%3E%20(property)%20created_at">Link to this property</a>

deployment\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20deployment%20%3E%20(property)%20deployment_id">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20deployment%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20deployment">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

version: object {active, created\_at, data, 2 more }

</summary>

<details>

<summary>

active: "true"or "false"

</summary>

One of the following:

"true"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%200">Link to this property</a>

"false"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20active">Link to this property</a>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20created_at">Link to this property</a>

data: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20data">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20version_id">Link to this property</a>

is\_valid: optional boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version%20%3E%20(property)%20is_valid">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20routes">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingGetResponse object {id, created\_at, deployment, 5 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

deployment: object {created\_at, deployment\_id, version\_id }

</summary>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20deployment%20%3E%20(property)%20created_at">Link to this property</a>

deployment\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20deployment%20%3E%20(property)%20deployment_id">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20deployment%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20deployment">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

version: object {active, created\_at, data, 2 more }

</summary>

<details>

<summary>

active: "true"or "false"

</summary>

One of the following:

"true"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%200">Link to this property</a>

"false"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20active">Link to this property</a>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20created_at">Link to this property</a>

data: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20data">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20version_id">Link to this property</a>

is\_valid: optional boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20is_valid">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingCreateResponse object {id, created\_at, deployment, 5 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

deployment: object {created\_at, deployment\_id, version\_id }

</summary>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20deployment%20%3E%20(property)%20created_at">Link to this property</a>

deployment\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20deployment%20%3E%20(property)%20deployment_id">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20deployment%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20deployment">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

version: object {active, created\_at, data, 2 more }

</summary>

<details>

<summary>

active: "true"or "false"

</summary>

One of the following:

"true"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%200">Link to this property</a>

"false"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20active">Link to this property</a>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20created_at">Link to this property</a>

data: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20data">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20version_id">Link to this property</a>

is\_valid: optional boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20is_valid">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingUpdateResponse object {route, success }

</summary>

<details>

<summary>

route: object {id, account\_tag, created\_at, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20id">Link to this property</a>

account\_tag: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20account_tag">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

deployment: object {created\_at, deployment\_id, version\_id }

</summary>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20deployment%20%3E%20(property)%20created_at">Link to this property</a>

deployment\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20deployment%20%3E%20(property)%20deployment_id">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20deployment%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20deployment">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

version: object {active, created\_at, data, 2 more }

</summary>

<details>

<summary>

active: "true"or "false"

</summary>

One of the following:

"true"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%200">Link to this property</a>

"false"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20active%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20active">Link to this property</a>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20created_at">Link to this property</a>

data: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20data">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20version_id">Link to this property</a>

is\_valid: optional boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version%20%3E%20(property)%20is_valid">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20route">Link to this property</a>

success: boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_update_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingDeleteResponse object {id, created\_at, elements, 3 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_delete_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingListDeploymentsResponse object {data, success }

</summary>

<details>

<summary>

data: object {deployments, order\_by, order\_by\_direction, 2 more }

</summary>

<details>

<summary>

deployments: array of object {created\_at, deployment\_id, version\_id }

</summary>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20deployments%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

deployment\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20deployments%20%3E%20(items)%20%3E%20(property)%20deployment_id">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20deployments%20%3E%20(items)%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20deployments">Link to this property</a>

order\_by: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20order_by">Link to this property</a>

order\_by\_direction: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20order_by_direction">Link to this property</a>

page: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20per_page">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_deployments_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingCreateDeploymentResponse object {id, created\_at, elements, 3 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_deployment_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingListVersionsResponse object {data, success }

</summary>

<details>

<summary>

data: object {order\_by, order\_by\_direction, page, 2 more }

</summary>

order\_by: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20order_by">Link to this property</a>

order\_by\_direction: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20order_by_direction">Link to this property</a>

page: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

versions: array of object {active, created\_at, data, 2 more }

</summary>

<details>

<summary>

active: "true"or "false"

</summary>

One of the following:

"true"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20active%20%3E%20(member)%200">Link to this property</a>

"false"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20active%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20active">Link to this property</a>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

data: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20data">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20version_id">Link to this property</a>

is\_valid: optional boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20is_valid">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20versions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_list_versions_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingCreateVersionResponse object {id, created\_at, elements, 3 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_create_version_response%20%3E%20(schema)>)

<details>

<summary>

DynamicRoutingGetVersionResponse object {id, active, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

active: "true"or "false"

</summary>

One of the following:

"true"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20active%20%3E%20(member)%200">Link to this property</a>

"false"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20active%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20active">Link to this property</a>

created\_at: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

data: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

<details>

<summary>

elements: array of object {id, outputs, type } or object {id, outputs, properties, type } or object {id, outputs, type } or 3 more

</summary>

One of the following:

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {next }

</summary>

<details>

<summary>

next: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs%20%3E%20(property)%20next">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20outputs">Link to this property</a>

type: "start"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {false, true }

</summary>

<details>

<summary>

false: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20false">Link to this property</a>

<details>

<summary>

true: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs%20%3E%20(property)%20true">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {conditions }

</summary>

conditions: optional unknown

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties%20%3E%20(property)%20conditions">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20properties">Link to this property</a>

type: "conditional"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20outputs">Link to this property</a>

type: "percentage"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {key, limit, limitType, window }

</summary>

key: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20key">Link to this property</a>

limit: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

limitType: "count"or "cost"

</summary>

One of the following:

"count"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%200">Link to this property</a>

"cost"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20limitType">Link to this property</a>

window: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties%20%3E%20(property)%20window">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20properties">Link to this property</a>

type: "rate"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {id, outputs, properties, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: object {fallback, success }

</summary>

<details>

<summary>

fallback: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20fallback">Link to this property</a>

<details>

<summary>

success: object {elementId }

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20outputs">Link to this property</a>

<details>

<summary>

properties: object {model, provider, retries, timeout }

</summary>

model: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20model">Link to this property</a>

provider: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20provider">Link to this property</a>

retries: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20retries">Link to this property</a>

timeout: number

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20properties">Link to this property</a>

type: "model"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {id, outputs, type }

</summary>

id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

outputs: map\[object {elementId } ]

</summary>

elementId: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs%20%3E%20(items)%20%3E%20(property)%20elementId">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20outputs">Link to this property</a>

type: "end"

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20elements">Link to this property</a>

gateway\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

minLength1

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

version\_id: string

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20version_id">Link to this property</a>

is\_valid: optional boolean

<a href="#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)%20%3E%20(property)%20is_valid">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.dynamic_routing%20%3E%20(model)%20dynamic_routing_get_version_response%20%3E%20(schema)>)