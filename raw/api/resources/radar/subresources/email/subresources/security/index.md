---
title: Security
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[Email](https://developers.cloudflare.com/api/resources/radar/subresources/email)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Security

##### [Get email security summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2)

GET/radar/email/security/summary/{dimension}

##### [Get email security time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/timeseries_groups_v2)

GET/radar/email/security/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

SecuritySummaryV2Response object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security%20%3E%20(model)%20security_summary_v2_response%20%3E%20(schema)>)

<details>

<summary>

SecurityTimeseriesGroupsV2Response object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security%20%3E%20(model)%20security_timeseries_groups_v2_response%20%3E%20(schema)>)

#### SecurityTop

#### SecurityTopTLDs

##### [Get top TLDs by email message volume](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/methods/get)

GET/radar/email/security/top/tlds

##### ModelsExpand Collapse

<details>

<summary>

TLDGetResponse object {meta, top\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.top.tlds%20%3E%20(model)%20tld_get_response%20%3E%20(schema)>)

#### SecurityTopTLDsMalicious

##### [Get top TLDs by email malicious classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/malicious/methods/get)

GET/radar/email/security/top/tlds/malicious/{malicious}

##### ModelsExpand Collapse

<details>

<summary>

MaliciousGetResponse object {meta, top\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.top.tlds.malicious%20%3E%20(model)%20malicious_get_response%20%3E%20(schema)>)

#### SecurityTopTLDsSpam

##### [Get top TLDs by email spam classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/spam/methods/get)

GET/radar/email/security/top/tlds/spam/{spam}

##### ModelsExpand Collapse

<details>

<summary>

SpamGetResponse object {meta, top\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.top.tlds.spam%20%3E%20(model)%20spam_get_response%20%3E%20(schema)>)

#### SecurityTopTLDsSpoof

##### [Get top TLDs by email spoof classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/spoof/methods/get)

GET/radar/email/security/top/tlds/spoof/{spoof}

##### ModelsExpand Collapse

<details>

<summary>

SpoofGetResponse object {meta, top\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.top.tlds.spoof%20%3E%20(model)%20spoof_get_response%20%3E%20(schema)>)

#### SecuritySummary

##### [Get email ARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/arc)

Deprecated

GET/radar/email/security/summary/arc

##### [Get email DKIM validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/dkim)

Deprecated

GET/radar/email/security/summary/dkim

##### [Get email DMARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/dmarc)

Deprecated

GET/radar/email/security/summary/dmarc

##### [Get email malicious classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/malicious)

Deprecated

GET/radar/email/security/summary/malicious

##### [Get email spam classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spam)

Deprecated

GET/radar/email/security/summary/spam

##### [Get email SPF validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spf)

Deprecated

GET/radar/email/security/summary/spf

##### [Get email threat category summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/threat_category)

Deprecated

GET/radar/email/security/summary/threat\_category

##### [Get email spoof classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spoof)

Deprecated

GET/radar/email/security/summary/spoof

##### [Get email TLS version summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/tls_version)

Deprecated

GET/radar/email/security/summary/tls\_version

##### ModelsExpand Collapse

<details>

<summary>

SummaryARCResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_summary%20%3E%20(schema)">RadarEmailSummary</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_arc_response%20%3E%20(schema)>)

<details>

<summary>

SummaryDKIMResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_summary%20%3E%20(schema)">RadarEmailSummary</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dkim_response%20%3E%20(schema)>)

<details>

<summary>

SummaryDMARCResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_summary%20%3E%20(schema)">RadarEmailSummary</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_dmarc_response%20%3E%20(schema)>)

<details>

<summary>

SummaryMaliciousResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {MALICIOUS, NOT\_MALICIOUS }

</summary>

MALICIOUS: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20MALICIOUS">Link to this property</a>

NOT\_MALICIOUS: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20NOT_MALICIOUS">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_malicious_response%20%3E%20(schema)>)

<details>

<summary>

SummarySpamResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {NOT\_SPAM, SPAM }

</summary>

NOT\_SPAM: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20NOT_SPAM">Link to this property</a>

SPAM: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20SPAM">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spam_response%20%3E%20(schema)>)

<details>

<summary>

SummarySPFResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_summary%20%3E%20(schema)">RadarEmailSummary</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spf_response%20%3E%20(schema)>)

<details>

<summary>

SummaryThreatCategoryResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {BrandImpersonation, CredentialHarvester, IdentityDeception, Link }

</summary>

BrandImpersonation: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20BrandImpersonation">Link to this property</a>

CredentialHarvester: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20CredentialHarvester">Link to this property</a>

