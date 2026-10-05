---
title: Registrations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Devices](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Registrations

##### [List registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/list)

GET/accounts/{account\_id}/devices/registrations

##### [Get registration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/get)

GET/accounts/{account\_id}/devices/registrations/{registration\_id}

##### [Delete registration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/delete)

DELETE/accounts/{account\_id}/devices/registrations/{registration\_id}

##### [Delete registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/bulk_delete)

DELETE/accounts/{account\_id}/devices/registrations

##### [Revoke registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/revoke)

Deprecated

POST/accounts/{account\_id}/devices/registrations/revoke

##### [Unrevoke registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/unrevoke)

Deprecated

POST/accounts/{account\_id}/devices/registrations/unrevoke

##### ModelsExpand Collapse

<details>

<summary>

RegistrationListResponse object {id, created\_at, device, 12 more }

A WARP configuration tied to a single user. Multiple registrations can be created from a single WARP device.

</summary>

id: string

The ID of the registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

The RFC3339 timestamp when the registration was created.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

device: object {id, name, client\_version }

Device details embedded inside of a registration.

</summary>

id: string

The ID of the device.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20device%20%3E%20(property)%20id">Link to this property</a>

name: string

The name of the device.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20device%20%3E%20(property)%20name">Link to this property</a>

client\_version: optional string

Version of the WARP client.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20device%20%3E%20(property)%20client_version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20device">Link to this property</a>

key: string

The public key used to connect to the Cloudflare network.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20key">Link to this property</a>

last\_seen\_at: string

The RFC3339 timestamp when the registration was last seen.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20last_seen_at">Link to this property</a>

<details>

<summary>

registration\_type: "warp"or "browser\_extension"

The registration client type, derived from device\_type.

</summary>

One of the following:

"warp"

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20registration_type%20%3E%20(member)%200">Link to this property</a>

"browser\_extension"

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20registration_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20registration_type">Link to this property</a>

updated\_at: string

The RFC3339 timestamp when the registration was last updated.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

deleted\_at: optional string

The RFC3339 timestamp when the registration was deleted.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20deleted_at">Link to this property</a>

key\_type: optional string

The type of encryption key used by the WARP client for the active key. Currently ‘curve25519’ for WireGuard and ‘secp256r1’ for MASQUE.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20key_type">Link to this property</a>

<details>

<summary>

policy: optional object {id, default, deleted, 2 more }

The device settings profile assigned to this registration.

</summary>

id: string

The ID of the device settings profile.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20id">Link to this property</a>

default: boolean

Whether the device settings profile is the default profile for the account.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20default">Link to this property</a>

deleted: boolean

Whether the device settings profile was deleted.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20deleted">Link to this property</a>

name: string

The name of the device settings profile.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20name">Link to this property</a>

updated\_at: string

The RFC3339 timestamp of when the device settings profile last changed for the registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

revoked\_at: optional string

The RFC3339 timestamp when the registration was revoked.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20revoked_at">Link to this property</a>

tunnel\_type: optional string

Type of the tunnel - wireguard or masque.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20tunnel_type">Link to this property</a>

<details>

<summary>

user: optional object {id, email, name }

</summary>

id: optional string

UUID.

maxLength36

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20email">Link to this property</a>

name: optional string

The enrolled device user’s name.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20user">Link to this property</a>

virtual\_ipv4: optional string

The virtual IPv4 address assigned to the network interface of the tunnel for this registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20virtual_ipv4">Link to this property</a>

virtual\_ipv6: optional string

The virtual IPv6 address assigned to the network interface of the tunnel for this registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)%20%3E%20(property)%20virtual_ipv6">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_list_response%20%3E%20(schema)>)

<details>

<summary>

RegistrationGetResponse object {id, created\_at, device, 12 more }

A WARP configuration tied to a single user. Multiple registrations can be created from a single WARP device.

</summary>

id: string

The ID of the registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

The RFC3339 timestamp when the registration was created.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

device: object {id, name, client\_version }

Device details embedded inside of a registration.

</summary>

id: string

The ID of the device.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20device%20%3E%20(property)%20id">Link to this property</a>

name: string

The name of the device.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20device%20%3E%20(property)%20name">Link to this property</a>

client\_version: optional string

Version of the WARP client.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20device%20%3E%20(property)%20client_version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20device">Link to this property</a>

key: string

The public key used to connect to the Cloudflare network.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20key">Link to this property</a>

last\_seen\_at: string

The RFC3339 timestamp when the registration was last seen.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20last_seen_at">Link to this property</a>

<details>

<summary>

registration\_type: "warp"or "browser\_extension"

The registration client type, derived from device\_type.

</summary>

One of the following:

"warp"

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20registration_type%20%3E%20(member)%200">Link to this property</a>

"browser\_extension"

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20registration_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20registration_type">Link to this property</a>

updated\_at: string

The RFC3339 timestamp when the registration was last updated.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

deleted\_at: optional string

The RFC3339 timestamp when the registration was deleted.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20deleted_at">Link to this property</a>

key\_type: optional string

The type of encryption key used by the WARP client for the active key. Currently ‘curve25519’ for WireGuard and ‘secp256r1’ for MASQUE.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20key_type">Link to this property</a>

<details>

<summary>

policy: optional object {id, default, deleted, 2 more }

The device settings profile assigned to this registration.

</summary>

id: string

The ID of the device settings profile.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20id">Link to this property</a>

default: boolean

Whether the device settings profile is the default profile for the account.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20default">Link to this property</a>

deleted: boolean

Whether the device settings profile was deleted.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20deleted">Link to this property</a>

name: string

The name of the device settings profile.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20name">Link to this property</a>

updated\_at: string

The RFC3339 timestamp of when the device settings profile last changed for the registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20policy%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

revoked\_at: optional string

The RFC3339 timestamp when the registration was revoked.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20revoked_at">Link to this property</a>

tunnel\_type: optional string

Type of the tunnel - wireguard or masque.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnel_type">Link to this property</a>

<details>

<summary>

user: optional object {id, email, name }

</summary>

id: optional string

UUID.

maxLength36

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20email">Link to this property</a>

name: optional string

The enrolled device user’s name.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20user">Link to this property</a>

virtual\_ipv4: optional string

The virtual IPv4 address assigned to the network interface of the tunnel for this registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20virtual_ipv4">Link to this property</a>

virtual\_ipv6: optional string

The virtual IPv6 address assigned to the network interface of the tunnel for this registration.

<a href="#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)%20%3E%20(property)%20virtual_ipv6">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_get_response%20%3E%20(schema)>)

RegistrationDeleteResponse = unknown

[Link to this property](<#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_delete_response%20%3E%20(schema)>)

RegistrationBulkDeleteResponse = unknown

[Link to this property](<#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_bulk_delete_response%20%3E%20(schema)>)

RegistrationRevokeResponse = unknown

[Link to this property](<#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_revoke_response%20%3E%20(schema)>)

RegistrationUnrevokeResponse = unknown

[Link to this property](<#(resource)%20zero_trust.devices.registrations%20%3E%20(model)%20registration_unrevoke_response%20%3E%20(schema)>)