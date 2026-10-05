---
title: Organizations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Organizations

##### [List organizations the user has access to](https://developers.cloudflare.com/api/resources/organizations/methods/list)

GET/organizations

##### [Get organization](https://developers.cloudflare.com/api/resources/organizations/methods/get)

GET/organizations/{organization\_id}

##### [Create organization](https://developers.cloudflare.com/api/resources/organizations/methods/create)

POST/organizations

##### [Update organization](https://developers.cloudflare.com/api/resources/organizations/methods/update)

PUT/organizations/{organization\_id}

##### [Delete organization](https://developers.cloudflare.com/api/resources/organizations/methods/delete)

DELETE/organizations/{organization\_id}

##### ModelsExpand Collapse

<details>

<summary>

Organization object {id, create\_time, meta, 3 more }

References an Organization in the Cloudflare data model.

</summary>

id: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

create\_time: string

formatdate-time

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20create_time">Link to this property</a>

<details>

<summary>

meta: object {hierarchy\_tags, managed\_by, tenant\_flags }

</summary>

hierarchy\_tags: optional array of string

Ordered chain of organization tags from the root organization down to (and including) this organization itself. Root organizations return a single-element array containing their own tag; sub-organizations return <code>[rootTag, ...intermediateTags, parentTag, selfTag]</code>. Useful for constructing authorization scopes that need to cover every ancestor in the hierarchy.

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20hierarchy_tags">Link to this property</a>

managed\_by: optional string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20managed_by">Link to this property</a>

<details>

<summary>

tenant\_flags: optional object {account\_creation, account\_creation\_applies\_tenant\_defaults, account\_deletion, 5 more }

Enable features for Organizations.

</summary>

account\_creation: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20account_creation">Link to this property</a>

account\_creation\_applies\_tenant\_defaults: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20account_creation_applies_tenant_defaults">Link to this property</a>

account\_deletion: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20account_deletion">Link to this property</a>

account\_migration: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20account_migration">Link to this property</a>

account\_mobility: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20account_mobility">Link to this property</a>

enterprise\_capability: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20enterprise_capability">Link to this property</a>

member\_management: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20member_management">Link to this property</a>

sub\_org\_creation: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags%20%3E%20(property)%20sub_org_creation">Link to this property</a>

</details>

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20tenant_flags">Link to this property</a>

</details>

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

name: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

parent: optional object {id, name }

</summary>

id: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20parent%20%3E%20(property)%20id">Link to this property</a>

name: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20parent%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20parent">Link to this property</a>

profile: optional <a href="https://developers.cloudflare.com/api/resources/accounts#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)">AccountProfile</a> { business\_address, business\_email, business\_name, 2 more }

<a href="#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)%20%3E%20(property)%20profile">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations%20%3E%20(model)%20organization%20%3E%20(schema)>)

<details>

<summary>

OrganizationDeleteResponse object {id }

</summary>

id: string

<a href="#(resource)%20organizations%20%3E%20(model)%20organization_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations%20%3E%20(model)%20organization_delete_response%20%3E%20(schema)>)

#### OrganizationsOrganization Accounts

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

#### OrganizationsOrganization Profile

##### [Get organization profile](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_profile/methods/get)

GET/organizations/{organization\_id}/profile

##### [Modify organization profile.](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_profile/methods/update)

PUT/organizations/{organization\_id}/profile

##### ModelsExpand Collapse

<details>

<summary>

OrganizationProfile object {business\_address, business\_email, business\_name, 2 more }

</summary>

business\_address: string

<a href="#(resource)%20organizations.organization_profile%20%3E%20(model)%20organization_profile%20%3E%20(schema)%20%3E%20(property)%20business_address">Link to this property</a>

business\_email: string

<a href="#(resource)%20organizations.organization_profile%20%3E%20(model)%20organization_profile%20%3E%20(schema)%20%3E%20(property)%20business_email">Link to this property</a>

business\_name: string

