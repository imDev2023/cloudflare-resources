---
title: Mitigations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Abuse Reports](https://developers.cloudflare.com/api/resources/abuse_reports)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Mitigations

##### [List abuse report mitigations](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/mitigations/methods/list)

GET/accounts/{account\_id}/abuse-reports/{report\_id}/mitigations

##### [Request review on mitigations](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/mitigations/methods/review)

POST/accounts/{account\_id}/abuse-reports/{report\_id}/mitigations/appeal

##### ModelsExpand Collapse

<details>

<summary>

MitigationListResponse object {mitigations }

</summary>

<details>

<summary>

mitigations: array of object {id, effective\_date, entity\_id, 3 more }

</summary>

id: string

ID of remediation.

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

effective\_date: string

Date when the mitigation will become active. Time in RFC 3339 format (<a href="https://www.rfc-editor.org/rfc/rfc3339.html">https://www.rfc-editor.org/rfc/rfc3339.html</a>)

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20effective_date">Link to this property</a>

entity\_id: string

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20entity_id">Link to this property</a>

<details>

<summary>

entity\_type: "url\_pattern"or "account"or "zone"or "custom\_expression"

The type of entity targeted by a mitigation.

</summary>

One of the following:

"url\_pattern"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20entity_type%20%3E%20(member)%200">Link to this property</a>

"account"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20entity_type%20%3E%20(member)%201">Link to this property</a>

"zone"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20entity_type%20%3E%20(member)%202">Link to this property</a>

"custom\_expression"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20entity_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20entity_type">Link to this property</a>

<details>

<summary>

status: "pending"or "active"or "in\_review"or 2 more

The status of a mitigation

</summary>

One of the following:

"pending"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"in\_review"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"cancelled"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"removed"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

type: string

The type of mitigation applied to a reported entity.

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)%20%3E%20(property)%20mitigations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_list_response%20%3E%20(schema)>)

<details>

<summary>

MitigationReviewResponse object {id, effective\_date, entity\_id, 3 more }

</summary>

id: string

ID of remediation.

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

effective\_date: string

Date when the mitigation will become active. Time in RFC 3339 format (<a href="https://www.rfc-editor.org/rfc/rfc3339.html">https://www.rfc-editor.org/rfc/rfc3339.html</a>)

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20effective_date">Link to this property</a>

entity\_id: string

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20entity_id">Link to this property</a>

<details>

<summary>

entity\_type: "url\_pattern"or "account"or "zone"or "custom\_expression"

The type of entity targeted by a mitigation.

</summary>

One of the following:

"url\_pattern"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20entity_type%20%3E%20(member)%200">Link to this property</a>

"account"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20entity_type%20%3E%20(member)%201">Link to this property</a>

"zone"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20entity_type%20%3E%20(member)%202">Link to this property</a>

"custom\_expression"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20entity_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20entity_type">Link to this property</a>

<details>

<summary>

status: "pending"or "active"or "in\_review"or 2 more

The status of a mitigation

</summary>

One of the following:

"pending"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"in\_review"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"cancelled"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"removed"

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

type: string

The type of mitigation applied to a reported entity.

<a href="#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports.mitigations%20%3E%20(model)%20mitigation_review_response%20%3E%20(schema)>)