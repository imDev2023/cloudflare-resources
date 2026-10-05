---
title: Investigate
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Investigate

##### [Search email messages](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/list)

GET/accounts/{account\_id}/email-security/investigate

##### [Get message details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}

##### ModelsExpand Collapse

<details>

<summary>

InvestigateListResponse object {id, action\_log, client\_recipients, 32 more }

</summary>

id: string

Unique identifier for a message retrieved from investigation.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

Deprecatedaction\_log: array of object {completed\_at, operation, completed\_timestamp, 2 more }

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

</summary>

completed\_at: string

Timestamp when action completed.

formatdate-time

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20completed_at">Link to this property</a>

<details>

<summary>

operation: "MOVE"or "RELEASE"or "RECLASSIFY"or 3 more

Type of action performed.

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"RECLASSIFY"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"QUARANTINE\_RELEASE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"PREVIEW"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation">Link to this property</a>

Deprecatedcompleted\_timestamp: optional string

Use <code>completed_at</code> instead.

Deprecated, use <code>completed_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20completed_timestamp">Link to this property</a>

<details>

<summary>

properties: optional object {folder, requested\_by }

Additional properties for the action.

</summary>

folder: optional string

Target folder for move operations.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties%20%3E%20(property)%20folder">Link to this property</a>

requested\_by: optional string

User who requested the action.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties%20%3E%20(property)%20requested_by">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

status: optional string

Status of the action.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20action_log">Link to this property</a>

client\_recipients: array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20client_recipients">Link to this property</a>

detection\_reasons: array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20detection_reasons">Link to this property</a>

is\_phish\_submission: boolean

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20is_phish_submission">Link to this property</a>

is\_quarantined: boolean

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20is_quarantined">Link to this property</a>

postfix\_id: string

The identifier of the message.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20postfix_id">Link to this property</a>

<details>

<summary>

properties: object {allowlisted\_pattern, allowlisted\_pattern\_type, blocklisted\_message, 2 more }

Message processing properties.

</summary>

allowlisted\_pattern: optional string

Pattern that allowlisted this message.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern">Link to this property</a>

<details>

<summary>

allowlisted\_pattern\_type: optional "quarantine\_release"or "acceptable\_sender"or "allowed\_sender"or 5 more

Type of allowlist pattern.

</summary>

One of the following:

"quarantine\_release"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%200">Link to this property</a>

"acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%201">Link to this property</a>

"allowed\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%202">Link to this property</a>

"allowed\_recipient"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%203">Link to this property</a>

"domain\_similarity"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%204">Link to this property</a>

"domain\_recency"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%205">Link to this property</a>

"managed\_acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%206">Link to this property</a>

"outbound\_ndr"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type">Link to this property</a>

blocklisted\_message: optional boolean

Whether message was blocklisted.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20blocklisted_message">Link to this property</a>

blocklisted\_pattern: optional string

Pattern that blocklisted this message.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20blocklisted_pattern">Link to this property</a>

<details>

<summary>

whitelisted\_pattern\_type: optional "quarantine\_release"or "acceptable\_sender"or "allowed\_sender"or 5 more

Legacy field for allowlist pattern type.

</summary>

One of the following:

"quarantine\_release"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%200">Link to this property</a>

"acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%201">Link to this property</a>

"allowed\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%202">Link to this property</a>

"allowed\_recipient"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%203">Link to this property</a>

"domain\_similarity"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%204">Link to this property</a>

"domain\_recency"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%205">Link to this property</a>

"managed\_acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%206">Link to this property</a>

"outbound\_ndr"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20properties">Link to this property</a>

Deprecatedts: string

Use <code>scanned_at</code> instead.

Deprecated, use <code>scanned_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20ts">Link to this property</a>

alert\_id: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_mode: optional "DIRECT"or "BCC"or "JOURNAL"or 8 more

</summary>

One of the following:

"DIRECT"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%200">Link to this property</a>

"BCC"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%201">Link to this property</a>

"JOURNAL"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%202">Link to this property</a>

"REVIEW\_SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%203">Link to this property</a>

"DMARC\_UNVERIFIED"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%204">Link to this property</a>

"DMARC\_FAILURE\_REPORT"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%205">Link to this property</a>

"DMARC\_AGGREGATE\_REPORT"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%206">Link to this property</a>

"THREAT\_INTEL\_SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%207">Link to this property</a>

"SIMULATION\_SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%208">Link to this property</a>

"API"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%209">Link to this property</a>

"RETRO\_SCAN"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%2010">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode">Link to this property</a>

<details>

<summary>

delivery\_status: optional array of "delivered"or "moved"or "quarantined"or 5 more

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status">Link to this property</a>

edf\_hash: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20edf_hash">Link to this property</a>

envelope\_from: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20envelope_from">Link to this property</a>

envelope\_to: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20envelope_to">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

Deprecatedfindings: optional array of object {attachment, detail, detection, 6 more }

Use the <code>findings</code> field from GET /investigate/{investigate\_id}/detections instead.

Deprecated, use the <code>findings</code> field from <code>GET /investigate/{investigate_id}/detections</code> instead. End of life: November 1, 2026. Detection findings for this message.

</summary>

attachment: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20attachment">Link to this property</a>

detail: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detail">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

field: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20field">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

portion: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20portion">Link to this property</a>

reason: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20reason">Link to this property</a>

score: optional number

formatdouble

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

value: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20findings">Link to this property</a>

from: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20from">Link to this property</a>

from\_name: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20from_name">Link to this property</a>

htmltext\_structure\_hash: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20htmltext_structure_hash">Link to this property</a>

message\_id: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20message_id">Link to this property</a>

<details>

<summary>

