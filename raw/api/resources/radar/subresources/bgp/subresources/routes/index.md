---
title: Routes
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Routes

##### [Get Multi-Origin AS (MOAS) prefixes](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/moas)

GET/radar/bgp/routes/moas

##### [Get prefix-to-ASN mapping](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/pfx2as)

GET/radar/bgp/routes/pfx2as

##### [Get BGP routing table stats](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/stats)

GET/radar/bgp/routes/stats

##### [List ASes from global routing tables](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/ases)

GET/radar/bgp/routes/ases

##### [Get real-time BGP routes for a prefix](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/realtime)

GET/radar/bgp/routes/realtime

##### ModelsExpand Collapse

<details>

<summary>

RouteMoasResponse object {meta, moas }

</summary>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

moas: array of object {origins, prefix }

</summary>

<details>

<summary>

origins: array of object {origin, peer\_count, rpki\_validation }

</summary>

origin: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

peer\_count: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20peer_count">Link to this property</a>

rpki\_validation: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20rpki_validation">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20origins">Link to this property</a>

prefix: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)%20%3E%20(property)%20moas">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_moas_response%20%3E%20(schema)>)

<details>

<summary>

RoutePfx2asResponse object {meta, prefix\_origins }

</summary>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

prefix\_origins: array of object {origin, peer\_count, prefix, rpki\_validation }

</summary>

origin: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

peer\_count: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20peer_count">Link to this property</a>

prefix: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

rpki\_validation: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20rpki_validation">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)%20%3E%20(property)%20prefix_origins">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_pfx2as_response%20%3E%20(schema)>)

<details>

<summary>

RouteStatsResponse object {meta, stats }

</summary>

<details>

<summary>

meta: object {data\_time, query\_time, total\_peers }

</summary>

data\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

query\_time: string

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

total\_peers: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20total_peers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

stats: object {distinct\_origins, distinct\_origins\_ipv4, distinct\_origins\_ipv6, 15 more }

</summary>

distinct\_origins: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_origins">Link to this property</a>

distinct\_origins\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_origins_ipv4">Link to this property</a>

distinct\_origins\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_origins_ipv6">Link to this property</a>

distinct\_prefixes: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_prefixes">Link to this property</a>

distinct\_prefixes\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_prefixes_ipv4">Link to this property</a>

distinct\_prefixes\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20distinct_prefixes_ipv6">Link to this property</a>

routes\_invalid: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_invalid">Link to this property</a>

routes\_invalid\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_invalid_ipv4">Link to this property</a>

routes\_invalid\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_invalid_ipv6">Link to this property</a>

routes\_total: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_total">Link to this property</a>

routes\_total\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_total_ipv4">Link to this property</a>

routes\_total\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_total_ipv6">Link to this property</a>

routes\_unknown: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_unknown">Link to this property</a>

routes\_unknown\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_unknown_ipv4">Link to this property</a>

routes\_unknown\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_unknown_ipv6">Link to this property</a>

routes\_valid: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_valid">Link to this property</a>

routes\_valid\_ipv4: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_valid_ipv4">Link to this property</a>

routes\_valid\_ipv6: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20routes_valid_ipv6">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)%20%3E%20(property)%20stats">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_stats_response%20%3E%20(schema)>)

<details>

<summary>

RouteAsesResponse object {asns, meta }

</summary>

<details>

<summary>

asns: array of object {asn, coneSize, country, 7 more }

</summary>

asn: number

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

coneSize: number

AS’s customer cone size.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20coneSize">Link to this property</a>

country: string

Alpha-2 code for the AS’s registration country.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20country">Link to this property</a>

ipv4Count: number

Number of IPv4 addresses originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20ipv4Count">Link to this property</a>

ipv6Count: string

Number of IPv6 addresses originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20ipv6Count">Link to this property</a>

name: string

Name of the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

pfxsCount: number

Number of total IP prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20pfxsCount">Link to this property</a>

