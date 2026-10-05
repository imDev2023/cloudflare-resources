---
title: Endpoint Healthchecks
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Diagnostics](https://developers.cloudflare.com/api/resources/diagnostics)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Endpoint Healthchecks

##### [List Endpoint Health Checks](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/list)

GET/accounts/{account\_id}/diagnostics/endpoint-healthchecks

##### [Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/create)

POST/accounts/{account\_id}/diagnostics/endpoint-healthchecks

##### [Get Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/get)

GET/accounts/{account\_id}/diagnostics/endpoint-healthchecks/{id}

##### [Delete Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/delete)

DELETE/accounts/{account\_id}/diagnostics/endpoint-healthchecks/{id}

##### [Update Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/update)

PUT/accounts/{account\_id}/diagnostics/endpoint-healthchecks/{id}

##### ModelsExpand Collapse

<details>

<summary>

EndpointHealthcheck object {check\_type, endpoint, name }

</summary>

check\_type: "icmp"

type of check to perform

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck%20%3E%20(schema)%20%3E%20(property)%20check_type">Link to this property</a>

endpoint: string

the IP address of the host to perform checks against

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

name: optional string

Optional name associated with this check

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck%20%3E%20(schema)>)

<details>

<summary>

EndpointHealthcheckListResponse object {check\_type, endpoint, id, name }

</summary>

check\_type: "icmp"

type of check to perform

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_list_response%20%3E%20(schema)%20%3E%20(property)%20check_type">Link to this property</a>

endpoint: string

the IP address of the host to perform checks against

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_list_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

id: optional string

UUID.

maxLength36

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

Optional name associated with this check

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_list_response%20%3E%20(schema)>)

<details>

<summary>

EndpointHealthcheckCreateResponse object {check\_type, endpoint, id, name }

</summary>

check\_type: "icmp"

type of check to perform

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_create_response%20%3E%20(schema)%20%3E%20(property)%20check_type">Link to this property</a>

endpoint: string

the IP address of the host to perform checks against

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_create_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

id: optional string

UUID.

maxLength36

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

Optional name associated with this check

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_create_response%20%3E%20(schema)>)

<details>

<summary>

EndpointHealthcheckGetResponse object {check\_type, endpoint, id, name }

</summary>

check\_type: "icmp"

type of check to perform

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_get_response%20%3E%20(schema)%20%3E%20(property)%20check_type">Link to this property</a>

endpoint: string

the IP address of the host to perform checks against

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_get_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

id: optional string

UUID.

maxLength36

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

Optional name associated with this check

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_get_response%20%3E%20(schema)>)

<details>

<summary>

EndpointHealthcheckDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_delete_response%20%3E%20(schema)>)

<details>

<summary>

EndpointHealthcheckUpdateResponse object {check\_type, endpoint, id, name }

</summary>

check\_type: "icmp"

type of check to perform

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_update_response%20%3E%20(schema)%20%3E%20(property)%20check_type">Link to this property</a>

endpoint: string

the IP address of the host to perform checks against

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_update_response%20%3E%20(schema)%20%3E%20(property)%20endpoint">Link to this property</a>

id: optional string

UUID.

maxLength36

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

Optional name associated with this check

<a href="#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.endpoint-healthchecks%20%3E%20(model)%20endpoint_healthcheck_update_response%20%3E%20(schema)>)