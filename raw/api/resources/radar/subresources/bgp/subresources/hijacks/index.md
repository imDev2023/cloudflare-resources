---
title: Hijacks
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Hijacks

#### HijacksEvents

##### [Get BGP hijack events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list)

GET/radar/bgp/hijacks/events

##### ModelsExpand Collapse

<details>

<summary>

EventListResponse object {asn\_info, events, total\_monitors }

</summary>

<details>

<summary>

asn\_info: array of object {asn, country\_code, org\_name }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country\_code: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20country_code">Link to this property</a>

org\_name: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20asn_info">Link to this property</a>

<details>

<summary>

events: array of object {id, confidence\_score, duration, 15 more }

</summary>

id: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

confidence\_score: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20confidence_score">Link to this property</a>

duration: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20duration">Link to this property</a>

event\_type: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20event_type">Link to this property</a>

hijack\_msgs\_count: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20hijack_msgs_count">Link to this property</a>

hijacker\_asn: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20hijacker_asn">Link to this property</a>

hijacker\_country: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20hijacker_country">Link to this property</a>

is\_stale: boolean

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20is_stale">Link to this property</a>

max\_hijack\_ts: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20max_hijack_ts">Link to this property</a>

max\_msg\_ts: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20max_msg_ts">Link to this property</a>

min\_hijack\_ts: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20min_hijack_ts">Link to this property</a>

on\_going\_count: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20on_going_count">Link to this property</a>

peer\_asns: array of number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20peer_asns">Link to this property</a>

peer\_ip\_count: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20peer_ip_count">Link to this property</a>

prefixes: array of string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20prefixes">Link to this property</a>

<details>

<summary>

tags: array of object {name, score }

</summary>

name: string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

score: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

victim\_asns: array of number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20victim_asns">Link to this property</a>

victim\_countries: array of string

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20victim_countries">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

total\_monitors: number

<a href="#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20total_monitors">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.hijacks.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)>)