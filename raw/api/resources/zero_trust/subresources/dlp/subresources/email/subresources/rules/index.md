---
title: Rules
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DLP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp)

[Email](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Rules

##### [List all email scanner rules](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/list)

GET/accounts/{account\_id}/dlp/email/rules

##### [Get an email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/get)

GET/accounts/{account\_id}/dlp/email/rules/{rule\_id}

##### [Create email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/create)

POST/accounts/{account\_id}/dlp/email/rules

##### [Update email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/update)

PUT/accounts/{account\_id}/dlp/email/rules/{rule\_id}

##### [Delete email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/delete)

DELETE/accounts/{account\_id}/dlp/email/rules/{rule\_id}

##### [Update email scanner rule priorities](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/bulk_edit)

PATCH/accounts/{account\_id}/dlp/email/rules

##### ModelsExpand Collapse

<details>

<summary>

RuleListResponse object {action, conditions, created\_at, 6 more }

</summary>

<details>

<summary>

action: object {action, message }

</summary>

action: "Block"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20action">Link to this property</a>

message: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

conditions: array of object {operator, selector, value }

Triggered if all conditions match.

</summary>

<details>

<summary>

operator: "InList"or "NotInList"or "MatchRegex"or "NotMatchRegex"

</summary>

One of the following:

"InList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"NotInList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"MatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"NotMatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

selector: "Recipients"or "Sender"or "DLPProfiles"

</summary>

One of the following:

"Recipients"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%200">Link to this property</a>

"Sender"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%201">Link to this property</a>

"DLPProfiles"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector">Link to this property</a>

<details>

<summary>

value: array of stringor string

</summary>

One of the following:

array of string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20conditions">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

rule\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20rule_id">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)>)

<details>

<summary>

RuleGetResponse object {action, conditions, created\_at, 6 more }

</summary>

<details>

<summary>

action: object {action, message }

</summary>

action: "Block"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20action">Link to this property</a>

message: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

conditions: array of object {operator, selector, value }

Triggered if all conditions match.

</summary>

<details>

<summary>

operator: "InList"or "NotInList"or "MatchRegex"or "NotMatchRegex"

</summary>

One of the following:

"InList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"NotInList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"MatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"NotMatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

selector: "Recipients"or "Sender"or "DLPProfiles"

</summary>

One of the following:

"Recipients"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%200">Link to this property</a>

"Sender"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%201">Link to this property</a>

"DLPProfiles"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector">Link to this property</a>

<details>

<summary>

value: array of stringor string

</summary>

One of the following:

array of string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20conditions">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

rule\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_id">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)>)

<details>

<summary>

RuleCreateResponse object {action, conditions, created\_at, 6 more }

</summary>

<details>

<summary>

action: object {action, message }

</summary>

action: "Block"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20action">Link to this property</a>

message: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

conditions: array of object {operator, selector, value }

Triggered if all conditions match.

</summary>

<details>

<summary>

operator: "InList"or "NotInList"or "MatchRegex"or "NotMatchRegex"

</summary>

One of the following:

"InList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"NotInList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"MatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"NotMatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

selector: "Recipients"or "Sender"or "DLPProfiles"

</summary>

One of the following:

"Recipients"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%200">Link to this property</a>

"Sender"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%201">Link to this property</a>

"DLPProfiles"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector">Link to this property</a>

<details>

<summary>

value: array of stringor string

</summary>

One of the following:

array of string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20conditions">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

rule\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_id">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)>)

<details>

<summary>

RuleUpdateResponse object {action, conditions, created\_at, 6 more }

</summary>

<details>

<summary>

action: object {action, message }

</summary>

action: "Block"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20action">Link to this property</a>

message: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

conditions: array of object {operator, selector, value }

Triggered if all conditions match.

</summary>

<details>

<summary>

operator: "InList"or "NotInList"or "MatchRegex"or "NotMatchRegex"

</summary>

One of the following:

"InList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"NotInList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"MatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"NotMatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

selector: "Recipients"or "Sender"or "DLPProfiles"

</summary>

One of the following:

"Recipients"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%200">Link to this property</a>

"Sender"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%201">Link to this property</a>

"DLPProfiles"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector">Link to this property</a>

<details>

<summary>

value: array of stringor string

</summary>

One of the following:

array of string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20conditions">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

rule\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20rule_id">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)>)

<details>

<summary>

RuleDeleteResponse object {action, conditions, created\_at, 6 more }

</summary>

<details>

<summary>

action: object {action, message }

</summary>

action: "Block"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20action">Link to this property</a>

message: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

conditions: array of object {operator, selector, value }

Triggered if all conditions match.

</summary>

<details>

<summary>

operator: "InList"or "NotInList"or "MatchRegex"or "NotMatchRegex"

</summary>

One of the following:

"InList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"NotInList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"MatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"NotMatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

selector: "Recipients"or "Sender"or "DLPProfiles"

</summary>

One of the following:

"Recipients"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%200">Link to this property</a>

"Sender"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%201">Link to this property</a>

"DLPProfiles"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector">Link to this property</a>

<details>

<summary>

value: array of stringor string

</summary>

One of the following:

array of string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20conditions">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

rule\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20rule_id">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)>)

<details>

<summary>

RuleBulkEditResponse object {action, conditions, created\_at, 6 more }

</summary>

<details>

<summary>

action: object {action, message }

</summary>

action: "Block"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20action">Link to this property</a>

message: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20action%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

conditions: array of object {operator, selector, value }

Triggered if all conditions match.

</summary>

<details>

<summary>

operator: "InList"or "NotInList"or "MatchRegex"or "NotMatchRegex"

</summary>

One of the following:

"InList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"NotInList"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"MatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"NotMatchRegex"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

selector: "Recipients"or "Sender"or "DLPProfiles"

</summary>

One of the following:

"Recipients"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%200">Link to this property</a>

"Sender"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%201">Link to this property</a>

"DLPProfiles"

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20selector">Link to this property</a>

<details>

<summary>

value: array of stringor string

</summary>

One of the following:

array of string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20conditions">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

rule\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_id">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.email.rules%20%3E%20(model)%20rule_bulk_edit_response%20%3E%20(schema)>)