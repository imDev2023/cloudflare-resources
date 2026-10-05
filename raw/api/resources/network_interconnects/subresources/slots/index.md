---
title: Slots
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Network Interconnects](https://developers.cloudflare.com/api/resources/network_interconnects)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Slots

##### [Retrieve a list of all slots matching the specified parameters](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/slots/methods/list)

GET/accounts/{account\_id}/cni/slots

##### [Get information about the specified slot](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/slots/methods/get)

GET/accounts/{account\_id}/cni/slots/{slot}

##### ModelsExpand Collapse

<details>

<summary>

SlotListResponse object {items, next }

</summary>

<details>

<summary>

items: array of object {id, facility, occupied, 4 more }

</summary>

id: string

Slot ID

formatuuid

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

facility: object {address, name }

</summary>

address: array of string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20facility%20%3E%20(property)%20address">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20facility%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20facility">Link to this property</a>

occupied: boolean

Whether the slot is occupied or not

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20occupied">Link to this property</a>

site: string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20site">Link to this property</a>

speed: string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20speed">Link to this property</a>

account: optional string

Customer account tag

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20account">Link to this property</a>

ccr\_device\_name: optional string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20ccr_device_name">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

next: optional number

formatint32

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)%20%3E%20(property)%20next">Link to this property</a>

</details>

[Link to this property](<#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_list_response%20%3E%20(schema)>)

<details>

<summary>

SlotGetResponse object {id, facility, occupied, 4 more }

</summary>

id: string

Slot ID

formatuuid

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

facility: object {address, name }

</summary>

address: array of string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20facility%20%3E%20(property)%20address">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20facility%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20facility">Link to this property</a>

occupied: boolean

Whether the slot is occupied or not

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20occupied">Link to this property</a>

site: string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20site">Link to this property</a>

speed: string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20speed">Link to this property</a>

account: optional string

Customer account tag

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20account">Link to this property</a>

ccr\_device\_name: optional string

<a href="#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)%20%3E%20(property)%20ccr_device_name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20network_interconnects.slots%20%3E%20(model)%20slot_get_response%20%3E%20(schema)>)