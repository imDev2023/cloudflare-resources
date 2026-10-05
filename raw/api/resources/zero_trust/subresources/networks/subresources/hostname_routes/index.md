---
title: Hostname Routes
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Networks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Hostname Routes

##### [List hostname routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/list)

GET/accounts/{account\_id}/zerotrust/routes/hostname

##### [Get hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/get)

GET/accounts/{account\_id}/zerotrust/routes/hostname/{hostname\_route\_id}

##### [Create hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/create)

POST/accounts/{account\_id}/zerotrust/routes/hostname

##### [Update hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/edit)

PATCH/accounts/{account\_id}/zerotrust/routes/hostname/{hostname\_route\_id}

##### [Delete hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/delete)

DELETE/accounts/{account\_id}/zerotrust/routes/hostname/{hostname\_route\_id}

##### ModelsExpand Collapse

<details>

<summary>

HostnameRoute object {id, comment, created\_at, 5 more }

</summary>

id: optional string

The hostname route ID.

formatuuid

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

comment: optional string

An optional description of the hostname route.

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20comment">Link to this property</a>

created\_at: optional string

Timestamp of when the resource was created.

formatdate-time

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

deleted\_at: optional string

Timestamp of when the resource was deleted. If <code>null</code>, the resource has not been deleted.

formatdate-time

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20deleted_at">Link to this property</a>

hostname: optional string

The hostname of the route.

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

<details>

<summary>

tun\_type: optional "cfd\_tunnel"or "warp\_connector"or "warp"or 4 more

The type of tunnel.

</summary>

One of the following:

"cfd\_tunnel"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%200">Link to this property</a>

"warp\_connector"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%201">Link to this property</a>

"warp"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%202">Link to this property</a>

"magic"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%203">Link to this property</a>

"ip\_sec"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%204">Link to this property</a>

"gre"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%205">Link to this property</a>

"cni"

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tun_type">Link to this property</a>

tunnel\_id: optional string

UUID of the tunnel.

formatuuid

maxLength36

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tunnel_id">Link to this property</a>

tunnel\_name: optional string

A user-friendly name for a tunnel.

<a href="#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)%20%3E%20(property)%20tunnel_name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.networks.hostname_routes%20%3E%20(model)%20hostname_route%20%3E%20(schema)>)