post\_delivery\_operations: optional array of "PREVIEW"or "QUARANTINE\_RELEASE"or "SUBMISSION"or "MOVE"

Post-delivery operations performed on this message.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"MOVE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations">Link to this property</a>

postfix\_id\_outbound: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20postfix_id_outbound">Link to this property</a>

replyto: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20replyto">Link to this property</a>

scanned\_at: optional string

When the message was scanned (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20scanned_at">Link to this property</a>

sent\_at: optional string

When the message was sent (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20sent_at">Link to this property</a>

sent\_date: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20sent_date">Link to this property</a>

smtp\_helo\_server\_ip: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20smtp_helo_server_ip">Link to this property</a>

smtp\_previous\_hop\_ip: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20smtp_previous_hop_ip">Link to this property</a>

subject: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20subject">Link to this property</a>

threat\_categories: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories">Link to this property</a>

to: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20to">Link to this property</a>

to\_name: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20to_name">Link to this property</a>

<details>

<summary>

validation: optional object {comment, dkim, dmarc, spf }

</summary>

comment: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20comment">Link to this property</a>

<details>

<summary>

dkim: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim">Link to this property</a>

<details>

<summary>

dmarc: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc">Link to this property</a>

<details>

<summary>

spf: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20validation">Link to this property</a>

x\_originating\_ip: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)%20%3E%20(property)%20x_originating_ip">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_list_response%20%3E%20(schema)>)

<details>

<summary>

InvestigateGetResponse object {id, action\_log, client\_recipients, 32 more }

</summary>

id: string

Unique identifier for a message retrieved from investigation.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

Deprecatedaction\_log: array of object {completed\_at, operation, completed\_timestamp, 2 more }

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

</summary>

completed\_at: string

Timestamp when action completed.

formatdate-time

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20completed_at">Link to this property</a>

<details>

<summary>

operation: "MOVE"or "RELEASE"or "RECLASSIFY"or 3 more

Type of action performed.

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"RECLASSIFY"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"QUARANTINE\_RELEASE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"PREVIEW"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation">Link to this property</a>

Deprecatedcompleted\_timestamp: optional string

Use <code>completed_at</code> instead.

Deprecated, use <code>completed_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20completed_timestamp">Link to this property</a>

<details>

<summary>

properties: optional object {folder, requested\_by }

Additional properties for the action.

</summary>

folder: optional string

Target folder for move operations.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties%20%3E%20(property)%20folder">Link to this property</a>

requested\_by: optional string

User who requested the action.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties%20%3E%20(property)%20requested_by">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

status: optional string

Status of the action.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20action_log">Link to this property</a>

client\_recipients: array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20client_recipients">Link to this property</a>

detection\_reasons: array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20detection_reasons">Link to this property</a>

is\_phish\_submission: boolean

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20is_phish_submission">Link to this property</a>

is\_quarantined: boolean

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20is_quarantined">Link to this property</a>

postfix\_id: string

The identifier of the message.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20postfix_id">Link to this property</a>

<details>

<summary>

properties: object {allowlisted\_pattern, allowlisted\_pattern\_type, blocklisted\_message, 2 more }

Message processing properties.

</summary>

allowlisted\_pattern: optional string

Pattern that allowlisted this message.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern">Link to this property</a>

<details>

<summary>

allowlisted\_pattern\_type: optional "quarantine\_release"or "acceptable\_sender"or "allowed\_sender"or 5 more

Type of allowlist pattern.

</summary>

One of the following:

"quarantine\_release"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%200">Link to this property</a>

"acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%201">Link to this property</a>

"allowed\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%202">Link to this property</a>

"allowed\_recipient"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%203">Link to this property</a>

"domain\_similarity"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%204">Link to this property</a>

"domain\_recency"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%205">Link to this property</a>

"managed\_acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%206">Link to this property</a>

"outbound\_ndr"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type">Link to this property</a>

blocklisted\_message: optional boolean

Whether message was blocklisted.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20blocklisted_message">Link to this property</a>

blocklisted\_pattern: optional string

Pattern that blocklisted this message.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20blocklisted_pattern">Link to this property</a>

<details>

<summary>

whitelisted\_pattern\_type: optional "quarantine\_release"or "acceptable\_sender"or "allowed\_sender"or 5 more

Legacy field for allowlist pattern type.

</summary>

One of the following:

"quarantine\_release"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%200">Link to this property</a>

"acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%201">Link to this property</a>

"allowed\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%202">Link to this property</a>

"allowed\_recipient"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%203">Link to this property</a>

"domain\_similarity"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%204">Link to this property</a>

"domain\_recency"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%205">Link to this property</a>

"managed\_acceptable\_sender"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%206">Link to this property</a>

"outbound\_ndr"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20properties">Link to this property</a>

Deprecatedts: string

Use <code>scanned_at</code> instead.

Deprecated, use <code>scanned_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20ts">Link to this property</a>

alert\_id: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_mode: optional "DIRECT"or "BCC"or "JOURNAL"or 8 more

</summary>

One of the following:

"DIRECT"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%200">Link to this property</a>

"BCC"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%201">Link to this property</a>

"JOURNAL"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%202">Link to this property</a>

"REVIEW\_SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%203">Link to this property</a>

"DMARC\_UNVERIFIED"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%204">Link to this property</a>

"DMARC\_FAILURE\_REPORT"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%205">Link to this property</a>

"DMARC\_AGGREGATE\_REPORT"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%206">Link to this property</a>

"THREAT\_INTEL\_SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%207">Link to this property</a>

"SIMULATION\_SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%208">Link to this property</a>

"API"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%209">Link to this property</a>

"RETRO\_SCAN"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode%20%3E%20(member)%2010">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_mode">Link to this property</a>

<details>

<summary>

delivery\_status: optional array of "delivered"or "moved"or "quarantined"or 5 more

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20delivery_status">Link to this property</a>

edf\_hash: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20edf_hash">Link to this property</a>

envelope\_from: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20envelope_from">Link to this property</a>

envelope\_to: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20envelope_to">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

Deprecatedfindings: optional array of object {attachment, detail, detection, 6 more }

Use the <code>findings</code> field from GET /investigate/{investigate\_id}/detections instead.

Deprecated, use the <code>findings</code> field from <code>GET /investigate/{investigate_id}/detections</code> instead. End of life: November 1, 2026. Detection findings for this message.

</summary>

attachment: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20attachment">Link to this property</a>

detail: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detail">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

field: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20field">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

portion: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20portion">Link to this property</a>

reason: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20reason">Link to this property</a>

score: optional number

formatdouble

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

value: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20findings">Link to this property</a>

from: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20from">Link to this property</a>

from\_name: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20from_name">Link to this property</a>

htmltext\_structure\_hash: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20htmltext_structure_hash">Link to this property</a>

message\_id: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20message_id">Link to this property</a>

<details>

<summary>

post\_delivery\_operations: optional array of "PREVIEW"or "QUARANTINE\_RELEASE"or "SUBMISSION"or "MOVE"

Post-delivery operations performed on this message.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"SUBMISSION"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"MOVE"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20post_delivery_operations">Link to this property</a>

postfix\_id\_outbound: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20postfix_id_outbound">Link to this property</a>

replyto: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20replyto">Link to this property</a>

scanned\_at: optional string

When the message was scanned (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20scanned_at">Link to this property</a>

sent\_at: optional string

When the message was sent (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20sent_at">Link to this property</a>

sent\_date: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20sent_date">Link to this property</a>

smtp\_helo\_server\_ip: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20smtp_helo_server_ip">Link to this property</a>

smtp\_previous\_hop\_ip: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20smtp_previous_hop_ip">Link to this property</a>

subject: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20subject">Link to this property</a>

threat\_categories: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories">Link to this property</a>

to: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20to">Link to this property</a>

to\_name: optional array of string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20to_name">Link to this property</a>

<details>

<summary>

validation: optional object {comment, dkim, dmarc, spf }

</summary>

comment: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20comment">Link to this property</a>

<details>

<summary>

dkim: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim">Link to this property</a>

<details>

<summary>

dmarc: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc">Link to this property</a>

<details>

<summary>

spf: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20validation">Link to this property</a>

x\_originating\_ip: optional string

<a href="#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)%20%3E%20(property)%20x_originating_ip">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate%20%3E%20(model)%20investigate_get_response%20%3E%20(schema)>)

#### InvestigateDetections

##### [Get message detection details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/detections/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}/detections

##### ModelsExpand Collapse

<details>

<summary>

DetectionGetResponse object {action, attachments, findings, 6 more }

</summary>

action: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

attachments: array of object {size, content\_type, detection, 6 more }

</summary>

size: number

Size of the attachment in bytes.

minimum0

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

content\_type: optional string

MIME type of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20content_type">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Detection result for this attachment.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

encrypted: optional boolean

Whether the attachment is encrypted.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20encrypted">Link to this property</a>

filename: optional string

Name of the attached file.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20filename">Link to this property</a>

md5: optional string

MD5 hash of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20md5">Link to this property</a>

name: optional string

Attachment name (alternative to filename).

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

sha1: optional string

SHA1 hash of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20sha1">Link to this property</a>

sha256: optional string

SHA256 hash of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20sha256">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments">Link to this property</a>

<details>

<summary>

findings: array of object {attachment, detail, detection, 6 more }

</summary>

attachment: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20attachment">Link to this property</a>

detail: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detail">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Detection result associated with this finding.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

field: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20field">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

portion: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20portion">Link to this property</a>

reason: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20reason">Link to this property</a>

score: optional number

formatdouble

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

value: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings">Link to this property</a>

<details>

<summary>

headers: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20headers">Link to this property</a>

<details>

<summary>

links: array of object {href, text }

</summary>

href: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20links%20%3E%20(items)%20%3E%20(property)%20href">Link to this property</a>

text: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20links%20%3E%20(items)%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20links">Link to this property</a>

<details>

<summary>

sender\_info: object {as\_name, as\_number, geo, 2 more }

</summary>

as\_name: optional string

The name of the autonomous system.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20as_name">Link to this property</a>

as\_number: optional number

The number of the autonomous system.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20as_number">Link to this property</a>

geo: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20geo">Link to this property</a>

ip: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20ip">Link to this property</a>

pld: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20pld">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info">Link to this property</a>

<details>

<summary>

threat\_categories: array of object {id, description, name }

</summary>

id: optional number

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories">Link to this property</a>

<details>

<summary>

validation: object {comment, dkim, dmarc, spf }

</summary>

comment: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20comment">Link to this property</a>

<details>

<summary>

dkim: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim">Link to this property</a>

<details>

<summary>

dmarc: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc">Link to this property</a>

<details>

<summary>

spf: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)>)

