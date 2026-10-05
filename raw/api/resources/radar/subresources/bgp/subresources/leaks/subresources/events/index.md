---
title: Events
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

[Leaks](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Events

##### [Get BGP route leak events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list)

GET/radar/bgp/leaks/events

##### ModelsExpand Collapse

<details>

<summary>

EventListResponse object {asn\_info, events }

</summary>

<details>

<summary>

asn\_info: array of object {asn, country\_code, org\_name }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country\_code: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20country_code">Link to this property</a>

org\_name: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info">Link to this property</a>

<details>

<summary>

events: array of object {id, countries, detected\_ts, 10 more }

</summary>

id: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

countries: array of string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

detected\_ts: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20detected_ts">Link to this property</a>

finished: boolean

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20finished">Link to this property</a>

leak\_asn: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_asn">Link to this property</a>

leak\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_count">Link to this property</a>

leak\_seg: array of number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_seg">Link to this property</a>

leak\_type: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20leak_type">Link to this property</a>

max\_ts: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20max_ts">Link to this property</a>

min\_ts: string

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20min_ts">Link to this property</a>

origin\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20origin_count">Link to this property</a>

peer\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20peer_count">Link to this property</a>

prefix\_count: number

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20prefix_count">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.leaks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)>)