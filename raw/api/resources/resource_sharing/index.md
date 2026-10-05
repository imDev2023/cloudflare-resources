---
title: Resource Sharing
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Resource Sharing

##### [List account shares](https://developers.cloudflare.com/api/resources/resource_sharing/methods/list)

GET/accounts/{account\_id}/shares

##### [Get account share by ID](https://developers.cloudflare.com/api/resources/resource_sharing/methods/get)

GET/accounts/{account\_id}/shares/{share\_id}

##### [Trigger a share creation](https://developers.cloudflare.com/api/resources/resource_sharing/methods/create)

POST/accounts/{account\_id}/shares

##### [Trigger a share rename](https://developers.cloudflare.com/api/resources/resource_sharing/methods/update)

PUT/accounts/{account\_id}/shares/{share\_id}

##### [Trigger a share deletion](https://developers.cloudflare.com/api/resources/resource_sharing/methods/delete)

DELETE/accounts/{account\_id}/shares/{share\_id}

##### ModelsExpand Collapse

<details>

<summary>

ResourceSharingListResponse object {id, account\_id, account\_name, 12 more }

</summary>

id: string

Share identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

account\_name: string

The display name of an account.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20account_name">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

name: string

The name of the share.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

organization\_id: string

Organization identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20organization_id">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target\_type: "account"or "organization"

</summary>

One of the following:

"account"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20target_type">Link to this property</a>

associated\_recipient\_count: optional number

The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20associated_recipient_count">Link to this property</a>

associating\_recipient\_count: optional number

The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20associating_recipient_count">Link to this property</a>

disassociated\_recipient\_count: optional number

The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20disassociated_recipient_count">Link to this property</a>

disassociating\_recipient\_count: optional number

The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20disassociating_recipient_count">Link to this property</a>

<details>

<summary>

kind: optional "sent"or "received"

</summary>

One of the following:

"sent"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"received"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

resources: optional array of object {id, created, meta, 6 more }

A list of resources that are part of the share. This field is only included when requested via the ‘include\_resources’ parameter.

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_list_response%20%3E%20(schema)>)

<details>

<summary>

ResourceSharingGetResponse object {id, account\_id, account\_name, 12 more }

</summary>

id: string

Share identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

account\_name: string

The display name of an account.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20account_name">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

name: string

The name of the share.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

organization\_id: string

Organization identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20organization_id">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target\_type: "account"or "organization"

</summary>

One of the following:

"account"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20target_type">Link to this property</a>

associated\_recipient\_count: optional number

The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20associated_recipient_count">Link to this property</a>

associating\_recipient\_count: optional number

The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20associating_recipient_count">Link to this property</a>

disassociated\_recipient\_count: optional number

The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20disassociated_recipient_count">Link to this property</a>

disassociating\_recipient\_count: optional number

The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20disassociating_recipient_count">Link to this property</a>

<details>

<summary>

kind: optional "sent"or "received"

</summary>

One of the following:

"sent"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"received"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

resources: optional array of object {id, created, meta, 6 more }

A list of resources that are part of the share. This field is only included when requested via the ‘include\_resources’ parameter.

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_get_response%20%3E%20(schema)>)

<details>

<summary>

ResourceSharingCreateResponse object {id, account\_id, account\_name, 12 more }

</summary>

id: string

Share identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

account\_name: string

The display name of an account.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20account_name">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

name: string

The name of the share.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

organization\_id: string

Organization identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20organization_id">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target\_type: "account"or "organization"

</summary>

One of the following:

"account"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20target_type">Link to this property</a>

associated\_recipient\_count: optional number

The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20associated_recipient_count">Link to this property</a>

associating\_recipient\_count: optional number

The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20associating_recipient_count">Link to this property</a>

disassociated\_recipient\_count: optional number

The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20disassociated_recipient_count">Link to this property</a>

disassociating\_recipient\_count: optional number

The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20disassociating_recipient_count">Link to this property</a>

<details>

<summary>

kind: optional "sent"or "received"

</summary>

One of the following:

"sent"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"received"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

resources: optional array of object {id, created, meta, 6 more }

A list of resources that are part of the share. This field is only included when requested via the ‘include\_resources’ parameter.

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_create_response%20%3E%20(schema)>)

<details>

<summary>

ResourceSharingUpdateResponse object {id, account\_id, account\_name, 12 more }

</summary>

id: string

Share identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

account\_name: string

The display name of an account.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20account_name">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

name: string

The name of the share.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

organization\_id: string

Organization identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20organization_id">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target\_type: "account"or "organization"

</summary>

One of the following:

"account"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20target_type">Link to this property</a>

associated\_recipient\_count: optional number

The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20associated_recipient_count">Link to this property</a>

associating\_recipient\_count: optional number

The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20associating_recipient_count">Link to this property</a>

disassociated\_recipient\_count: optional number

The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20disassociated_recipient_count">Link to this property</a>

disassociating\_recipient\_count: optional number

The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20disassociating_recipient_count">Link to this property</a>

<details>

<summary>

kind: optional "sent"or "received"

</summary>

One of the following:

