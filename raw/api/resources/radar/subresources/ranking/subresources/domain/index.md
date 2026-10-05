---
title: Domain
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[Ranking](https://developers.cloudflare.com/api/resources/radar/subresources/ranking)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Domain

##### [Get domain rank details](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/domain/methods/get)

GET/radar/ranking/domain/{domain}

##### ModelsExpand Collapse

<details>

<summary>

DomainGetResponse object {details\_0, meta }

</summary>

<details>

<summary>

details\_0: object {categories, bucket, rank, top\_locations }

</summary>

<details>

<summary>

categories: array of object {id, name, superCategoryId }

</summary>

id: number

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: string

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

superCategoryId: number

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20superCategoryId">Link to this property</a>

</details>

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20categories">Link to this property</a>

bucket: optional string

Only available in POPULAR ranking for the most recent ranking.

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20bucket">Link to this property</a>

rank: optional number

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20rank">Link to this property</a>

<details>

<summary>

top\_locations: optional array of object {locationCode, locationName, rank }

</summary>

locationCode: string

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20top_locations%20%3E%20(items)%20%3E%20(property)%20locationCode">Link to this property</a>

locationName: string

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20top_locations%20%3E%20(items)%20%3E%20(property)%20locationName">Link to this property</a>

rank: number

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20top_locations%20%3E%20(items)%20%3E%20(property)%20rank">Link to this property</a>

</details>

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0%20%3E%20(property)%20top_locations">Link to this property</a>

</details>

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20details_0">Link to this property</a>

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

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

startTime: string

Adjusted start of date range.

formatdate-time

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dateRange">Link to this property</a>

</details>

<a href="#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.ranking.domain%20%3E%20(model)%20domain_get_response%20%3E%20(schema)>)