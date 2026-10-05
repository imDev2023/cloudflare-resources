---
title: Suppressions
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Sending](https://developers.cloudflare.com/api/resources/email_sending)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Suppressions

##### [List account Email Sending suppressions](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/list)

GET/accounts/{account\_id}/email/sending/suppressions

##### [Get account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/get)

GET/accounts/{account\_id}/email/sending/suppressions/{suppression\_id}

##### [Create account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/create)

POST/accounts/{account\_id}/email/sending/suppressions

##### [Update account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/edit)

PATCH/accounts/{account\_id}/email/sending/suppressions/{suppression\_id}

##### [Delete account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/delete)

DELETE/accounts/{account\_id}/email/sending/suppressions/{suppression\_id}

##### [Bulk import account Email Sending suppressions](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/import)

POST/accounts/{account\_id}/email/sending/suppressions/bulk

##### ModelsExpand Collapse

<details>

<summary>

SuppressionListResponse object {id, created\_at, email, 5 more }

</summary>

id: string

Unique identifier for this suppression.

formatuuid

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the suppression was created.

formatdate-time

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

email: string

The suppressed email address.

formatemail

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20email">Link to this property</a>

expires\_at: string

When the suppression expires. Null for a permanent suppression.

formatdate-time

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

read\_only: boolean

Whether clients may mutate this suppression. This is determined by the server and must not be inferred from <code>reason</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20read_only">Link to this property</a>

reason: string

Why the address is suppressed: <code>manual</code>, <code>complaint</code>, <code>hard_bounce</code>, <code>soft_bounce</code>, or <code>policy</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20reason">Link to this property</a>

note: optional string

Advisory note for this suppression, if any.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20note">Link to this property</a>

<details>

<summary>

scope: optional object {type } or object {type, value }

Where the suppression applies: <code>account</code> for every sending domain of the account, or <code>sending_domain</code> for one envelope MAIL FROM domain.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "account"

Blocks the recipient for every sending domain of the account.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, value }

</summary>

type: "sending\_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses <code>value</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_list_response%20%3E%20(schema)>)

<details>

<summary>

SuppressionGetResponse object {id, created\_at, email, 5 more }

</summary>

id: string

Unique identifier for this suppression.

formatuuid

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the suppression was created.

formatdate-time

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

email: string

The suppressed email address.

formatemail

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20email">Link to this property</a>

expires\_at: string

When the suppression expires. Null for a permanent suppression.

formatdate-time

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

read\_only: boolean

Whether clients may mutate this suppression. This is determined by the server and must not be inferred from <code>reason</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20read_only">Link to this property</a>

reason: string

Why the address is suppressed: <code>manual</code>, <code>complaint</code>, <code>hard_bounce</code>, <code>soft_bounce</code>, or <code>policy</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20reason">Link to this property</a>

note: optional string

Advisory note for this suppression, if any.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20note">Link to this property</a>

<details>

<summary>

scope: optional object {type } or object {type, value }

Where the suppression applies: <code>account</code> for every sending domain of the account, or <code>sending_domain</code> for one envelope MAIL FROM domain.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "account"

Blocks the recipient for every sending domain of the account.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, value }

</summary>

type: "sending\_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses <code>value</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_get_response%20%3E%20(schema)>)

<details>

<summary>

SuppressionCreateResponse object {id, scope }

</summary>

id: string

The suppression’s identifier.

formatuuid

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

scope: optional object {type } or object {type, value }

Where the suppression applies: <code>account</code> for every sending domain of the account, or <code>sending_domain</code> for one envelope MAIL FROM domain.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "account"

Blocks the recipient for every sending domain of the account.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, value }

</summary>

type: "sending\_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses <code>value</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_create_response%20%3E%20(schema)>)

<details>

<summary>

SuppressionEditResponse object {id, created\_at, email, 5 more }

</summary>

id: string

Unique identifier for this suppression.

formatuuid

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the suppression was created.

formatdate-time

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

email: string

The suppressed email address.

formatemail

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20email">Link to this property</a>

expires\_at: string

When the suppression expires. Null for a permanent suppression.

formatdate-time

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

read\_only: boolean

Whether clients may mutate this suppression. This is determined by the server and must not be inferred from <code>reason</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20read_only">Link to this property</a>

reason: string

Why the address is suppressed: <code>manual</code>, <code>complaint</code>, <code>hard_bounce</code>, <code>soft_bounce</code>, or <code>policy</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20reason">Link to this property</a>

note: optional string

Advisory note for this suppression, if any.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20note">Link to this property</a>

<details>

<summary>

scope: optional object {type } or object {type, value }

Where the suppression applies: <code>account</code> for every sending domain of the account, or <code>sending_domain</code> for one envelope MAIL FROM domain.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "account"

Blocks the recipient for every sending domain of the account.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, value }

</summary>

type: "sending\_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses <code>value</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_edit_response%20%3E%20(schema)>)

<details>

<summary>

SuppressionDeleteResponse object {id, scope }

</summary>

id: string

The suppression’s identifier.

formatuuid

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

scope: optional object {type } or object {type, value }

Where the suppression applies: <code>account</code> for every sending domain of the account, or <code>sending_domain</code> for one envelope MAIL FROM domain.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "account"

Blocks the recipient for every sending domain of the account.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, value }

</summary>

type: "sending\_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses <code>value</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_delete_response%20%3E%20(schema)>)

<details>

<summary>

SuppressionImportResponse object {deduplicated, errors, invalid, 4 more }

</summary>

deduplicated: number

Number of items dropped because their email address and scope repeated an earlier item in this request. Counted once and excluded from <code>items</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20deduplicated">Link to this property</a>

errors: number

Number of items that failed to import due to an unexpected error.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

invalid: number

Number of items with an invalid email address or sending domain.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20invalid">Link to this property</a>

<details>

<summary>

items: array of object {index, status, id, 3 more }

Per-item results, in the same order as the request body.

</summary>

index: number

Zero-based index of this item in the request body.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20index">Link to this property</a>

<details>

<summary>

status: "processed"or "invalid"or "error"or "skipped"

Outcome for this item.

</summary>

One of the following:

"processed"

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"invalid"

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"error"

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"skipped"

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

id: optional string

The created or promoted suppression’s identifier. Present when <code>status</code> is <code>processed</code>.

formatuuid

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The submitted email address for this item.

formatemail

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20email">Link to this property</a>

error: optional string

Human-readable error message. Present when <code>status</code> is <code>invalid</code>, <code>error</code>, or <code>skipped</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

scope: optional object {type } or object {type, value }

Where the suppression applies: <code>account</code> for every sending domain of the account, or <code>sending_domain</code> for one envelope MAIL FROM domain.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "account"

Blocks the recipient for every sending domain of the account.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20scope%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20scope%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, value }

</summary>

type: "sending\_domain"

Blocks the recipient only for mail whose envelope MAIL FROM uses <code>value</code>.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

The sending domain: the domain part of the envelope MAIL FROM, lowercase, without a trailing dot.

maxLength1024

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20scope%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20scope%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

</details>

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

processed: number

Number of items successfully created or promoted.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20processed">Link to this property</a>

skipped: number

Number of items skipped because the existing suppression is not customer-managed (for example, a read-only policy suppression).

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20skipped">Link to this property</a>

total: number

Total number of items in the request body, including duplicates.

<a href="#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)%20%3E%20(property)%20total">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_sending.suppressions%20%3E%20(model)%20suppression_import_response%20%3E%20(schema)>)