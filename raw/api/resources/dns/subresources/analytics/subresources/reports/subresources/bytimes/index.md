---
title: Bytimes
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[DNS](https://developers.cloudflare.com/api/resources/dns)

[Analytics](https://developers.cloudflare.com/api/resources/dns/subresources/analytics)

[Reports](https://developers.cloudflare.com/api/resources/dns/subresources/analytics/subresources/reports)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Bytimes

##### [By Time](https://developers.cloudflare.com/api/resources/dns/subresources/analytics/subresources/reports/subresources/bytimes/methods/get)

Deprecated

GET/zones/{zone\_id}/dns\_analytics/report/bytime

##### ModelsExpand Collapse

<details>

<summary>

ByTime object {data, data\_lag, max, 5 more }

</summary>

<details>

<summary>

data: array of object {dimensions, metrics }

Array with one row per combination of dimension values.

</summary>

dimensions: array of string

Array of dimension values, representing the combination of dimension values corresponding to this row.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20dimensions">Link to this property</a>

metrics: array of array of number

Array with one item per requested metric. Each item is an array of values, broken down by time interval.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20metrics">Link to this property</a>

</details>

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

data\_lag: number

Number of seconds between current time and last processed event, in another words how many seconds of data could be missing.

minimum0

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20data_lag">Link to this property</a>

max: unknown

Maximum results for each metric (object mapping metric names to values). Currently always an empty object.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20max">Link to this property</a>

min: unknown

Minimum results for each metric (object mapping metric names to values). Currently always an empty object.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20min">Link to this property</a>

<details>

<summary>

query: object {dimensions, limit, metrics, 5 more }

</summary>

dimensions: array of string

Array of dimension names.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20dimensions">Link to this property</a>

limit: number

Limit number of returned metrics.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20limit">Link to this property</a>

metrics: array of string

Array of metric names.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20metrics">Link to this property</a>

since: string

Start date and time of requesting data period in ISO 8601 format.

formatdate-time

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20since">Link to this property</a>

<details>

<summary>

time\_delta: "all"or "auto"or "year"or 7 more

Unit of time to group data by.

</summary>

One of the following:

"all"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%200">Link to this property</a>

"auto"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%201">Link to this property</a>

"year"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%202">Link to this property</a>

"quarter"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%203">Link to this property</a>

"month"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%204">Link to this property</a>

"week"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%205">Link to this property</a>

"day"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%206">Link to this property</a>

"hour"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%207">Link to this property</a>

"dekaminute"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%208">Link to this property</a>

"minute"

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20time_delta">Link to this property</a>

until: string

End date and time of requesting data period in ISO 8601 format.

formatdate-time

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20until">Link to this property</a>

filters: optional string

Segmentation filter in ‘attribute operator value’ format.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20filters">Link to this property</a>

sort: optional array of string

Array of dimensions to sort by, where each dimension may be prefixed by - (descending) or + (ascending).

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query%20%3E%20(property)%20sort">Link to this property</a>

</details>

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20query">Link to this property</a>

rows: number

Total number of rows in the result.

minimum0

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20rows">Link to this property</a>

time\_intervals: array of array of string

Array of time intervals in the response data. Each interval is represented as an array containing two values: the start time, and the end time.

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20time_intervals">Link to this property</a>

totals: unknown

Total results for metrics across all data (object mapping metric names to values).

<a href="#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)%20%3E%20(property)%20totals">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.analytics.reports.bytimes%20%3E%20(model)%20by_time%20%3E%20(schema)>)