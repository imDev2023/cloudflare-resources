---
title: Accounts
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Accounts

##### [List Accounts](https://developers.cloudflare.com/api/resources/accounts/methods/list)

GET/accounts

##### [Account Details](https://developers.cloudflare.com/api/resources/accounts/methods/get)

GET/accounts/{account\_id}

##### [Create an Account](https://developers.cloudflare.com/api/resources/accounts/methods/create)

POST/accounts

##### [Update Account](https://developers.cloudflare.com/api/resources/accounts/methods/update)

PUT/accounts/{account\_id}

##### [Delete a specific account](https://developers.cloudflare.com/api/resources/accounts/methods/delete)

DELETE/accounts/{account\_id}

##### ModelsExpand Collapse

<details>

<summary>

Account object {id, name, type, 3 more }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

name: string

Account name

maxLength100

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: "standard"or "enterprise"

</summary>

One of the following:

"standard"

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"enterprise"

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

created\_on: optional string

Timestamp for the creation of the account

formatdate-time

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

<details>

<summary>

managed\_by: optional object {parent\_org\_id, parent\_org\_name }

Parent container details

</summary>

parent\_org\_id: optional string

ID of the parent Organization, if one exists

maxLength32

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(property)%20parent_org_id">Link to this property</a>

parent\_org\_name: optional string

Name of the parent Organization, if one exists

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(property)%20parent_org_name">Link to this property</a>

</details>

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20managed_by">Link to this property</a>

<details>

<summary>

settings: optional object {abuse\_contact\_email, enforce\_twofactor }

Account settings

</summary>

abuse\_contact\_email: optional string

Sets an abuse contact email to notify for abuse reports.

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20abuse_contact_email">Link to this property</a>

enforce\_twofactor: optional boolean

Indicates whether membership in this account requires that Two-Factor Authentication is enabled

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20enforce_twofactor">Link to this property</a>

</details>

<a href="#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)%20%3E%20(property)%20settings">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts%20%3E%20(model)%20account%20%3E%20(schema)>)

<details>

<summary>

AccountDeleteResponse object {id }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20accounts%20%3E%20(model)%20account_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts%20%3E%20(model)%20account_delete_response%20%3E%20(schema)>)

#### AccountsAccount Organizations

##### [Move account to organization](https://developers.cloudflare.com/api/resources/accounts/subresources/account_organizations/methods/create)

POST/accounts/{account\_id}/move

##### ModelsExpand Collapse

<details>

<summary>

AccountOrganizationCreateResponse object {account\_id, destination\_organization\_id, source\_organization\_id }

</summary>

account\_id: string

<a href="#(resource)%20accounts.account_organizations%20%3E%20(model)%20account_organization_create_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

destination\_organization\_id: string

<a href="#(resource)%20accounts.account_organizations%20%3E%20(model)%20account_organization_create_response%20%3E%20(schema)%20%3E%20(property)%20destination_organization_id">Link to this property</a>

source\_organization\_id: string

<a href="#(resource)%20accounts.account_organizations%20%3E%20(model)%20account_organization_create_response%20%3E%20(schema)%20%3E%20(property)%20source_organization_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.account_organizations%20%3E%20(model)%20account_organization_create_response%20%3E%20(schema)>)

#### AccountsAccount Profile

##### [Get account profile](https://developers.cloudflare.com/api/resources/accounts/subresources/account_profile/methods/get)

GET/accounts/{account\_id}/profile

##### [Update account profile](https://developers.cloudflare.com/api/resources/accounts/subresources/account_profile/methods/update)

PUT/accounts/{account\_id}/profile

##### ModelsExpand Collapse

<details>

<summary>

AccountProfile object {business\_address, business\_email, business\_name, 2 more }

</summary>

business\_address: string

<a href="#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)%20%3E%20(property)%20business_address">Link to this property</a>

business\_email: string

<a href="#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)%20%3E%20(property)%20business_email">Link to this property</a>

business\_name: string

<a href="#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)%20%3E%20(property)%20business_name">Link to this property</a>

business\_phone: string

<a href="#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)%20%3E%20(property)%20business_phone">Link to this property</a>

external\_metadata: string

<a href="#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)%20%3E%20(property)%20external_metadata">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.account_profile%20%3E%20(model)%20account_profile%20%3E%20(schema)>)

#### AccountsMembers

##### [List Members](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/list)

GET/accounts/{account\_id}/members

##### [Member Details](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/get)

