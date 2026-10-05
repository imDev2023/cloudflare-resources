---
title: Radar
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Radar

#### RadarAgent Readiness

##### [Get agent readiness summary](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary)

GET/radar/agent\_readiness/summary/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

AgentReadinessSummaryResponse object {meta, summary\_0 }

</summary>

<details>

<summary>

meta: object {date, domainCategories, lastUpdated, 4 more }

</summary>

date: string

Date of the returned scan (YYYY-MM-DD). May differ from the requested date if no scan exists for that exact date.

formatdate

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20date">Link to this property</a>

<details>

<summary>

domainCategories: array of object {name, value }

Available domain sub-categories with their scan counts. Use as filter options for the domainCategory parameter.

</summary>

name: string

Sub-category name.

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20domainCategories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: number

Number of successfully scanned domains in this sub-category.

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20domainCategories%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20domainCategories">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

successfulDomains: number

Domains successfully scanned (excludes errors).

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20successfulDomains">Link to this property</a>

totalDomains: number

Total domains attempted in the scan.

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20totalDomains">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.agent_readiness%20%3E%20(model)%20agent_readiness_summary_response%20%3E%20(schema)>)

#### RadarAI

#### RadarAITo Markdown

##### [Convert uploaded files to Markdown](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/to_markdown/methods/create)

Deprecated

POST/accounts/{account\_id}/ai/tomarkdown

##### ModelsExpand Collapse

<details>

<summary>

ToMarkdownCreateResponse object {data, format, mimeType, 2 more }

</summary>

data: string

<a href="#(resource)%20radar.ai.to_markdown%20%3E%20(model)%20to_markdown_create_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

format: string

<a href="#(resource)%20radar.ai.to_markdown%20%3E%20(model)%20to_markdown_create_response%20%3E%20(schema)%20%3E%20(property)%20format">Link to this property</a>

mimeType: string

<a href="#(resource)%20radar.ai.to_markdown%20%3E%20(model)%20to_markdown_create_response%20%3E%20(schema)%20%3E%20(property)%20mimeType">Link to this property</a>

name: string

<a href="#(resource)%20radar.ai.to_markdown%20%3E%20(model)%20to_markdown_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

tokens: string

<a href="#(resource)%20radar.ai.to_markdown%20%3E%20(model)%20to_markdown_create_response%20%3E%20(schema)%20%3E%20(property)%20tokens">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.to_markdown%20%3E%20(model)%20to_markdown_create_response%20%3E%20(schema)>)

#### RadarAIInference

##### [Get Workers AI inference distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2)

GET/radar/ai/inference/summary/{dimension}

##### [Get time series distribution of Workers AI inference by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2)

GET/radar/ai/inference/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

InferenceSummaryV2Response object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_summary_v2_response%20%3E%20(schema)>)

<details>

<summary>

InferenceTimeseriesGroupsV2Response object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.inference%20%3E%20(model)%20inference_timeseries_groups_v2_response%20%3E%20(schema)>)

#### RadarAIInferenceSummary

##### [Get Workers AI models summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/methods/model)

Deprecated

GET/radar/ai/inference/summary/model

##### [Get Workers AI tasks summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/methods/task)

Deprecated

GET/radar/ai/inference/summary/task

##### ModelsExpand Collapse

<details>

<summary>

SummaryModelResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)>)

<details>

<summary>

SummaryTaskResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.inference.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)>)

#### RadarAIInferenceTimeseries Groups

#### RadarAIInferenceTimeseries GroupsSummary

##### [Get Workers AI models time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/subresources/summary/methods/model)

Deprecated

GET/radar/ai/inference/timeseries\_groups/model

##### [Get Workers AI tasks time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/subresources/summary/methods/task)

Deprecated

GET/radar/ai/inference/timeseries\_groups/task

##### ModelsExpand Collapse

<details>

<summary>

SummaryModelResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_model_response%20%3E%20(schema)>)

<details>

<summary>

SummaryTaskResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.inference.timeseries_groups.summary%20%3E%20(model)%20summary_task_response%20%3E%20(schema)>)

#### RadarAIBots

##### [Get AI bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2)

GET/radar/ai/bots/summary/{dimension}

##### [Get AI bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries)

GET/radar/ai/bots/timeseries

##### [Get time series distribution of AI bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups)

GET/radar/ai/bots/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

BotSummaryV2Response object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_summary_v2_response%20%3E%20(schema)>)

<details>

<summary>

BotTimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)>)

<details>

<summary>

BotTimeseriesGroupsResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)>)

#### RadarAIBotsSummary

##### [Get AI user agents summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/subresources/summary/methods/user_agent)

Deprecated

GET/radar/ai/bots/summary/user\_agent

##### ModelsExpand Collapse

<details>

<summary>

SummaryUserAgentResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.bots.summary%20%3E%20(model)%20summary_user_agent_response%20%3E%20(schema)>)

#### RadarAITimeseries Groups

##### [Get AI user agents time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/user_agent)

Deprecated