<a href="#(resource)%20organizations.organization_profile%20%3E%20(model)%20organization_profile%20%3E%20(schema)%20%3E%20(property)%20business_name">Link to this property</a>

business\_phone: string

<a href="#(resource)%20organizations.organization_profile%20%3E%20(model)%20organization_profile%20%3E%20(schema)%20%3E%20(property)%20business_phone">Link to this property</a>

external\_metadata: string

<a href="#(resource)%20organizations.organization_profile%20%3E%20(model)%20organization_profile%20%3E%20(schema)%20%3E%20(property)%20external_metadata">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.organization_profile%20%3E%20(model)%20organization_profile%20%3E%20(schema)>)

#### OrganizationsMembers

##### [List organization members](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/list)

GET/organizations/{organization\_id}/members

##### [Get organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/get)

GET/organizations/{organization\_id}/members/{member\_id}

##### [Create organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/create)

POST/organizations/{organization\_id}/members

##### [Delete organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/delete)

DELETE/organizations/{organization\_id}/members/{member\_id}

##### ModelsExpand Collapse

<details>

<summary>

OrganizationMember object {id, create\_time, meta, 3 more }

</summary>

id: string

Organization Member ID

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

create\_time: string

formatdate-time

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20create_time">Link to this property</a>

meta: map\[unknown]

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

status: "active"or "pending"or "rejected"or "canceled"

</summary>

One of the following:

"active"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"rejected"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"canceled"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

update\_time: string

formatdate-time

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20update_time">Link to this property</a>

<details>

<summary>

user: object {id, email, name, two\_factor\_authentication\_enabled }

</summary>

id: string

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20id">Link to this property</a>

email: string

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20email">Link to this property</a>

name: string

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20name">Link to this property</a>

two\_factor\_authentication\_enabled: boolean

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20two_factor_authentication_enabled">Link to this property</a>

</details>

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)>)

#### OrganizationsLogs

#### OrganizationsLogsAudit

##### [Get organization audit logs (Version 2)](https://developers.cloudflare.com/api/resources/organizations/subresources/logs/subresources/audit/methods/list)

GET/organizations/{organization\_id}/logs/audit

##### [Get resource change history from an organization audit log entry (Version 2)](https://developers.cloudflare.com/api/resources/organizations/subresources/logs/subresources/audit/methods/history)

GET/organizations/{organization\_id}/logs/audit/{id}/history

##### ModelsExpand Collapse

<details>

<summary>

AuditListResponse object {id, action, actor, 3 more }

</summary>

id: optional string

A unique identifier for the audit log entry.

maxLength32

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

action: optional object {description, result, time, type }

Provides information about the action performed.

</summary>

description: optional string

A short description of the action performed.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20description">Link to this property</a>

result: optional string

The result of the action, indicating success or failure.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20result">Link to this property</a>

time: optional string

A timestamp indicating when the action was logged.

formatdate-time

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20time">Link to this property</a>

type: optional string

A short string that describes the action that was performed.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

actor: optional object {id, context, email, 4 more }

Provides details about the actor who performed the action.

</summary>

id: optional string

The ID of the actor who performed the action. If a user performed the action, this will be their User ID.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

context: optional "api"or "api\_key"or "api\_token"or 3 more

The context in which the action was initiated.

- <code>api</code>: The action was performed through the API. The specific credential type was not recorded.
- <code>api_key</code>: The action was authenticated with a Cloudflare Global API Key.
- <code>api_token</code>: The action was authenticated with an API token.
- <code>dash</code>: The action was performed through the Cloudflare dashboard.
- <code>oauth</code>: The action was authenticated with an OAuth token.
- <code>origin_ca_key</code>: The action was authenticated with an Origin CA key.

</summary>

One of the following:

"api"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%200">Link to this property</a>

"api\_key"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%201">Link to this property</a>

"api\_token"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%202">Link to this property</a>

"dash"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%203">Link to this property</a>

"oauth"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%204">Link to this property</a>

"origin\_ca\_key"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context">Link to this property</a>

email: optional string

