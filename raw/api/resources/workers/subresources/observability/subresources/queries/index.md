---
title: Queries
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workers](https://developers.cloudflare.com/api/resources/workers)

[Observability](https://developers.cloudflare.com/api/resources/workers/subresources/observability)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Queries

##### [Save query](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/queries/methods/create)

POST/accounts/{account\_id}/workers/observability/queries

##### [List queries](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/queries/methods/list)

GET/accounts/{account\_id}/workers/observability/queries

##### ModelsExpand Collapse

<details>

<summary>

QueryCreateResponse object {id, adhoc, created, 6 more }

</summary>

id: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

adhoc: boolean

If the query wasn’t explcitly saved

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20adhoc">Link to this property</a>

created: string

formatdate-time

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

createdBy: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20createdBy">Link to this property</a>

description: string

maxLength1000

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

name: string

Query name

maxLength250

minLength1

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

parameters: object {calculations, datasets, filterCombination, 6 more }

</summary>

<details>

<summary>

calculations: optional array of object {operator, alias, key, keyType } or object {key, operator, alias, keyType }

Create Calculations to compute as part of the query.

</summary>

One of the following:

<details>

<summary>

object {operator, alias, key, keyType }

</summary>

<details>

<summary>

operator: "count"or "COUNT"

</summary>

One of the following:

"count"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"COUNT"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operator">Link to this property</a>

alias: optional string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alias">Link to this property</a>

key: optional string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

keyType: optional "string"or "number"or "boolean"

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {key, operator, alias, keyType }

</summary>

key: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operator: "uniq"or "max"or "min"or 33 more

</summary>

One of the following:

"uniq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"max"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"min"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"sum"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"avg"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

"median"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%205">Link to this property</a>

"p001"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%206">Link to this property</a>

"p01"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%207">Link to this property</a>

"p05"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%208">Link to this property</a>

"p10"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%209">Link to this property</a>

"p25"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2010">Link to this property</a>

"p75"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2011">Link to this property</a>

"p90"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2012">Link to this property</a>

"p95"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2013">Link to this property</a>

"p99"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2014">Link to this property</a>

"p999"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2015">Link to this property</a>

"stddev"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2016">Link to this property</a>

"variance"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2017">Link to this property</a>

"COUNT\_DISTINCT"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2018">Link to this property</a>

"MAX"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2019">Link to this property</a>

"MIN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2020">Link to this property</a>

"SUM"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2021">Link to this property</a>

"AVG"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2022">Link to this property</a>

"MEDIAN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2023">Link to this property</a>

"P001"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2024">Link to this property</a>

"P01"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2025">Link to this property</a>

"P05"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2026">Link to this property</a>

"P10"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2027">Link to this property</a>

"P25"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2028">Link to this property</a>

"P75"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2029">Link to this property</a>

"P90"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2030">Link to this property</a>

"P95"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2031">Link to this property</a>

"P99"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2032">Link to this property</a>

"P999"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2033">Link to this property</a>

"STDDEV"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2034">Link to this property</a>

"VARIANCE"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2035">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator">Link to this property</a>

alias: optional string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20alias">Link to this property</a>

<details>

<summary>

keyType: optional "string"or "number"or "boolean"

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations">Link to this property</a>

datasets: optional array of string

Set the Datasets to query. Leave it empty to query all the datasets.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20datasets">Link to this property</a>

<details>

<summary>

filterCombination: optional "and"or "or"or "AND"or "OR"

Set a Flag to describe how to combine the filters on the query.

</summary>

One of the following:

"and"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%200">Link to this property</a>

"or"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%201">Link to this property</a>

"AND"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%202">Link to this property</a>

"OR"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination">Link to this property</a>

<details>

<summary>

filters: optional array of object {filterCombination, filters, kind } or object {key, operation, type, 2 more }

Configure the Filters to apply to the query. Supports nested groups via kind: ‘group’.

</summary>

One of the following:

<details>

<summary>

object {filterCombination, filters, kind }

</summary>

<details>

<summary>

filterCombination: "and"or "or"or "AND"or "OR"

</summary>

One of the following:

"and"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%200">Link to this property</a>

"or"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%201">Link to this property</a>

"AND"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%202">Link to this property</a>

"OR"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination">Link to this property</a>

filters: array of unknown

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filters">Link to this property</a>

kind: "group"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kind">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersObservabilityFilterLeaf object {key, operation, type, 2 more }

A filter condition applied to query results. Use the keys and values endpoints to discover available fields and their values before constructing filters.

</summary>

key: string

Filter field name. Use verified keys from previous query results or the keys endpoint. Common keys include $metadata.service, $metadata.origin, $metadata.trigger, $metadata.message, and $metadata.error.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operation: "includes"or "not\_includes"or "starts\_with"or 27 more

Comparison operator. String operators: includes, not\_includes, starts\_with, ends\_with, regex. Existence: exists, is\_null. Set membership: in, not\_in (comma-separated values). Numeric: eq, neq, gt, gte, lt, lte.

</summary>

One of the following:

"includes"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"not\_includes"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"starts\_with"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"ends\_with"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"regex"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"exists"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

"is\_null"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%206">Link to this property</a>

"in"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%207">Link to this property</a>

"not\_in"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%208">Link to this property</a>

"eq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%209">Link to this property</a>

"neq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2010">Link to this property</a>

"gt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2011">Link to this property</a>

"gte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2012">Link to this property</a>

"lt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2013">Link to this property</a>

"lte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2014">Link to this property</a>

"="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2015">Link to this property</a>

"!="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2016">Link to this property</a>

"&gt;"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2017">Link to this property</a>

"&gt;="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2018">Link to this property</a>

"&lt;"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2019">Link to this property</a>

"&lt;="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2020">Link to this property</a>

"INCLUDES"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2021">Link to this property</a>

"DOES\_NOT\_INCLUDE"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2022">Link to this property</a>

"MATCH\_REGEX"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2023">Link to this property</a>

"EXISTS"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2024">Link to this property</a>

"DOES\_NOT\_EXIST"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2025">Link to this property</a>

"IN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2026">Link to this property</a>

"NOT\_IN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2027">Link to this property</a>

"STARTS\_WITH"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2028">Link to this property</a>

"ENDS\_WITH"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2029">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

<details>

<summary>

type: "string"or "number"or "boolean"

Data type of the filter field. Must match the actual type of the key being filtered.

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

kind: optional "filter"

Discriminator for leaf filter nodes. Always ‘filter’ when present; may be omitted.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

value: optional stringor numberor boolean

Comparison value. Must match actual values in your data — verify with the values endpoint. Ensure the value type (string/number/boolean) matches the field type. String comparisons are case-sensitive. Regex uses RE2 syntax (no lookaheads/lookbehinds).

</summary>

One of the following:

string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters">Link to this property</a>

<details>

<summary>

groupBys: optional array of object {type, value }

Define how to group the results of the query.

</summary>

<details>

<summary>

type: "string"or "number"or "boolean"

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

value: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys">Link to this property</a>

<details>

<summary>

havings: optional array of object {key, operation, value }

Configure the Having clauses that filter on calculations in the query result.

</summary>

key: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operation: "eq"or "neq"or "gt"or 3 more

</summary>

One of the following:

"eq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"neq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"gt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"gte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"lt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"lte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation">Link to this property</a>

value: number

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings">Link to this property</a>

limit: optional number

Set a limit on the number of results / records returned by the query

maximum100

minimum0

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

needle: optional object {value, isRegex, matchCase }

Define an expression to search using full-text search.

</summary>

<details>

<summary>

value: stringor numberor boolean

maxLength1000

</summary>

One of the following:

string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value">Link to this property</a>

isRegex: optional boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20isRegex">Link to this property</a>

matchCase: optional boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20matchCase">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle">Link to this property</a>

<details>

<summary>

orderBy: optional object {value, order }

Configure the order of the results returned by the query.

</summary>

value: string

Configure which Calculation to order the results by.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

order: optional "asc"or "desc"

Set the order of the results

</summary>

One of the following:

"asc"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20order%20%3E%20(member)%200">Link to this property</a>

"desc"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20order%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20order">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20parameters">Link to this property</a>

updated: string

formatdate-time

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

updatedBy: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20updatedBy">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.observability.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)>)

<details>

<summary>

QueryListResponse object {id, adhoc, created, 6 more }

</summary>

id: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

adhoc: boolean

If the query wasn’t explcitly saved

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20adhoc">Link to this property</a>

created: string

formatdate-time

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

createdBy: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20createdBy">Link to this property</a>

description: string

maxLength1000

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

name: string

Query name

maxLength250

minLength1

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

parameters: object {calculations, datasets, filterCombination, 6 more }

</summary>

<details>

<summary>

calculations: optional array of object {operator, alias, key, keyType } or object {key, operator, alias, keyType }

Create Calculations to compute as part of the query.

</summary>

One of the following:

<details>

<summary>

object {operator, alias, key, keyType }

</summary>

<details>

<summary>

operator: "count"or "COUNT"

</summary>

One of the following:

"count"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"COUNT"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operator">Link to this property</a>

alias: optional string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20alias">Link to this property</a>

key: optional string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

keyType: optional "string"or "number"or "boolean"

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20keyType">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {key, operator, alias, keyType }

</summary>

key: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operator: "uniq"or "max"or "min"or 33 more

</summary>

One of the following:

"uniq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"max"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"min"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"sum"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"avg"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

"median"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%205">Link to this property</a>

"p001"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%206">Link to this property</a>

"p01"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%207">Link to this property</a>

"p05"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%208">Link to this property</a>

"p10"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%209">Link to this property</a>

"p25"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2010">Link to this property</a>

"p75"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2011">Link to this property</a>

"p90"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2012">Link to this property</a>

"p95"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2013">Link to this property</a>

"p99"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2014">Link to this property</a>

"p999"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2015">Link to this property</a>

"stddev"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2016">Link to this property</a>

"variance"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2017">Link to this property</a>

"COUNT\_DISTINCT"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2018">Link to this property</a>

"MAX"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2019">Link to this property</a>

"MIN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2020">Link to this property</a>

"SUM"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2021">Link to this property</a>

"AVG"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2022">Link to this property</a>

"MEDIAN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2023">Link to this property</a>

"P001"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2024">Link to this property</a>

"P01"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2025">Link to this property</a>

"P05"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2026">Link to this property</a>

"P10"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2027">Link to this property</a>

"P25"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2028">Link to this property</a>

"P75"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2029">Link to this property</a>

"P90"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2030">Link to this property</a>

"P95"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2031">Link to this property</a>

"P99"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2032">Link to this property</a>

"P999"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2033">Link to this property</a>

"STDDEV"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2034">Link to this property</a>

"VARIANCE"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator%20%3E%20(member)%2035">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operator">Link to this property</a>

alias: optional string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20alias">Link to this property</a>

<details>

<summary>

keyType: optional "string"or "number"or "boolean"

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20keyType">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20calculations">Link to this property</a>

datasets: optional array of string

Set the Datasets to query. Leave it empty to query all the datasets.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20datasets">Link to this property</a>

<details>

<summary>

filterCombination: optional "and"or "or"or "AND"or "OR"

Set a Flag to describe how to combine the filters on the query.

</summary>

One of the following:

"and"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%200">Link to this property</a>

"or"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%201">Link to this property</a>

"AND"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%202">Link to this property</a>

"OR"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filterCombination">Link to this property</a>

<details>

<summary>

filters: optional array of object {filterCombination, filters, kind } or object {key, operation, type, 2 more }

Configure the Filters to apply to the query. Supports nested groups via kind: ‘group’.

</summary>

One of the following:

<details>

<summary>

object {filterCombination, filters, kind }

</summary>

<details>

<summary>

filterCombination: "and"or "or"or "AND"or "OR"

</summary>

One of the following:

"and"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%200">Link to this property</a>

"or"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%201">Link to this property</a>

"AND"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%202">Link to this property</a>

"OR"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filterCombination">Link to this property</a>

filters: array of unknown

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20filters">Link to this property</a>

kind: "group"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20kind">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersObservabilityFilterLeaf object {key, operation, type, 2 more }

A filter condition applied to query results. Use the keys and values endpoints to discover available fields and their values before constructing filters.

</summary>

key: string

Filter field name. Use verified keys from previous query results or the keys endpoint. Common keys include $metadata.service, $metadata.origin, $metadata.trigger, $metadata.message, and $metadata.error.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operation: "includes"or "not\_includes"or "starts\_with"or 27 more

Comparison operator. String operators: includes, not\_includes, starts\_with, ends\_with, regex. Existence: exists, is\_null. Set membership: in, not\_in (comma-separated values). Numeric: eq, neq, gt, gte, lt, lte.

</summary>

One of the following:

"includes"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"not\_includes"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"starts\_with"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"ends\_with"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"regex"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"exists"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

"is\_null"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%206">Link to this property</a>

"in"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%207">Link to this property</a>

"not\_in"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%208">Link to this property</a>

"eq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%209">Link to this property</a>

"neq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2010">Link to this property</a>

"gt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2011">Link to this property</a>

"gte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2012">Link to this property</a>

"lt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2013">Link to this property</a>

"lte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2014">Link to this property</a>

"="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2015">Link to this property</a>

"!="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2016">Link to this property</a>

"&gt;"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2017">Link to this property</a>

"&gt;="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2018">Link to this property</a>

"&lt;"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2019">Link to this property</a>

"&lt;="

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2020">Link to this property</a>

"INCLUDES"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2021">Link to this property</a>

"DOES\_NOT\_INCLUDE"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2022">Link to this property</a>

"MATCH\_REGEX"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2023">Link to this property</a>

"EXISTS"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2024">Link to this property</a>

"DOES\_NOT\_EXIST"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2025">Link to this property</a>

"IN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2026">Link to this property</a>

"NOT\_IN"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2027">Link to this property</a>

"STARTS\_WITH"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2028">Link to this property</a>

"ENDS\_WITH"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%2029">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

<details>

<summary>

type: "string"or "number"or "boolean"

Data type of the filter field. Must match the actual type of the key being filtered.

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

kind: optional "filter"

Discriminator for leaf filter nodes. Always ‘filter’ when present; may be omitted.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20kind">Link to this property</a>

<details>

<summary>

value: optional stringor numberor boolean

Comparison value. Must match actual values in your data — verify with the values endpoint. Ensure the value type (string/number/boolean) matches the field type. String comparisons are case-sensitive. Regex uses RE2 syntax (no lookaheads/lookbehinds).

</summary>

One of the following:

string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20filters">Link to this property</a>

<details>

<summary>

groupBys: optional array of object {type, value }

Define how to group the results of the query.

</summary>

<details>

<summary>

type: "string"or "number"or "boolean"

</summary>

One of the following:

"string"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"number"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"boolean"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

value: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20groupBys">Link to this property</a>

<details>

<summary>

havings: optional array of object {key, operation, value }

Configure the Having clauses that filter on calculations in the query result.

</summary>

key: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20key">Link to this property</a>

<details>

<summary>

operation: "eq"or "neq"or "gt"or 3 more

</summary>

One of the following:

"eq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"neq"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"gt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

"gte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%203">Link to this property</a>

"lt"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%204">Link to this property</a>

"lte"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20operation">Link to this property</a>

value: number

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20havings">Link to this property</a>

limit: optional number

Set a limit on the number of results / records returned by the query

maximum100

minimum0

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

needle: optional object {value, isRegex, matchCase }

Define an expression to search using full-text search.

</summary>

<details>

<summary>

value: stringor numberor boolean

maxLength1000

</summary>

One of the following:

string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20value">Link to this property</a>

isRegex: optional boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20isRegex">Link to this property</a>

matchCase: optional boolean

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle%20%3E%20(property)%20matchCase">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20needle">Link to this property</a>

<details>

<summary>

orderBy: optional object {value, order }

Configure the order of the results returned by the query.

</summary>

value: string

Configure which Calculation to order the results by.

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20value">Link to this property</a>

<details>

<summary>

order: optional "asc"or "desc"

Set the order of the results

</summary>

One of the following:

"asc"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20order%20%3E%20(member)%200">Link to this property</a>

"desc"

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20order%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy%20%3E%20(property)%20order">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20orderBy">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters">Link to this property</a>

updated: string

formatdate-time

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

updatedBy: string

<a href="#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(property)%20updatedBy">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.observability.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)>)