GET/radar/ai/bots/timeseries\_groups/user\_agent

##### [Get AI bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/summary)

Deprecated

GET/radar/ai/bots/summary/{dimension}

##### [Get AI bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries)

Deprecated

GET/radar/ai/bots/timeseries

##### [Get time series distribution of AI bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries_groups)

Deprecated

GET/radar/ai/bots/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

TimeseriesGroupUserAgentResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_user_agent_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupSummaryResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_summary_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupTimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_response%20%3E%20(schema)>)

<details>

<summary>

TimeseriesGroupTimeseriesGroupsResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.timeseries_groups%20%3E%20(model)%20timeseries_group_timeseries_groups_response%20%3E%20(schema)>)

#### RadarAIMarkdown For Agents

##### [Get AI markdown for agents reduction ratio summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary)

GET/radar/ai/markdown\_for\_agents/summary

##### [Get AI markdown for agents reduction ratio time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/timeseries)

GET/radar/ai/markdown\_for\_agents/timeseries

##### ModelsExpand Collapse

<details>

<summary>

MarkdownForAgentSummaryResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

summary\_0: object {value }

</summary>

value: string

A numeric string that can include decimals and infinity values.

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_summary_response%20%3E%20(schema)>)

<details>

<summary>

MarkdownForAgentTimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ai.markdown_for_agents%20%3E%20(model)%20markdown_for_agent_timeseries_response%20%3E%20(schema)>)

#### RadarCT

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

#### RadarCTAuthorities

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

#### RadarCTLogs

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

#### RadarAnnotations

##### [Get latest annotations](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/methods/list)

GET/radar/annotations

##### ModelsExpand Collapse

<details>

<summary>

AnnotationListResponse object {annotations }

</summary>

<details>

<summary>

annotations: array of object {id, asns, asnsDetails, 15 more }

</summary>

id: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

asns: array of number

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

asnsDetails: array of object {asn, location, name }

</summary>

asn: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

<details>

<summary>

location: object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails">Link to this property</a>

dataSource: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

entities: array of object {entityName, entityType, entityValue }

</summary>

entityName: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityName">Link to this property</a>

entityType: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityType">Link to this property</a>

entityValue: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityValue">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities">Link to this property</a>

eventType: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

geoIds: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20geoIds">Link to this property</a>

linkedUrl: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

locations: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locations">Link to this property</a>

<details>

<summary>

locationsDetails: array of object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails">Link to this property</a>

origins: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20origins">Link to this property</a>

<details>

<summary>

originsDetails: array of object {name, origin }

</summary>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

origin: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails">Link to this property</a>

<details>

<summary>

outage: object {outageCause, outageType }

</summary>

outageCause: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageCause">Link to this property</a>

outageType: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageType">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage">Link to this property</a>

scope: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

startDate: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)>)

#### RadarAnnotationsOutages

##### [Get latest Internet outages and anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/get)

GET/radar/annotations/outages

##### [Get the number of outages by location](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/locations)

GET/radar/annotations/outages/locations

##### ModelsExpand Collapse

<details>

<summary>

OutageGetResponse object {annotations }

</summary>

<details>

<summary>

annotations: array of object {id, asns, asnsDetails, 15 more }

</summary>

id: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

asns: array of number

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

asnsDetails: array of object {asn, location, name }

</summary>

asn: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

<details>

<summary>

location: object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails">Link to this property</a>

dataSource: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

entities: array of object {entityName, entityType, entityValue }

</summary>

entityName: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityName">Link to this property</a>

entityType: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityType">Link to this property</a>

entityValue: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityValue">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities">Link to this property</a>

eventType: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

geoIds: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20geoIds">Link to this property</a>

linkedUrl: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

locations: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locations">Link to this property</a>

<details>

<summary>

locationsDetails: array of object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails">Link to this property</a>

origins: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20origins">Link to this property</a>

<details>

<summary>

originsDetails: array of object {name, origin }

</summary>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

origin: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails">Link to this property</a>

<details>

<summary>

outage: object {outageCause, outageType }

</summary>

outageCause: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageCause">Link to this property</a>

outageType: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageType">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage">Link to this property</a>

scope: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)>)

<details>

<summary>

OutageLocationsResponse object {annotations }

</summary>

<details>

<summary>

annotations: array of object {clientCountryAlpha2, clientCountryName, value }

</summary>

clientCountryAlpha2: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20clientCountryAlpha2">Link to this property</a>

clientCountryName: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20clientCountryName">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)>)

#### RadarBGP

##### [Get BGP time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/methods/timeseries)

GET/radar/bgp/timeseries

##### ModelsExpand Collapse

<details>

<summary>

BGPTimeseriesResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, lastUpdated }

</summary>

<details>

<summary>

aggInterval: "15m"or "1h"or "1d"or "1w"

</summary>

One of the following:

"15m"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"1h"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"1d"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"1w"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

formatdate-time

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps, values }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

