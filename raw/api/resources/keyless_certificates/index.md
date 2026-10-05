---
title: Keyless Certificates
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Keyless Certificates

##### [List Keyless SSL Configurations](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/list)

GET/zones/{zone\_id}/keyless\_certificates

##### [Get Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/get)

GET/zones/{zone\_id}/keyless\_certificates/{keyless\_certificate\_id}

##### [Create Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/create)

POST/zones/{zone\_id}/keyless\_certificates

##### [Edit Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/edit)

PATCH/zones/{zone\_id}/keyless\_certificates/{keyless\_certificate\_id}

##### [Delete Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/delete)

DELETE/zones/{zone\_id}/keyless\_certificates/{keyless\_certificate\_id}

##### ModelsExpand Collapse

<details>

<summary>

KeylessCertificate object {id, created\_on, enabled, 7 more }

</summary>

id: string

Keyless certificate identifier tag.

maxLength32

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

When the Keyless SSL was created.

formatdate-time

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

enabled: boolean

Whether or not the Keyless SSL is on or off.

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

host: string

The keyless SSL name.

formathostname

maxLength253

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

modified\_on: string

When the Keyless SSL was last modified.

formatdate-time

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: string

The keyless SSL name.

maxLength180

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

permissions: array of string

Available permissions for the Keyless SSL for the current user requesting the item.

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20permissions">Link to this property</a>

port: number

The keyless SSL port used to communicate between Cloudflare and the client’s Keyless SSL server.

maxLength65535

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20port">Link to this property</a>

<details>

<summary>

status: "active"or "deleted"

Status of the Keyless SSL.

</summary>

One of the following:

"active"

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleted"

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

tunnel: optional <a href="https://developers.cloudflare.com/api/resources/keyless_certificates#(resource)%20keyless_certificates%20%3E%20(model)%20tunnel%20%3E%20(schema)">Tunnel</a> { private\_ip, vnet\_id }

Configuration for using Keyless SSL through a Cloudflare Tunnel.

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)%20%3E%20(property)%20tunnel">Link to this property</a>

</details>

[Link to this property](<#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate%20%3E%20(schema)>)

<details>

<summary>

Tunnel object {private\_ip, vnet\_id }

Configuration for using Keyless SSL through a Cloudflare Tunnel.

</summary>

private\_ip: string

Private IP of the Key Server Host.

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20tunnel%20%3E%20(schema)%20%3E%20(property)%20private_ip">Link to this property</a>

vnet\_id: string

Cloudflare Tunnel Virtual Network ID.

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20tunnel%20%3E%20(schema)%20%3E%20(property)%20vnet_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20keyless_certificates%20%3E%20(model)%20tunnel%20%3E%20(schema)>)

<details>

<summary>

KeylessCertificateDeleteResponse object {id }

</summary>

id: optional string

Keyless certificate identifier tag.

maxLength32

<a href="#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20keyless_certificates%20%3E%20(model)%20keyless_certificate_delete_response%20%3E%20(schema)>)