---
title: Interconnects
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Network Interconnects](https://developers.cloudflare.com/api/resources/network_interconnects)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Interconnects

##### [List existing interconnects](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/list)

GET/accounts/{account\_id}/cni/interconnects

##### [Get information about an interconnect object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/get)

GET/accounts/{account\_id}/cni/interconnects/{icon}

##### [Create a new interconnect](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/create)

POST/accounts/{account\_id}/cni/interconnects

##### [Delete an interconnect object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/delete)

DELETE/accounts/{account\_id}/cni/interconnects/{icon}

##### [Generate the Letter of Authorization (LOA) for a given interconnect](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/loa)

GET/accounts/{account\_id}/cni/interconnects/{icon}/loa

##### [Get the current status of an interconnect object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/status)

GET/accounts/{account\_id}/cni/interconnects/{icon}/status

##### ModelsExpand Collapse

<details>

<summary>

InterconnectListResponse object {items, next }

</summary>

<details>

<summary>

items: array of object {account, facility, name, 7 more } or object {account, name, region, 4 more }

</summary>

One of the following:

<details>

<summary>

NscInterconnectPhysicalBody object {account, facility, name, 7 more }

</summary>

account: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20account">Link to this property</a>

<details>

<summary>

facility: object {address, name }

</summary>

address: array of string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20facility%20%3E%20(property)%20address">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20facility%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20facility">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

site: string

A Cloudflare site name.

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20site">Link to this property</a>

slot\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20slot_id">Link to this property</a>

speed: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20speed">Link to this property</a>

type: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

virtual\_port\_reservation\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

ccr\_device\_name: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20ccr_device_name">Link to this property</a>

owner: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20owner">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

NscInterconnectGcpPartnerBody object {account, name, region, 4 more }

</summary>

account: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20account">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

region: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

type: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

virtual\_port\_reservation\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

owner: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20owner">Link to this property</a>

<details>

<summary>

speed: optional "50M"or "100M"or "200M"or 9 more

Bandwidth structure as visible through the customer-facing API.

</summary>

One of the following:

"50M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%200">Link to this property</a>

"100M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%201">Link to this property</a>

"200M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%202">Link to this property</a>

"300M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%203">Link to this property</a>

"400M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%204">Link to this property</a>

"500M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%205">Link to this property</a>

"1G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%206">Link to this property</a>

"2G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%207">Link to this property</a>

"5G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%208">Link to this property</a>

"10G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%209">Link to this property</a>

"20G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%2010">Link to this property</a>

"50G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%2011">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20speed">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

next: optional number

formatint32

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20next">Link to this property</a>

</details>

[Link to this property](<#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_list_response%20%3E%20(schema)>)

<details>

<summary>

InterconnectGetResponse = object {account, facility, name, 7 more } or object {account, name, region, 4 more }

</summary>

One of the following:

<details>

<summary>

NscInterconnectPhysicalBody object {account, facility, name, 7 more }

</summary>

account: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20account">Link to this property</a>

<details>

<summary>

facility: object {address, name }

</summary>

address: array of string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20facility%20%3E%20(property)%20address">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20facility%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20facility">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

site: string

A Cloudflare site name.

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20site">Link to this property</a>

slot\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20slot_id">Link to this property</a>

speed: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20speed">Link to this property</a>

type: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

virtual\_port\_reservation\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

ccr\_device\_name: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20ccr_device_name">Link to this property</a>

owner: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20owner">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

NscInterconnectGcpPartnerBody object {account, name, region, 4 more }

</summary>

account: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20account">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

region: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

type: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

virtual\_port\_reservation\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

owner: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20owner">Link to this property</a>

<details>

<summary>

speed: optional "50M"or "100M"or "200M"or 9 more

Bandwidth structure as visible through the customer-facing API.

</summary>

One of the following:

"50M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%200">Link to this property</a>

"100M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%201">Link to this property</a>

"200M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%202">Link to this property</a>

"300M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%203">Link to this property</a>

"400M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%204">Link to this property</a>

"500M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%205">Link to this property</a>

"1G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%206">Link to this property</a>

"2G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%207">Link to this property</a>

"5G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%208">Link to this property</a>

"10G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%209">Link to this property</a>

"20G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%2010">Link to this property</a>

"50G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%2011">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_get_response%20%3E%20(schema)>)

<details>

<summary>

InterconnectCreateResponse = object {account, facility, name, 7 more } or object {account, name, region, 4 more }

</summary>

One of the following:

<details>

<summary>

NscInterconnectPhysicalBody object {account, facility, name, 7 more }

</summary>

account: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20account">Link to this property</a>

<details>

<summary>

facility: object {address, name }

</summary>

address: array of string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20facility%20%3E%20(property)%20address">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20facility%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20facility">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

site: string

A Cloudflare site name.

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20site">Link to this property</a>

slot\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20slot_id">Link to this property</a>

speed: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20speed">Link to this property</a>

type: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

virtual\_port\_reservation\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

ccr\_device\_name: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20ccr_device_name">Link to this property</a>

owner: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20owner">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

NscInterconnectGcpPartnerBody object {account, name, region, 4 more }

</summary>

account: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20account">Link to this property</a>

name: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

region: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

type: string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

virtual\_port\_reservation\_id: string

formatuuid

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

owner: optional string

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20owner">Link to this property</a>

<details>

<summary>

speed: optional "50M"or "100M"or "200M"or 9 more

Bandwidth structure as visible through the customer-facing API.

</summary>

One of the following:

"50M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%200">Link to this property</a>

"100M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%201">Link to this property</a>

"200M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%202">Link to this property</a>

"300M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%203">Link to this property</a>

"400M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%204">Link to this property</a>

"500M"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%205">Link to this property</a>

"1G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%206">Link to this property</a>

"2G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%207">Link to this property</a>

"5G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%208">Link to this property</a>

"10G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%209">Link to this property</a>

"20G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%2010">Link to this property</a>

"50G"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed%20%3E%20(member)%2011">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20speed">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_create_response%20%3E%20(schema)>)

<details>

<summary>

InterconnectStatusResponse = object {state } or object {state, reason } or object {state, reason } or object {state }

</summary>

One of the following:

<details>

<summary>

Pending object {state }

</summary>

state: "Pending"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Down object {state, reason }

</summary>

state: "Down"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

reason: optional string

Diagnostic information, if available

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20reason">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Unhealthy object {state, reason }

</summary>

state: "Unhealthy"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

reason: optional string

Diagnostic information, if available

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%202%20%3E%20(property)%20reason">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

Healthy object {state }

</summary>

state: "Healthy"

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)%20%3E%20(variant)%203">Link to this property</a>

</details>

[Link to this property](<#(resource)%20network_interconnects.interconnects%20%3E%20(model)%20interconnect_status_response%20%3E%20(schema)>)