values: array of string

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp%20%3E%20(model)%20bgp_timeseries_response%20%3E%20(schema)>)

#### RadarBGPLeaks

#### RadarBGPLeaksEvents

##### [Get BGP route leak events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list)

GET/radar/bgp/leaks/events

##### ModelsExpand Collapse

<details>

<summary>

EventListResponse object {asn\_info, events }

</summary>

<details>

<summary>

asn\_info: array of object {asn, country\_code, org\_name }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country\_code: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20country_code">Link to this property</a>

org\_name: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info">Link to this property</a>

<details>

<summary>

events: array of object {id, countries, detected\_ts, 10 more }

</summary>

id: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

countries: array of string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

detected\_ts: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20detected_ts">Link to this property</a>

finished: boolean

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20finished">Link to this property</a>

leak\_asn: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_asn">Link to this property</a>

leak\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_count">Link to this property</a>

leak\_seg: array of number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_seg">Link to this property</a>

leak\_type: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_type">Link to this property</a>

max\_ts: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20max_ts">Link to this property</a>

min\_ts: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20min_ts">Link to this property</a>

origin\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20origin_count">Link to this property</a>

peer\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20peer_count">Link to this property</a>

prefix\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20prefix_count">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)>)

#### RadarBGPTop

##### [Get top prefixes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/methods/prefixes)

GET/radar/bgp/top/prefixes

##### ModelsExpand Collapse

<details>

<summary>

TopPrefixesResponse object {meta, top\_0 }

</summary>

<details>

<summary>

meta: object {dateRange }

</summary>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {prefix, value }

</summary>

prefix: string

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.top%20%3E%20(model)%20top_prefixes_response%20%3E%20(schema)>)

#### RadarBGPTopAses

##### [Get top ASes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/get)

GET/radar/bgp/top/ases

##### [Get top ASes by prefix count](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/prefixes)

GET/radar/bgp/top/ases/prefixes

##### ModelsExpand Collapse

<details>

<summary>

AseGetResponse object {meta, top\_0 }

</summary>

<details>

<summary>

meta: object {dateRange }

</summary>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {asn, ASName, value }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

ASName: string

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20ASName">Link to this property</a>

value: string

Percentage of updates by this AS out of the total updates by all autonomous systems.

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_get_response%20%3E%20(schema)>)

<details>

<summary>

AsePrefixesResponse object {asns, meta }

</summary>

<details>

<summary>

asns: array of object {asn, country, name, pfxs\_count }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country: string

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20country">Link to this property</a>

name: string

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

pfxs\_count: number

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20pfxs_count">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.top.ases%20%3E%20(model)%20ase_prefixes_response%20%3E%20(schema)>)

#### RadarBGPHijacks

#### RadarBGPHijacksEvents

##### [Get BGP hijack events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list)

GET/radar/bgp/hijacks/events

##### ModelsExpand Collapse

<details>

<summary>

EventListResponse object {asn\_info, events, total\_monitors }

</summary>

<details>

<summary>

asn\_info: array of object {asn, country\_code, org\_name }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country\_code: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20country_code">Link to this property</a>

org\_name: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info">Link to this property</a>

<details>

<summary>

events: array of object {id, confidence\_score, duration, 15 more }

</summary>

id: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

confidence\_score: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20confidence_score">Link to this property</a>

duration: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20duration">Link to this property</a>

event\_type: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20event_type">Link to this property</a>

hijack\_msgs\_count: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20hijack_msgs_count">Link to this property</a>

hijacker\_asn: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20hijacker_asn">Link to this property</a>

hijacker\_country: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20hijacker_country">Link to this property</a>

is\_stale: boolean

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20is_stale">Link to this property</a>

max\_hijack\_ts: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20max_hijack_ts">Link to this property</a>

max\_msg\_ts: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20max_msg_ts">Link to this property</a>

min\_hijack\_ts: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20min_hijack_ts">Link to this property</a>

on\_going\_count: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20on_going_count">Link to this property</a>

peer\_asns: array of number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20peer_asns">Link to this property</a>

peer\_ip\_count: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20peer_ip_count">Link to this property</a>

prefixes: array of string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20prefixes">Link to this property</a>

<details>

<summary>

tags: array of object {name, score }

</summary>

name: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

score: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

victim\_asns: array of number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20victim_asns">Link to this property</a>

victim\_countries: array of string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20victim_countries">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

total\_monitors: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20total_monitors">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)>)

#### RadarBGPRoutes

##### [Get Multi-Origin AS (MOAS) prefixes](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/moas)

GET/radar/bgp/routes/moas

##### [Get prefix-to-ASN mapping](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/pfx2as)

GET/radar/bgp/routes/pfx2as

##### [Get BGP routing table stats](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/stats)

GET/radar/bgp/routes/stats

##### [List ASes from global routing tables](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/ases)

GET/radar/bgp/routes/ases

##### [Get real-time BGP routes for a prefix](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/realtime)

GET/radar/bgp/routes/realtime

##### ModelsExpand Collapse

<details>

<summary>

RouteMoasResponse object {meta, moas }

