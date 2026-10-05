---
title: Assets
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Requests](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Assets

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