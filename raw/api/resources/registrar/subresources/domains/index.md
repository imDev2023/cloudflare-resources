---
title: Domains
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Registrar](https://developers.cloudflare.com/api/resources/registrar)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Domains

##### [List domains](https://developers.cloudflare.com/api/resources/registrar/subresources/domains/methods/list)

Deprecated

GET/accounts/{account\_id}/registrar/domains

##### [Get domain](https://developers.cloudflare.com/api/resources/registrar/subresources/domains/methods/get)

Deprecated

GET/accounts/{account\_id}/registrar/domains/{domain\_name}

##### [Update domain](https://developers.cloudflare.com/api/resources/registrar/subresources/domains/methods/update)

Deprecated

PUT/accounts/{account\_id}/registrar/domains/{domain\_name}

##### ModelsExpand Collapse

<details>

<summary>

Domain object {id, available, can\_register, 9 more }

</summary>

id: optional string

Domain identifier.

maxLength32

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

available: optional boolean

Shows if a domain is available for transferring into Cloudflare Registrar.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20available">Link to this property</a>

can\_register: optional boolean

Indicates eligibility to register the domain as a new domain.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20can_register">Link to this property</a>

created\_at: optional string

Shows time of creation.

formatdate-time

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

current\_registrar: optional string

Shows name of current registrar.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20current_registrar">Link to this property</a>

expires\_at: optional string

Shows when domain name registration expires.

formatdate-time

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

locked: optional boolean

Shows whether a registrar lock is in place for a domain.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20locked">Link to this property</a>

<details>

<summary>

registrant\_contact: optional object {address, city, country, 10 more }

Shows contact information for domain registrant.

</summary>

address: string

Address.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20address">Link to this property</a>

city: string

City.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20city">Link to this property</a>

country: string

The country in which the user lives.

maxLength30

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20country">Link to this property</a>

first\_name: string

User’s first name.

maxLength60

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20first_name">Link to this property</a>

last\_name: string

User’s last name.

maxLength60

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20last_name">Link to this property</a>

organization: string

Name of organization.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20organization">Link to this property</a>

phone: string

User’s telephone number.

maxLength20

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20phone">Link to this property</a>

state: string

State.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20state">Link to this property</a>

zip: string

The zipcode or postal code where the user lives.

maxLength20

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20zip">Link to this property</a>

id: optional string

Contact Identifier.

maxLength32

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20id">Link to this property</a>

address2: optional string

Optional address line for unit, floor, suite, etc.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20address2">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20email">Link to this property</a>

fax: optional string

Contact fax number.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact%20%3E%20(property)%20fax">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registrant_contact">Link to this property</a>

registry\_statuses: optional string

A comma-separated list of registry status codes. Refer to <a href="https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en">EPP Status Codes</a> for the full list.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20registry_statuses">Link to this property</a>

supported\_tld: optional boolean

Indicates whether Cloudflare Registrar currently supports a particular TLD. Refer to <a href="https://www.cloudflare.com/tld-policies/">TLD Policies</a> for a list of supported TLDs.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20supported_tld">Link to this property</a>

<details>

<summary>

transfer\_in: optional object {accept\_foa, approve\_transfer, can\_cancel\_transfer, 3 more }

Statuses for domain transfers into Cloudflare Registrar.

</summary>

<details>

<summary>

accept\_foa: optional "needed"or "ok"

Status of the registrant authorization step.

</summary>

One of the following:

"needed"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20accept_foa%20%3E%20(member)%200">Link to this property</a>

"ok"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20accept_foa%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20accept_foa">Link to this property</a>

<details>

<summary>

approve\_transfer: optional "needed"or "ok"or "pending"or 3 more

Status of the registry transfer-approval step.

</summary>

One of the following:

"needed"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer%20%3E%20(member)%200">Link to this property</a>

"ok"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer%20%3E%20(member)%202">Link to this property</a>

"trying"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer%20%3E%20(member)%203">Link to this property</a>

"rejected"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer%20%3E%20(member)%204">Link to this property</a>

"unknown"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20approve_transfer">Link to this property</a>

can\_cancel\_transfer: optional boolean

Indicates if cancellation is still possible.

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20can_cancel_transfer">Link to this property</a>

<details>

<summary>

disable\_privacy: optional "needed"or "ok"or "unknown"

Status of the privacy-guard disabling step at the foreign registrar.

</summary>

One of the following:

"needed"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20disable_privacy%20%3E%20(member)%200">Link to this property</a>

"ok"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20disable_privacy%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20disable_privacy%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20disable_privacy">Link to this property</a>

<details>

<summary>

enter\_auth\_code: optional "needed"or "ok"or "pending"or 2 more

Status of the auth-code entry and verification step.

</summary>

One of the following:

"needed"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20enter_auth_code%20%3E%20(member)%200">Link to this property</a>

"ok"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20enter_auth_code%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20enter_auth_code%20%3E%20(member)%202">Link to this property</a>

"trying"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20enter_auth_code%20%3E%20(member)%203">Link to this property</a>

"rejected"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20enter_auth_code%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20enter_auth_code">Link to this property</a>

<details>

<summary>

unlock\_domain: optional "needed"or "ok"or "pending"or 2 more

Status of the domain-unlock step at the foreign registrar.

</summary>

One of the following:

"needed"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20unlock_domain%20%3E%20(member)%200">Link to this property</a>

"ok"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20unlock_domain%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20unlock_domain%20%3E%20(member)%202">Link to this property</a>

"trying"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20unlock_domain%20%3E%20(member)%203">Link to this property</a>

"unknown"

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20unlock_domain%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in%20%3E%20(property)%20unlock_domain">Link to this property</a>

</details>

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20transfer_in">Link to this property</a>

updated\_at: optional string

Last updated.

formatdate-time

<a href="#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20registrar.domains%20%3E%20(model)%20domain%20%3E%20(schema)>)

DomainGetResponse = unknown

[Link to this property](<#(resource)%20registrar.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)>)

DomainUpdateResponse = unknown

[Link to this property](<#(resource)%20registrar.domains%20%3E%20(model)%20domain_update_response%20%3E%20(schema)>)