</summary>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

moas: array of object {origins, prefix }

</summary>

<details>

<summary>

origins: array of object {origin, peer\_count, rpki\_validation }

</summary>

origin: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

peer\_count: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20peer_count">Link to this property</a>

rpki\_validation: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20rpki_validation">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins">Link to this property</a>

prefix: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)>)

<details>

<summary>

RoutePfx2asResponse object {meta, prefix\_origins }

</summary>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

prefix\_origins: array of object {origin, peer\_count, prefix, rpki\_validation }

</summary>

origin: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

peer\_count: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20peer_count">Link to this property</a>

prefix: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

rpki\_validation: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20rpki_validation">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)>)

<details>

<summary>

RouteStatsResponse object {meta, stats }

</summary>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

stats: object {distinct\_origins, distinct\_origins\_ipv4, distinct\_origins\_ipv6, 15 more }

</summary>

distinct\_origins: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_origins">Link to this property</a>

distinct\_origins\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_origins_ipv4">Link to this property</a>

distinct\_origins\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_origins_ipv6">Link to this property</a>

distinct\_prefixes: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_prefixes">Link to this property</a>

distinct\_prefixes\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_prefixes_ipv4">Link to this property</a>

distinct\_prefixes\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_prefixes_ipv6">Link to this property</a>

routes\_invalid: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_invalid">Link to this property</a>

routes\_invalid\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_invalid_ipv4">Link to this property</a>

routes\_invalid\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_invalid_ipv6">Link to this property</a>

routes\_total: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_total">Link to this property</a>

routes\_total\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_total_ipv4">Link to this property</a>

routes\_total\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_total_ipv6">Link to this property</a>

routes\_unknown: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_unknown">Link to this property</a>

routes\_unknown\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_unknown_ipv4">Link to this property</a>

routes\_unknown\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_unknown_ipv6">Link to this property</a>

routes\_valid: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_valid">Link to this property</a>

routes\_valid\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_valid_ipv4">Link to this property</a>

routes\_valid\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_valid_ipv6">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)>)

<details>

<summary>

RouteAsesResponse object {asns, meta }

</summary>

<details>

<summary>

asns: array of object {asn, coneSize, country, 7 more }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

coneSize: number

AS’s customer cone size.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20coneSize">Link to this property</a>

country: string

Alpha-2 code for the AS’s registration country.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20country">Link to this property</a>

ipv4Count: number

Number of IPv4 addresses originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20ipv4Count">Link to this property</a>

ipv6Count: string

Number of IPv6 addresses originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20ipv6Count">Link to this property</a>

name: string

Name of the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

pfxsCount: number

Number of total IP prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20pfxsCount">Link to this property</a>

rpkiInvalid: number

Number of RPKI invalid prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20rpkiInvalid">Link to this property</a>

rpkiUnknown: number

Number of RPKI unknown prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20rpkiUnknown">Link to this property</a>

rpkiValid: number

Number of RPKI valid prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20rpkiValid">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

meta: object {dataTime, queryTime, totalPeers }

</summary>

dataTime: string

The timestamp of when the data is generated.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

queryTime: string

The timestamp of the query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

totalPeers: number

Total number of route collector peers used to generate this data.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20totalPeers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)>)

<details>

<summary>

RouteRealtimeResponse object {meta, routes }

</summary>

<details>

<summary>

meta: object {asn\_info, collectors, data\_time, 2 more }

</summary>

<details>

<summary>

asn\_info: array of object {as\_name, asn, country\_code, 2 more }

</summary>

as\_name: string

Name of the autonomous system.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20as_name">Link to this property</a>

asn: number

AS number.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country\_code: string

Alpha-2 code for the AS’s registration country.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20country_code">Link to this property</a>

org\_id: string

Organization ID.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_id">Link to this property</a>

org\_name: string

Organization name.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info">Link to this property</a>

<details>

<summary>

collectors: array of object {collector, latest\_realtime\_ts, latest\_rib\_ts, 4 more }

</summary>

collector: string

Public route collector ID.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20collector">Link to this property</a>

latest\_realtime\_ts: string

Latest real-time stream timestamp for this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20latest_realtime_ts">Link to this property</a>

latest\_rib\_ts: string

Latest RIB dump MRT file timestamp for this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20latest_rib_ts">Link to this property</a>

latest\_updates\_ts: string

Latest BGP updates MRT file timestamp for this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20latest_updates_ts">Link to this property</a>

peers\_count: number

Total number of collector peers used from this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20peers_count">Link to this property</a>

peers\_v4\_count: number

Total number of collector peers used from this collector for IPv4 prefixes.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20peers_v4_count">Link to this property</a>

peers\_v6\_count: number

Total number of collector peers used from this collector for IPv6 prefixes.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20peers_v6_count">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors">Link to this property</a>

data\_time: string

The most recent data timestamp for from the real-time sources.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

<details>

<summary>

prefix\_origins: array of object {origin, prefix, rpki\_validation, 3 more }

</summary>

origin: number

