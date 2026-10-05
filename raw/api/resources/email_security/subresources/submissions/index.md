---
title: Submissions
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Submissions

##### [List reclassify submissions](https://developers.cloudflare.com/api/resources/email_security/subresources/submissions/methods/list)

GET/accounts/{account\_id}/email-security/submissions

##### ModelsExpand Collapse

<details>

<summary>

SubmissionListResponse object {requested\_at, submission\_id, customer\_status, 15 more }

</summary>

requested\_at: string

When the submission was requested (UTC).

formatdate-time

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_at">Link to this property</a>

submission\_id: string

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20submission_id">Link to this property</a>

<details>

<summary>

customer\_status: optional "escalated"or "reviewed"or "unreviewed"

</summary>

One of the following:

"escalated"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20customer_status%20%3E%20(member)%200">Link to this property</a>

"reviewed"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20customer_status%20%3E%20(member)%201">Link to this property</a>

"unreviewed"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20customer_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20customer_status">Link to this property</a>

<details>

<summary>

escalated\_as: optional "MALICIOUS"or "SUSPICIOUS"or "SPOOF"or 3 more

The disposition a message is submitted to have.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as%20%3E%20(member)%200">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as%20%3E%20(member)%201">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as%20%3E%20(member)%202">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as%20%3E%20(member)%203">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as%20%3E%20(member)%204">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_as">Link to this property</a>

escalated\_at: optional string

When the submission was escalated to the security team.

formatdate-time

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_at">Link to this property</a>

escalated\_by: optional string

Email address of the user who escalated the submission.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_by">Link to this property</a>

escalated\_submission\_id: optional string

Submission ID of the escalated team submission, when this user submission was escalated.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20escalated_submission_id">Link to this property</a>

<details>

<summary>

original\_disposition: optional "MALICIOUS"or "SUSPICIOUS"or "SPOOF"or 3 more

The disposition a message is submitted to have.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition%20%3E%20(member)%200">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition%20%3E%20(member)%201">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition%20%3E%20(member)%202">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition%20%3E%20(member)%203">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition%20%3E%20(member)%204">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_disposition">Link to this property</a>

original\_edf\_hash: optional string

EDF hash of the original message.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_edf_hash">Link to this property</a>

original\_postfix\_id: optional string

The postfix ID of the original message that was submitted.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20original_postfix_id">Link to this property</a>

outcome: optional string

Processing outcome of the submission.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome">Link to this property</a>

<details>

<summary>

outcome\_disposition: optional "MALICIOUS"or "SUSPICIOUS"or "SPOOF"or 3 more

The disposition a message is submitted to have.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition%20%3E%20(member)%200">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition%20%3E%20(member)%201">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition%20%3E%20(member)%202">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition%20%3E%20(member)%203">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition%20%3E%20(member)%204">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20outcome_disposition">Link to this property</a>

requested\_by: optional string

Email address of the user who requested the submission.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_by">Link to this property</a>

<details>

<summary>

requested\_disposition: optional "MALICIOUS"or "SUSPICIOUS"or "SPOOF"or 3 more

The disposition a message is submitted to have.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition%20%3E%20(member)%200">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition%20%3E%20(member)%201">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition%20%3E%20(member)%202">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition%20%3E%20(member)%203">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition%20%3E%20(member)%204">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_disposition">Link to this property</a>

Deprecatedrequested\_ts: optional string

Use <code>requested_at</code> instead.

Deprecated, use <code>requested_at</code> instead.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20requested_ts">Link to this property</a>

status: optional string

Processing status of the submission.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subject: optional string

Subject line of the submitted message.

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20subject">Link to this property</a>

<details>

<summary>

type: optional "Team"or "User"

Indicates whether a team member or an end user created the submission.

</summary>

One of the following:

"Team"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"User"

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.submissions%20%3E%20(model)%20submission_list_response%20%3E%20(schema)>)