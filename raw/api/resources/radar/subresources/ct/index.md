---
title: CT
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# CT

##### [Get certificate distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/summary)

GET/radar/ct/summary/{dimension}

##### [Get certificates time series](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries)

GET/radar/ct/timeseries

##### [Get time series of certificate distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries_groups)

GET/radar/ct/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

CTSummaryResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: map\[string]or object {rfc6962, static } or object {gt\_121d, gt\_16d\_lte\_31d, gt\_31d\_lte\_91d, 3 more } or 5 more

</summary>

One of the following:

map\[string]

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {rfc6962, static }

</summary>

rfc6962: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%201%20%3E%20(property)%20rfc6962">Link to this property</a>

static: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%201%20%3E%20(property)%20static">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {gt\_121d, gt\_16d\_lte\_31d, gt\_31d\_lte\_91d, 3 more }

</summary>

gt\_121d: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_121d">Link to this property</a>

gt\_16d\_lte\_31d: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_16d_lte_31d">Link to this property</a>

gt\_31d\_lte\_91d: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_31d_lte_91d">Link to this property</a>

gt\_3d\_lte\_16d: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_3d_lte_16d">Link to this property</a>

gt\_91d\_lte\_121d: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_91d_lte_121d">Link to this property</a>

lte\_3d: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202%20%3E%20(property)%20lte_3d">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {CERTIFICATE, PRECERTIFICATE }

</summary>

CERTIFICATE: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%203%20%3E%20(property)%20CERTIFICATE">Link to this property</a>

PRECERTIFICATE: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%203%20%3E%20(property)%20PRECERTIFICATE">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {EXPIRED, VALID }

</summary>

EXPIRED: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%204%20%3E%20(property)%20EXPIRED">Link to this property</a>

VALID: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%204%20%3E%20(property)%20VALID">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {NEGATIVE, POSITIVE }

</summary>

NEGATIVE: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%205%20%3E%20(property)%20NEGATIVE">Link to this property</a>

POSITIVE: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%205%20%3E%20(property)%20POSITIVE">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {DSA, ECDSA, RSA }

</summary>

DSA: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%206%20%3E%20(property)%20DSA">Link to this property</a>

ECDSA: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%206%20%3E%20(property)%20ECDSA">Link to this property</a>

RSA: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%206%20%3E%20(property)%20RSA">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {domain, extended, organization, unknown }

</summary>

domain: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%207%20%3E%20(property)%20domain">Link to this property</a>

extended: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%207%20%3E%20(property)%20extended">Link to this property</a>

organization: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%207%20%3E%20(property)%20organization">Link to this property</a>

unknown: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%207%20%3E%20(property)%20unknown">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct%20%3E%20(model)%20ct_summary_response%20%3E%20(schema)>)

<details>

<summary>

CTTimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_response%20%3E%20(schema)>)

<details>

<summary>

CTTimeseriesGroupsResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps } or object {rfc6962, static } or object {gt\_121d, gt\_16d\_lte\_31d, gt\_31d\_lte\_91d, 3 more } or 5 more

</summary>

One of the following:

<details>

<summary>

UnnamedSchemaRef7826220e105d84352ba1108d9ed88e55 object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%200%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {rfc6962, static }

</summary>

rfc6962: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%201%20%3E%20(property)%20rfc6962">Link to this property</a>

static: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%201%20%3E%20(property)%20static">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {gt\_121d, gt\_16d\_lte\_31d, gt\_31d\_lte\_91d, 3 more }

</summary>

gt\_121d: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_121d">Link to this property</a>

gt\_16d\_lte\_31d: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_16d_lte_31d">Link to this property</a>

gt\_31d\_lte\_91d: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_31d_lte_91d">Link to this property</a>

gt\_3d\_lte\_16d: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_3d_lte_16d">Link to this property</a>

gt\_91d\_lte\_121d: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202%20%3E%20(property)%20gt_91d_lte_121d">Link to this property</a>

