---
title: Indicators
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events)

[Tags](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Indicators

##### [List indicators related to a tag](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/tags/{tag\_uuid}/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {createdAt, indicatorType, updatedAt, 7 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)

#### IndicatorsBy Dataset

##### [List indicators related to a tag within a dataset (deprecated)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/indicators/subresources/by_dataset/methods/list)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/tags/{tag\_uuid}/indicators

##### ModelsExpand Collapse

<details>

<summary>

ByDatasetListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {createdAt, indicatorType, updatedAt, 7 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.tags.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)>)