#### InvestigatePreview

##### [Get preview for a detection](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/preview/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}/preview

##### [Generate preview for a non-detection message](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/preview/methods/create)

POST/accounts/{account\_id}/email-security/investigate/preview

##### ModelsExpand Collapse

<details>

<summary>

PreviewGetResponse object {screenshot }

</summary>

screenshot: string

A base64 encoded PNG image of the email.

<a href="#(resource)%20email_security.investigate.preview%20%3E%20(model)%20preview_get_response%20%3E%20(schema)%20%3E%20(property)%20screenshot">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.preview%20%3E%20(model)%20preview_get_response%20%3E%20(schema)>)

<details>

<summary>

PreviewCreateResponse object {screenshot }

</summary>

screenshot: string

A base64 encoded PNG image of the email.

<a href="#(resource)%20email_security.investigate.preview%20%3E%20(model)%20preview_create_response%20%3E%20(schema)%20%3E%20(property)%20screenshot">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.preview%20%3E%20(model)%20preview_create_response%20%3E%20(schema)>)

#### InvestigateRaw

##### [Get raw email content](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/raw/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}/raw

##### ModelsExpand Collapse

<details>

<summary>

RawGetResponse object {raw }

</summary>

raw: string

A UTF-8 encoded eml file of the email.

<a href="#(resource)%20email_security.investigate.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)%20%3E%20(property)%20raw">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)>)

