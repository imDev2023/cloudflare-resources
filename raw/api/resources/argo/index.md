---
title: Argo
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Argo

#### ArgoSmart Routing

##### [Get Argo Smart Routing setting](https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/get)

GET/zones/{zone\_id}/argo/smart\_routing

##### [Patch Argo Smart Routing setting](https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/edit)

PATCH/zones/{zone\_id}/argo/smart\_routing

##### ModelsExpand Collapse

<details>

<summary>

SmartRoutingGetResponse object {id, editable, value, modified\_on }

</summary>

id: string

Specifies the identifier of the Argo Smart Routing setting.

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Specifies if the setting is editable.

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Specifies the enablement value of Argo Smart Routing.

</summary>

One of the following:

"on"

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Specifies the time when the setting was last modified.

formatdate-time

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_get_response%20%3E%20(schema)>)

<details>

<summary>

SmartRoutingEditResponse object {id, editable, value, modified\_on }

</summary>

id: string

Specifies the identifier of the Argo Smart Routing setting.

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Specifies if the setting is editable.

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Specifies the enablement value of Argo Smart Routing.

</summary>

One of the following:

"on"

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Specifies the time when the setting was last modified.

formatdate-time

<a href="#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20argo.smart_routing%20%3E%20(model)%20smart_routing_edit_response%20%3E%20(schema)>)

#### ArgoTiered Caching

##### [Get Tiered Caching setting](https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching/methods/get)

GET/zones/{zone\_id}/argo/tiered\_caching

##### [Patch Tiered Caching setting](https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching/methods/edit)

PATCH/zones/{zone\_id}/argo/tiered\_caching

##### ModelsExpand Collapse

<details>

<summary>

TieredCachingGetResponse object {id, editable, value, modified\_on }

</summary>

id: "tiered\_caching"

The identifier of the caching setting.

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_get_response%20%3E%20(schema)>)

<details>

<summary>

TieredCachingEditResponse object {id, editable, value, modified\_on }

</summary>

id: "tiered\_caching"

The identifier of the caching setting.

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "on"or "off"

Value of the Tiered Cache zone setting.

</summary>

One of the following:

"on"

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20argo.tiered_caching%20%3E%20(model)%20tiered_caching_edit_response%20%3E%20(schema)>)