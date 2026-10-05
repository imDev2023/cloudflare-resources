---
title: Paths
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

[Routes](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Paths

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