#### InvestigateTrace

##### [Get email trace](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/trace/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}/trace

##### ModelsExpand Collapse

<details>

<summary>

TraceGetResponse object {inbound, outbound }

</summary>

<details>

<summary>

inbound: object {lines, pending }

</summary>

<details>

<summary>

lines: optional array of object {lineno, logged\_at, message, ts }

</summary>

lineno: optional number

Line number in the trace log.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20lineno">Link to this property</a>

logged\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20logged_at">Link to this property</a>

message: optional string

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

Deprecatedts: optional string

Use <code>logged_at</code> instead.

Deprecated, use <code>logged_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20ts">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines">Link to this property</a>

pending: optional boolean

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20pending">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound">Link to this property</a>

<details>

<summary>

outbound: object {lines, pending }

</summary>

<details>

<summary>

lines: optional array of object {lineno, logged\_at, message, ts }

</summary>

lineno: optional number

Line number in the trace log.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20lineno">Link to this property</a>

logged\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20logged_at">Link to this property</a>

message: optional string

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

Deprecatedts: optional string

Use <code>logged_at</code> instead.

Deprecated, use <code>logged_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20ts">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines">Link to this property</a>

pending: optional boolean

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20pending">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)>)

#### InvestigateMove

##### [Move a message](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/move/methods/create)

POST/accounts/{account\_id}/email-security/investigate/{investigate\_id}/move

##### [Move messages](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/move/methods/bulk)

POST/accounts/{account\_id}/email-security/investigate/move

##### ModelsExpand Collapse

<details>

<summary>

MoveCreateResponse object {success, completed\_at, completed\_timestamp, 6 more }

</summary>

success: boolean

Whether the operation succeeded.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

completed\_at: optional string

When the move operation completed (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20completed_at">Link to this property</a>

Deprecatedcompleted\_timestamp: optional string

Use <code>completed_at</code> instead.

Deprecated, use <code>completed_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20completed_timestamp">Link to this property</a>

destination: optional string

Destination folder for the message.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

Deprecateditem\_count: optional number

This field is deprecated.

Number of items moved. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20item_count">Link to this property</a>

message\_id: optional string

Message identifier.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20message_id">Link to this property</a>

operation: optional string

Type of operation performed.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20operation">Link to this property</a>

recipient: optional string

Recipient email address.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20recipient">Link to this property</a>

status: optional string

Operation status.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_create_response%20%3E%20(schema)>)

<details>

<summary>

MoveBulkResponse object {success, completed\_at, completed\_timestamp, 6 more }

</summary>

success: boolean

Whether the operation succeeded.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

completed\_at: optional string

