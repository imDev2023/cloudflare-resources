---
title: Abuse Reports
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Abuse Reports

##### [Submit an abuse report](https://developers.cloudflare.com/api/resources/abuse_reports/methods/create)

POST/accounts/{account\_id}/abuse-reports/{report\_param}

##### [Get an abuse report against the account](https://developers.cloudflare.com/api/resources/abuse_reports/methods/get)

GET/accounts/{account\_id}/abuse-reports/{report\_param}

##### [List abuse reports against the account](https://developers.cloudflare.com/api/resources/abuse_reports/methods/list)

GET/accounts/{account\_id}/abuse-reports

##### ModelsExpand Collapse

AbuseReportCreateResponse = string

The result should be ‘success’ for successful response

[Link to this property](<#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_create_response%20%3E%20(schema)>)

<details>

<summary>

AbuseReportGetResponse object {id, cdate, domain, 7 more }

</summary>

id: string

Public facing ID of abuse report, aka abuse\_rand.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

cdate: string

Creation date of report. Time in RFC 3339 format (<a href="https://www.rfc-editor.org/rfc/rfc3339.html">https://www.rfc-editor.org/rfc/rfc3339.html</a>)

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20cdate">Link to this property</a>

domain: string

Domain that relates to the report.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20domain">Link to this property</a>

<details>

<summary>

mitigation\_summary: object {accepted\_url\_count, active\_count, external\_host\_notified, 2 more }

A summary of the mitigations related to this report.

</summary>

accepted\_url\_count: number

How many of the reported URLs were confirmed as abusive.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20accepted_url_count">Link to this property</a>

active\_count: number

How many mitigations are active.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20active_count">Link to this property</a>

external\_host\_notified: boolean

Whether the report has been forwarded to an external hosting provider.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20external_host_notified">Link to this property</a>

in\_review\_count: number

How many mitigations are under review.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20in_review_count">Link to this property</a>

pending\_count: number

How many mitigations are pending their effective date.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20pending_count">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20mitigation_summary">Link to this property</a>

<details>

<summary>

status: "accepted"or "in\_review"

An enum value that represents the status of an abuse record

</summary>

One of the following:

"accepted"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"in\_review"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "PHISH"or "GEN"or "THREAT"or 6 more

The abuse report type

</summary>

One of the following:

"PHISH"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"GEN"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"THREAT"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"DMCA"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"EMER"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"TM"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"REG\_WHO"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"NCSEI"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"NETWORK"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

justification: optional string

Justification for the report.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20justification">Link to this property</a>

original\_work: optional string

Original work / Targeted brand in the alleged abuse.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20original_work">Link to this property</a>

<details>

<summary>

submitter: optional object {company, email, name, telephone }

Information about the submitter of the report.

</summary>

company: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20company">Link to this property</a>

email: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20email">Link to this property</a>

name: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20name">Link to this property</a>

telephone: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20telephone">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter">Link to this property</a>

urls: optional array of string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)%20%3E%20(property)%20urls">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_get_response%20%3E%20(schema)>)

<details>

<summary>

AbuseReportListResponse object {reports }

</summary>

<details>

<summary>

reports: array of object {id, cdate, domain, 7 more }

</summary>

id: string

Public facing ID of abuse report, aka abuse\_rand.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

cdate: string

Creation date of report. Time in RFC 3339 format (<a href="https://www.rfc-editor.org/rfc/rfc3339.html">https://www.rfc-editor.org/rfc/rfc3339.html</a>)

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20cdate">Link to this property</a>

domain: string

Domain that relates to the report.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

<details>

<summary>

mitigation\_summary: object {accepted\_url\_count, active\_count, external\_host\_notified, 2 more }

A summary of the mitigations related to this report.

</summary>

accepted\_url\_count: number

How many of the reported URLs were confirmed as abusive.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20accepted_url_count">Link to this property</a>

active\_count: number

How many mitigations are active.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20active_count">Link to this property</a>

external\_host\_notified: boolean

Whether the report has been forwarded to an external hosting provider.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20external_host_notified">Link to this property</a>

in\_review\_count: number

How many mitigations are under review.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20in_review_count">Link to this property</a>

pending\_count: number

How many mitigations are pending their effective date.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20mitigation_summary%20%3E%20(property)%20pending_count">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20mitigation_summary">Link to this property</a>

<details>

<summary>

status: "accepted"or "in\_review"

An enum value that represents the status of an abuse record

</summary>

One of the following:

"accepted"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"in\_review"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "PHISH"or "GEN"or "THREAT"or 6 more

The abuse report type

</summary>

One of the following:

"PHISH"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"GEN"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"THREAT"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"DMCA"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"EMER"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"TM"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"REG\_WHO"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"NCSEI"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"NETWORK"

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

justification: optional string

Justification for the report.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20justification">Link to this property</a>

original\_work: optional string

Original work / Targeted brand in the alleged abuse.

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20original_work">Link to this property</a>

<details>

<summary>

submitter: optional object {company, email, name, telephone }

Information about the submitter of the report.

</summary>

company: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20company">Link to this property</a>

email: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20email">Link to this property</a>

name: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20name">Link to this property</a>

telephone: optional string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20telephone">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter">Link to this property</a>

urls: optional array of string

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20urls">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)%20%3E%20(property)%20reports">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports%20%3E%20(model)%20abuse_report_list_response%20%3E%20(schema)>)

#### Abuse ReportsSubmitted

##### [List submitted abuse reports](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/submitted/methods/list)

GET/accounts/{account\_id}/abuse-reports/submitted

##### [Get a submitted abuse report](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/submitted/methods/get)

GET/accounts/{account\_id}/abuse-reports/submitted/{report\_id}

##### ModelsExpand Collapse

<details>

<summary>

SubmittedListResponse object {reports }

</summary>

<details>

<summary>

reports: array of object {id, cdate, denial\_reason, 4 more }

</summary>

id: string

Public report code.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

cdate: string

Time the report was submitted.

formatdate-time

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20cdate">Link to this property</a>

<details>

<summary>

denial\_reason: "unable\_to\_confirm"or "incomplete\_report"or "not\_on\_cloudflare"or 10 more

Submitter-safe reason for a denied report. Null when unavailable.

</summary>

One of the following:

"unable\_to\_confirm"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%200">Link to this property</a>

"incomplete\_report"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%201">Link to this property</a>

"not\_on\_cloudflare"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%202">Link to this property</a>

"duplicate\_report"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%203">Link to this property</a>

"content\_removed"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%204">Link to this property</a>

"report\_details\_mismatch"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%205">Link to this property</a>

"no\_abuse\_found"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%206">Link to this property</a>

"missing\_original\_work"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%207">Link to this property</a>

"direct\_url\_required"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%208">Link to this property</a>

"wrong\_report\_category"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%209">Link to this property</a>

"content\_unavailable"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%2010">Link to this property</a>

"law\_enforcement\_referral\_required"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%2011">Link to this property</a>

"domain\_dispute\_process\_required"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20denial_reason">Link to this property</a>

domain: string

Domain identified in the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

<details>

<summary>

status: "submitted"or "accepted"or "denied"

Status visible to the account that submitted the report.

</summary>

One of the following:

"submitted"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"accepted"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"denied"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "PHISH"or "GEN"or "THREAT"or 6 more

The abuse report type

</summary>

One of the following:

"PHISH"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"GEN"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"THREAT"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"DMCA"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"EMER"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"TM"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"REG\_WHO"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"NCSEI"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"NETWORK"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

submitter: optional object {company, email, name, telephone }

Information about the submitter of the report.

</summary>

company: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20company">Link to this property</a>

email: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20email">Link to this property</a>

name: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20name">Link to this property</a>

telephone: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter%20%3E%20(property)%20telephone">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports%20%3E%20(items)%20%3E%20(property)%20submitter">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)%20%3E%20(property)%20reports">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_list_response%20%3E%20(schema)>)