rpkiInvalid: number

Number of RPKI invalid prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20rpkiInvalid">Link to this property</a>

rpkiUnknown: number

Number of RPKI unknown prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20rpkiUnknown">Link to this property</a>

rpkiValid: number

Number of RPKI valid prefixes originated by the AS.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns%20%3E%20(items)%20%3E%20(property)%20rpkiValid">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

meta: object {dataTime, queryTime, totalPeers }

</summary>

dataTime: string

The timestamp of when the data is generated.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20dataTime">Link to this property</a>

queryTime: string

The timestamp of the query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20queryTime">Link to this property</a>

totalPeers: number

Total number of route collector peers used to generate this data.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20totalPeers">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_ases_response%20%3E%20(schema)>)

<details>

<summary>

RouteRealtimeResponse object {meta, routes }

</summary>

<details>

<summary>

meta: object {asn\_info, collectors, data\_time, 2 more }

</summary>

<details>

<summary>

asn\_info: array of object {as\_name, asn, country\_code, 2 more }

</summary>

as\_name: string

Name of the autonomous system.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20as_name">Link to this property</a>

asn: number

AS number.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country\_code: string

Alpha-2 code for the AS’s registration country.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20country_code">Link to this property</a>

org\_id: string

Organization ID.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_id">Link to this property</a>

org\_name: string

Organization name.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info%20%3E%20(items)%20%3E%20(property)%20org_name">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20asn_info">Link to this property</a>

<details>

<summary>

collectors: array of object {collector, latest\_realtime\_ts, latest\_rib\_ts, 4 more }

</summary>

collector: string

Public route collector ID.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20collector">Link to this property</a>

latest\_realtime\_ts: string

Latest real-time stream timestamp for this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20latest_realtime_ts">Link to this property</a>

latest\_rib\_ts: string

Latest RIB dump MRT file timestamp for this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20latest_rib_ts">Link to this property</a>

latest\_updates\_ts: string

Latest BGP updates MRT file timestamp for this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20latest_updates_ts">Link to this property</a>

peers\_count: number

Total number of collector peers used from this collector.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20peers_count">Link to this property</a>

peers\_v4\_count: number

Total number of collector peers used from this collector for IPv4 prefixes.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20peers_v4_count">Link to this property</a>

peers\_v6\_count: number

Total number of collector peers used from this collector for IPv6 prefixes.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors%20%3E%20(items)%20%3E%20(property)%20peers_v6_count">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20collectors">Link to this property</a>

data\_time: string

The most recent data timestamp for from the real-time sources.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20data_time">Link to this property</a>

<details>

<summary>

prefix\_origins: array of object {origin, prefix, rpki\_validation, 3 more }

</summary>

origin: number

Origin ASN.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

prefix: string

IP prefix of this query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

rpki\_validation: string

Prefix-origin RPKI validation: valid, invalid, unknown.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20rpki_validation">Link to this property</a>

total\_peers: number

Total number of peers.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20total_peers">Link to this property</a>

total\_visible: number

Total number of peers seeing this prefix.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20total_visible">Link to this property</a>

visibility: number

Ratio of peers seeing this prefix to total number of peers.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins%20%3E%20(items)%20%3E%20(property)%20visibility">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20prefix_origins">Link to this property</a>

query\_time: string

The timestamp of this query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20query_time">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

routes: array of object {as\_path, collector, communities, 2 more }

</summary>

as\_path: array of number

AS-level path for this route, from collector to origin.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20as_path">Link to this property</a>

collector: string

Public collector ID for this route.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20collector">Link to this property</a>

communities: array of string

BGP community values.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20communities">Link to this property</a>

prefix: string

IP prefix of this query.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

timestamp: string

Latest timestamp of change for this route.

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)%20%3E%20(property)%20routes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.bgp.routes%20%3E%20(model)%20route_realtime_response%20%3E%20(schema)>)

#### RoutesUpstreams

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

#### RoutesPaths

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