When the move operation completed (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20completed_at">Link to this property</a>

Deprecatedcompleted\_timestamp: optional string

Use <code>completed_at</code> instead.

Deprecated, use <code>completed_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20completed_timestamp">Link to this property</a>

destination: optional string

Destination folder for the message.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

Deprecateditem\_count: optional number

This field is deprecated.

Number of items moved. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20item_count">Link to this property</a>

message\_id: optional string

Message identifier.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20message_id">Link to this property</a>

operation: optional string

Type of operation performed.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20operation">Link to this property</a>

recipient: optional string

Recipient email address.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20recipient">Link to this property</a>

status: optional string

Operation status.

<a href="#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.move%20%3E%20(model)%20move_bulk_response%20%3E%20(schema)>)

#### InvestigateReclassify

##### [Change email classification](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/reclassify/methods/create)

Deprecated

POST/accounts/{account\_id}/email-security/investigate/{investigate\_id}/reclassify

##### ModelsExpand Collapse

ReclassifyCreateResponse = unknown

[Link to this property](<#(resource)%20email_security.investigate.reclassify%20%3E%20(model)%20reclassify_create_response%20%3E%20(schema)>)

#### InvestigateRelease

##### [Release messages from quarantine](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/release/methods/bulk)

POST/accounts/{account\_id}/email-security/investigate/release

##### ModelsExpand Collapse

<details>

<summary>

ReleaseBulkResponse object {id, delivered, failed, 2 more }

</summary>

id: string

Unique identifier for a message retrieved from investigation.

<a href="#(resource)%20email_security.investigate.release%20%3E%20(model)%20release_bulk_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

delivered: optional array of string

<a href="#(resource)%20email_security.investigate.release%20%3E%20(model)%20release_bulk_response%20%3E%20(schema)%20%3E%20(property)%20delivered">Link to this property</a>

failed: optional array of string

<a href="#(resource)%20email_security.investigate.release%20%3E%20(model)%20release_bulk_response%20%3E%20(schema)%20%3E%20(property)%20failed">Link to this property</a>

Deprecatedpostfix\_id: optional string

Use <code>id</code> instead.

Deprecated, use <code>id</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.release%20%3E%20(model)%20release_bulk_response%20%3E%20(schema)%20%3E%20(property)%20postfix_id">Link to this property</a>

undelivered: optional array of string

<a href="#(resource)%20email_security.investigate.release%20%3E%20(model)%20release_bulk_response%20%3E%20(schema)%20%3E%20(property)%20undelivered">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.release%20%3E%20(model)%20release_bulk_response%20%3E%20(schema)>)

#### InvestigateBulk

##### [List bulk action jobs](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/list)

GET/accounts/{account\_id}/email-security/investigate/bulk

##### [Create a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/create)

POST/accounts/{account\_id}/email-security/investigate/bulk

##### [Get bulk action job details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/get)

GET/accounts/{account\_id}/email-security/investigate/bulk/{job\_id}

##### [Delete a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/delete)

DELETE/accounts/{account\_id}/email-security/investigate/bulk/{job\_id}

##### ModelsExpand Collapse

<details>

<summary>

BulkListResponse object {action\_params, action\_type, created\_at, 13 more }

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

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%200">Link to this property</a>

"JunkEmail"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%201">Link to this property</a>

"DeletedItems"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%202">Link to this property</a>

"RecoverableItemsDeletions"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%203">Link to this property</a>

"RecoverableItemsPurges"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination">Link to this property</a>

type: "MOVE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

Deprecatedexpected\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

This field is nonfunctional.

Nonfunctional field. End of life: December 1, 2026.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Release object {type }

</summary>

type: "RELEASE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params">Link to this property</a>

<details>

<summary>

action\_type: "MOVE"or "RELEASE"

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20action_type">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

job\_id: string

formatuuid

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20job_id">Link to this property</a>

messages\_cancelled: number

Messages that were cancelled: rows cancelled via the API before being claimed, and rows whose in-flight attempt ended when the job reached a terminal state. Together the counters satisfy total\_messages\_discovered = messages\_pending + messages\_successful + messages\_failed + messages\_skipped + messages\_cancelled.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20messages_cancelled">Link to this property</a>

messages\_failed: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20messages_failed">Link to this property</a>

messages\_pending: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20messages_pending">Link to this property</a>

messages\_skipped: number

Messages that discovery skipped (for example, phish submissions, which the job cannot action).

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20messages_skipped">Link to this property</a>

messages\_successful: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20messages_successful">Link to this property</a>

<details>

<summary>

search\_params: object {action\_log, alert\_id, delivery\_status, 15 more }

</summary>

Deprecatedaction\_log: optional boolean

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20action_log">Link to this property</a>

alert\_id: optional string

Alert ID of the detection to filter by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_status: optional "delivered"or "moved"or "quarantined"or 5 more

Delivery status to filter by.

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status">Link to this property</a>

detections\_only: optional boolean

Whether to include only detections in search results.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20detections_only">Link to this property</a>

domain: optional string

Match messages that mention this domain — sender domain, recipient domain, or a domain in a link.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20domain">Link to this property</a>

end: optional string

End of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20end">Link to this property</a>

exact\_subject: optional string

Match messages whose subject line equals this value exactly.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20exact_subject">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Dispositions to filter by.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

message\_action: optional "PREVIEW"or "QUARANTINE\_RELEASED"or "MOVED"

Message actions to filter by.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%201">Link to this property</a>

"MOVED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action">Link to this property</a>

message\_id: optional string

Message-ID header value to filter by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_id">Link to this property</a>

metric: optional string

Metric name to filter the search by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20metric">Link to this property</a>

query: optional string

Space-delimited search term. Case-insensitive.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20query">Link to this property</a>

recipient: optional string

Match messages whose recipient is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20recipient">Link to this property</a>

sender: optional string

Match messages whose sender is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20sender">Link to this property</a>

smtp\_helo\_ip: optional string

Matches messages whose SMTP HELO server IP address equals this value.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20smtp_helo_ip">Link to this property</a>

start: optional string

Beginning of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20start">Link to this property</a>

subject: optional string

Match messages whose subject contains these keywords, in any order.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20subject">Link to this property</a>

submissions: optional boolean

Whether to search reclassification submissions instead of original messages.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20submissions">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20search_params">Link to this property</a>

<details>

<summary>

status: "PENDING"or "DISCOVERING"or "PROCESSING"or 3 more

Status of a bulk action job.

</summary>

One of the following:

"PENDING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"DISCOVERING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"PROCESSING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"COMPLETED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"FAILED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"CANCELLED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

total\_messages\_discovered: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20total_messages_discovered">Link to this property</a>

comment: optional string

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20comment">Link to this property</a>

completed\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20completed_at">Link to this property</a>

started\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

status\_message: optional string

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)%20%3E%20(property)%20status_message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_list_response%20%3E%20(schema)>)

<details>

<summary>

BulkCreateResponse object {action\_params, action\_type, created\_at, 13 more }

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

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%200">Link to this property</a>

"JunkEmail"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%201">Link to this property</a>

"DeletedItems"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%202">Link to this property</a>

"RecoverableItemsDeletions"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%203">Link to this property</a>

"RecoverableItemsPurges"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination">Link to this property</a>

type: "MOVE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

Deprecatedexpected\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

This field is nonfunctional.

Nonfunctional field. End of life: December 1, 2026.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Release object {type }

</summary>

type: "RELEASE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_params">Link to this property</a>

<details>

<summary>

action\_type: "MOVE"or "RELEASE"

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20action_type">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

job\_id: string

formatuuid

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20job_id">Link to this property</a>

messages\_cancelled: number

Messages that were cancelled: rows cancelled via the API before being claimed, and rows whose in-flight attempt ended when the job reached a terminal state. Together the counters satisfy total\_messages\_discovered = messages\_pending + messages\_successful + messages\_failed + messages\_skipped + messages\_cancelled.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_cancelled">Link to this property</a>

messages\_failed: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_failed">Link to this property</a>