<details>

<summary>

SubmittedGetResponse object {id, cdate, denial\_reason, 25 more }

</summary>

id: string

Public report code.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

cdate: string

Time the report was submitted.

formatdate-time

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20cdate">Link to this property</a>

<details>

<summary>

denial\_reason: "unable\_to\_confirm"or "incomplete\_report"or "not\_on\_cloudflare"or 10 more

Submitter-safe reason for a denied report. Null when unavailable.

</summary>

One of the following:

"unable\_to\_confirm"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%200">Link to this property</a>

"incomplete\_report"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%201">Link to this property</a>

"not\_on\_cloudflare"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%202">Link to this property</a>

"duplicate\_report"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%203">Link to this property</a>

"content\_removed"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%204">Link to this property</a>

"report\_details\_mismatch"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%205">Link to this property</a>

"no\_abuse\_found"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%206">Link to this property</a>

"missing\_original\_work"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%207">Link to this property</a>

"direct\_url\_required"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%208">Link to this property</a>

"wrong\_report\_category"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%209">Link to this property</a>

"content\_unavailable"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%2010">Link to this property</a>

"law\_enforcement\_referral\_required"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%2011">Link to this property</a>

"domain\_dispute\_process\_required"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason%20%3E%20(member)%2012">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20denial_reason">Link to this property</a>

