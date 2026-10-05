---
title: Finetunes
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AI](https://developers.cloudflare.com/api/resources/ai)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Finetunes

##### [List Finetunes](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/methods/list)

GET/accounts/{account\_id}/ai/finetunes

##### [Create a new Finetune](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/methods/create)

POST/accounts/{account\_id}/ai/finetunes

##### ModelsExpand Collapse

<details>

<summary>

FinetuneListResponse object {id, created\_at, model, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

model: string

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)%20%3E%20(property)%20model">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

description: optional string

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_list_response%20%3E%20(schema)>)

<details>

<summary>

FinetuneCreateResponse object {id, created\_at, model, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

model: string

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20model">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

public: boolean

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20public">Link to this property</a>

description: optional string

<a href="#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai.finetunes%20%3E%20(model)%20finetune_create_response%20%3E%20(schema)>)

#### FinetunesAssets

##### [Upload a Finetune Asset](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/subresources/assets/methods/create)

POST/accounts/{account\_id}/ai/finetunes/{finetune\_id}/finetune-assets

##### ModelsExpand Collapse

<details>

<summary>

AssetCreateResponse object {success }

</summary>

success: boolean

<a href="#(resource)%20ai.finetunes.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai.finetunes.assets%20%3E%20(model)%20asset_create_response%20%3E%20(schema)>)

#### FinetunesPublic

##### [List Public Finetunes](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/subresources/public/methods/list)

GET/accounts/{account\_id}/ai/finetunes/public

##### ModelsExpand Collapse

<details>

<summary>

PublicListResponse object {id, created\_at, model, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

model: string

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20model">Link to this property</a>

modified\_at: string

formatdate-time

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

public: boolean

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20public">Link to this property</a>

description: optional string

<a href="#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai.finetunes.public%20%3E%20(model)%20public_list_response%20%3E%20(schema)>)