The email of the actor who performed the action.

formatemail

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20email">Link to this property</a>

ip\_address: optional string

The IP address of the request that performed the action.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20ip_address">Link to this property</a>

token\_id: optional string

The API token ID when the actor context is an api\_token or oauth.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20token_id">Link to this property</a>

token\_name: optional string

The API token name when the actor context is an api\_token or oauth.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20token_name">Link to this property</a>

<details>

<summary>

type: optional "cloudflare\_admin"or "system"or "user"

The type of actor.

</summary>

One of the following:

"cloudflare\_admin"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"system"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"user"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor">Link to this property</a>

<details>

<summary>

organization: optional object {id }

Contains organization related information.

</summary>

id: optional string

A unique identifier for the organization.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20organization%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20organization">Link to this property</a>

<details>

<summary>

raw: optional object {cf\_ray\_id, method, status\_code, 2 more }

Provides raw information about the request and response.

</summary>

cf\_ray\_id: optional string

The Cloudflare Ray ID for the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20cf_ray_id">Link to this property</a>

method: optional string

The HTTP method of the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20method">Link to this property</a>

status\_code: optional number

The HTTP response status code returned by the API.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20status_code">Link to this property</a>

uri: optional string

The URI of the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20uri">Link to this property</a>

user\_agent: optional string

The client’s user agent string sent with the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20user_agent">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw">Link to this property</a>

<details>

<summary>

resource: optional object {id, product, request, 3 more }

Provides details about the affected resource.

</summary>

id: optional string

The unique identifier for the affected resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20id">Link to this property</a>

product: optional string

The Cloudflare product associated with the resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20product">Link to this property</a>

request: optional unknown

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20request">Link to this property</a>

response: optional unknown

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20response">Link to this property</a>

scope: optional unknown

The scope of the resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20scope">Link to this property</a>

type: optional string

The type of the resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)>)

<details>

<summary>

AuditHistoryResponse = array of object {id, action, actor, 3 more }

</summary>

id: optional string

A unique identifier for the audit log entry.

maxLength32

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

action: optional object {description, result, time, type }

Provides information about the action performed.

</summary>

description: optional string

A short description of the action performed.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20description">Link to this property</a>

result: optional string

The result of the action, indicating success or failure.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20result">Link to this property</a>

time: optional string

A timestamp indicating when the action was logged.

formatdate-time

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20time">Link to this property</a>

type: optional string

A short string that describes the action that was performed.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

actor: optional object {id, context, email, 4 more }

Provides details about the actor who performed the action.

</summary>

id: optional string

The ID of the actor who performed the action. If a user performed the action, this will be their User ID.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

context: optional "api"or "api\_key"or "api\_token"or 3 more

The context in which the action was initiated.

- <code>api</code>: The action was performed through the API. The specific credential type was not recorded.
- <code>api_key</code>: The action was authenticated with a Cloudflare Global API Key.
- <code>api_token</code>: The action was authenticated with an API token.
- <code>dash</code>: The action was performed through the Cloudflare dashboard.
- <code>oauth</code>: The action was authenticated with an OAuth token.
- <code>origin_ca_key</code>: The action was authenticated with an Origin CA key.

</summary>

One of the following:

"api"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%200">Link to this property</a>

"api\_key"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%201">Link to this property</a>

"api\_token"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%202">Link to this property</a>

"dash"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%203">Link to this property</a>

"oauth"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%204">Link to this property</a>

"origin\_ca\_key"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context">Link to this property</a>

email: optional string

The email of the actor who performed the action.

formatemail

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20email">Link to this property</a>

ip\_address: optional string

The IP address of the request that performed the action.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20ip_address">Link to this property</a>

token\_id: optional string

The API token ID when the actor context is an api\_token or oauth.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20token_id">Link to this property</a>

token\_name: optional string

The API token name when the actor context is an api\_token or oauth.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20token_name">Link to this property</a>

<details>

<summary>

type: optional "cloudflare\_admin"or "system"or "user"

The type of actor.

