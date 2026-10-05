---
title: Domains
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Pages](https://developers.cloudflare.com/api/resources/pages)

[Projects](https://developers.cloudflare.com/api/resources/pages/subresources/projects)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Domains

##### [List Pages custom domains](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/list)

GET/accounts/{account\_id}/pages/projects/{project\_name}/domains

##### [Get a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/get)

GET/accounts/{account\_id}/pages/projects/{project\_name}/domains/{domain\_name}

##### [Add a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/create)

POST/accounts/{account\_id}/pages/projects/{project\_name}/domains

##### [Retry custom domain validation](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/edit)

PATCH/accounts/{account\_id}/pages/projects/{project\_name}/domains/{domain\_name}

##### [Delete a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/delete)

DELETE/accounts/{account\_id}/pages/projects/{project\_name}/domains/{domain\_name}

##### ModelsExpand Collapse

<details>

<summary>

DomainListResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)>)

<details>

<summary>

DomainGetResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)>)

<details>

<summary>

DomainCreateResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)>)

<details>

<summary>

DomainEditResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)>)

DomainDeleteResponse = unknown

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_delete_response%20%3E%20(schema)>)