Origin ASN.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

prefix: string

IP prefix of this query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

rpki\_validation: string

Prefix-origin RPKI validation: valid, invalid, unknown.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20rpki_validation">Link to this property</a>

total\_peers: number

Total number of peers.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20total_peers">Link to this property</a>

total\_visible: number

Total number of peers seeing this prefix.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20total_visible">Link to this property</a>

visibility: number

Ratio of peers seeing this prefix to total number of peers.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20visibility">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins">Link to this property</a>

query\_time: string

The timestamp of this query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

routes: array of object {as\_path, collector, communities, 2 more }

</summary>

as\_path: array of number

AS-level path for this route, from collector to origin.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20as_path">Link to this property</a>

collector: string

Public collector ID for this route.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20collector">Link to this property</a>

communities: array of string

BGP community values.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20communities">Link to this property</a>

prefix: string

IP prefix of this query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

timestamp: string

Latest timestamp of change for this route.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)>)

#### RadarBGPRoutesUpstreams

##### [Get upstream composition time series for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries)

GET/radar/bgp/routes/upstreams/{asn}/timeseries

##### ModelsExpand Collapse

<details>

<summary>

UpstreamTimeseriesResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {dataTime, effectiveCollector, queryTime, stale }

</summary>

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

effectiveCollector: string

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20effectiveCollector">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

stale: boolean

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20stale">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)>)

#### RadarBGPRoutesPaths

##### [Get tier-1 path segments for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list)

GET/radar/bgp/routes/paths/{asn}

##### ModelsExpand Collapse

<details>

<summary>

PathListResponse object {asnInfo, collectors, meta, paths }

</summary>

<details>

<summary>

asnInfo: map\[object {asn, country, name } ]

</summary>

asn: number

ASN number.

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country: string

Alpha-2 country code.

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(items)%20%3E%20(property)%20country">Link to this property</a>

name: string

AS name.

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo">Link to this property</a>

collectors: array of string

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20collectors">Link to this property</a>

<details>

<summary>

meta: object {dataTime, effectiveCollector, queryTime, stale }

</summary>

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

effectiveCollector: string

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20effectiveCollector">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

stale: boolean

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20stale">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

paths: array of object {collectors, pathsCount, peersCount, segment }

</summary>

collectors: array of string

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20paths%20%3E%20(items)%20%3E%20(property)%20collectors">Link to this property</a>

pathsCount: number

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20paths%20%3E%20(items)%20%3E%20(property)%20pathsCount">Link to this property</a>

peersCount: number

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20paths%20%3E%20(items)%20%3E%20(property)%20peersCount">Link to this property</a>

segment: array of number

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20paths%20%3E%20(items)%20%3E%20(property)%20segment">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)%20%3E%20(property)%20paths">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes.paths%20%3E%20(model)%20path_list_response%20%3E%20(schema)>)

#### RadarBGPIPs

##### [Get announced IP address space time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/methods/timeseries)

GET/radar/bgp/ips/timeseries

##### ModelsExpand Collapse

<details>

<summary>

IPTimeseriesResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {aggInterval, confidenceInfo, dateRange, 4 more }

Metadata for the results.

</summary>

<details>

<summary>

aggInterval: "FIFTEEN\_MINUTES"or "ONE\_HOUR"or "ONE\_DAY"or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to <a href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/">Aggregation intervals</a>.

</summary>

One of the following:

"FIFTEEN\_MINUTES"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

<details>

<summary>

delay: optional object {asn\_data, country\_data, healthy, nowTs }

</summary>

<details>

<summary>

asn\_data: object {delaySecs, delayStr, healthy, latest }

</summary>

delaySecs: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20delaySecs">Link to this property</a>

delayStr: string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20delayStr">Link to this property</a>

healthy: boolean

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20healthy">Link to this property</a>

<details>

<summary>

latest: object {entries\_count, path, timestamp }

</summary>

entries\_count: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20latest%20%3E%20(property)%20entries_count">Link to this property</a>

path: string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20latest%20%3E%20(property)%20path">Link to this property</a>

timestamp: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20latest%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data%20%3E%20(property)%20latest">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20asn_data">Link to this property</a>

<details>

<summary>

country\_data: object {delaySecs, delayStr, healthy, latest }

</summary>

delaySecs: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data%20%3E%20(property)%20delaySecs">Link to this property</a>

delayStr: string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data%20%3E%20(property)%20delayStr">Link to this property</a>

healthy: boolean

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data%20%3E%20(property)%20healthy">Link to this property</a>

<details>

<summary>

latest: object {count, timestamp }

</summary>

count: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data%20%3E%20(property)%20latest%20%3E%20(property)%20count">Link to this property</a>

timestamp: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data%20%3E%20(property)%20latest%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data%20%3E%20(property)%20latest">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20country_data">Link to this property</a>

healthy: boolean

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20healthy">Link to this property</a>

nowTs: number

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay%20%3E%20(property)%20nowTs">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20delay">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {ipv4, ipv6, timestamps }

</summary>