GET/accounts/{account\_id}/members/{member\_id}

##### [Add Member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/create)

POST/accounts/{account\_id}/members

##### [Update Member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/update)

PUT/accounts/{account\_id}/members/{member\_id}

##### [Remove Member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/delete)

DELETE/accounts/{account\_id}/members/{member\_id}

##### ModelsExpand Collapse

<details>

<summary>

Status = "member"or "invited"

Whether the user is a member of the organization or has an invitation pending.

</summary>

One of the following:

"member"

<a href="#(resource)%20accounts.members%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"invited"

<a href="#(resource)%20accounts.members%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.members%20%3E%20(model)%20status%20%3E%20(schema)>)

<details>

<summary>

MemberDeleteResponse object {id }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20accounts.members%20%3E%20(model)%20member_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.members%20%3E%20(model)%20member_delete_response%20%3E%20(schema)>)

#### AccountsRoles

##### [List Roles](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/methods/list)

Deprecated

GET/accounts/{account\_id}/roles

##### [Role Details](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/methods/get)

Deprecated

GET/accounts/{account\_id}/roles/{role\_id}

#### AccountsSubscriptions

##### [List Subscriptions](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/get)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/subscriptions

##### [Get Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/get_by_identifier)

GET/accounts/{account\_id}/subscriptions/{subscription\_identifier}

##### [Create Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/create)

POST/{accounts\_or\_zones}/{account\_or\_zone\_id}/subscriptions

##### [Update Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/update)

PUT/accounts/{account\_id}/subscriptions/{subscription\_identifier}

##### [Delete Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/delete)

DELETE/accounts/{account\_id}/subscriptions/{subscription\_identifier}

##### [Cancel Delayed Downgrade](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/cancel_downgrade)

POST/accounts/{account\_id}/subscriptions/cancel-downgrade

##### ModelsExpand Collapse

<details>

<summary>

SubscriptionDeleteResponse object {subscription\_id }

</summary>

subscription\_id: optional string

Subscription identifier tag.

maxLength32

<a href="#(resource)%20accounts.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20subscription_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)>)

<details>

<summary>

SubscriptionCancelDowngradeResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20accounts.subscriptions%20%3E%20(model)%20subscription_cancel_downgrade_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20accounts.subscriptions%20%3E%20(model)%20subscription_cancel_downgrade_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.subscriptions%20%3E%20(model)%20subscription_cancel_downgrade_response%20%3E%20(schema)>)

#### AccountsSubscriptionsCancel Reason

##### [Create Cancel Reason](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/cancel_reason/methods/create)

POST/accounts/{account\_id}/subscriptions/{subscription\_identifier}/cancel-reason

##### [Get Cancel Reason](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/cancel_reason/methods/get)

GET/accounts/{account\_id}/subscriptions/{subscription\_identifier}/cancel-reason

##### ModelsExpand Collapse

<details>

<summary>

CancelReasonCreateResponse object {id, other, reason\_code, 2 more }

</summary>

id: optional string

The cancel reason identifier.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

other: optional string

Additional cancellation details.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_create_response%20%3E%20(schema)%20%3E%20(property)%20other">Link to this property</a>

reason\_code: optional array of string

The cancellation reason codes.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_create_response%20%3E%20(schema)%20%3E%20(property)%20reason_code">Link to this property</a>

submitted: optional string

When the cancel reason was submitted.

formatdate-time

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_create_response%20%3E%20(schema)%20%3E%20(property)%20submitted">Link to this property</a>

subscription\_id: optional string

The subscription identifier.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_create_response%20%3E%20(schema)%20%3E%20(property)%20subscription_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_create_response%20%3E%20(schema)>)

<details>

<summary>

CancelReasonGetResponse object {id, other, reason\_code, 2 more }

</summary>

id: optional string

The cancel reason identifier.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

other: optional string

Additional cancellation details.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_get_response%20%3E%20(schema)%20%3E%20(property)%20other">Link to this property</a>

reason\_code: optional array of string

The cancellation reason codes.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_get_response%20%3E%20(schema)%20%3E%20(property)%20reason_code">Link to this property</a>

submitted: optional string

When the cancel reason was submitted.

formatdate-time

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_get_response%20%3E%20(schema)%20%3E%20(property)%20submitted">Link to this property</a>

subscription\_id: optional string

The subscription identifier.