IdentityDeception: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20IdentityDeception">Link to this property</a>

Link: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20Link">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_threat_category_response%20%3E%20(schema)>)

<details>

<summary>

SummarySpoofResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {NOT\_SPOOF, SPOOF }

</summary>

NOT\_SPOOF: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20NOT_SPOOF">Link to this property</a>

SPOOF: string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20SPOOF">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_spoof_response%20%3E%20(schema)>)

<details>

<summary>

SummaryTLSVersionResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {confidenceInfo, dateRange, lastUpdated, 2 more }

Metadata for the results.

</summary>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {"TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3" }

</summary>

"TLS 1.0": string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20TLS%201.0">Link to this property</a>

"TLS 1.1": string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20TLS%201.1">Link to this property</a>

"TLS 1.2": string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20TLS%201.2">Link to this property</a>

"TLS 1.3": string

A numeric string.

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20TLS%201.3">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.summary%20%3E%20(model)%20summary_tls_version_response%20%3E%20(schema)>)

#### SecurityTimeseries Groups

##### [Get email ARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/arc)

Deprecated

GET/radar/email/security/timeseries\_groups/arc

##### [Get email DKIM validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/dkim)

Deprecated

GET/radar/email/security/timeseries\_groups/dkim

##### [Get email DMARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/dmarc)

Deprecated

GET/radar/email/security/timeseries\_groups/dmarc

##### [Get email malicious classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/malicious)

Deprecated

GET/radar/email/security/timeseries\_groups/malicious

##### [Get email spam classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spam)

Deprecated

GET/radar/email/security/timeseries\_groups/spam

##### [Get email SPF validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spf)

Deprecated

GET/radar/email/security/timeseries\_groups/spf

##### [Get email threat category time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/threat_category)

Deprecated

GET/radar/email/security/timeseries\_groups/threat\_category

##### [Get email spoof classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spoof)

Deprecated

GET/radar/email/security/timeseries\_groups/spoof

##### [Get email TLS version time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/tls_version)

Deprecated

GET/radar/email/security/timeseries\_groups/tls\_version

##### ModelsExpand Collapse

<details>

<summary>

TimeseriesGroupARCResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

serie\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_series%20%3E%20(schema)">RadarEmailSeries</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_arc_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupDKIMResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

serie\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_series%20%3E%20(schema)">RadarEmailSeries</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dkim_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupDMARCResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

serie\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_series%20%3E%20(schema)">RadarEmailSeries</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_dmarc_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupMaliciousResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {MALICIOUS, NOT\_MALICIOUS }

</summary>

MALICIOUS: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20MALICIOUS">Link to this property</a>

NOT\_MALICIOUS: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20NOT_MALICIOUS">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_malicious_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupSpamResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {NOT\_SPAM, SPAM }

</summary>

NOT\_SPAM: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20NOT_SPAM">Link to this property</a>

SPAM: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20SPAM">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spam_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupSPFResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

serie\_0: <a href="https://developers.cloudflare.com/api/resources/radar#(resource)%20radar.email%20%3E%20(model)%20radar_email_series%20%3E%20(schema)">RadarEmailSeries</a> { FAIL, NONE, PASS }

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spf_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupThreatCategoryResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {BrandImpersonation, CredentialHarvester, IdentityDeception, Link }

</summary>

BrandImpersonation: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20BrandImpersonation">Link to this property</a>

CredentialHarvester: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20CredentialHarvester">Link to this property</a>

IdentityDeception: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20IdentityDeception">Link to this property</a>

Link: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20Link">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_threat_category_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupSpoofResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {NOT\_SPOOF, SPOOF }

</summary>

NOT\_SPOOF: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20NOT_SPOOF">Link to this property</a>

SPOOF: array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20SPOOF">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_spoof_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupTLSVersionResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 3 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

<details>

<summary>

confidenceInfo: object {annotations, level }

</summary>

<details>

<summary>

annotations: array of object {dataSource, description, endDate, 5 more }

</summary>

<details>

<summary>

dataSource: "ALL"or "AI\_BOTS"or "AI\_GATEWAY"or 22 more

Data source for annotations.

</summary>

One of the following:

"ALL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {"TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3" }

</summary>

"TLS 1.0": array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20TLS%201.0">Link to this property</a>

"TLS 1.1": array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20TLS%201.1">Link to this property</a>

"TLS 1.2": array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20TLS%201.2">Link to this property</a>

"TLS 1.3": array of string

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20TLS%201.3">Link to this property</a>

</details>

<a href="#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.email.security.timeseries_groups%20%3E%20(model)%20timeseries_group_tls_version_response%20%3E%20(schema)>)