"sent"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"received"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

resources: optional array of object {id, created, meta, 6 more }

A list of resources that are part of the share. This field is only included when requested via the ‘include\_resources’ parameter.

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_update_response%20%3E%20(schema)>)

<details>

<summary>

ResourceSharingDeleteResponse object {id, account\_id, account\_name, 12 more }

</summary>

id: string

Share identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

account\_name: string

The display name of an account.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20account_name">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

name: string

The name of the share.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

organization\_id: string

Organization identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20organization_id">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target\_type: "account"or "organization"

</summary>

One of the following:

"account"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20target_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20target_type">Link to this property</a>

associated\_recipient\_count: optional number

The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20associated_recipient_count">Link to this property</a>

associating\_recipient\_count: optional number

The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20associating_recipient_count">Link to this property</a>

disassociated\_recipient\_count: optional number

The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20disassociated_recipient_count">Link to this property</a>

disassociating\_recipient\_count: optional number

The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include\_recipient\_counts’ parameter.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20disassociating_recipient_count">Link to this property</a>

<details>

<summary>

kind: optional "sent"or "received"

</summary>

One of the following:

"sent"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"received"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

resources: optional array of object {id, created, meta, 6 more }

A list of resources that are part of the share. This field is only included when requested via the ‘include\_resources’ parameter.

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing%20%3E%20(model)%20resource_sharing_delete_response%20%3E%20(schema)>)

#### Resource SharingRecipients

##### [List share recipients by share ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/list)

GET/accounts/{account\_id}/shares/{share\_id}/recipients

##### [Get share recipient by ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/get)

GET/accounts/{account\_id}/shares/{share\_id}/recipients/{recipient\_id}

##### [Trigger a recipient addition to a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/create)

POST/accounts/{account\_id}/shares/{share\_id}/recipients

##### [Trigger a recipient removal from a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/delete)

DELETE/accounts/{account\_id}/shares/{share\_id}/recipients/{recipient\_id}

##### ModelsExpand Collapse

<details>

<summary>

RecipientListResponse object {id, account\_id, association\_status, 3 more }

A recipient of a share. The <code>association_status</code> field tracks the lifecycle of the shared resources in the recipient account. All recipients are returned by the list endpoint regardless of status; filter client-side if only active recipients are needed.

</summary>

id: string

Share Recipient identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

<details>

<summary>

association\_status: "associating"or "associated"or "disassociating"or "disassociated"

The current state of the recipient relative to the share. The <code>desired_association_status</code> (not exposed in the response) tracks the target state set by the API; the background reconciliation workflow drives <code>current_association_status</code> toward it.

- <code>associating</code> — The recipient was recently added; the workflow is pushing shared resources into the recipient account.
- <code>associated</code> — Shared resources have been successfully applied to the recipient account.
- <code>disassociating</code> — The recipient was removed (via DELETE or PUT replacement); the workflow is removing shared resources from the recipient account.
- <code>disassociated</code> — Shared resources have been removed from the recipient account. The recipient record remains in the database.

</summary>

One of the following:

"associating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%200">Link to this property</a>

"associated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%201">Link to this property</a>

"disassociating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%202">Link to this property</a>

"disassociated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20association_status">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

resources: optional array of object {error, resource\_id, resource\_version, terminal }

</summary>

error: string

Share Recipient error message.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

terminal: boolean

Whether the error is terminal or will be continually retried.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20terminal">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_list_response%20%3E%20(schema)>)

<details>

<summary>

RecipientGetResponse object {id, account\_id, association\_status, 3 more }

A recipient of a share. The <code>association_status</code> field tracks the lifecycle of the shared resources in the recipient account. All recipients are returned by the list endpoint regardless of status; filter client-side if only active recipients are needed.

</summary>

id: string

Share Recipient identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

<details>

<summary>

association\_status: "associating"or "associated"or "disassociating"or "disassociated"

The current state of the recipient relative to the share. The <code>desired_association_status</code> (not exposed in the response) tracks the target state set by the API; the background reconciliation workflow drives <code>current_association_status</code> toward it.

- <code>associating</code> — The recipient was recently added; the workflow is pushing shared resources into the recipient account.
- <code>associated</code> — Shared resources have been successfully applied to the recipient account.
- <code>disassociating</code> — The recipient was removed (via DELETE or PUT replacement); the workflow is removing shared resources from the recipient account.
- <code>disassociated</code> — Shared resources have been removed from the recipient account. The recipient record remains in the database.

</summary>

One of the following:

"associating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%200">Link to this property</a>

"associated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%201">Link to this property</a>

"disassociating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%202">Link to this property</a>

"disassociated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20association_status">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

resources: optional array of object {error, resource\_id, resource\_version, terminal }

</summary>

error: string

Share Recipient error message.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

terminal: boolean

Whether the error is terminal or will be continually retried.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20terminal">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_get_response%20%3E%20(schema)>)

<details>

<summary>

RecipientCreateResponse object {id, account\_id, association\_status, 3 more }

A recipient of a share. The <code>association_status</code> field tracks the lifecycle of the shared resources in the recipient account. All recipients are returned by the list endpoint regardless of status; filter client-side if only active recipients are needed.