<a href="#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_get_response%20%3E%20(schema)%20%3E%20(property)%20subscription_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.subscriptions.cancel_reason%20%3E%20(model)%20cancel_reason_get_response%20%3E%20(schema)>)

#### AccountsSubscriptionsActions

##### [Append Subscription Action](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/actions/methods/append)

POST/accounts/{account\_id}/subscriptions/{subscription\_identifier}/action/append

#### AccountsSubscriptionsBulk

##### [Create Subscriptions](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/bulk/methods/create)

POST/accounts/{account\_id}/bulk/subscriptions

##### ModelsExpand Collapse

BulkCreateResponse = array of unknown

[Link to this property](<#(resource)%20accounts.subscriptions.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)>)

#### AccountsTokens

##### [List Tokens](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/list)

GET/accounts/{account\_id}/tokens

##### [Token Details](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/get)

GET/accounts/{account\_id}/tokens/{token\_id}

##### [Create Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/create)

POST/accounts/{account\_id}/tokens

##### [Update Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/update)

PUT/accounts/{account\_id}/tokens/{token\_id}

##### [Delete Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/delete)

DELETE/accounts/{account\_id}/tokens/{token\_id}

##### [Verify Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/verify)

GET/accounts/{account\_id}/tokens/verify

##### ModelsExpand Collapse

<details>

<summary>

TokenCreateResponse object {id, condition, creator\_email\_at\_creation, 11 more }

</summary>

id: optional string

Token identifier tag.

maxLength32

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

condition: optional object {request\_ip }

</summary>

<details>

<summary>

request\_ip: optional object {in, not\_in }

Client IP restrictions.

</summary>

in: optional array of <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20token_condition_cidr_list%20%3E%20(schema)">TokenConditionCIDRList</a>

List of IPv4/IPv6 CIDR addresses.

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20condition%20%3E%20(property)%20request_ip%20%3E%20(property)%20in">Link to this property</a>

not\_in: optional array of <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20token_condition_cidr_list%20%3E%20(schema)">TokenConditionCIDRList</a>

List of IPv4/IPv6 CIDR addresses.

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20condition%20%3E%20(property)%20request_ip%20%3E%20(property)%20not_in">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20condition%20%3E%20(property)%20request_ip">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20condition">Link to this property</a>

creator\_email\_at\_creation: optional string

The email address of the user who created the token at the time of creation. Only present for Account Owned API Tokens when a creator email was available.

maxLength90

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20creator_email_at_creation">Link to this property</a>

expires\_on: optional string

The expiration time on or after which the JWT MUST NOT be accepted for processing.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_on">Link to this property</a>

issued\_on: optional string

The time on which the token was created.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20issued_on">Link to this property</a>

last\_used\_on: optional string

Last time the token was used.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20last_used_on">Link to this property</a>

modified\_on: optional string

Last time the token was modified.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: optional string

Token name.

maxLength120

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

not\_before: optional string

The time before which the token MUST NOT be accepted for processing.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20not_before">Link to this property</a>

<details>

<summary>

policies: optional array of <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)">TokenPolicy</a> { id, effect, permission\_groups, resources }

List of access policies assigned to the token.

</summary>

id: string

Policy identifier.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

effect: "allow"or "deny"

Allow or deny operations against the resources.

</summary>

One of the following:

"allow"

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20effect%20%3E%20(member)%200">Link to this property</a>

"deny"

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20effect%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20effect">Link to this property</a>

<details>

<summary>

permission\_groups: array of object {id, meta, name }

A set of permission groups that are specified to the policy.

</summary>

id: string

Identifier of the permission group.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

meta: optional object {category, deprecated, description, 5 more }

Attributes associated to the permission group.

</summary>

category: optional string

A category used to group permission groups.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20category">Link to this property</a>

deprecated: optional string

Indicates whether the permission group is deprecated.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20deprecated">Link to this property</a>

description: optional string

Additional information about the permission group.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20description">Link to this property</a>

editable: optional string

Indicates whether the permission group can be edited.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20editable">Link to this property</a>

eol\_at: optional string

The planned end-of-life date and time, when provided.

formatdate-time

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20eol_at">Link to this property</a>

label: optional string

A label identifying the permission group.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20label">Link to this property</a>

scopes: optional string

The scope associated with the permission group.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20scopes">Link to this property</a>

visibility: optional string

Indicates the permission group’s availability or visibility.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20visibility">Link to this property</a>

</details>

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

name: optional string

Name of the permission group.

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20permission_groups">Link to this property</a>

