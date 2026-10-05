---
title: Top
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Top

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

#### TopAses

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