domain: string

Domain identified in the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20domain">Link to this property</a>

dsa\_attestation: boolean

Whether the submitter provided the Digital Services Act attestation.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20dsa_attestation">Link to this property</a>

<details>

<summary>

status: "submitted"or "accepted"or "denied"

Status visible to the account that submitted the report.

</summary>

One of the following:

"submitted"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"accepted"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"denied"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "PHISH"or "GEN"or "THREAT"or 6 more

The abuse report type

</summary>

One of the following:

"PHISH"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"GEN"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"THREAT"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"DMCA"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"EMER"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"TM"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"REG\_WHO"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"NCSEI"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"NETWORK"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

urls: array of string

URLs supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20urls">Link to this property</a>

agent\_name: optional string

Authorized agent name supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20agent_name">Link to this property</a>

comments: optional string

Additional comments supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20comments">Link to this property</a>

court: optional string

The string “on” when a court proceeding applies to the report; otherwise omitted.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20court">Link to this property</a>

destination\_ips: optional array of string

Destination IP addresses supplied with a network abuse report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20destination_ips">Link to this property</a>

host\_notification: optional string

Submitter preference for notifying the hosting provider.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20host_notification">Link to this property</a>

justification: optional string

Evidence supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20justification">Link to this property</a>

ncmec\_notification: optional string

Submitter preference for notifying NCMEC.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20ncmec_notification">Link to this property</a>

ncsei\_subject\_representation: optional boolean

Representation supplied for an NCSEI report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20ncsei_subject_representation">Link to this property</a>

original\_work: optional string

Original work or targeted brand supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20original_work">Link to this property</a>

owner\_notification: optional string

Submitter preference for notifying the content owner.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20owner_notification">Link to this property</a>

ports\_protocols: optional array of string

Ports and protocols supplied with a network abuse report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20ports_protocols">Link to this property</a>

<details>

<summary>

reg\_who\_request: optional object {reg\_who\_good\_faith\_affirmation, reg\_who\_lawful\_processing\_agreement, reg\_who\_legal\_basis, 4 more }

RDP-mandated fields for registrar WHOIS data disclosure requests.

</summary>

reg\_who\_good\_faith\_affirmation: boolean

Affirmation that the request is made in good faith per RDP 10.2.4. Must be true.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_good_faith_affirmation">Link to this property</a>

reg\_who\_lawful\_processing\_agreement: boolean

Agreement to process data lawfully per RDP 10.2.5. Must be true.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_lawful_processing_agreement">Link to this property</a>

reg\_who\_legal\_basis: string

Legal rights and rationale for the request per RDP 10.2.3. Required for all WHOIS requests.

maxLength5000

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_legal_basis">Link to this property</a>

<details>

<summary>

reg\_who\_request\_type: "disclosure"or "invalid\_whois"

The type of WHOIS data request per RDP procedure.

</summary>

One of the following:

"disclosure"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_request_type%20%3E%20(member)%200">Link to this property</a>

"invalid\_whois"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_request_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_request_type">Link to this property</a>

<details>

<summary>

reg\_who\_requested\_data\_elements: array of "registrant\_name"or "registrant\_organization"or "registrant\_email"or 14 more

The specific WHOIS data elements being requested per RDP 10.2.2. Required for all WHOIS requests.

</summary>

One of the following:

