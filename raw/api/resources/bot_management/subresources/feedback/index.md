---
title: Feedback
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Bot Management](https://developers.cloudflare.com/api/resources/bot_management)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Feedback

##### [List zone feedback reports](https://developers.cloudflare.com/api/resources/bot_management/subresources/feedback/methods/list)

GET/zones/{zone\_id}/bot\_management/feedback

##### [Submit a feedback report](https://developers.cloudflare.com/api/resources/bot_management/subresources/feedback/methods/create)

POST/zones/{zone\_id}/bot\_management/feedback

##### ModelsExpand Collapse

<details>

<summary>

FeedbackReport object {description, expression, first\_request\_seen\_at, 8 more }

</summary>

description: string

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

expression: string

Wirefilter expression describing the traffic being reported.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

first\_request\_seen\_at: string

formatdate-time

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20first_request_seen_at">Link to this property</a>

last\_request\_seen\_at: string

formatdate-time

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20last_request_seen_at">Link to this property</a>

requests: number

formatint64

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests">Link to this property</a>

requests\_by\_attribute: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_attribute%20%3E%20(schema)">RequestsByAttribute</a> { metric, requests }

Top attributes contributing to the feedback sample. Keys include topASNs, topCountries, topHosts, topIPs, topJA3Hashes, topJA4s, topPaths, topUserAgents.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests_by_attribute">Link to this property</a>

requests\_by\_score: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_score%20%3E%20(schema)">RequestsByScore</a>

Map of bot scores (1-99) to request counts. Sum must equal <code>requests</code>.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests_by_score">Link to this property</a>

requests\_by\_score\_src: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_score_src%20%3E%20(schema)">RequestsByScoreSrc</a>

Map of score source to request counts. Sum must equal <code>requests</code>.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests_by_score_src">Link to this property</a>

type: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_type%20%3E%20(schema)">FeedbackType</a>

Type of feedback report.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

subtype: optional string

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20subtype">Link to this property</a>

</details>

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)>)

<details>

<summary>

FeedbackType = "false\_positive"or "false\_negative"

Type of feedback report.

</summary>

One of the following:

"false\_positive"

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_type%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"false\_negative"

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_type%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_type%20%3E%20(schema)>)

<details>

<summary>

MetricRequests object {metric, requests }

</summary>

metric: string

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20metric_requests%20%3E%20(schema)%20%3E%20(property)%20metric">Link to this property</a>

requests: number

formatint64

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20metric_requests%20%3E%20(schema)%20%3E%20(property)%20requests">Link to this property</a>

</details>

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20metric_requests%20%3E%20(schema)>)

<details>

<summary>

RequestsByAttribute = map\[array of <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20metric_requests%20%3E%20(schema)">MetricRequests</a> { metric, requests } ]

Top attributes contributing to the feedback sample. Keys include topASNs, topCountries, topHosts, topIPs, topJA3Hashes, topJA4s, topPaths, topUserAgents.

</summary>

metric: string

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20metric_requests%20%3E%20(schema)%20%3E%20(property)%20metric">Link to this property</a>

requests: number

formatint64

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20metric_requests%20%3E%20(schema)%20%3E%20(property)%20requests">Link to this property</a>

</details>

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_attribute%20%3E%20(schema)>)

RequestsByScore = map\[number]

Map of bot scores (1-99) to request counts. Sum must equal `requests`.

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_score%20%3E%20(schema)>)

RequestsByScoreSrc = map\[number]

Map of score source to request counts. Sum must equal `requests`.

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_score_src%20%3E%20(schema)>)

<details>

<summary>

FeedbackListResponse = array of <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)">FeedbackReport</a> { description, expression, first\_request\_seen\_at, 8 more }

</summary>

description: string

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

expression: string

Wirefilter expression describing the traffic being reported.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

first\_request\_seen\_at: string

formatdate-time

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20first_request_seen_at">Link to this property</a>

last\_request\_seen\_at: string

formatdate-time

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20last_request_seen_at">Link to this property</a>

requests: number

formatint64

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests">Link to this property</a>

requests\_by\_attribute: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_attribute%20%3E%20(schema)">RequestsByAttribute</a> { metric, requests }

Top attributes contributing to the feedback sample. Keys include topASNs, topCountries, topHosts, topIPs, topJA3Hashes, topJA4s, topPaths, topUserAgents.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests_by_attribute">Link to this property</a>

requests\_by\_score: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_score%20%3E%20(schema)">RequestsByScore</a>

Map of bot scores (1-99) to request counts. Sum must equal <code>requests</code>.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests_by_score">Link to this property</a>

requests\_by\_score\_src: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20requests_by_score_src%20%3E%20(schema)">RequestsByScoreSrc</a>

Map of score source to request counts. Sum must equal <code>requests</code>.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20requests_by_score_src">Link to this property</a>

type: <a href="https://developers.cloudflare.com/api/resources/bot_management#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_type%20%3E%20(schema)">FeedbackType</a>

Type of feedback report.

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

subtype: optional string

<a href="#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_report%20%3E%20(schema)%20%3E%20(property)%20subtype">Link to this property</a>

</details>

[Link to this property](<#(resource)%20bot_management.feedback%20%3E%20(model)%20feedback_list_response%20%3E%20(schema)>)