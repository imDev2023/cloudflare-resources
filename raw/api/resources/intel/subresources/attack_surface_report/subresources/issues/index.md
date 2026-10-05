---
title: Issues
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Intel](https://developers.cloudflare.com/api/resources/intel)

[Attack Surface Report](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Issues

##### [Retrieves Security Center Issues](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/list)

Deprecated

GET/accounts/{account\_id}/intel/attack-surface-report/issues

##### [Retrieves Security Center Issue Counts by Class](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/class)

Deprecated

GET/accounts/{account\_id}/intel/attack-surface-report/issues/class

##### [Retrieves Security Center Issue Counts by Severity](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/severity)

Deprecated

GET/accounts/{account\_id}/intel/attack-surface-report/issues/severity

##### [Retrieves Security Center Issue Counts by Type](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/type)

Deprecated

GET/accounts/{account\_id}/intel/attack-surface-report/issues/type

##### ModelsExpand Collapse

<details>

<summary>

IssueType = "compliance\_violation"or "email\_security"or "exposed\_infrastructure"or 3 more

</summary>

One of the following:

"compliance\_violation"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"email\_security"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"exposed\_infrastructure"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

"insecure\_configuration"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)%20%3E%20(member)%203">Link to this property</a>

"weak\_authentication"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)%20%3E%20(member)%204">Link to this property</a>

"configuration\_suggestion"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)%20%3E%20(member)%205">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)>)

<details>

<summary>

SeverityQueryParam = "low"or "moderate"or "critical"

</summary>

One of the following:

"low"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20severity_query_param%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"moderate"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20severity_query_param%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"critical"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20severity_query_param%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20severity_query_param%20%3E%20(schema)>)

<details>

<summary>

IssueListResponse object {count, issues, page, per\_page }

</summary>

count: optional number

Indicates the total number of results.

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

issues: optional array of object {id, dismissed, has\_extended\_context, 11 more }

</summary>

id: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

dismissed: optional boolean

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20dismissed">Link to this property</a>

has\_extended\_context: optional boolean

Indicates whether the insight has a large payload that requires fetching via the context endpoint.

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20has_extended_context">Link to this property</a>

issue\_class: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20issue_class">Link to this property</a>

issue\_type: optional <a href="https://developers.cloudflare.com/api/resources/intel#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type%20%3E%20(schema)">IssueType</a>

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20issue_type">Link to this property</a>

<details>

<summary>

payload: optional object {detection\_method, zone\_tag }

</summary>

detection\_method: optional string

Describes the method used to detect insight.

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20payload%20%3E%20(property)%20detection_method">Link to this property</a>

zone\_tag: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20payload%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20payload">Link to this property</a>

resolve\_link: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20resolve_link">Link to this property</a>

resolve\_text: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20resolve_text">Link to this property</a>

<details>

<summary>

severity: optional "Low"or "Moderate"or "Critical"

</summary>

One of the following:

"Low"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%200">Link to this property</a>

"Moderate"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%201">Link to this property</a>

"Critical"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20severity">Link to this property</a>

since: optional string

formatdate-time

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20since">Link to this property</a>

<details>

<summary>

status: optional "active"or "resolved"

The current status of the insight.

</summary>

One of the following:

"active"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"resolved"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

subject: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20subject">Link to this property</a>

timestamp: optional string

formatdate-time

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

<details>

<summary>

user\_classification: optional "false\_positive"or "accept\_risk"or "other"

User-defined classification for the insight. Can be ‘false\_positive’, ‘accept\_risk’, ‘other’, or null.

</summary>

One of the following:

"false\_positive"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20user_classification%20%3E%20(member)%200">Link to this property</a>

"accept\_risk"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20user_classification%20%3E%20(member)%201">Link to this property</a>

"other"

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20user_classification%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues%20%3E%20(items)%20%3E%20(property)%20user_classification">Link to this property</a>

</details>

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20issues">Link to this property</a>

page: optional number

Specifies the current page within paginated list of results.

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

per\_page: optional number

Sets the number of results per page of results.

maximum1000

minimum1

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)%20%3E%20(property)%20per_page">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_list_response%20%3E%20(schema)>)

<details>

<summary>

IssueClassResponse = array of object {count, value }

</summary>

count: optional number

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_class_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

value: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_class_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_class_response%20%3E%20(schema)>)

<details>

<summary>

IssueSeverityResponse = array of object {count, value }

</summary>

count: optional number

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_severity_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

value: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_severity_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_severity_response%20%3E%20(schema)>)

<details>

<summary>

IssueTypeResponse = array of object {count, value }

</summary>

count: optional number

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

value: optional string

<a href="#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.attack_surface_report.issues%20%3E%20(model)%20issue_type_response%20%3E%20(schema)>)