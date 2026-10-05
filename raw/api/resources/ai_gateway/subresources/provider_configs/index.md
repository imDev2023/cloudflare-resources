---
title: Provider Configs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AI Gateway](https://developers.cloudflare.com/api/resources/ai_gateway)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Provider Configs

##### [List provider keys](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/provider_configs/methods/list)

GET/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/provider\_configs

##### [Store a provider key](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/provider_configs/methods/create)

POST/accounts/{account\_id}/ai-gateway/gateways/{gateway\_id}/provider\_configs

##### ModelsExpand Collapse

<details>

<summary>

ProviderConfigListResponse object {id, alias, default\_config, 7 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

alias: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20alias">Link to this property</a>

default\_config: boolean

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20default_config">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

provider\_slug: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20provider_slug">Link to this property</a>

secret\_id: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20secret_id">Link to this property</a>

secret\_preview: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20secret_preview">Link to this property</a>

rate\_limit: optional number

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit">Link to this property</a>

rate\_limit\_period: optional number

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit_period">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_list_response%20%3E%20(schema)>)

<details>

<summary>

ProviderConfigCreateResponse object {id, alias, default\_config, 7 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

alias: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20alias">Link to this property</a>

default\_config: boolean

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20default_config">Link to this property</a>

gateway\_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20gateway_id">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

provider\_slug: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20provider_slug">Link to this property</a>

secret\_id: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20secret_id">Link to this property</a>

secret\_preview: string

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20secret_preview">Link to this property</a>

rate\_limit: optional number

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit">Link to this property</a>

rate\_limit\_period: optional number

<a href="#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)%20%3E%20(property)%20rate_limit_period">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.provider_configs%20%3E%20(model)%20provider_config_create_response%20%3E%20(schema)>)