<details>

<summary>

resources: map\[string]or map\[map\[string]]

A list of resource names that the policy applies to.

</summary>

One of the following:

IAMResourcesTypeObjectString = map\[string]

Map of simple string resource permissions

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(variant)%200">Link to this property</a>

IAMResourcesTypeObjectNested = map\[map\[string]]

Map of nested resource permissions

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20%24shared%20%3E%20(model)%20token_policy%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20policies">Link to this property</a>

provisioner\_id: optional string

The identifier of the service that provisioned the token. For an OAuth-provisioned token, this is the OAuth client identifier. Present when <code>provisioner_type</code> is present and null when the identifier is unavailable.

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20provisioner_id">Link to this property</a>

provisioner\_type: optional string

The type of service that provisioned the token. Only present for provisioned Account Owned API Tokens.

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20provisioner_type">Link to this property</a>

<details>

<summary>

status: optional "active"or "disabled"or "expired"

Status of the token.

</summary>

One of the following:

"active"

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"expired"

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

value: optional <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20token_value%20%3E%20(schema)">TokenValue</a>

The token value.

maxLength80

minLength40

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.tokens%20%3E%20(model)%20token_create_response%20%3E%20(schema)>)

<details>

<summary>

TokenDeleteResponse object {id }

</summary>

id: string

Identifier

maxLength32

minLength32

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.tokens%20%3E%20(model)%20token_delete_response%20%3E%20(schema)>)

<details>

<summary>

TokenVerifyResponse object {id, status, expires\_on, not\_before }

</summary>

id: string

Token identifier tag.

maxLength32

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

status: "active"or "disabled"or "expired"

Status of the token.

</summary>

One of the following:

"active"

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"expired"

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

expires\_on: optional string

The expiration time on or after which the JWT MUST NOT be accepted for processing.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20expires_on">Link to this property</a>

not\_before: optional string

The time before which the token MUST NOT be accepted for processing.

formatdate-time

<a href="#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)%20%3E%20(property)%20not_before">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.tokens%20%3E%20(model)%20token_verify_response%20%3E%20(schema)>)

#### AccountsTokensPermission Groups

##### [List Permission Groups](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/permission_groups/methods/list)

GET/accounts/{account\_id}/tokens/permission\_groups

##### [List Permission Groups](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/permission_groups/methods/get)

GET/accounts/{account\_id}/tokens/permission\_groups

##### ModelsExpand Collapse

<details>

<summary>

PermissionGroupListResponse object {id, category, is\_selectable, 2 more }

</summary>

id: optional string

Public ID.

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

category: optional "developer\_platform"or "ai\_and\_machine\_learning"or "dns\_and\_zones"or 10 more

Product category that this permission group belongs to.

</summary>

One of the following:

"developer\_platform"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%200">Link to this property</a>

"ai\_and\_machine\_learning"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%201">Link to this property</a>

"dns\_and\_zones"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%202">Link to this property</a>

"app\_security"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%203">Link to this property</a>

"rules\_and\_configuration"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%204">Link to this property</a>

"cloudflare\_one\_and\_zero\_trust"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%205">Link to this property</a>

"analytics\_and\_logs"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%206">Link to this property</a>

"network\_services"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%207">Link to this property</a>

"media"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%208">Link to this property</a>

"email\_and\_messaging"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%209">Link to this property</a>

"cache\_and\_performance"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%2010">Link to this property</a>

"account\_and\_billing"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%2011">Link to this property</a>

"other"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

is\_selectable: optional boolean

Whether the caller can select this permission group when creating a token.

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20is_selectable">Link to this property</a>

name: optional string

Permission Group Name

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

scopes: optional array of "com.cloudflare.api.account"or "com.cloudflare.api.account.zone"or "com.cloudflare.api.user"or "com.cloudflare.edge.r2.bucket"

Resources to which the Permission Group is scoped

</summary>

One of the following:

"com.cloudflare.api.account"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"com.cloudflare.api.account.zone"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"com.cloudflare.api.user"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"com.cloudflare.edge.r2.bucket"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)%20%3E%20(property)%20scopes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_list_response%20%3E%20(schema)>)

<details>

<summary>

PermissionGroupGetResponse = array of object {id, category, is\_selectable, 2 more }

</summary>

id: optional string

Public ID.

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

category: optional "developer\_platform"or "ai\_and\_machine\_learning"or "dns\_and\_zones"or 10 more

Product category that this permission group belongs to.