lte\_3d: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202%20%3E%20(property)%20lte_3d">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {CERTIFICATE, PRECERTIFICATE }

</summary>

CERTIFICATE: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%203%20%3E%20(property)%20CERTIFICATE">Link to this property</a>

PRECERTIFICATE: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%203%20%3E%20(property)%20PRECERTIFICATE">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {EXPIRED, VALID }

</summary>

EXPIRED: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%204%20%3E%20(property)%20EXPIRED">Link to this property</a>

VALID: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%204%20%3E%20(property)%20VALID">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {NEGATIVE, POSITIVE }

</summary>

NEGATIVE: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%205%20%3E%20(property)%20NEGATIVE">Link to this property</a>

POSITIVE: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%205%20%3E%20(property)%20POSITIVE">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {DSA, ECDSA, RSA }

</summary>

DSA: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%206%20%3E%20(property)%20DSA">Link to this property</a>

ECDSA: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%206%20%3E%20(property)%20ECDSA">Link to this property</a>

RSA: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%206%20%3E%20(property)%20RSA">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {domain, extended, organization, unknown }

</summary>

domain: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%207%20%3E%20(property)%20domain">Link to this property</a>

extended: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%207%20%3E%20(property)%20extended">Link to this property</a>

organization: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%207%20%3E%20(property)%20organization">Link to this property</a>

unknown: array of string

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%207%20%3E%20(property)%20unknown">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct%20%3E%20(model)%20ct_timeseries_groups_response%20%3E%20(schema)>)

#### CTAuthorities

##### [Get certificate authority details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/get)

GET/radar/ct/authorities/{ca\_slug}

##### [List certificate authorities](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/list)

GET/radar/ct/authorities

##### ModelsExpand Collapse

<details>

<summary>

AuthorityGetResponse object {certificateAuthority }

</summary>

<details>

<summary>

certificateAuthority: object {appleStatus, authorityKeyIdentifier, certificateRecordType, 15 more }

</summary>

<details>

<summary>

appleStatus: "INCLUDED"or "NOT\_YET\_INCLUDED"or "NOT\_INCLUDED"or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

</summary>

One of the following:

"INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%200">Link to this property</a>

"NOT\_YET\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%201">Link to this property</a>

"NOT\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%202">Link to this property</a>

"NOT\_BEFORE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%203">Link to this property</a>

"REMOVED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%204">Link to this property</a>

"DISABLED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%205">Link to this property</a>

"BLOCKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20appleStatus">Link to this property</a>

authorityKeyIdentifier: string

The authorityKeyIdentifier value extracted from the certificate PEM.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20authorityKeyIdentifier">Link to this property</a>

<details>

<summary>

certificateRecordType: "ROOT\_CERTIFICATE"or "INTERMEDIATE\_CERTIFICATE"

Specifies the type of certificate in the trust chain.

</summary>

One of the following:

"ROOT\_CERTIFICATE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20certificateRecordType%20%3E%20(member)%200">Link to this property</a>

"INTERMEDIATE\_CERTIFICATE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20certificateRecordType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20certificateRecordType">Link to this property</a>

<details>

<summary>

chromeStatus: "INCLUDED"or "NOT\_YET\_INCLUDED"or "NOT\_INCLUDED"or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

</summary>

One of the following:

"INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%200">Link to this property</a>

"NOT\_YET\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%201">Link to this property</a>

"NOT\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%202">Link to this property</a>

"NOT\_BEFORE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%203">Link to this property</a>

"REMOVED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%204">Link to this property</a>

"DISABLED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%205">Link to this property</a>

"BLOCKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20chromeStatus">Link to this property</a>

country: string

The two-letter ISO country code where the CA organization is based.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20country">Link to this property</a>

countryName: string

The full country name corresponding to the country code.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20countryName">Link to this property</a>

<details>

<summary>

microsoftStatus: "INCLUDED"or "NOT\_YET\_INCLUDED"or "NOT\_INCLUDED"or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

</summary>

One of the following:

"INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%200">Link to this property</a>