</summary>

One of the following:

"cloudflare\_admin"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"system"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"user"

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor">Link to this property</a>

<details>

<summary>

organization: optional object {id }

Contains organization related information.

</summary>

id: optional string

A unique identifier for the organization.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20organization%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20organization">Link to this property</a>

<details>

<summary>

raw: optional object {cf\_ray\_id, method, status\_code, 2 more }

Provides raw information about the request and response.

</summary>

cf\_ray\_id: optional string

The Cloudflare Ray ID for the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20cf_ray_id">Link to this property</a>

method: optional string

The HTTP method of the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20method">Link to this property</a>

status\_code: optional number

The HTTP response status code returned by the API.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20status_code">Link to this property</a>

uri: optional string

The URI of the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20uri">Link to this property</a>

user\_agent: optional string

The client’s user agent string sent with the request.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20user_agent">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw">Link to this property</a>

<details>

<summary>

resource: optional object {id, product, request, 3 more }

Provides details about the affected resource.

</summary>

id: optional string

The unique identifier for the affected resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20id">Link to this property</a>

product: optional string

The Cloudflare product associated with the resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20product">Link to this property</a>

request: optional unknown

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20request">Link to this property</a>

response: optional unknown

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20response">Link to this property</a>

scope: optional unknown

The scope of the resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20scope">Link to this property</a>

type: optional string

The type of the resource.

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)>)

#### OrganizationsBilling

#### OrganizationsBillingUsage

##### [Get Organization Usage (Version 2, Alpha, Restricted)](https://developers.cloudflare.com/api/resources/organizations/subresources/billing/subresources/usage/methods/get)

GET/organizations/{organization\_id}/billable/usage

##### ModelsExpand Collapse

<details>

<summary>

UsageGetResponse = array of object {ChargeCategory, ChargeDescription, ChargeFrequency, 33 more }

Contains the array of cost and usage records.

</summary>

ChargeCategory: "Usage"

Highest-level classification of a charge based on the nature of how it gets billed. Currently only “Usage” is supported.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeCategory">Link to this property</a>

ChargeDescription: string

Self-contained summary of the charge’s purpose and price.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeDescription">Link to this property</a>

ChargeFrequency: "Usage-Based"

Indicates how often a charge occurs. Currently only “Usage-Based” is supported.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeFrequency">Link to this property</a>

ChargePeriodEnd: string

Exclusive end of the time interval during which the usage was consumed.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargePeriodEnd">Link to this property</a>

ChargePeriodStart: string

Inclusive start of the time interval during which the usage was consumed.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargePeriodStart">Link to this property</a>

ConsumedQuantity: number

Measured usage amount within the charge period. Reflects raw metered consumption before pricing transformations.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ConsumedQuantity">Link to this property</a>

ConsumedUnit: string

Unit of measure for the consumed quantity (e.g., “GB”, “Requests”, “vCPU-Hours”).

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ConsumedUnit">Link to this property</a>

HostProviderName: string

Name of the entity providing the underlying infrastructure or platform.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20HostProviderName">Link to this property</a>

InvoiceIssuerName: string

Name of the entity responsible for invoicing for the services consumed.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20InvoiceIssuerName">Link to this property</a>

ServiceProviderName: string

Name of the entity that made the services available for purchase.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ServiceProviderName">Link to this property</a>

x\_BillableMetricId: string

The unique identifier for the billable metric in the Cloudflare catalog. Cloudflare extension; replaces FOCUS SkuId.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_BillableMetricId">Link to this property</a>

BilledCost: optional number

A charge serving as the basis for invoicing, inclusive of all reduced rates and discounts while excluding the amortization of upfront charges (one-time or recurring).

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BilledCost">Link to this property</a>

BillingAccountId: optional string

Public identifier of the Cloudflare account (account tag). Omitted when account is not part of the requested grouping, and always omitted for usage measured at contract level, even when grouping by account: that usage is returned as its own record with no account.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingAccountId">Link to this property</a>

BillingAccountName: optional string