ipv4: array of string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20ipv4">Link to this property</a>

ipv6: array of string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20ipv6">Link to this property</a>

timestamps: array of string

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.ips%20%3E%20(model)%20ip_timeseries_response%20%3E%20(schema)>)

#### RadarBGPIPsTop

##### [Get top ASes by announced IP space](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases)

GET/radar/bgp/ips/top/ases

##### ModelsExpand Collapse

<details>

<summary>

TopAsesResponse object {anchorTs, asns, country, metric }

</summary>

anchorTs: string

formatdate-time

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20anchorTs">Link to this property</a>

<details>

<summary>

asns: array of object {asn, v4\_24s, v6\_48s }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

v4\_24s: number

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20v4_24s">Link to this property</a>

v6\_48s: number

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20v6_48s">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns">Link to this property</a>

country: string

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

metric: string

<a href="#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20metric">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.ips.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)>)

#### RadarBGPRPKI

#### RadarBGPRPKIASPA

##### [Get ASPA objects snapshot](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot)

GET/radar/bgp/rpki/aspa/snapshot

##### [Get ASPA changes over time](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes)

GET/radar/bgp/rpki/aspa/changes

##### [Get ASPA count time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries)

GET/radar/bgp/rpki/aspa/timeseries

##### ModelsExpand Collapse

<details>

<summary>

ASPASnapshotResponse object {asnInfo, aspaObjects, meta }

</summary>

<details>

<summary>

asnInfo: object {"13335" }

</summary>

<details>

<summary>

"13335": object {asn, country, name }

</summary>

asn: number

ASN number.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335%20%3E%20(property)%20asn">Link to this property</a>

country: string

Alpha-2 country code.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335%20%3E%20(property)%20country">Link to this property</a>

name: string

AS name.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo">Link to this property</a>

<details>

<summary>

aspaObjects: array of object {customerAsn, providers }

</summary>

customerAsn: number

The customer ASN publishing the ASPA object.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20aspaObjects%20%3E%20(items)%20%3E%20(property)%20customerAsn">Link to this property</a>

providers: array of number

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20aspaObjects%20%3E%20(items)%20%3E%20(property)%20providers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20aspaObjects">Link to this property</a>

<details>

<summary>

meta: object {dataTime, queryTime, totalCount }

</summary>

dataTime: string

Timestamp of the underlying data.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

totalCount: number

Total number of ASPA objects.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20totalCount">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_snapshot_response%20%3E%20(schema)>)

<details>

<summary>

ASPAChangesResponse object {asnInfo, changes, meta }

</summary>

<details>

<summary>

asnInfo: object {"13335" }

</summary>

<details>

<summary>

"13335": object {asn, country, name }

</summary>

asn: number

ASN number.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335%20%3E%20(property)%20asn">Link to this property</a>

country: string

Alpha-2 country code.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335%20%3E%20(property)%20country">Link to this property</a>

name: string

AS name.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo%20%3E%20(property)%2013335">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20asnInfo">Link to this property</a>

<details>

<summary>

changes: array of object {customersAdded, customersRemoved, date, 4 more }

</summary>

customersAdded: number

Number of new ASPA objects created.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20customersAdded">Link to this property</a>

customersRemoved: number

Number of ASPA objects deleted.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20customersRemoved">Link to this property</a>

date: string

Date of the changes in ISO 8601 format.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20date">Link to this property</a>

<details>

<summary>

entries: array of object {customerAsn, providers, type }

</summary>

customerAsn: number

The customer ASN affected.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20customerAsn">Link to this property</a>

providers: array of number

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20providers">Link to this property</a>

<details>

<summary>

type: "CustomerAdded"or "CustomerRemoved"or "ProvidersAdded"or "ProvidersRemoved"

</summary>

One of the following:

"CustomerAdded"

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"CustomerRemoved"

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"ProvidersAdded"

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"ProvidersRemoved"

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20entries">Link to this property</a>

providersAdded: number

Number of providers added to existing objects.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20providersAdded">Link to this property</a>

providersRemoved: number

Number of providers removed from existing objects.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20providersRemoved">Link to this property</a>

totalCount: number

Running total of active ASPA objects after this day.

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes%20%3E%20(items)%20%3E%20(property)%20totalCount">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20changes">Link to this property</a>

<details>

<summary>

meta: object {dataTime, queryTime }

</summary>

dataTime: string

Timestamp of the underlying data.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_changes_response%20%3E%20(schema)>)

<details>

<summary>

ASPATimeseriesResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {dataTime, queryTime }

</summary>

dataTime: string

Timestamp of the underlying data.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps, values }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

values: array of string

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.rpki.aspa%20%3E%20(model)%20aspa_timeseries_response%20%3E%20(schema)>)

#### RadarBGPRPKIRoas

##### [Get RPKI ROA deployment time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries)

GET/radar/bgp/rpki/roas/timeseries

##### ModelsExpand Collapse

<details>

<summary>

RoaTimeseriesResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {dataTime, queryTime }

</summary>

