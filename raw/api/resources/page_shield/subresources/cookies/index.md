---
title: Cookies
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Page Shield](https://developers.cloudflare.com/api/resources/page_shield)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Cookies

##### [List detected cookies](https://developers.cloudflare.com/api/resources/page_shield/subresources/cookies/methods/list)

GET/zones/{zone\_id}/page\_shield/cookies

##### [Get a detected cookie](https://developers.cloudflare.com/api/resources/page_shield/subresources/cookies/methods/get)

GET/zones/{zone\_id}/page\_shield/cookies/{cookie\_id}

##### ModelsExpand Collapse

<details>

<summary>

CookieListResponse object {id, first\_seen\_at, host, 11 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

first\_seen\_at: string

formatdate-time

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20first_seen_at">Link to this property</a>

host: string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_seen\_at: string

formatdate-time

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20last_seen_at">Link to this property</a>

name: string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: "first\_party"or "unknown"

</summary>

One of the following:

"first\_party"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"unknown"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

domain\_attribute: optional string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20domain_attribute">Link to this property</a>

expires\_attribute: optional string

formatdate-time

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_attribute">Link to this property</a>

http\_only\_attribute: optional boolean

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20http_only_attribute">Link to this property</a>

max\_age\_attribute: optional number

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20max_age_attribute">Link to this property</a>

page\_urls: optional array of string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20page_urls">Link to this property</a>

path\_attribute: optional string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20path_attribute">Link to this property</a>

<details>

<summary>

same\_site\_attribute: optional "lax"or "strict"or "none"

</summary>

One of the following:

"lax"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute%20%3E%20(member)%200">Link to this property</a>

"strict"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute">Link to this property</a>

secure\_attribute: optional boolean

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)%20%3E%20(property)%20secure_attribute">Link to this property</a>

</details>

[Link to this property](<#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_list_response%20%3E%20(schema)>)

<details>

<summary>

CookieGetResponse object {id, first\_seen\_at, host, 11 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

first\_seen\_at: string

formatdate-time

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20first_seen_at">Link to this property</a>

host: string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

last\_seen\_at: string

formatdate-time

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20last_seen_at">Link to this property</a>

name: string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: "first\_party"or "unknown"

</summary>

One of the following:

"first\_party"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"unknown"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

domain\_attribute: optional string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20domain_attribute">Link to this property</a>

expires\_attribute: optional string

formatdate-time

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20expires_attribute">Link to this property</a>

http\_only\_attribute: optional boolean

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20http_only_attribute">Link to this property</a>

max\_age\_attribute: optional number

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20max_age_attribute">Link to this property</a>

page\_urls: optional array of string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20page_urls">Link to this property</a>

path\_attribute: optional string

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20path_attribute">Link to this property</a>

<details>

<summary>

same\_site\_attribute: optional "lax"or "strict"or "none"

</summary>

One of the following:

"lax"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute%20%3E%20(member)%200">Link to this property</a>

"strict"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20same_site_attribute">Link to this property</a>

secure\_attribute: optional boolean

<a href="#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)%20%3E%20(property)%20secure_attribute">Link to this property</a>

</details>

[Link to this property](<#(resource)%20page_shield.cookies%20%3E%20(model)%20cookie_get_response%20%3E%20(schema)>)