</summary>

One of the following:

"developer\_platform"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%200">Link to this property</a>

"ai\_and\_machine\_learning"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%201">Link to this property</a>

"dns\_and\_zones"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%202">Link to this property</a>

"app\_security"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%203">Link to this property</a>

"rules\_and\_configuration"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%204">Link to this property</a>

"cloudflare\_one\_and\_zero\_trust"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%205">Link to this property</a>

"analytics\_and\_logs"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%206">Link to this property</a>

"network\_services"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%207">Link to this property</a>

"media"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%208">Link to this property</a>

"email\_and\_messaging"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%209">Link to this property</a>

"cache\_and\_performance"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%2010">Link to this property</a>

"account\_and\_billing"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%2011">Link to this property</a>

"other"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

is\_selectable: optional boolean

Whether the caller can select this permission group when creating a token.

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20is_selectable">Link to this property</a>

name: optional string

Permission Group Name

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

scopes: optional array of "com.cloudflare.api.account"or "com.cloudflare.api.account.zone"or "com.cloudflare.api.user"or "com.cloudflare.edge.r2.bucket"

Resources to which the Permission Group is scoped

</summary>

One of the following:

"com.cloudflare.api.account"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"com.cloudflare.api.account.zone"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"com.cloudflare.api.user"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"com.cloudflare.edge.r2.bucket"

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20scopes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.tokens.permission_groups%20%3E%20(model)%20permission_group_get_response%20%3E%20(schema)>)

#### AccountsTokensValue

##### [Roll Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/value/methods/update)

PUT/accounts/{account\_id}/tokens/{token\_id}/value

#### AccountsLogs

#### AccountsLogsAudit

##### [Get account audit logs (Version 2)](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list)

GET/accounts/{account\_id}/logs/audit

##### [Get resource change history from an account audit log entry (Version 2)](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/history)

GET/accounts/{account\_id}/logs/audit/{id}/history

##### [List account audit log product categories (Version 2)](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/product_categories)

GET/accounts/{account\_id}/logs/audit/product\_categories

##### ModelsExpand Collapse

<details>

<summary>

AuditListResponse object {id, account, action, 4 more }

</summary>

id: optional string

A unique identifier for the audit log entry.

maxLength32

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

account: optional object {id, name }

Contains account related information.

</summary>

id: optional string

A unique identifier for the account.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20account%20%3E%20(property)%20id">Link to this property</a>

name: optional string

A string that identifies the account name.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20account%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20account">Link to this property</a>

<details>

<summary>

action: optional object {description, result, time, type }

Provides information about the action performed.

</summary>

description: optional string

A short description of the action performed.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20description">Link to this property</a>

result: optional string

The result of the action, indicating success or failure.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20result">Link to this property</a>

time: optional string

A timestamp indicating when the action was logged.

formatdate-time

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20time">Link to this property</a>

type: optional string

A short string that describes the action that was performed.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

actor: optional object {id, context, email, 4 more }

Provides details about the actor who performed the action.

</summary>

id: optional string

The ID of the actor who performed the action. If a user performed the action, this will be their User ID.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20id">Link to this property</a>

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

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%200">Link to this property</a>

"api\_key"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%201">Link to this property</a>

"api\_token"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%202">Link to this property</a>

"dash"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%203">Link to this property</a>

"oauth"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%204">Link to this property</a>

"origin\_ca\_key"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20context">Link to this property</a>

email: optional string

The email of the actor who performed the action.

formatemail

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20email">Link to this property</a>

ip\_address: optional string

The IP address of the request that performed the action.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20ip_address">Link to this property</a>

token\_id: optional string

The API token ID when the actor context is an api\_token or oauth.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20token_id">Link to this property</a>

token\_name: optional string

The API token name when the actor context is an api\_token or oauth.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20token_name">Link to this property</a>

<details>

<summary>

type: optional "account"or "cloudflare\_admin"or "delegated\_service"or 2 more

The type of actor.

</summary>

One of the following:

"account"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"cloudflare\_admin"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"delegated\_service"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"system"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"user"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20actor">Link to this property</a>

<details>

<summary>

raw: optional object {cf\_ray\_id, method, status\_code, 2 more }

Provides raw information about the request and response.

</summary>

cf\_ray\_id: optional string

The Cloudflare Ray ID for the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20cf_ray_id">Link to this property</a>

method: optional string

The HTTP method of the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20method">Link to this property</a>