dataTime: string

Timestamp of the underlying data.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps, values }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

values: array of string

<a href="#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.rpki.roas%20%3E%20(model)%20roa_timeseries_response%20%3E%20(schema)>)

#### RadarBots

##### [List bots](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/list)

GET/radar/bots

##### [Get bot details](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/get)

GET/radar/bots/{bot\_slug}

##### [Get bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/summary)

GET/radar/bots/summary/{dimension}

##### [Get bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries)

GET/radar/bots/timeseries

##### [Get time series distribution of bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries_groups)

GET/radar/bots/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

BotListResponse object {bots }

</summary>

<details>

<summary>

bots: array of object {category, description, kind, 4 more }

</summary>

category: string

The category of the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

description: string

A summary for the bot (e.g., purpose).

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

Deprecatedkind: string

The kind of the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

name: string

The name of the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

operator: string

The organization that owns and operates the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20operator">Link to this property</a>

slug: string

A kebab-case identifier derived from the bot name.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20slug">Link to this property</a>

userAgentPatterns: array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots%20%3E%20(items)%20%3E%20(property)%20userAgentPatterns">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)%20%3E%20(property)%20bots">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots%20%3E%20(model)%20bot_list_response%20%3E%20(schema)>)

<details>

<summary>

BotGetResponse object {bot }

</summary>

<details>

<summary>

bot: object {category, description, kind, 7 more }

</summary>

category: string

The category of the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20category">Link to this property</a>

description: string

A summary for the bot (e.g., purpose).

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20description">Link to this property</a>

Deprecatedkind: string

The kind of the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20kind">Link to this property</a>

name: string

The name of the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20name">Link to this property</a>

operator: string

The organization that owns and operates the bot.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20operator">Link to this property</a>

operatorUrl: string

The link to the bot documentation.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20operatorUrl">Link to this property</a>

slug: string

A kebab-case identifier derived from the bot name.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20slug">Link to this property</a>

userAgentPatterns: array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20userAgentPatterns">Link to this property</a>

userAgents: array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20userAgents">Link to this property</a>

signatureAgentUrl: optional string

The URL of the agent’s <a href="https://blog.cloudflare.com/web-bot-auth/">Web Bot Auth</a> resource. Null for bots not verified via request signature.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot%20%3E%20(property)%20signatureAgentUrl">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)%20%3E%20(property)%20bot">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots%20%3E%20(model)%20bot_get_response%20%3E%20(schema)>)

<details>

<summary>

BotSummaryResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots%20%3E%20(model)%20bot_summary_response%20%3E%20(schema)>)

<details>

<summary>

BotTimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_response%20%3E%20(schema)>)

<details>

<summary>

BotTimeseriesGroupsResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots%20%3E%20(model)%20bot_timeseries_groups_response%20%3E%20(schema)>)

#### RadarBotsWeb Crawlers

##### [Get crawler HTTP request distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary)

GET/radar/bots/crawlers/summary/{dimension}

##### [Get time series of crawler HTTP request distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups)

GET/radar/bots/crawlers/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

WebCrawlerSummaryResponse object {meta, summary\_0 }

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

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_summary_response%20%3E%20(schema)>)

<details>

<summary>

WebCrawlerTimeseriesGroupsResponse object {meta, serie\_0 }

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

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bots.web_crawlers%20%3E%20(model)%20web_crawler_timeseries_groups_response%20%3E%20(schema)>)

#### RadarDatasets

##### [List datasets](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/list)

GET/radar/datasets

##### [Get dataset CSV stream](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/get)

GET/radar/datasets/{alias}

##### [Get dataset download URL](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/download)

POST/radar/datasets/download

##### ModelsExpand Collapse

<details>

<summary>

DatasetListResponse object {datasets }

</summary>

<details>

<summary>

datasets: array of object {id, description, meta, 3 more }

</summary>

id: number

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

description: string

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

meta: unknown

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

tags: array of string

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

type: string

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20datasets">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.datasets%20%3E%20(model)%20dataset_list_response%20%3E%20(schema)>)

DatasetGetResponse = string

[Link to this property](<#(resource)%20radar.datasets%20%3E%20(model)%20dataset_get_response%20%3E%20(schema)>)

<details>

<summary>

DatasetDownloadResponse object {dataset }

</summary>

<details>

<summary>

dataset: object {url }

</summary>

url: string

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_download_response%20%3E%20(schema)%20%3E%20(property)%20dataset%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20radar.datasets%20%3E%20(model)%20dataset_download_response%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.datasets%20%3E%20(model)%20dataset_download_response%20%3E%20(schema)>)

#### RadarDNS

##### [Get DNS summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2)

GET/radar/dns/summary/{dimension}

##### [Get DNS queries time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries)

GET/radar/dns/timeseries

##### [Get DNS time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries_groups_v2)

GET/radar/dns/timeseries\_groups/{dimension}

##### ModelsExpand Collapse

<details>

<summary>

DNSSummaryV2Response object {meta, summary\_0 }

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

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