messages\_pending: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_pending">Link to this property</a>

messages\_skipped: number

Messages that discovery skipped (for example, phish submissions, which the job cannot action).

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_skipped">Link to this property</a>

messages\_successful: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20messages_successful">Link to this property</a>

<details>

<summary>

search\_params: object {action\_log, alert\_id, delivery\_status, 15 more }

</summary>

Deprecatedaction\_log: optional boolean

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20action_log">Link to this property</a>

alert\_id: optional string

Alert ID of the detection to filter by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_status: optional "delivered"or "moved"or "quarantined"or 5 more

Delivery status to filter by.

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status">Link to this property</a>

detections\_only: optional boolean

Whether to include only detections in search results.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20detections_only">Link to this property</a>

domain: optional string

Match messages that mention this domain — sender domain, recipient domain, or a domain in a link.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20domain">Link to this property</a>

end: optional string

End of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20end">Link to this property</a>

exact\_subject: optional string

Match messages whose subject line equals this value exactly.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20exact_subject">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Dispositions to filter by.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

message\_action: optional "PREVIEW"or "QUARANTINE\_RELEASED"or "MOVED"

Message actions to filter by.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%201">Link to this property</a>

"MOVED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action">Link to this property</a>

message\_id: optional string

Message-ID header value to filter by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_id">Link to this property</a>

metric: optional string

Metric name to filter the search by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20metric">Link to this property</a>

query: optional string

Space-delimited search term. Case-insensitive.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20query">Link to this property</a>

recipient: optional string

Match messages whose recipient is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20recipient">Link to this property</a>

sender: optional string

Match messages whose sender is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20sender">Link to this property</a>

smtp\_helo\_ip: optional string

Matches messages whose SMTP HELO server IP address equals this value.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20smtp_helo_ip">Link to this property</a>

start: optional string

Beginning of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20start">Link to this property</a>

subject: optional string

Match messages whose subject contains these keywords, in any order.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20subject">Link to this property</a>

submissions: optional boolean

Whether to search reclassification submissions instead of original messages.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20submissions">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20search_params">Link to this property</a>

<details>

<summary>

status: "PENDING"or "DISCOVERING"or "PROCESSING"or 3 more

Status of a bulk action job.

</summary>

One of the following:

"PENDING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"DISCOVERING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"PROCESSING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"COMPLETED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"FAILED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"CANCELLED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

total\_messages\_discovered: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20total_messages_discovered">Link to this property</a>

comment: optional string

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20comment">Link to this property</a>

completed\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20completed_at">Link to this property</a>

started\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

status\_message: optional string

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)%20%3E%20(property)%20status_message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_create_response%20%3E%20(schema)>)

<details>

<summary>

BulkGetResponse object {action\_params, action\_type, created\_at, 13 more }

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

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%200">Link to this property</a>

"JunkEmail"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%201">Link to this property</a>

"DeletedItems"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%202">Link to this property</a>

"RecoverableItemsDeletions"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%203">Link to this property</a>

"RecoverableItemsPurges"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination">Link to this property</a>

type: "MOVE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

Deprecatedexpected\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

This field is nonfunctional.

Nonfunctional field. End of life: December 1, 2026.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Release object {type }

</summary>

type: "RELEASE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_params">Link to this property</a>

<details>

<summary>

action\_type: "MOVE"or "RELEASE"

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20action_type">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

job\_id: string

formatuuid

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20job_id">Link to this property</a>

messages\_cancelled: number

Messages that were cancelled: rows cancelled via the API before being claimed, and rows whose in-flight attempt ended when the job reached a terminal state. Together the counters satisfy total\_messages\_discovered = messages\_pending + messages\_successful + messages\_failed + messages\_skipped + messages\_cancelled.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20messages_cancelled">Link to this property</a>

messages\_failed: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20messages_failed">Link to this property</a>

messages\_pending: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20messages_pending">Link to this property</a>

messages\_skipped: number

Messages that discovery skipped (for example, phish submissions, which the job cannot action).

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20messages_skipped">Link to this property</a>

messages\_successful: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20messages_successful">Link to this property</a>

<details>

<summary>

search\_params: object {action\_log, alert\_id, delivery\_status, 15 more }

</summary>

Deprecatedaction\_log: optional boolean

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20action_log">Link to this property</a>

alert\_id: optional string

Alert ID of the detection to filter by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_status: optional "delivered"or "moved"or "quarantined"or 5 more

Delivery status to filter by.

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20delivery_status">Link to this property</a>

detections\_only: optional boolean

Whether to include only detections in search results.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20detections_only">Link to this property</a>

domain: optional string

Match messages that mention this domain — sender domain, recipient domain, or a domain in a link.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20domain">Link to this property</a>

end: optional string

End of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20end">Link to this property</a>

exact\_subject: optional string

Match messages whose subject line equals this value exactly.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20exact_subject">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Dispositions to filter by.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

message\_action: optional "PREVIEW"or "QUARANTINE\_RELEASED"or "MOVED"

Message actions to filter by.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%201">Link to this property</a>

"MOVED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_action">Link to this property</a>

message\_id: optional string

Message-ID header value to filter by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20message_id">Link to this property</a>

metric: optional string

Metric name to filter the search by.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20metric">Link to this property</a>

query: optional string

Space-delimited search term. Case-insensitive.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20query">Link to this property</a>

recipient: optional string

Match messages whose recipient is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20recipient">Link to this property</a>

sender: optional string

Match messages whose sender is this email address or domain.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20sender">Link to this property</a>

smtp\_helo\_ip: optional string

Matches messages whose SMTP HELO server IP address equals this value.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20smtp_helo_ip">Link to this property</a>

start: optional string

