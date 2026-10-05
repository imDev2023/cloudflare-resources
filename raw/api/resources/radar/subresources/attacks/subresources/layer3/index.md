---
title: Layer3
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[Attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Layer3

##### [Get layer 3 attacks summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/summary_v2)

GET/radar/attacks/layer3/summary/{dimension}

##### [Get layer 3 attacks by bytes time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries)

GET/radar/attacks/layer3/timeseries

##### [Get layer 3 attacks time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries_groups_v2)

GET/radar/attacks/layer3/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

Layer3SummaryV2Response object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_summary_v2_response%20%3E%20(schema)>)

<details>

<summary>

Layer3TimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_response%20%3E%20(schema)>)

<details>

<summary>

Layer3TimeseriesGroupsV2Response object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3%20%3E%20(model)%20layer3_timeseries_groups_v2_response%20%3E%20(schema)>)

#### Layer3Summary

##### [Get layer 3 attacks by bitrate summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/bitrate)

Deprecated

GET/radar/attacks/layer3/summary/bitrate

##### [Get layer 3 attacks by duration summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/duration)

Deprecated

GET/radar/attacks/layer3/summary/duration

##### [Get layer 3 attacks by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/ip_version)

Deprecated

GET/radar/attacks/layer3/summary/ip\_version

##### [Get layer 3 attacks by protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/protocol)

Deprecated

GET/radar/attacks/layer3/summary/protocol

##### [Get layer 3 attacks by vector summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vector)

Deprecated

GET/radar/attacks/layer3/summary/vector

##### [Get layer 3 attacks by targeted industry summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/industry)

Deprecated

GET/radar/attacks/layer3/summary/industry

##### [Get layer 3 attacks by targeted vertical summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vertical)

Deprecated

GET/radar/attacks/layer3/summary/vertical

##### ModelsExpand Collapse

<details>

<summary>

SummaryBitrateResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {\_1\_GBPS\_TO\_10\_GBPS, \_10\_GBPS\_TO\_100\_GBPS, \_500\_MBPS\_TO\_1\_GBPS, 2 more }

</summary>

\_1\_GBPS\_TO\_10\_GBPS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_1_GBPS_TO_10_GBPS">Link to this property</a>

\_10\_GBPS\_TO\_100\_GBPS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_10_GBPS_TO_100_GBPS">Link to this property</a>

\_500\_MBPS\_TO\_1\_GBPS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_500_MBPS_TO_1_GBPS">Link to this property</a>

OVER\_100\_GBPS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20OVER_100_GBPS">Link to this property</a>

UNDER\_500\_MBPS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20UNDER_500_MBPS">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_bitrate_response%20%3E%20(schema)>)

<details>

<summary>

SummaryDurationResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {\_1\_HOUR\_TO\_3\_HOURS, \_10\_MINS\_TO\_20\_MINS, \_20\_MINS\_TO\_40\_MINS, 3 more }

</summary>

\_1\_HOUR\_TO\_3\_HOURS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_1_HOUR_TO_3_HOURS">Link to this property</a>

\_10\_MINS\_TO\_20\_MINS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_10_MINS_TO_20_MINS">Link to this property</a>

\_20\_MINS\_TO\_40\_MINS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_20_MINS_TO_40_MINS">Link to this property</a>

\_40\_MINS\_TO\_1\_HOUR: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20_40_MINS_TO_1_HOUR">Link to this property</a>

OVER\_3\_HOURS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20OVER_3_HOURS">Link to this property</a>

UNDER\_10\_MINS: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20UNDER_10_MINS">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_duration_response%20%3E%20(schema)>)

<details>

<summary>

SummaryIPVersionResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {IPv4, IPv6 }

</summary>

IPv4: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20IPv4">Link to this property</a>

IPv6: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20IPv6">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_ip_version_response%20%3E%20(schema)>)

<details>

<summary>

SummaryProtocolResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {GRE, ICMP, TCP, UDP }

</summary>

GRE: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20GRE">Link to this property</a>

ICMP: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20ICMP">Link to this property</a>

TCP: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20TCP">Link to this property</a>

UDP: string

A numeric string.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20UDP">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_protocol_response%20%3E%20(schema)>)

<details>

<summary>

SummaryVectorResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vector_response%20%3E%20(schema)>)

<details>

<summary>

SummaryIndustryResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_industry_response%20%3E%20(schema)>)

<details>

<summary>

SummaryVerticalResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.summary%20%3E%20(model)%20summary_vertical_response%20%3E%20(schema)>)

#### Layer3Timeseries Groups

##### [Get layer 3 attacks by target industries time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/industry)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/industry

##### [Get layer 3 attacks by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/ip\_version

##### [Get layer 3 attacks by protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/protocol