summary\_0: map\[string]

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)%20%3E%20(property)%20summary_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.dns%20%3E%20(model)%20dns_summary_v2_response%20%3E%20(schema)>)

<details>

<summary>

DNSTimeseriesResponse object {meta }

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

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_response%20%3E%20(schema)>)

<details>

<summary>

DNSTimeseriesGroupsV2Response object {meta, serie\_0 }

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

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%200">Link to this property</a>

"ONE\_HOUR"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%201">Link to this property</a>

"ONE\_DAY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%202">Link to this property</a>

"ONE\_WEEK"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%203">Link to this property</a>

"ONE\_MONTH"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20aggInterval">Link to this property</a>

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

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.dns%20%3E%20(model)%20dns_timeseries_groups_v2_response%20%3E%20(schema)>)

#### RadarDNSTop

##### [Get top ASes by DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/methods/ases)

GET/radar/dns/top/ases

##### [Get top locations by DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/methods/locations)

GET/radar/dns/top/locations

##### ModelsExpand Collapse

<details>

<summary>

TopAsesResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

"ROLLING\_AVERAGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%205">Link to this property</a>

"OVERLAPPED\_PERCENTAGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%206">Link to this property</a>

"RATIO"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization">Link to this property</a>

<details>

<summary>

units: array of object {name, value }

Measurement units for the results.

</summary>

name: string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20units">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

top\_0: array of object {clientASN, clientASName, value }

</summary>

clientASN: number

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20clientASN">Link to this property</a>

clientASName: string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20clientASName">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20top_0%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)%20%3E%20(property)%20top_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.dns.top%20%3E%20(model)%20top_ases_response%20%3E%20(schema)>)

<details>

<summary>

TopLocationsResponse object {meta, top\_0 }

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

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%200">Link to this property</a>

"AI\_BOTS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%201">Link to this property</a>

"AI\_GATEWAY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%202">Link to this property</a>

"BGP"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%203">Link to this property</a>

"BOTS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%204">Link to this property</a>

"CONNECTION\_ANOMALY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%205">Link to this property</a>

"CT"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%206">Link to this property</a>

"DNS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%207">Link to this property</a>

"DNS\_MAGNITUDE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%208">Link to this property</a>

"DNS\_AS112"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%209">Link to this property</a>

"DOS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2010">Link to this property</a>

"EMAIL\_ROUTING"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2011">Link to this property</a>

"EMAIL\_SECURITY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2012">Link to this property</a>

"FW"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2013">Link to this property</a>

"FW\_PG"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2014">Link to this property</a>

"HTTP"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2015">Link to this property</a>

"HTTP\_CONTROL"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2016">Link to this property</a>

"HTTP\_CRAWLER\_REFERER"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2017">Link to this property</a>

"HTTP\_ORIGINS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2018">Link to this property</a>

"IQI"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2019">Link to this property</a>

"LEAKED\_CREDENTIALS"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2020">Link to this property</a>

"NET"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2021">Link to this property</a>

"ROBOTS\_TXT"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2022">Link to this property</a>

"SPEED"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2023">Link to this property</a>

"WORKERS\_AI"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource%20%3E%20(member)%2024">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

eventType: "GENERAL"or "OUTAGE"or "PARTIAL\_PROJECTION"or 2 more

Event type for annotations.

</summary>

One of the following:

"GENERAL"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%200">Link to this property</a>

"OUTAGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%201">Link to this property</a>

"PARTIAL\_PROJECTION"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%202">Link to this property</a>

"PIPELINE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%203">Link to this property</a>

"TRAFFIC\_ANOMALY"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

isInstantaneous: boolean

Whether event is a single point in time or a time range.

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20isInstantaneous">Link to this property</a>

linkedUrl: string

formaturi

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: optional array of string

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20annotations">Link to this property</a>

level: number

Provides an indication of how much confidence Cloudflare has in the data.

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo%20%3E%20(property)%20level">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20confidenceInfo">Link to this property</a>

<details>

<summary>

dateRange: array of object {endTime, startTime }

</summary>

endTime: string

Adjusted end of date range.

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20lastUpdated">Link to this property</a>

<details>

<summary>

normalization: "PERCENTAGE"or "MIN0\_MAX"or "MIN\_MAX"or 5 more

Normalization method applied to the results. Refer to <a href="https://developers.cloudflare.com/radar/concepts/normalization/">Normalization methods</a>.

</summary>

One of the following:

"PERCENTAGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%200">Link to this property</a>

"MIN0\_MAX"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%201">Link to this property</a>

"MIN\_MAX"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%202">Link to this property</a>

"RAW\_VALUES"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%203">Link to this property</a>

"PERCENTAGE\_CHANGE"

<a href="#(resource)%20radar.dns.top%20%3E%20(model)%20top_locations_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20normalization%20%3E%20(member)%204">Link to this property</a>

</details>

</details>

</details>

<!-- Cloudflare Markdown for Agents: incomplete conversion; source HTML truncated at the conversion size limit -->