"NOT\_YET\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%201">Link to this property</a>

"NOT\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%202">Link to this property</a>

"NOT\_BEFORE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%203">Link to this property</a>

"REMOVED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%204">Link to this property</a>

"DISABLED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%205">Link to this property</a>

"BLOCKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20microsoftStatus">Link to this property</a>

<details>

<summary>

mozillaStatus: "INCLUDED"or "NOT\_YET\_INCLUDED"or "NOT\_INCLUDED"or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

</summary>

One of the following:

"INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%200">Link to this property</a>

"NOT\_YET\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%201">Link to this property</a>

"NOT\_INCLUDED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%202">Link to this property</a>

"NOT\_BEFORE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%203">Link to this property</a>

"REMOVED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%204">Link to this property</a>

"DISABLED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%205">Link to this property</a>

"BLOCKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20mozillaStatus">Link to this property</a>

name: string

The full name of the certificate authority (CA).

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20name">Link to this property</a>

owner: string

The organization that owns and operates the CA.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20owner">Link to this property</a>

parentName: string

The name of the parent/root certificate authority that issued this intermediate certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20parentName">Link to this property</a>

parentSha256Fingerprint: string

The SHA-256 fingerprint of the parent certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20parentSha256Fingerprint">Link to this property</a>

<details>

<summary>

related: array of object {certificateRecordType, name, revocationStatus, sha256Fingerprint }

CAs from the same owner.

</summary>

<details>

<summary>

certificateRecordType: "ROOT\_CERTIFICATE"or "INTERMEDIATE\_CERTIFICATE"

Specifies the type of certificate in the trust chain.

</summary>

One of the following:

"ROOT\_CERTIFICATE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20certificateRecordType%20%3E%20(member)%200">Link to this property</a>

"INTERMEDIATE\_CERTIFICATE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20certificateRecordType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20certificateRecordType">Link to this property</a>

name: string

The full name of the certificate authority (CA).

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

revocationStatus: "NOT\_REVOKED"or "REVOKED"or "PARENT\_CERT\_REVOKED"

The current revocation status of a Certificate Authority (CA) certificate.

</summary>

One of the following:

"NOT\_REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20revocationStatus%20%3E%20(member)%200">Link to this property</a>

"REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20revocationStatus%20%3E%20(member)%201">Link to this property</a>

"PARENT\_CERT\_REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20revocationStatus%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20revocationStatus">Link to this property</a>

sha256Fingerprint: string

The SHA-256 fingerprint of the intermediate certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20sha256Fingerprint">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20related">Link to this property</a>

<details>

<summary>

revocationStatus: "NOT\_REVOKED"or "REVOKED"or "PARENT\_CERT\_REVOKED"

The current revocation status of a Certificate Authority (CA) certificate.

</summary>

One of the following:

"NOT\_REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20revocationStatus%20%3E%20(member)%200">Link to this property</a>

"REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20revocationStatus%20%3E%20(member)%201">Link to this property</a>

"PARENT\_CERT\_REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20revocationStatus%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20revocationStatus">Link to this property</a>

sha256Fingerprint: string

The SHA-256 fingerprint of the intermediate certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20sha256Fingerprint">Link to this property</a>

subjectKeyIdentifier: string

The subjectKeyIdentifier value extracted from the certificate PEM.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20subjectKeyIdentifier">Link to this property</a>

validFrom: string

The start date of the certificate’s validity period (ISO format).

formatdate

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20validFrom">Link to this property</a>

validTo: string

The end date of the certificate’s validity period (ISO format).

formatdate

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority%20%3E%20(property)%20validTo">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthority">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_get_response%20%3E%20(schema)>)

<details>

<summary>

AuthorityListResponse object {certificateAuthorities }

</summary>

<details>

<summary>

certificateAuthorities: array of object {certificateRecordType, country, countryName, 6 more }

</summary>

<details>

<summary>

certificateRecordType: "ROOT\_CERTIFICATE"or "INTERMEDIATE\_CERTIFICATE"