##### [Get layer 3 attacks by vector time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vector)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/vector

##### [Get layer 3 attacks by vertical time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vertical)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/vertical

##### [Get layer 3 attacks by bitrate time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/bitrate)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/bitrate

##### [Get layer 3 attacks by duration time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/duration)

Deprecated

GET/radar/attacks/layer3/timeseries\_groups/duration

##### ModelsExpand Collapse

<details>

<summary>

TimeseriesGroupIndustryResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_industry_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupIPVersionResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {IPv4, IPv6, timestamps }

</summary>

IPv4: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20IPv4">Link to this property</a>

IPv6: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20IPv6">Link to this property</a>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_ip_version_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupProtocolResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {GRE, ICMP, TCP, 2 more }

</summary>

GRE: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20GRE">Link to this property</a>

ICMP: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20ICMP">Link to this property</a>

TCP: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20TCP">Link to this property</a>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

UDP: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20UDP">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_protocol_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupVectorResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vector_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupVerticalResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_vertical_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupBitrateResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {\_1\_GBPS\_TO\_10\_GBPS, \_10\_GBPS\_TO\_100\_GBPS, \_500\_MBPS\_TO\_1\_GBPS, 3 more }

</summary>

\_1\_GBPS\_TO\_10\_GBPS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_1_GBPS_TO_10_GBPS">Link to this property</a>

\_10\_GBPS\_TO\_100\_GBPS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_10_GBPS_TO_100_GBPS">Link to this property</a>

\_500\_MBPS\_TO\_1\_GBPS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_500_MBPS_TO_1_GBPS">Link to this property</a>

OVER\_100\_GBPS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20OVER_100_GBPS">Link to this property</a>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

UNDER\_500\_MBPS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20UNDER_500_MBPS">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_bitrate_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupDurationResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {\_1\_HOUR\_TO\_3\_HOURS, \_10\_MINS\_TO\_20\_MINS, \_20\_MINS\_TO\_40\_MINS, 4 more }

</summary>

\_1\_HOUR\_TO\_3\_HOURS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_1_HOUR_TO_3_HOURS">Link to this property</a>

\_10\_MINS\_TO\_20\_MINS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_10_MINS_TO_20_MINS">Link to this property</a>

\_20\_MINS\_TO\_40\_MINS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_20_MINS_TO_40_MINS">Link to this property</a>

\_40\_MINS\_TO\_1\_HOUR: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20_40_MINS_TO_1_HOUR">Link to this property</a>

OVER\_3\_HOURS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20OVER_3_HOURS">Link to this property</a>

timestamps: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

UNDER\_10\_MINS: array of string

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20UNDER_10_MINS">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.timeseries_groups%20%3E%20(model)%20timeseries_group_duration_response%20%3E%20(schema)>)

#### Layer3Top

##### [Get top layer 3 attack pairs (origin and target locations)](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/attacks)

GET/radar/attacks/layer3/top/attacks

##### [Get top industries targeted by layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/industry)

Deprecated

GET/radar/attacks/layer3/top/industry

##### [Get top verticals targeted by layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/vertical)

Deprecated

GET/radar/attacks/layer3/top/vertical

##### ModelsExpand Collapse

<details>

<summary>

TopAttacksResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {originCountryAlpha2, originCountryName, value }

</summary>

originCountryAlpha2: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20originCountryAlpha2">Link to this property</a>

originCountryName: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20originCountryName">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_attacks_response%20%3E%20(schema)>)

<details>

<summary>

TopIndustryResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_industry_response%20%3E%20(schema)>)

<details>

<summary>

TopVerticalResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.top%20%3E%20(model)%20top_vertical_response%20%3E%20(schema)>)

#### Layer3TopLocations

##### [Get top origin locations of layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/origin)

GET/radar/attacks/layer3/top/locations/origin

##### [Get top target locations of layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/target)

GET/radar/attacks/layer3/top/locations/target

##### ModelsExpand Collapse

<details>

<summary>

LocationOriginResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {originCountryAlpha2, originCountryName, rank, value }

</summary>

originCountryAlpha2: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20originCountryAlpha2">Link to this property</a>

originCountryName: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20originCountryName">Link to this property</a>

rank: number

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20rank">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_origin_response%20%3E%20(schema)>)

<details>

<summary>

LocationTargetResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {rank, targetCountryAlpha2, targetCountryName, value }

</summary>

rank: number

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20rank">Link to this property</a>

targetCountryAlpha2: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20targetCountryAlpha2">Link to this property</a>

targetCountryName: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20targetCountryName">Link to this property</a>

value: string

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.attacks.layer3.top.locations%20%3E%20(model)%20location_target_response%20%3E%20(schema)>)