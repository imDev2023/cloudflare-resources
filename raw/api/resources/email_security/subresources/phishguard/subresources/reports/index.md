---
title: Reports
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

[Phishguard](https://developers.cloudflare.com/api/resources/email_security/subresources/phishguard)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Reports

##### [List PhishGuard reports](https://developers.cloudflare.com/api/resources/email_security/subresources/phishguard/subresources/reports/methods/list)

GET/accounts/{account\_id}/email-security/phishguard/reports

##### ModelsExpand Collapse

<details>

<summary>

ReportListResponse object {id, content, disposition, 7 more }

</summary>

id: number

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

content: string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20content">Link to this property</a>

<details>

<summary>

disposition: "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20disposition">Link to this property</a>

<details>

<summary>

fields: object {to, from, occurred\_at, 2 more }

</summary>

to: array of string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(property)%20to">Link to this property</a>

from: optional string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(property)%20from">Link to this property</a>

occurred\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(property)%20occurred_at">Link to this property</a>

postfix\_id: optional string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(property)%20postfix_id">Link to this property</a>

Deprecatedts: optional string

Use <code>occurred_at</code> instead.

Deprecated, use <code>occurred_at</code> instead.

formatdate-time

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(property)%20ts">Link to this property</a>

</details>

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20fields">Link to this property</a>

priority: string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

title: string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

tags: optional array of object {category, value }

</summary>

category: string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

value: string

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

Deprecatedts: optional string

Use <code>created_at</code> instead.

Deprecated, use <code>created_at</code> instead.

formatdate-time

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20ts">Link to this property</a>

updated\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.phishguard.reports%20%3E%20(model)%20report_list_response%20%3E%20(schema)>)