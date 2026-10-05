---
title: Security TXT
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Security TXT

##### [Retrieves security.txt](https://developers.cloudflare.com/api/resources/security_txt/methods/get)

GET/zones/{zone\_id}/security-center/securitytxt

##### [Updates security.txt](https://developers.cloudflare.com/api/resources/security_txt/methods/update)

PUT/zones/{zone\_id}/security-center/securitytxt

##### [Deletes security.txt](https://developers.cloudflare.com/api/resources/security_txt/methods/delete)

DELETE/zones/{zone\_id}/security-center/securitytxt

##### ModelsExpand Collapse

<details>

<summary>

SecurityTXTGetResponse object {acknowledgments, canonical, contact, 6 more }

</summary>

acknowledgments: optional array of string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20acknowledgments">Link to this property</a>

canonical: optional array of string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20canonical">Link to this property</a>

contact: optional array of string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20contact">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

encryption: optional array of string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20encryption">Link to this property</a>

expires: optional string

formatdate-time

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20expires">Link to this property</a>

hiring: optional array of string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20hiring">Link to this property</a>

policy: optional array of string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

preferred\_languages: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)%20%3E%20(property)%20preferred_languages">Link to this property</a>

</details>

[Link to this property](<#(resource)%20security_txt%20%3E%20(model)%20security_txt_get_response%20%3E%20(schema)>)

<details>

<summary>

SecurityTXTUpdateResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20security_txt%20%3E%20(model)%20security_txt_update_response%20%3E%20(schema)>)

<details>

<summary>

SecurityTXTDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20security_txt%20%3E%20(model)%20security_txt_delete_response%20%3E%20(schema)>)