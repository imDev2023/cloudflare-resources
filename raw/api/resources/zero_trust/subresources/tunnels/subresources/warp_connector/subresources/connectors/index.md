---
title: Connectors
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels)

[WARP Connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Connectors

##### [Get a Mesh node connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connectors/methods/get)

GET/accounts/{account\_id}/warp\_connector/{tunnel\_id}/connectors/{connector\_id}

##### ModelsExpand Collapse

<details>

<summary>

ConnectorGetResponse object {id, arch, conns, 4 more }

A Mesh node connector that maintains a connection to a Cloudflare data center.

</summary>

id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

arch: optional string

The cloudflared OS architecture used to establish this connection.

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20arch">Link to this property</a>

<details>

<summary>

conns: optional array of object {id, client\_id, client\_version, 3 more }

The Mesh node connections between your origin and Cloudflare’s edge.

</summary>

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

client\_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns%20%3E%20(items)%20%3E%20(property)%20client_id">Link to this property</a>

client\_version: optional string

The cloudflared version used to establish this connection.

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns%20%3E%20(items)%20%3E%20(property)%20client_version">Link to this property</a>

colo\_name: optional string

The Cloudflare data center used for this connection.

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns%20%3E%20(items)%20%3E%20(property)%20colo_name">Link to this property</a>

opened\_at: optional string

Timestamp of when the connection was established.

formatdate-time

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns%20%3E%20(items)%20%3E%20(property)%20opened_at">Link to this property</a>

origin\_ip: optional string

The public IP address of the host running the Mesh node connector.

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns%20%3E%20(items)%20%3E%20(property)%20origin_ip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20conns">Link to this property</a>

features: optional array of string

Features enabled for the Cloudflare Tunnel.

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20features">Link to this property</a>

<details>

<summary>

ha\_status: optional "offline"or "passive"or "active"

The HA status of a Mesh node connector.

</summary>

One of the following:

"offline"

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20ha_status%20%3E%20(member)%200">Link to this property</a>

"passive"

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20ha_status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20ha_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20ha_status">Link to this property</a>

run\_at: optional string

Timestamp of when the tunnel connection was started.

formatdate-time

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20run_at">Link to this property</a>

version: optional string

The cloudflared version used to establish this connection.

<a href="#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.tunnels.warp_connector.connectors%20%3E%20(model)%20connector_get_response%20%3E%20(schema)>)