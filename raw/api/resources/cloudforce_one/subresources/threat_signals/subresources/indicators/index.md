---
title: Indicators
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Signals](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Indicators

##### [List Threat Signals article indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {id, article\_id, article\_title, 5 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20article_id">Link to this property</a>

article\_title: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20article_title">Link to this property</a>

dataset\_id: string

Threat Events dataset identifier for navigating from this indicator. Null when the account feeds dataset mapping is unavailable.

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {count, cursor, has\_more, 4 more }

</summary>

count: number

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20count">Link to this property</a>

cursor: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20cursor">Link to this property</a>

has\_more: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20has_more">Link to this property</a>

page: number

Ordinal of this cursor page; not a total-results offset.

minimum1

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

maximum100

minimum1

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20per_page">Link to this property</a>

total\_count: number

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count">Link to this property</a>

total\_count\_is\_exact: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)