Beginning of search date range.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20start">Link to this property</a>

subject: optional string

Match messages whose subject contains these keywords, in any order.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20subject">Link to this property</a>

submissions: optional boolean

Whether to search reclassification submissions instead of original messages.

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params%20%3E%20(property)%20submissions">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20search_params">Link to this property</a>

<details>

<summary>

status: "PENDING"or "DISCOVERING"or "PROCESSING"or 3 more

Status of a bulk action job.

</summary>

One of the following:

"PENDING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"DISCOVERING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"PROCESSING"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"COMPLETED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"FAILED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"CANCELLED"

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

total\_messages\_discovered: number

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20total_messages_discovered">Link to this property</a>

comment: optional string

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20comment">Link to this property</a>

completed\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20completed_at">Link to this property</a>

started\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

status\_message: optional string

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(property)%20status_message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)>)

<details>

<summary>

BulkDeleteResponse object {id }

</summary>

id: string

formatuuid

<a href="#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.bulk%20%3E%20(model)%20bulk_delete_response%20%3E%20(schema)>)

#### InvestigateBulkCancel

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

#### InvestigateBulkMessages

##### [List messages for a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/subresources/messages/methods/list)

GET/accounts/{account\_id}/email-security/investigate/bulk/{job\_id}/messages

##### ModelsExpand Collapse

<details>

<summary>

MessageListResponse object {action\_params, action\_type, created\_at, 10 more }

</summary>

<details>

<summary>

action\_params: object {client\_recipient, destination, type, expected\_disposition } or object {client\_recipient, type }

</summary>

One of the following:

<details>

<summary>

Move object {client\_recipient, destination, type, expected\_disposition }

</summary>

client\_recipient: string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20client_recipient">Link to this property</a>

<details>

<summary>

destination: "Inbox"or "JunkEmail"or "DeletedItems"or 2 more

The mailbox folder to move messages to.

</summary>

One of the following:

"Inbox"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%200">Link to this property</a>

"JunkEmail"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%201">Link to this property</a>

"DeletedItems"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%202">Link to this property</a>

"RecoverableItemsDeletions"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%203">Link to this property</a>

"RecoverableItemsPurges"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20destination">Link to this property</a>

type: "MOVE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

Deprecatedexpected\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

This field is nonfunctional.

Nonfunctional field. End of life: December 1, 2026.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200%20%3E%20(property)%20expected_disposition">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Release object {client\_recipient, type }

</summary>

client\_recipient: string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201%20%3E%20(property)%20client_recipient">Link to this property</a>

type: "RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_params">Link to this property</a>

<details>

<summary>

action\_type: "MOVE"or "RELEASE"

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20action_type">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

message\_id: string

formatuuid

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message_id">Link to this property</a>

postfix\_id: string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20postfix_id">Link to this property</a>

retry\_count: number

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20retry_count">Link to this property</a>

<details>

<summary>

status: "PENDING"or "PROCESSING"or "COMPLETED"or 3 more

Status of a message within a bulk action job.

</summary>

One of the following:

"PENDING"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"PROCESSING"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"COMPLETED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"FAILED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"CANCELLED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"SKIPPED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

alert\_id: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20alert_id">Link to this property</a>

email\_message\_id: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20email_message_id">Link to this property</a>

<details>

<summary>

message: optional object {id, action\_log, client\_recipients, 32 more }

</summary>

id: string

Unique identifier for a message retrieved from investigation.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

Deprecatedaction\_log: array of object {completed\_at, operation, completed\_timestamp, 2 more }

Use GET /investigate/{investigate\_id}/action\_log instead.

Deprecated, use <code>GET /investigate/{investigate_id}/action_log</code> instead. End of life: November 1, 2026.

</summary>

completed\_at: string

Timestamp when action completed.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20completed_at">Link to this property</a>

<details>

<summary>

operation: "MOVE"or "RELEASE"or "RECLASSIFY"or 3 more

Type of action performed.

</summary>

One of the following:

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"RECLASSIFY"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"SUBMISSION"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"QUARANTINE\_RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"PREVIEW"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20operation">Link to this property</a>

Deprecatedcompleted\_timestamp: optional string

Use <code>completed_at</code> instead.

Deprecated, use <code>completed_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20completed_timestamp">Link to this property</a>

<details>

<summary>

properties: optional object {folder, requested\_by }

Additional properties for the action.

</summary>

folder: optional string

Target folder for move operations.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties%20%3E%20(property)%20folder">Link to this property</a>

requested\_by: optional string

User who requested the action.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties%20%3E%20(property)%20requested_by">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20properties">Link to this property</a>

status: optional string

Status of the action.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20action_log">Link to this property</a>

client\_recipients: array of string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20client_recipients">Link to this property</a>

detection\_reasons: array of string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20detection_reasons">Link to this property</a>

is\_phish\_submission: boolean

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20is_phish_submission">Link to this property</a>

is\_quarantined: boolean

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20is_quarantined">Link to this property</a>

postfix\_id: string

The identifier of the message.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20postfix_id">Link to this property</a>

<details>

<summary>

properties: object {allowlisted\_pattern, allowlisted\_pattern\_type, blocklisted\_message, 2 more }

Message processing properties.

</summary>

allowlisted\_pattern: optional string

Pattern that allowlisted this message.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern">Link to this property</a>

<details>

<summary>

allowlisted\_pattern\_type: optional "quarantine\_release"or "acceptable\_sender"or "allowed\_sender"or 5 more

Type of allowlist pattern.

</summary>

One of the following:

"quarantine\_release"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%200">Link to this property</a>

"acceptable\_sender"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%201">Link to this property</a>

"allowed\_sender"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%202">Link to this property</a>

"allowed\_recipient"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%203">Link to this property</a>