status\_code: optional number

The HTTP response status code returned by the API.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20status_code">Link to this property</a>

uri: optional string

The URI of the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20uri">Link to this property</a>

user\_agent: optional string

The client’s user agent string sent with the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw%20%3E%20(property)%20user_agent">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20raw">Link to this property</a>

<details>

<summary>

resource: optional object {id, product, request, 3 more }

Provides details about the affected resource.

</summary>

id: optional string

The unique identifier for the affected resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20id">Link to this property</a>

product: optional string

The Cloudflare product associated with the resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20product">Link to this property</a>

request: optional unknown

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20request">Link to this property</a>

response: optional unknown

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20response">Link to this property</a>

scope: optional unknown

The scope of the resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20scope">Link to this property</a>

type: optional string

The type of the resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20resource">Link to this property</a>

<details>

<summary>

zone: optional object {id, name }

Provides details about the zone affected by the action.

</summary>

id: optional string

A string that identifies the zone id.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20zone%20%3E%20(property)%20id">Link to this property</a>

name: optional string

A string that identifies the zone name.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20zone%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)%20%3E%20(property)%20zone">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_list_response%20%3E%20(schema)>)

<details>

<summary>

AuditHistoryResponse = array of object {id, account, action, 4 more }

</summary>

id: optional string

A unique identifier for the audit log entry.

maxLength32

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

account: optional object {id, name }

Contains account related information.

</summary>

id: optional string

A unique identifier for the account.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20account%20%3E%20(property)%20id">Link to this property</a>

name: optional string

A string that identifies the account name.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20account%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20account">Link to this property</a>

<details>

<summary>

action: optional object {description, result, time, type }

Provides information about the action performed.

</summary>

description: optional string

A short description of the action performed.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20description">Link to this property</a>

result: optional string

The result of the action, indicating success or failure.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20result">Link to this property</a>

time: optional string

A timestamp indicating when the action was logged.

formatdate-time

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20time">Link to this property</a>

type: optional string

A short string that describes the action that was performed.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

actor: optional object {id, context, email, 4 more }

Provides details about the actor who performed the action.

</summary>

id: optional string

The ID of the actor who performed the action. If a user performed the action, this will be their User ID.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20id">Link to this property</a>

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

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%200">Link to this property</a>

"api\_key"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%201">Link to this property</a>

"api\_token"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%202">Link to this property</a>

"dash"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%203">Link to this property</a>

"oauth"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%204">Link to this property</a>

"origin\_ca\_key"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20context">Link to this property</a>

email: optional string

The email of the actor who performed the action.

formatemail

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20email">Link to this property</a>

ip\_address: optional string

The IP address of the request that performed the action.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20ip_address">Link to this property</a>

token\_id: optional string

The API token ID when the actor context is an api\_token or oauth.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20token_id">Link to this property</a>

token\_name: optional string

The API token name when the actor context is an api\_token or oauth.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20token_name">Link to this property</a>

<details>

<summary>

type: optional "account"or "cloudflare\_admin"or "delegated\_service"or 2 more

The type of actor.

</summary>

One of the following:

"account"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"cloudflare\_admin"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"delegated\_service"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"system"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"user"

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20actor">Link to this property</a>

<details>

<summary>

raw: optional object {cf\_ray\_id, method, status\_code, 2 more }

Provides raw information about the request and response.

</summary>

cf\_ray\_id: optional string

The Cloudflare Ray ID for the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20cf_ray_id">Link to this property</a>

method: optional string

The HTTP method of the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20method">Link to this property</a>

status\_code: optional number

The HTTP response status code returned by the API.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20status_code">Link to this property</a>

uri: optional string

The URI of the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20uri">Link to this property</a>

user\_agent: optional string

The client’s user agent string sent with the request.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw%20%3E%20(property)%20user_agent">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20raw">Link to this property</a>

<details>

<summary>

resource: optional object {id, product, request, 3 more }

Provides details about the affected resource.

</summary>

id: optional string

The unique identifier for the affected resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20id">Link to this property</a>

product: optional string

The Cloudflare product associated with the resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20product">Link to this property</a>

request: optional unknown

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20request">Link to this property</a>

response: optional unknown

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20response">Link to this property</a>

scope: optional unknown

The scope of the resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20scope">Link to this property</a>

type: optional string

The type of the resource.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20resource">Link to this property</a>

<details>

<summary>

zone: optional object {id, name }

Provides details about the zone affected by the action.