Display name of the Cloudflare account. Omitted when account is not part of the requested grouping, and for usage measured at contract level.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingAccountName">Link to this property</a>

BillingCurrency: optional string

Currency that a charge was billed in (ISO 4217).

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingCurrency">Link to this property</a>

BillingPeriodEnd: optional string

Exclusive end of the billing cycle that contains this usage record.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingPeriodEnd">Link to this property</a>

BillingPeriodStart: optional string

Inclusive start of the billing cycle that contains this usage record.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingPeriodStart">Link to this property</a>

ChargeClass: optional "Correction"

Indicates whether the row represents a correction to one or more charges invoiced in a previous billing period.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeClass">Link to this property</a>

ContractedCost: optional number

Cost calculated by multiplying ContractedUnitPrice and the corresponding PricingQuantity.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ContractedCost">Link to this property</a>

ContractedUnitPrice: optional number

The agreed-upon unit price for a single PricingUnit of the associated billable metric, inclusive of negotiated discounts, if present, while excluding any other discounts.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ContractedUnitPrice">Link to this property</a>

EffectiveCost: optional number

The amortized cost of the charge after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered the charge.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20EffectiveCost">Link to this property</a>

ListCost: optional number

Cost calculated by multiplying ListUnitPrice and the corresponding PricingQuantity.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ListCost">Link to this property</a>

ListUnitPrice: optional number

Suggested provider-published unit price for a single PricingUnit of the associated billable metric, exclusive of any discounts.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ListUnitPrice">Link to this property</a>

PricingQuantity: optional number

Volume of a given service used or purchased, based on the PricingUnit.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20PricingQuantity">Link to this property</a>

PricingUnit: optional string

Provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage after applying pricing rules like block pricing.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20PricingUnit">Link to this property</a>

RegionId: optional string

Provider-assigned identifier for an isolated geographic area where a service is provided.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20RegionId">Link to this property</a>

RegionName: optional string

Name of an isolated geographic area where a service is provided.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20RegionName">Link to this property</a>

SubAccountId: optional string

Unique identifier assigned to a grouping of services. For Cloudflare, this is the subscription or contract ID.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20SubAccountId">Link to this property</a>

SubAccountName: optional string

Name assigned to a grouping of services. For Cloudflare, this is the subscription or contract display name.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20SubAccountName">Link to this property</a>

<details>

<summary>

Tags: optional map\[stringor true]

Tag values for the requested <code>GroupBy</code> keys. Omitted when <code>GroupBy</code> is not provided. Missing keys are omitted, and key-only tags are returned as boolean <code>true</code>. All other tag values are strings.

</summary>

One of the following:

string

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20Tags%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

true

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20Tags%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20Tags">Link to this property</a>

x\_BillableMetricName: optional string

The display name of the billable metric. Cloudflare extension; replaces FOCUS SkuMeter.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_BillableMetricName">Link to this property</a>

x\_ProductCategoryName: optional string

The product category the charge belongs to (e.g., “Developer”, “Cloudflare One”). Cloudflare extension; replaces FOCUS ServiceCategory.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ProductCategoryName">Link to this property</a>

x\_ProductFamilyId: optional string

The unique identifier for the product family in the Cloudflare catalog. Cloudflare extension; replaces FOCUS ServiceId.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ProductFamilyId">Link to this property</a>

x\_ProductFamilyName: optional string

The product family the charge belongs to (e.g., “R2”, “Workers”). Cloudflare extension; replaces FOCUS ServiceName.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ProductFamilyName">Link to this property</a>

x\_ZoneId: optional string

The identifier for the Cloudflare zone (zone tag). Omitted when zone is not part of the requested grouping, and always omitted for usage measured at contract level, even when grouping by zone. Cloudflare extension.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ZoneId">Link to this property</a>

x\_ZoneName: optional string

The display name of the Cloudflare zone. Omitted when zone is not part of the requested grouping, and for usage measured at contract level. Cloudflare extension.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ZoneName">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)>)