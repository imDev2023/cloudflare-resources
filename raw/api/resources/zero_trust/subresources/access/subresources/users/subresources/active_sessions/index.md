---
title: Active Sessions
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Access](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access)

[Users](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Active Sessions

##### [Get active sessions](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/subresources/active_sessions/methods/list)

GET/accounts/{account\_id}/access/users/{user\_id}/active\_sessions

##### [Get single active session](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/subresources/active_sessions/methods/get)

GET/accounts/{account\_id}/access/users/{user\_id}/active\_sessions/{nonce}

##### ModelsExpand Collapse

<details>

<summary>

ActiveSessionListResponse object {expiration, metadata, name }

</summary>

expiration: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20expiration">Link to this property</a>

<details>

<summary>

metadata: optional object {apps, expires, iat, 2 more }

</summary>

<details>

<summary>

apps: optional map\[object {hostname, name, type, uid } ]

</summary>

hostname: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20apps%20%3E%20(items)%20%3E%20(property)%20hostname">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20apps%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

type: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20apps%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

uid: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20apps%20%3E%20(items)%20%3E%20(property)%20uid">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20apps">Link to this property</a>

expires: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20expires">Link to this property</a>

iat: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20iat">Link to this property</a>

nonce: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20nonce">Link to this property</a>

ttl: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20ttl">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_list_response%20%3E%20(schema)>)

<details>

<summary>

ActiveSessionGetResponse object {account\_id, auth\_status, common\_name, 16 more }

</summary>

account\_id: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

auth\_status: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_status">Link to this property</a>

common\_name: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20common_name">Link to this property</a>

device\_id: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20device_id">Link to this property</a>

<details>

<summary>

device\_sessions: optional map\[object {last\_authenticated } ]

</summary>

last\_authenticated: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20device_sessions%20%3E%20(items)%20%3E%20(property)%20last_authenticated">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20device_sessions">Link to this property</a>

<details>

<summary>

devicePosture: optional map\[object {id, check, data, 6 more } ]

</summary>

id: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

check: optional object {exists, path }

</summary>

exists: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20check%20%3E%20(property)%20exists">Link to this property</a>

path: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20check%20%3E%20(property)%20path">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20check">Link to this property</a>

data: optional unknown

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20data">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

error: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

rule\_name: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20rule_name">Link to this property</a>

success: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20success">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

type: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20devicePosture">Link to this property</a>

email: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20email">Link to this property</a>

<details>

<summary>

geo: optional object {country }

</summary>

country: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20geo%20%3E%20(property)%20country">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20geo">Link to this property</a>

iat: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20iat">Link to this property</a>

<details>

<summary>

idp: optional object {id, type }

</summary>

id: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20idp%20%3E%20(property)%20id">Link to this property</a>

type: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20idp%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20idp">Link to this property</a>

ip: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20ip">Link to this property</a>

is\_gateway: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20is_gateway">Link to this property</a>

is\_warp: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20is_warp">Link to this property</a>

isActive: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20isActive">Link to this property</a>

<details>

<summary>

mtls\_auth: optional object {auth\_status, cert\_issuer\_dn, cert\_issuer\_ski, 2 more }

</summary>

auth\_status: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20mtls_auth%20%3E%20(property)%20auth_status">Link to this property</a>

cert\_issuer\_dn: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20mtls_auth%20%3E%20(property)%20cert_issuer_dn">Link to this property</a>

cert\_issuer\_ski: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20mtls_auth%20%3E%20(property)%20cert_issuer_ski">Link to this property</a>

cert\_presented: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20mtls_auth%20%3E%20(property)%20cert_presented">Link to this property</a>

cert\_serial: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20mtls_auth%20%3E%20(property)%20cert_serial">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20mtls_auth">Link to this property</a>

service\_token\_id: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20service_token_id">Link to this property</a>

service\_token\_status: optional boolean

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20service_token_status">Link to this property</a>

user\_uuid: optional string

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20user_uuid">Link to this property</a>

version: optional number

<a href="#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.users.active_sessions%20%3E%20(model)%20active_session_get_response%20%3E%20(schema)>)