Specifies the type of certificate in the trust chain.

</summary>

One of the following:

"ROOT\_CERTIFICATE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20certificateRecordType%20%3E%20(member)%200">Link to this property</a>

"INTERMEDIATE\_CERTIFICATE"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20certificateRecordType%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20certificateRecordType">Link to this property</a>

country: string

The two-letter ISO country code where the CA organization is based.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20country">Link to this property</a>

countryName: string

The full country name corresponding to the country code.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20countryName">Link to this property</a>

name: string

The full name of the certificate authority (CA).

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

owner: string

The organization that owns and operates the CA.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20owner">Link to this property</a>

parentName: string

The name of the parent/root certificate authority that issued this intermediate certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20parentName">Link to this property</a>

parentSha256Fingerprint: string

The SHA-256 fingerprint of the parent certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20parentSha256Fingerprint">Link to this property</a>

<details>

<summary>

revocationStatus: "NOT\_REVOKED"or "REVOKED"or "PARENT\_CERT\_REVOKED"

The current revocation status of a Certificate Authority (CA) certificate.

</summary>

One of the following:

"NOT\_REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20revocationStatus%20%3E%20(member)%200">Link to this property</a>

"REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20revocationStatus%20%3E%20(member)%201">Link to this property</a>

"PARENT\_CERT\_REVOKED"

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20revocationStatus%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20revocationStatus">Link to this property</a>

sha256Fingerprint: string

The SHA-256 fingerprint of the intermediate certificate.

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities%20%3E%20(items)%20%3E%20(property)%20sha256Fingerprint">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateAuthorities">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct.authorities%20%3E%20(model)%20authority_list_response%20%3E%20(schema)>)

#### CTLogs

##### [Get certificate log details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get)

GET/radar/ct/logs/{log\_slug}

##### [List certificate logs](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/list)

GET/radar/ct/logs

##### ModelsExpand Collapse

<details>

<summary>

LogGetResponse object {certificateLog }

</summary>

<details>

<summary>

certificateLog: object {api, avgThroughput, description, 12 more }

</summary>

<details>

<summary>

api: "RFC6962"or "STATIC"

The API standard that the certificate log follows.

</summary>

One of the following:

"RFC6962"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20api%20%3E%20(member)%200">Link to this property</a>

"STATIC"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20api%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20api">Link to this property</a>

avgThroughput: number

The average throughput of the CT log, measured in certificates per hour (certs/hour).

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20avgThroughput">Link to this property</a>

description: string

A brief description of the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20description">Link to this property</a>

endExclusive: string

The end date and time for when the log will stop accepting certificates.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20endExclusive">Link to this property</a>

lastUpdate: string

Timestamp of the most recent update to the CT log.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20lastUpdate">Link to this property</a>

operator: string

The organization responsible for operating the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

performance: object {endpoints, responseTime, uptime }

Log performance metrics, including averages and per-endpoint details.

</summary>

<details>

<summary>

endpoints: array of object {endpoint, responseTime, uptime }

</summary>

<details>

<summary>

endpoint: "add-chain (new)"or "add-chain (old)"or "add-pre-chain (new)"or 4 more

The certificate log endpoint names used in performance metrics.

</summary>

One of the following:

"add-chain (new)"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%200">Link to this property</a>

"add-chain (old)"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%201">Link to this property</a>

"add-pre-chain (new)"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%202">Link to this property</a>

"add-pre-chain (old)"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%203">Link to this property</a>

"get-entries"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%204">Link to this property</a>

"get-roots"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%205">Link to this property</a>

"get-sth"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20endpoint">Link to this property</a>

responseTime: number

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20responseTime">Link to this property</a>

uptime: number

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints%20%3E%20(items)%20%3E%20(property)%20uptime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20endpoints">Link to this property</a>

responseTime: number

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20responseTime">Link to this property</a>

uptime: number

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance%20%3E%20(property)%20uptime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20performance">Link to this property</a>

<details>

<summary>