</summary>

id: optional string

A string that identifies the zone id.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20zone%20%3E%20(property)%20id">Link to this property</a>

name: optional string

A string that identifies the zone name.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20zone%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20zone">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_history_response%20%3E%20(schema)>)

<details>

<summary>

AuditProductCategoriesResponse object {label, products, value }

A predefined product category and the resource products it expands to.

</summary>

label: optional string

A human-readable label for the product category.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_product_categories_response%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

products: optional array of object {label, value }

The resource products that the product category expands to.

</summary>

label: optional string

A human-readable label for the product.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_product_categories_response%20%3E%20(schema)%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

value: optional string

The resource\_product value that the product category expands to.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_product_categories_response%20%3E%20(schema)%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_product_categories_response%20%3E%20(schema)%20%3E%20(property)%20products">Link to this property</a>

value: optional string

The product category identifier used with the product\_category filter.

<a href="#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_product_categories_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.logs.audit%20%3E%20(model)%20audit_product_categories_response%20%3E%20(schema)>)

#### AccountsEntitlements

##### [Get Account Entitlements](https://developers.cloudflare.com/api/resources/accounts/subresources/entitlements/methods/list)

GET/accounts/{account\_id}/entitlements

##### ModelsExpand Collapse

<details>

<summary>

EntitlementListResponse object {id, allocation, created\_date, 3 more }

A single entitlement record for a zone or account.

</summary>

id: string

Entitlement identifier — equal to the feature key.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

allocation: object {type, value }

Represents the allocation value for an entitlement. The shape of <code>value</code> depends on <code>type</code>: <code>bool</code> uses a boolean, <code>max_count</code> uses an integer, <code>enum_number</code> uses an array of numbers, <code>range</code> uses an object with <code>min</code> and <code>max</code> integer fields, and <code>string</code> uses a string.

</summary>

<details>

<summary>

type: "bool"or "max\_count"or "enum\_number"or 2 more

Allocation type discriminator.

</summary>

One of the following:

"bool"

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"max\_count"

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"enum\_number"

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"range"

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"string"

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

value: booleanor numberor stringor 2 more

Contains the allocation value whose concrete type the <code>type</code> field determines: bool yields a boolean, max\_count yields an integer, enum\_number yields an array of numbers, range yields an object with <code>min</code> and <code>max</code>, and string yields a string.

</summary>

One of the following:

boolean

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

string

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

array of number

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {max, min }

</summary>

max: number

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20max">Link to this property</a>

min: number

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20allocation">Link to this property</a>

created\_date: string

ISO 8601 timestamp (microsecond precision, no timezone offset) when the entitlement was created. Format: <code>YYYY-MM-DDTHH:MM:SS.ffffff</code>.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20created_date">Link to this property</a>

deleted\_date: string

ISO 8601 timestamp when the entitlement was deleted, or empty string if not deleted.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20deleted_date">Link to this property</a>

edited\_date: string

ISO 8601 timestamp (microsecond precision, no timezone offset) when the entitlement was last edited.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20edited_date">Link to this property</a>

<details>

<summary>

feature: object {id, feature\_set, key, name }

Describes a product feature associated with an entitlement.

</summary>

id: number

Numeric identifier of the feature.

formatint64

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20feature%20%3E%20(property)%20id">Link to this property</a>

feature\_set: string

The logical grouping (set) this feature belongs to.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20feature%20%3E%20(property)%20feature_set">Link to this property</a>

key: string

Unique string key for the feature.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20feature%20%3E%20(property)%20key">Link to this property</a>

name: string

Human-readable name of the feature.

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20feature%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)%20%3E%20(property)%20feature">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.entitlements%20%3E%20(model)%20entitlement_list_response%20%3E%20(schema)>)

#### AccountsSpeed Settings

#### AccountsSpeed SettingsTransformations

##### [List Image Resizing configurations for account](https://developers.cloudflare.com/api/resources/accounts/subresources/speed_settings/subresources/transformations/methods/get)

GET/accounts/{account\_id}/settings/transformations

##### ModelsExpand Collapse

<details>

<summary>

TransformationsConfig object {id, cf\_zone\_tag, editable, 2 more }

A configuration item for a specific zone and feature.

</summary>

id: optional string

Feature identifier.

<a href="#(resource)%20accounts.speed_settings.transformations%20%3E%20(model)%20transformations_config%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

cf\_zone\_tag: optional string

Zone tag identifier.

