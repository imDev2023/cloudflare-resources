---
title: Roas
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

[RPKI](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Roas

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