</summary>

id: string

Share Recipient identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

<details>

<summary>

association\_status: "associating"or "associated"or "disassociating"or "disassociated"

The current state of the recipient relative to the share. The <code>desired_association_status</code> (not exposed in the response) tracks the target state set by the API; the background reconciliation workflow drives <code>current_association_status</code> toward it.

- <code>associating</code> — The recipient was recently added; the workflow is pushing shared resources into the recipient account.
- <code>associated</code> — Shared resources have been successfully applied to the recipient account.
- <code>disassociating</code> — The recipient was removed (via DELETE or PUT replacement); the workflow is removing shared resources from the recipient account.
- <code>disassociated</code> — Shared resources have been removed from the recipient account. The recipient record remains in the database.

</summary>

One of the following:

"associating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%200">Link to this property</a>

"associated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%201">Link to this property</a>

"disassociating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%202">Link to this property</a>

"disassociated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20association_status">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

resources: optional array of object {error, resource\_id, resource\_version, terminal }

</summary>

error: string

Share Recipient error message.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

terminal: boolean

Whether the error is terminal or will be continually retried.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20terminal">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_create_response%20%3E%20(schema)>)

<details>

<summary>

RecipientDeleteResponse object {id, account\_id, association\_status, 3 more }

A recipient of a share. The <code>association_status</code> field tracks the lifecycle of the shared resources in the recipient account. All recipients are returned by the list endpoint regardless of status; filter client-side if only active recipients are needed.

</summary>

id: string

Share Recipient identifier tag.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

<details>

<summary>

association\_status: "associating"or "associated"or "disassociating"or "disassociated"

The current state of the recipient relative to the share. The <code>desired_association_status</code> (not exposed in the response) tracks the target state set by the API; the background reconciliation workflow drives <code>current_association_status</code> toward it.

- <code>associating</code> — The recipient was recently added; the workflow is pushing shared resources into the recipient account.
- <code>associated</code> — Shared resources have been successfully applied to the recipient account.
- <code>disassociating</code> — The recipient was removed (via DELETE or PUT replacement); the workflow is removing shared resources from the recipient account.
- <code>disassociated</code> — Shared resources have been removed from the recipient account. The recipient record remains in the database.

</summary>

One of the following:

"associating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%200">Link to this property</a>

"associated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%201">Link to this property</a>

"disassociating"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%202">Link to this property</a>

"disassociated"

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20association_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20association_status">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

resources: optional array of object {error, resource\_id, resource\_version, terminal }

</summary>

error: string

Share Recipient error message.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20resource_version">Link to this property</a>

terminal: boolean

Whether the error is terminal or will be continually retried.

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(items)%20%3E%20(property)%20terminal">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.recipients%20%3E%20(model)%20recipient_delete_response%20%3E%20(schema)>)

#### Resource SharingResources

##### [List share resources by share ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/list)

GET/accounts/{account\_id}/shares/{share\_id}/resources

##### [Get share resource by ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/get)

GET/accounts/{account\_id}/shares/{share\_id}/resources/{share\_resource\_id}

##### [Trigger a resource addition to a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/create)

POST/accounts/{account\_id}/shares/{share\_id}/resources

##### [Trigger a resource metadata update in a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/update)

PUT/accounts/{account\_id}/shares/{share\_id}/resources/{share\_resource\_id}

##### [Trigger a resource deletion from a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/delete)

DELETE/accounts/{account\_id}/shares/{share\_id}/resources/{share\_resource\_id}

##### ModelsExpand Collapse

<details>

<summary>

ResourceListResponse object {id, created, meta, 6 more }

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)>)

<details>

<summary>

ResourceGetResponse object {id, created, meta, 6 more }

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)>)

<details>

<summary>

ResourceCreateResponse object {id, created, meta, 6 more }

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_create_response%20%3E%20(schema)>)

<details>

<summary>

ResourceUpdateResponse object {id, created, meta, 6 more }

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_update_response%20%3E%20(schema)>)

<details>

<summary>

ResourceDeleteResponse object {id, created, meta, 6 more }

</summary>

id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created: string

When the share was created.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

meta: unknown

Resource Metadata.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

modified: string

When the share was modified.

formatdate-time

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

resource\_account\_id: string

Account identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_account_id">Link to this property</a>

resource\_id: string

Share Resource identifier.

maxLength32

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_id">Link to this property</a>

<details>

<summary>

resource\_type: "custom-ruleset"or "gateway-policy"or "gateway-destination-ip"or 4 more

Resource Type.

</summary>

One of the following:

"custom-ruleset"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"gateway-policy"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"gateway-destination-ip"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"gateway-block-page-settings"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"gateway-extended-email-matching"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"idp-federation-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"trust-grant"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

resource\_version: number

Resource Version.

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20resource_version">Link to this property</a>

<details>

<summary>

status: "active"or "deleting"or "deleted"

Resource Status.

</summary>

One of the following:

"active"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"deleting"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20resource_sharing.resources%20%3E%20(model)%20resource_delete_response%20%3E%20(schema)>)