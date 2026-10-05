---
title: Organization Accounts
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Organizations](https://developers.cloudflare.com/api/resources/organizations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Organization Accounts

##### [List organization accounts](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_accounts/methods/get)

GET/organizations/{organization\_id}/accounts

##### ModelsExpand Collapse

<details>

<summary>

OrganizationAccounts object {id, name, type, 3 more }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: string

Account name

maxLength100

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: "standard"or "enterprise"

</summary>

One of the following:

"standard"

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"enterprise"

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

created\_on: optional string

Timestamp for the creation of the account

formatdate-time

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

<details>

<summary>

managed\_by: optional object {parent\_org\_id, parent\_org\_name }

Parent container details

</summary>

parent\_org\_id: optional string

ID of the parent Organization, if one exists

maxLength32

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(property)%20parent_org_id">Link to this property</a>

parent\_org\_name: optional string

Name of the parent Organization, if one exists

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(property)%20parent_org_name">Link to this property</a>

</details>

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20managed_by">Link to this property</a>

<details>

<summary>

settings: optional object {abuse\_contact\_email, enforce\_twofactor }

Account settings

</summary>

abuse\_contact\_email: optional string

Sets an abuse contact email to notify for abuse reports.

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20abuse_contact_email">Link to this property</a>

enforce\_twofactor: optional boolean

Indicates whether membership in this account requires that Two-Factor Authentication is enabled

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20enforce_twofactor">Link to this property</a>

</details>

<a href="#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)%20%3E%20(property)%20settings">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_accounts%20%3E%20(schema)>)

<details>

<summary>

OrganizationAccountGetResponse = array of <a href="https://developers.cloudflare.com/api/resources/tenants#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)">TenantAccount</a> { id, created\_on, name, 3 more }

</summary>

id: string

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

name: string

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

settings: object {abuse\_contact\_email, access\_approval\_expiry, api\_access\_enabled, 3 more }

</summary>

abuse\_contact\_email: string

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20abuse_contact_email">Link to this property</a>

access\_approval\_expiry: string

formatdate-time

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20access_approval_expiry">Link to this property</a>

api\_access\_enabled: boolean

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20api_access_enabled">Link to this property</a>

Deprecateddefault\_nameservers: string

Use <a href="https://developers.cloudflare.com/api/operations/dns-settings-for-an-account-list-dns-settings">DNS Settings</a> instead. Deprecated.

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20default_nameservers">Link to this property</a>

enforce\_twofactor: boolean

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20enforce_twofactor">Link to this property</a>

Deprecateduse\_account\_custom\_ns\_by\_default: boolean

Use <a href="https://developers.cloudflare.com/api/operations/dns-settings-for-an-account-list-dns-settings">DNS Settings</a> instead. Deprecated.

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20use_account_custom_ns_by_default">Link to this property</a>

</details>

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20settings">Link to this property</a>

<details>

<summary>

type: "standard"or "enterprise"

</summary>

One of the following:

"standard"

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"enterprise"

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

tags: optional map\[string]

Account tags, present only when <code>include_tags=true</code> is requested.

<a href="#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.organization_accounts%20%3E%20(model)%20organization_account_get_response%20%3E%20(schema)>)