related: array of object {description, endExclusive, slug, 2 more }

Logs from the same operator.

</summary>

description: string

A brief description of the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endExclusive: string

The end date and time for when the log will stop accepting certificates.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20endExclusive">Link to this property</a>

slug: string

A URL-friendly, kebab-case identifier for the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20slug">Link to this property</a>

startInclusive: string

The start date and time for when the log starts accepting certificates.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20startInclusive">Link to this property</a>

<details>

<summary>

state: "USABLE"or "PENDING"or "QUALIFIED"or 3 more

The current state of the certificate log. More details about log states can be found here: <a href="https://googlechrome.github.io/CertificateTransparency/log_states.html">https://googlechrome.github.io/CertificateTransparency/log\_states.html</a>

</summary>

One of the following:

"USABLE"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"PENDING"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

"QUALIFIED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%202">Link to this property</a>

"READ\_ONLY"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%203">Link to this property</a>

"RETIRED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%204">Link to this property</a>

"REJECTED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related%20%3E%20(items)%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20related">Link to this property</a>

slug: string

A URL-friendly, kebab-case identifier for the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20slug">Link to this property</a>

startInclusive: string

The start date and time for when the log starts accepting certificates.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20startInclusive">Link to this property</a>

<details>

<summary>

state: "USABLE"or "PENDING"or "QUALIFIED"or 3 more

The current state of the certificate log. More details about log states can be found here: <a href="https://googlechrome.github.io/CertificateTransparency/log_states.html">https://googlechrome.github.io/CertificateTransparency/log\_states.html</a>

</summary>

One of the following:

"USABLE"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"PENDING"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

"QUALIFIED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state%20%3E%20(member)%202">Link to this property</a>

"READ\_ONLY"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state%20%3E%20(member)%203">Link to this property</a>

"RETIRED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state%20%3E%20(member)%204">Link to this property</a>

"REJECTED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20state">Link to this property</a>

stateTimestamp: string

Timestamp of when the log state was last updated.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20stateTimestamp">Link to this property</a>

submittableCertCount: string

Number of certificates that are eligible for inclusion to this log but have not been included yet. Based on certificates signed by trusted root CAs within the log’s accepted date range.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20submittableCertCount">Link to this property</a>

submittedCertCount: string

Number of certificates already included in this CT log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20submittedCertCount">Link to this property</a>

url: string

The URL for the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20certificateLog">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)>)

<details>

<summary>

LogListResponse object {certificateLogs }

</summary>

<details>

<summary>

certificateLogs: array of object {api, description, endExclusive, 6 more }

</summary>

<details>

<summary>

api: "RFC6962"or "STATIC"

The API standard that the certificate log follows.

</summary>

One of the following:

"RFC6962"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20api%20%3E%20(member)%200">Link to this property</a>

"STATIC"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20api%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20api">Link to this property</a>

description: string

A brief description of the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endExclusive: string

The end date and time for when the log will stop accepting certificates.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20endExclusive">Link to this property</a>

operator: string

The organization responsible for operating the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

slug: string

A URL-friendly, kebab-case identifier for the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20slug">Link to this property</a>

startInclusive: string

The start date and time for when the log starts accepting certificates.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20startInclusive">Link to this property</a>

<details>

<summary>

state: "USABLE"or "PENDING"or "QUALIFIED"or 3 more

The current state of the certificate log. More details about log states can be found here: <a href="https://googlechrome.github.io/CertificateTransparency/log_states.html">https://googlechrome.github.io/CertificateTransparency/log\_states.html</a>

</summary>

One of the following:

"USABLE"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"PENDING"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

"QUALIFIED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%202">Link to this property</a>

"READ\_ONLY"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%203">Link to this property</a>

"RETIRED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%204">Link to this property</a>

"REJECTED"

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20state">Link to this property</a>

stateTimestamp: string

Timestamp of when the log state was last updated.

formatdate-time

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20stateTimestamp">Link to this property</a>

url: string

The URL for the certificate log.

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20certificateLogs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ct.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)>)