---
title: Indicators
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Indicators

##### [Lists indicators across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {properties, type }

</summary>

<details>

<summary>

properties: object {completeness, indicators, pagination }

</summary>

<details>

<summary>

completeness: object {properties, type }

</summary>

<details>

<summary>

properties: object {complete, failedDatasets, failedShards, warnings }

</summary>

<details>

<summary>

complete: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20complete%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20complete">Link to this property</a>

<details>

<summary>

failedDatasets: object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedDatasets">Link to this property</a>

<details>

<summary>

failedShards: object {items, type }

</summary>

<details>

<summary>

items: object {properties, type }

</summary>

<details>

<summary>

properties: object {datasetId, shardId }

</summary>

<details>

<summary>

datasetId: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20datasetId%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

shardId: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20shardId%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties%20%3E%20(property)%20shardId">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20failedShards">Link to this property</a>

<details>

<summary>

warnings: object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties%20%3E%20(property)%20warnings">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20completeness">Link to this property</a>

<details>

<summary>

indicators: object {items, type }

</summary>

<details>

<summary>

items: object {createdAt, indicatorType, sources, 8 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20indicatorType">Link to this property</a>

<details>

<summary>

sources: array of object {resourceId, resourceType, system, title }

RSS article sources from which this indicator was extracted.

</summary>

resourceId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceId">Link to this property</a>

resourceType: "article"

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceType">Link to this property</a>

system: "threat-signals"

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20system">Link to this property</a>

title: string

Threat Signals article title; null for historical provenance without a stored title.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20sources">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {properties, type }

</summary>

<details>

<summary>

properties: object {count, cursor, has\_more, 4 more }

</summary>

<details>

<summary>

count: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20count%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

cursor: object {description, nullable, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor%20%3E%20(property)%20description">Link to this property</a>

nullable: boolean

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor%20%3E%20(property)%20nullable">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20cursor">Link to this property</a>

<details>

<summary>

has\_more: object {description, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20has_more%20%3E%20(property)%20description">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20has_more%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20has_more">Link to this property</a>

<details>

<summary>

page: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20page%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20page">Link to this property</a>

<details>

<summary>

per\_page: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20per_page%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

total\_count: object {description, nullable, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count%20%3E%20(property)%20description">Link to this property</a>

nullable: boolean

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count%20%3E%20(property)%20nullable">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count">Link to this property</a>

<details>

<summary>

total\_count\_is\_exact: object {description, type }

</summary>

description: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count_is_exact%20%3E%20(property)%20description">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count_is_exact%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties%20%3E%20(property)%20pagination">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20properties">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)

#### IndicatorsAggregate

##### [Aggregate indicators by column(s)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/aggregate/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/indicators/aggregate

##### ModelsExpand Collapse

<details>

<summary>

AggregateListResponse object {aggregateBy, aggregations, failedDatasets, total }

</summary>

aggregateBy: string

Column(s) that were aggregated by

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregateBy">Link to this property</a>

<details>

<summary>

aggregations: array of object {count }

Array of aggregation results with dynamic fields based on aggregateBy columns

</summary>

count: number

Number of indicators for this aggregation

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20aggregations">Link to this property</a>

failedDatasets: number

Number of datasets whose aggregation failed and were excluded from the result

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20failedDatasets">Link to this property</a>

total: number

Total count in the aggregation: indicator rows when measure=indicators, or linked-event rows when measure=relationships

<a href="#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)%20%3E%20(property)%20total">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.aggregate%20%3E%20(model)%20aggregate_list_response%20%3E%20(schema)>)

#### IndicatorsTypes

##### [Lists indicator types across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/types/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/indicator-types

##### ModelsExpand Collapse

<details>

<summary>

TypeListResponse object {items, type }

</summary>

<details>

<summary>

items: object {type }

</summary>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.types%20%3E%20(model)%20type_list_response%20%3E%20(schema)>)

#### IndicatorsBy Dataset

##### [Lists indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/methods/list)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/indicators

##### [Reads an indicator](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/indicators/{indicator\_id}

##### ModelsExpand Collapse

<details>

<summary>

ByDatasetListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {createdAt, indicatorType, sources, 8 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

<details>

<summary>

sources: array of object {resourceId, resourceType, system, title }

RSS article sources from which this indicator was extracted.

</summary>

resourceId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceId">Link to this property</a>

resourceType: "article"

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20resourceType">Link to this property</a>

system: "threat-signals"

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20system">Link to this property</a>

title: string

Threat Signals article title; null for historical provenance without a stored title.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20sources">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {page, pageSize, totalCount, totalPages }

</summary>

page: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

pageSize: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20pageSize">Link to this property</a>

totalCount: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalCount">Link to this property</a>

totalPages: number

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20totalPages">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_list_response%20%3E%20(schema)>)

<details>

<summary>

ByDatasetGetResponse object {createdAt, indicatorType, updatedAt, 7 more }

</summary>

createdAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20indicatorType">Link to this property</a>

updatedAt: string

formatdate-time

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

datasetId: optional string

The dataset ID this indicator belongs to. Included in list responses.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20datasetId">Link to this property</a>

<details>

<summary>

relatedEvents: optional array of object {datasetId, eventId, eventDate }

Related events, capped by <code>relatedEventsLimit</code> (default 2). Check <code>relatedEventsHasMore</code> to detect a capped list; pass <code>relatedEventsLimit=-1</code> to retrieve all of them.

</summary>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

eventId: string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventId">Link to this property</a>

eventDate: optional string

ISO 8601 date of the related event. Null for legacy relationships created before event-date tracking was added.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents%20%3E%20(items)%20%3E%20(property)%20eventDate">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEvents">Link to this property</a>

relatedEventsHasMore: optional boolean

True when this indicator appears in more events than <code>relatedEvents</code> contains because <code>relatedEventsLimit</code> capped the list. Pass <code>relatedEventsLimit=-1</code> to retrieve every related event.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20relatedEventsHasMore">Link to this property</a>

<details>

<summary>

tags: optional array of object {categoryId, categoryName, uuid, value }

</summary>

categoryId: optional string

The UUID of the tag category, or null when the tag is uncategorized.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

categoryName: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryName">Link to this property</a>

uuid: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: optional string

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

tlp: optional string

Traffic Light Protocol designation. UPPERCASE. Possible values: CLEAR, GREEN, AMBER, AMBER-STRICT, RED, PURPLE. Null when not set.

<a href="#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)%20%3E%20(property)%20tlp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.by_dataset%20%3E%20(model)%20by_dataset_get_response%20%3E%20(schema)>)

#### IndicatorsBy DatasetTags

##### [List mirrored tags for an indicator dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/subresources/tags/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/dataset/{dataset\_id}/indicators/tags

##### ModelsExpand Collapse

TagListResponse = array of unknown

Array of mirror tag rows

[Link to this property](<#(resource)%20cloudforce_one.threat_events.indicators.by_dataset.tags%20%3E%20(model)%20tag_list_response%20%3E%20(schema)>)