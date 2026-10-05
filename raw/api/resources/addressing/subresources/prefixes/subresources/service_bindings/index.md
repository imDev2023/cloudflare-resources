---
title: Service Bindings
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Service Bindings

##### [List Service Bindings](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list)

GET/accounts/{account\_id}/addressing/prefixes/{prefix\_id}/bindings

##### [Get Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/get)

GET/accounts/{account\_id}/addressing/prefixes/{prefix\_id}/bindings/{binding\_id}

##### [Create Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create)

POST/accounts/{account\_id}/addressing/prefixes/{prefix\_id}/bindings

##### [Delete Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/delete)

DELETE/accounts/{account\_id}/addressing/prefixes/{prefix\_id}/bindings/{binding\_id}

##### ModelsExpand Collapse

<details>

<summary>

ServiceBinding object {id, cidr, provisioning, 2 more }

</summary>

id: optional string

Identifier of a Service Binding.

maxLength32

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

cidr: optional string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20cidr">Link to this property</a>

<details>

<summary>

provisioning: optional object {state }

Status of a Service Binding’s deployment to the Cloudflare network

</summary>

<details>

<summary>

state: optional "provisioning"or "active"or "magic\_transit\_route\_missing"

When a binding has been deployed to a majority of Cloudflare datacenters, the binding will become active and can be used with its associated service.

</summary>

One of the following:

"provisioning"

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20provisioning%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20provisioning%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

"magic\_transit\_route\_missing"

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20provisioning%20%3E%20(property)%20state%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20provisioning%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20provisioning">Link to this property</a>

service\_id: optional string

Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint.

maxLength32

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20service_id">Link to this property</a>

service\_name: optional string

Name of a service running on the Cloudflare network

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)%20%3E%20(property)%20service_name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding%20%3E%20(schema)>)

<details>

<summary>

ServiceBindingDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20addressing.prefixes.service_bindings%20%3E%20(model)%20service_binding_delete_response%20%3E%20(schema)>)