<a href="#(resource)%20accounts.speed_settings.transformations%20%3E%20(model)%20transformations_config%20%3E%20(schema)%20%3E%20(property)%20cf_zone_tag">Link to this property</a>

editable: optional boolean

Whether this setting can be modified.

<a href="#(resource)%20accounts.speed_settings.transformations%20%3E%20(model)%20transformations_config%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: optional string

When this setting was last modified.

formatdate-time

<a href="#(resource)%20accounts.speed_settings.transformations%20%3E%20(model)%20transformations_config%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

value: optional string

Current value of the feature setting.

<a href="#(resource)%20accounts.speed_settings.transformations%20%3E%20(model)%20transformations_config%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.speed_settings.transformations%20%3E%20(model)%20transformations_config%20%3E%20(schema)>)

#### AccountsPayment Methods

##### [List Payment Methods](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/list)

GET/accounts/{account\_id}/payment-methods

##### [Create Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/create)

POST/accounts/{account\_id}/payment-methods

##### [Get Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/get)

GET/accounts/{account\_id}/payment-methods/{payment\_method\_id}

##### [Update Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/update)

PUT/accounts/{account\_id}/payment-methods/{payment\_method\_id}

##### [Delete Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/delete)

DELETE/accounts/{account\_id}/payment-methods/{payment\_method\_id}

##### [Set Default Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/set_as_default)

POST/accounts/{account\_id}/payment-methods/{payment\_method\_id}/set-as-default

##### ModelsExpand Collapse

<details>

<summary>

PaymentMethodListResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodCreateResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodGetResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodUpdateResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodDeleteResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_delete_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_delete_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_delete_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodSetAsDefaultResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_set_as_default_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_set_as_default_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_set_as_default_response%20%3E%20(schema)>)

#### AccountsPay Invoice

##### [Pay Invoice](https://developers.cloudflare.com/api/resources/accounts/subresources/pay_invoice/methods/create)

POST/accounts/{account\_id}/pay-invoice

##### ModelsExpand Collapse

<details>

<summary>

PayInvoiceCreateResponse object {client\_secret }

</summary>

client\_secret: optional string

The Stripe client secret for frontend payment confirmation.

<a href="#(resource)%20accounts.pay_invoice%20%3E%20(model)%20pay_invoice_create_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.pay_invoice%20%3E%20(model)%20pay_invoice_create_response%20%3E%20(schema)>)

#### AccountsPay Bad Debt

##### [Pay Bad Debt](https://developers.cloudflare.com/api/resources/accounts/subresources/pay_bad_debt/methods/create)

POST/accounts/{account\_id}/pay-bad-debt

##### ModelsExpand Collapse

<details>

<summary>

PayBadDebtCreateResponse object {client\_secret }

</summary>

client\_secret: optional string

The Stripe client secret for frontend payment confirmation.

<a href="#(resource)%20accounts.pay_bad_debt%20%3E%20(model)%20pay_bad_debt_create_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.pay_bad_debt%20%3E%20(model)%20pay_bad_debt_create_response%20%3E%20(schema)>)

#### AccountsReceipts

##### [Get Receipt PDF](https://developers.cloudflare.com/api/resources/accounts/subresources/receipts/methods/pdf)

GET/accounts/{account\_id}/receipts/{receipt\_id}/pdf

#### AccountsInvoices

##### [Toggle PDF Invoices](https://developers.cloudflare.com/api/resources/accounts/subresources/invoices/methods/edit)

PATCH/accounts/{account\_id}/invoices

##### ModelsExpand Collapse

<details>

<summary>

InvoiceEditResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20accounts.invoices%20%3E%20(model)%20invoice_edit_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20accounts.invoices%20%3E%20(model)%20invoice_edit_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.invoices%20%3E%20(model)%20invoice_edit_response%20%3E%20(schema)>)

#### AccountsClient Secret

##### [Create Setup Intent](https://developers.cloudflare.com/api/resources/accounts/subresources/client_secret/methods/create)

POST/accounts/{account\_id}/client-secret

##### ModelsExpand Collapse

<details>

<summary>

ClientSecretCreateResponse object {client\_secret }

</summary>

client\_secret: optional string

The Stripe client secret for frontend payment confirmation.

<a href="#(resource)%20accounts.client_secret%20%3E%20(model)%20client_secret_create_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.client_secret%20%3E%20(model)%20client_secret_create_response%20%3E%20(schema)>)