"domain\_similarity"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%204">Link to this property</a>

"domain\_recency"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%205">Link to this property</a>

"managed\_acceptable\_sender"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%206">Link to this property</a>

"outbound\_ndr"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20allowlisted_pattern_type">Link to this property</a>

blocklisted\_message: optional boolean

Whether message was blocklisted.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20blocklisted_message">Link to this property</a>

blocklisted\_pattern: optional string

Pattern that blocklisted this message.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20blocklisted_pattern">Link to this property</a>

<details>

<summary>

whitelisted\_pattern\_type: optional "quarantine\_release"or "acceptable\_sender"or "allowed\_sender"or 5 more

Legacy field for allowlist pattern type.

</summary>

One of the following:

"quarantine\_release"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%200">Link to this property</a>

"acceptable\_sender"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%201">Link to this property</a>

"allowed\_sender"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%202">Link to this property</a>

"allowed\_recipient"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%203">Link to this property</a>

"domain\_similarity"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%204">Link to this property</a>

"domain\_recency"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%205">Link to this property</a>

"managed\_acceptable\_sender"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%206">Link to this property</a>

"outbound\_ndr"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties%20%3E%20(property)%20whitelisted_pattern_type">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20properties">Link to this property</a>

Deprecatedts: string

Use <code>scanned_at</code> instead.

Deprecated, use <code>scanned_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20ts">Link to this property</a>

alert\_id: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20alert_id">Link to this property</a>

<details>

<summary>

delivery\_mode: optional "DIRECT"or "BCC"or "JOURNAL"or 8 more

</summary>

One of the following:

"DIRECT"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%200">Link to this property</a>

"BCC"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%201">Link to this property</a>

"JOURNAL"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%202">Link to this property</a>

"REVIEW\_SUBMISSION"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%203">Link to this property</a>

"DMARC\_UNVERIFIED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%204">Link to this property</a>

"DMARC\_FAILURE\_REPORT"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%205">Link to this property</a>

"DMARC\_AGGREGATE\_REPORT"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%206">Link to this property</a>

"THREAT\_INTEL\_SUBMISSION"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%207">Link to this property</a>

"SIMULATION\_SUBMISSION"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%208">Link to this property</a>

"API"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%209">Link to this property</a>

"RETRO\_SCAN"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode%20%3E%20(member)%2010">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_mode">Link to this property</a>

<details>

<summary>

delivery\_status: optional array of "delivered"or "moved"or "quarantined"or 5 more

</summary>

One of the following:

"delivered"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"moved"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"quarantined"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"rejected"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deferred"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"bounced"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"queued"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"move\_failed"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20delivery_status">Link to this property</a>

edf\_hash: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20edf_hash">Link to this property</a>

envelope\_from: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20envelope_from">Link to this property</a>

envelope\_to: optional array of string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20envelope_to">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20final_disposition">Link to this property</a>

<details>

<summary>

Deprecatedfindings: optional array of object {attachment, detail, detection, 6 more }

Use the <code>findings</code> field from GET /investigate/{investigate\_id}/detections instead.

Deprecated, use the <code>findings</code> field from <code>GET /investigate/{investigate_id}/detections</code> instead. End of life: November 1, 2026. Detection findings for this message.

</summary>

attachment: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20attachment">Link to this property</a>

detail: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detail">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

field: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20field">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

portion: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20portion">Link to this property</a>

reason: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20reason">Link to this property</a>

score: optional number

formatdouble

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

value: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20findings">Link to this property</a>

from: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20from">Link to this property</a>

from\_name: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20from_name">Link to this property</a>

htmltext\_structure\_hash: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20htmltext_structure_hash">Link to this property</a>

message\_id: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20message_id">Link to this property</a>

<details>

<summary>

post\_delivery\_operations: optional array of "PREVIEW"or "QUARANTINE\_RELEASE"or "SUBMISSION"or "MOVE"

Post-delivery operations performed on this message.

</summary>

One of the following:

"PREVIEW"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"QUARANTINE\_RELEASE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"SUBMISSION"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"MOVE"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20post_delivery_operations%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20post_delivery_operations">Link to this property</a>

postfix\_id\_outbound: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20postfix_id_outbound">Link to this property</a>

replyto: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20replyto">Link to this property</a>

scanned\_at: optional string

When the message was scanned (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20scanned_at">Link to this property</a>

sent\_at: optional string

When the message was sent (UTC).

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20sent_at">Link to this property</a>

sent\_date: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20sent_date">Link to this property</a>

smtp\_helo\_server\_ip: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20smtp_helo_server_ip">Link to this property</a>

smtp\_previous\_hop\_ip: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20smtp_previous_hop_ip">Link to this property</a>

subject: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20subject">Link to this property</a>

threat\_categories: optional array of string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20threat_categories">Link to this property</a>

to: optional array of string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20to">Link to this property</a>

to\_name: optional array of string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20to_name">Link to this property</a>

<details>

<summary>

validation: optional object {comment, dkim, dmarc, spf }

</summary>

comment: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20comment">Link to this property</a>

<details>

<summary>

dkim: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dkim">Link to this property</a>

<details>

<summary>

dmarc: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc">Link to this property</a>

<details>

<summary>

spf: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation%20%3E%20(property)%20spf">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20validation">Link to this property</a>

x\_originating\_ip: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message%20%3E%20(property)%20x_originating_ip">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

processed\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20processed_at">Link to this property</a>

retry\_after: optional string

When to retry the action if it failed.

formatdate-time

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20retry_after">Link to this property</a>

status\_message: optional string

<a href="#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)%20%3E%20(property)%20status_message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.bulk.messages%20%3E%20(model)%20message_list_response%20%3E%20(schema)>)