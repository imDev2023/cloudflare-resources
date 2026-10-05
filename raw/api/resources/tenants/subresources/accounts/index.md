---
title: Accounts
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Tenants](https://developers.cloudflare.com/api/resources/tenants)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Accounts

##### [List tenant accounts](https://developers.cloudflare.com/api/resources/tenants/subresources/accounts/methods/list)

GET/tenants/{tenant\_id}/accounts

##### ModelsExpand Collapse

<details>

<summary>

TenantAccount object {id, created\_on, name, 3 more }

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

[Link to this property](<#(resource)%20tenants.accounts%20%3E%20(model)%20tenant_account%20%3E%20(schema)>)