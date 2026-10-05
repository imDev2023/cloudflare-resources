---
title: Aggregates
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Spectrum](https://developers.cloudflare.com/api/resources/spectrum)

[Analytics](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Aggregates

#### AggregatesCurrents

##### [Get current aggregated analytics](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/aggregates/subresources/currents/methods/get)

GET/zones/{zone\_id}/spectrum/analytics/aggregate/current

##### ModelsExpand Collapse

<details>

<summary>

CurrentGetResponse = array of object {appID, bytesEgress, bytesIngress, 2 more }

</summary>

appID: string

Application identifier.

maxLength32

<a href="#(resource)%20spectrum.analytics.aggregates.currents%20%3E%20(model)%20current_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20appID">Link to this property</a>

bytesEgress: number

Number of bytes sent.

<a href="#(resource)%20spectrum.analytics.aggregates.currents%20%3E%20(model)%20current_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20bytesEgress">Link to this property</a>

bytesIngress: number

Number of bytes received.

<a href="#(resource)%20spectrum.analytics.aggregates.currents%20%3E%20(model)%20current_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20bytesIngress">Link to this property</a>

connections: number

Number of connections.

<a href="#(resource)%20spectrum.analytics.aggregates.currents%20%3E%20(model)%20current_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20connections">Link to this property</a>

durationAvg: number

Average duration of connections.

<a href="#(resource)%20spectrum.analytics.aggregates.currents%20%3E%20(model)%20current_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20durationAvg">Link to this property</a>

</details>

[Link to this property](<#(resource)%20spectrum.analytics.aggregates.currents%20%3E%20(model)%20current_get_response%20%3E%20(schema)>)