"registrant\_name"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"registrant\_organization"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"registrant\_email"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"registrant\_phone"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"registrant\_address"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"registrant\_address\_country"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"registrant\_address\_postal\_code"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"admin\_name"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

"admin\_organization"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%208">Link to this property</a>

"admin\_email"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%209">Link to this property</a>

"admin\_phone"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2010">Link to this property</a>

"admin\_address"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2011">Link to this property</a>

"tech\_name"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2012">Link to this property</a>

"tech\_organization"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2013">Link to this property</a>

"tech\_email"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2014">Link to this property</a>

"tech\_phone"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2015">Link to this property</a>

"tech\_address"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements%20%3E%20(items)%20%3E%20(member)%2016">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requested_data_elements">Link to this property</a>

reg\_who\_authorization\_statement: optional string

Optional authorization statement or power of attorney per RDP 10.2.1.3.

maxLength5000

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_authorization_statement">Link to this property</a>

<details>

<summary>

reg\_who\_requestor\_type: optional "government"or "corporation"or "individual"

The nature of the requestor per RDP 10.2.1.2.

</summary>

One of the following:

"government"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requestor_type%20%3E%20(member)%200">Link to this property</a>

"corporation"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requestor_type%20%3E%20(member)%201">Link to this property</a>

"individual"

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requestor_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request%20%3E%20(property)%20reg_who_requestor_type">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reg_who_request">Link to this property</a>

reported\_country: optional string

Country associated with the reported activity.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reported_country">Link to this property</a>

reported\_user\_agent: optional string

User agent associated with the reported activity.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20reported_user_agent">Link to this property</a>

source\_ips: optional array of string

Source IP addresses supplied with a network abuse report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20source_ips">Link to this property</a>

<details>

<summary>

submitter: optional object {company, email, name, telephone }

Information about the submitter of the report.

</summary>

company: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20company">Link to this property</a>

email: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20email">Link to this property</a>

name: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20name">Link to this property</a>

telephone: optional string

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter%20%3E%20(property)%20telephone">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20submitter">Link to this property</a>

subtypes: optional array of string

Additional abuse classifications supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20subtypes">Link to this property</a>

title: optional string

Title supplied with the report.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

udrp: optional string

The string “on” when a UDRP proceeding applies to the report; otherwise omitted.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20udrp">Link to this property</a>

urs: optional string

The string “on” when a URS proceeding applies to the report; otherwise omitted.

<a href="#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)%20%3E%20(property)%20urs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports.submitted%20%3E%20(model)%20submitted_get_response%20%3E%20(schema)>)

#### Abuse ReportsSubmittedEmails

##### [List emails sent to an abuse report submitter](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/submitted/subresources/emails/methods/list)

GET/accounts/{account\_id}/abuse-reports/submitted/{report\_id}/emails

##### ModelsExpand Collapse

<details>

<summary>

EmailListResponse object {emails }

</summary>

<details>

<summary>

emails: array of object {id, body, recipient, 2 more }

</summary>

id: string

Unique identifier of the email.

<a href="#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)%20%3E%20(property)%20emails%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

body: string

Body content of the email.

<a href="#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)%20%3E%20(property)%20emails%20%3E%20(items)%20%3E%20(property)%20body">Link to this property</a>

recipient: string

Email address of the recipient.

<a href="#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)%20%3E%20(property)%20emails%20%3E%20(items)%20%3E%20(property)%20recipient">Link to this property</a>

sent\_at: string

When the email was sent. Time in RFC 3339 format (<a href="https://www.rfc-editor.org/rfc/rfc3339.html">https://www.rfc-editor.org/rfc/rfc3339.html</a>)

<a href="#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)%20%3E%20(property)%20emails%20%3E%20(items)%20%3E%20(property)%20sent_at">Link to this property</a>

subject: string

Subject line of the email.

<a href="#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)%20%3E%20(property)%20emails%20%3E%20(items)%20%3E%20(property)%20subject">Link to this property</a>

</details>

<a href="#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)%20%3E%20(property)%20emails">Link to this property</a>

</details>

[Link to this property](<#(resource)%20abuse_reports.submitted.emails%20%3E%20(model)%20email_list_response%20%3E%20(schema)>)

#### Abuse ReportsMitigations

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