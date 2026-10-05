---
title: Cancel
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

[Investigate](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate)

[Bulk](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Cancel

##### [Cancel a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/subresources/cancel/methods/create)

POST/accounts/{account\_id}/email-security/investigate/bulk/{job\_id}/cancel

##### ModelsExpand Collapse

<details>

<summary>

CancelCreateResponse object {action\_params, action\_type, created\_at, 13 more }

</summary>

<details>

<summary>

action\_params: object {destination, type, expected\_disposition } or object {type }

</summary>

One of the following:

<details>

<summary>

Move object {destination, type, expected\_disposition }

</summary>

<details>

<summary>

destination: "Inbox"or "JunkEmail"or "DeletedItems"or 2 more

The mailbox folder to move messages to.

</summary>

One of the following:

"Inbox"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%200">Link to this property</a>

"JunkEmail"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%201">Link to this property</a>

"DeletedItems"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%202">Link to this property</a>

"RecoverableItemsDeletions"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%203">Link to this property</a>

"RecoverableItemsPurges"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination">Link to this property</a>

type: "MOVE"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

Deprecatedexpected\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

This field is nonfunctional.

Nonfunctional field. End of life: December 1, 2026.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Release object {type }

</summary>

type: "RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params">Link to this property</a>

<details>

<summary>

action\_type: "MOVE"or "RELEASE"

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20action_type">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

job\_id: string

formatuuid

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20job_id">Link to this property</a>

messages\_cancelled: number

Messages that were cancelled: rows cancelled via the API before being claimed, and rows whose in-flight attempt ended when the job reached a terminal state. Together the counters satisfy total\_messages\_discovered = messages\_pending + messages\_successful + messages\_failed + messages\_skipped + messages\_cancelled.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_cancelled">Link to this property</a>

messages\_failed: number

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_failed">Link to this property</a>

messages\_pending: number

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_pending">Link to this property</a>

messages\_skipped: number

Messages that discovery skipped (for example, phish submissions, which the job cannot action).

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_skipped">Link to this property</a>

messages\_successful: number

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_successful">Link to this property</a>

<details>

<summary>

search\_params: object {action\_log, alert\_id, delivery\_status, 15 more }

</summary>

Deprecatedaction\_log: optional boolean

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20action_log">Link to this property</a>

alert\_id: optional string

Alert ID of the detection to filter by.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_status: optional "delivered"or "moved"or "quarantined"or 5 more

Delivery status to filter by.

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status">Link to this property</a>

detections\_only: optional boolean

Whether to include only detections in search results.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20detections_only">Link to this property</a>

domain: optional string

Match messages that mention this domain — sender domain, recipient domain, or a domain in a link.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20domain">Link to this property</a>

end: optional string

End of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20end">Link to this property</a>

exact\_subject: optional string

Match messages whose subject line equals this value exactly.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20exact_subject">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Dispositions to filter by.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

message\_action: optional "PREVIEW"or "QUARANTINE\_RELEASED"or "MOVED"

Message actions to filter by.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%201">Link to this property</a>

"MOVED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action">Link to this property</a>

message\_id: optional string

Message-ID header value to filter by.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_id">Link to this property</a>

metric: optional string

Metric name to filter the search by.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20metric">Link to this property</a>

query: optional string

Space-delimited search term. Case-insensitive.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20query">Link to this property</a>

recipient: optional string

Match messages whose recipient is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20recipient">Link to this property</a>

sender: optional string

Match messages whose sender is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20sender">Link to this property</a>

smtp\_helo\_ip: optional string

Matches messages whose SMTP HELO server IP address equals this value.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20smtp_helo_ip">Link to this property</a>

start: optional string

Beginning of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20start">Link to this property</a>

subject: optional string

Match messages whose subject contains these keywords, in any order.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20subject">Link to this property</a>

submissions: optional boolean

Whether to search reclassification submissions instead of original messages.

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20submissions">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params">Link to this property</a>

<details>

<summary>

status: "PENDING"or "DISCOVERING"or "PROCESSING"or 3 more

Status of a bulk action job.

</summary>

One of the following:

"PENDING"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"DISCOVERING"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"PROCESSING"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"COMPLETED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"FAILED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"CANCELLED"

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

total\_messages\_discovered: number

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20total_messages_discovered">Link to this property</a>

comment: optional string

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20comment">Link to this property</a>

completed\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20completed_at">Link to this property</a>

started\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

status\_message: optional string

<a href="#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)%20%3E%20(property)%20status_message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.bulk.cancel%20%3E%20(model)%20cancel_create_response%20%3E%20(schema)>)