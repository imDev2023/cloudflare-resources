---
title: Ramps
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Transit](https://developers.cloudflare.com/api/resources/magic_transit)

[Cf1 Sites](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Ramps

##### [List CF1 Site Ramps](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/list)

GET/accounts/{account\_id}/magic/cf1\_sites/{cf1\_site\_id}/ramps

##### [Get CF1 Site Ramp](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/get)

GET/accounts/{account\_id}/magic/cf1\_sites/{cf1\_site\_id}/ramps/{ramp\_id}

##### [Create CF1 Site Ramps](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/create)

POST/accounts/{account\_id}/magic/cf1\_sites/{cf1\_site\_id}/ramps

##### [Delete CF1 Site Ramp](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/delete)

DELETE/accounts/{account\_id}/magic/cf1\_sites/{cf1\_site\_id}/ramps/{ramp\_id}

##### ModelsExpand Collapse

<details>

<summary>

Ramp object {id, created\_on, modified\_on, 8 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: string

A human-provided name describing the ramp that should be unique within the CF1 Site.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

type: <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)">RampType</a>

The type of network connection (ramp) linking a CF1 Site to Cloudflare’s network.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

description: optional string

A human-provided description of the ramp.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

gre: optional object {managed\_by }

</summary>

managed\_by: optional string

URL reference to the source network resource that this ramp is managed by.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20gre%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20gre">Link to this property</a>

<details>

<summary>

gre\_interconnect: optional object {managed\_by }

</summary>

managed\_by: optional string

URL reference to the source network resource that this ramp is managed by.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20gre_interconnect%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20gre_interconnect">Link to this property</a>

<details>

<summary>

ipsec: optional object {managed\_by }

</summary>

managed\_by: optional string

URL reference to the source network resource that this ramp is managed by.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20ipsec%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20ipsec">Link to this property</a>

<details>

<summary>

mconn: optional object {managed\_by }

</summary>

managed\_by: optional string

URL reference to the source network resource that this ramp is managed by.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20mconn%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20mconn">Link to this property</a>

<details>

<summary>

mpls\_interconnect: optional object {managed\_by }

</summary>

managed\_by: optional string

URL reference to the source network resource that this ramp is managed by.

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20mpls_interconnect%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)%20%3E%20(property)%20mpls_interconnect">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp%20%3E%20(schema)>)

<details>

<summary>

RampType = "gre"or "gre\_interconnect"or "mpls\_interconnect"or 2 more

The type of network connection (ramp) linking a CF1 Site to Cloudflare’s network.

</summary>

One of the following:

"gre"

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"gre\_interconnect"

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"mpls\_interconnect"

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

"mconn"

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)%20%3E%20(member)%203">Link to this property</a>

"ipsec"

<a href="#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)%20%3E%20(member)%204">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.cf1_sites.ramps%20%3E%20(model)%20ramp_type%20%3E%20(schema)>)