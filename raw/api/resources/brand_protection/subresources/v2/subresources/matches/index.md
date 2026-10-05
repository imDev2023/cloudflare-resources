---
title: Matches
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Brand Protection](https://developers.cloudflare.com/api/resources/brand_protection)

[V2](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Matches

##### [List saved query matches](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/matches/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/brand-protection/domain/matches

##### ModelsExpand Collapse

<details>

<summary>

MatchGetResponse object {matches, total }

</summary>

<details>

<summary>

matches: array of object {domain, first\_seen, public\_scans, 6 more }

</summary>

domain: string

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

first\_seen: string

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20first_seen">Link to this property</a>

<details>

<summary>

public\_scans: object {submission\_id }

</summary>

submission\_id: string

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20public_scans%20%3E%20(property)%20submission_id">Link to this property</a>

</details>

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20public_scans">Link to this property</a>

registrar: string

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20registrar">Link to this property</a>

scan\_status: string

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20scan_status">Link to this property</a>

scan\_submission\_id: number

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20scan_submission_id">Link to this property</a>

source: string

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

dismissed: optional boolean

Whether the match is dismissed. Only present for single-query requests. For multi-query requests, use the dismissed field in each match\_details entry.

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20dismissed">Link to this property</a>

<details>

<summary>

match\_details: optional array of object {dismissed, match\_id, query\_id, query\_tag }

Per-match detail objects with query metadata and individual dismissed state. Only present when multiple query\_ids are requested.

</summary>

dismissed: boolean

Individual dismissed state for this specific match.

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20match_details%20%3E%20(items)%20%3E%20(property)%20dismissed">Link to this property</a>

match\_id: number

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20match_details%20%3E%20(items)%20%3E%20(property)%20match_id">Link to this property</a>

query\_id: number

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20match_details%20%3E%20(items)%20%3E%20(property)%20query_id">Link to this property</a>

query\_tag: string

Tag associated with the query, if one exists.

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20match_details%20%3E%20(items)%20%3E%20(property)%20query_tag">Link to this property</a>

</details>

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches%20%3E%20(items)%20%3E%20(property)%20match_details">Link to this property</a>

</details>

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20matches">Link to this property</a>

total: number

minimum0

<a href="#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)%20%3E%20(property)%20total">Link to this property</a>

</details>

[Link to this property](<#(resource)%20brand_protection.v2.matches%20%3E%20(model)%20match_get_response%20%3E%20(schema)>)