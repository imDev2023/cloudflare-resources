---
title: Upstreams
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

# Upstreams

##### [Get upstream composition time series for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries)

GET/radar/bgp/routes/upstreams/{asn}/timeseries

##### ModelsExpand Collapse

<details>

<summary>

UpstreamTimeseriesResponse object {meta, serie\_0 }

</summary>

<details>

<summary>

meta: object {dataTime, effectiveCollector, queryTime, stale }

</summary>

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

effectiveCollector: string

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20effectiveCollector">Link to this property</a>

queryTime: string

Timestamp when the query was executed.

formatdate-time

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

stale: boolean

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20stale">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

serie\_0: object {timestamps }

</summary>

timestamps: array of string

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0%20%3E%20(property)%20timestamps">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)%20%3E%20(property)%20serie_0">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes.upstreams%20%3E%20(model)%20upstream_timeseries_response%20%3E%20(schema)>)