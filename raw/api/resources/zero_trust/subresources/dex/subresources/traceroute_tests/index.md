---
title: Traceroute Tests
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DEX](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Traceroute Tests

##### [Get details and aggregate metrics for a traceroute test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_tests/methods/get)

GET/accounts/{account\_id}/dex/traceroute-tests/{test\_id}

##### [Get percentiles for a traceroute test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_tests/methods/percentiles)

GET/accounts/{account\_id}/dex/traceroute-tests/{test\_id}/percentiles

##### [Get network path breakdown for a traceroute test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_tests/methods/network_path)

GET/accounts/{account\_id}/dex/traceroute-tests/{test\_id}/network-path

##### ModelsExpand Collapse

<details>

<summary>

Traceroute object {host, interval, kind, 5 more }

</summary>

host: string

The host of the Traceroute synthetic application test.

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

interval: string

The interval at which the Traceroute synthetic application test is set to run.

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

kind: "traceroute"

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

name: string

The name of the Traceroute synthetic application test.

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

target\_policies: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)">DigitalExperienceMonitor</a> { id, default, name }

</summary>

id: string

API Resource UUID tag.

maxLength36

<a href="#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

default: boolean

Whether the policy is the default for the account.

<a href="#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20target_policies">Link to this property</a>

targeted: optional boolean

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20targeted">Link to this property</a>

<details>

<summary>

tracerouteStats: optional object {availabilityPct, hopsCount, packetLossPct, 2 more }

</summary>

<details>

<summary>

availabilityPct: object {slots, avg, max, min }

</summary>

<details>

<summary>

slots: array of object {timestamp, value }

</summary>

timestamp: string

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

value: number

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20slots">Link to this property</a>

avg: optional number

average observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20avg">Link to this property</a>

max: optional number

highest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20max">Link to this property</a>

min: optional number

lowest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20availabilityPct">Link to this property</a>

hopsCount: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.http_tests.percentiles%20%3E%20(model)%20test_stat_over_time%20%3E%20(schema)">TestStatOverTime</a> { slots, avg, max, min }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20hopsCount">Link to this property</a>

<details>

<summary>

packetLossPct: object {slots, avg, max, min }

</summary>

<details>

<summary>

slots: array of object {timestamp, value }

</summary>

timestamp: string

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

value: number

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20slots">Link to this property</a>

avg: optional number

average observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20avg">Link to this property</a>

max: optional number

highest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20max">Link to this property</a>

min: optional number

lowest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20packetLossPct">Link to this property</a>

roundTripTimeMs: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.http_tests.percentiles%20%3E%20(model)%20test_stat_over_time%20%3E%20(schema)">TestStatOverTime</a> { slots, avg, max, min }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20roundTripTimeMs">Link to this property</a>

uniqueDevicesTotal: number

Count of unique devices that have run this test in the given time period.

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats%20%3E%20(property)%20uniqueDevicesTotal">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStats">Link to this property</a>

<details>

<summary>

tracerouteStatsByColo: optional array of object {availabilityPct, colo, hopsCount, 3 more }

</summary>

<details>

<summary>

availabilityPct: object {slots, avg, max, min }

</summary>

<details>

<summary>

slots: array of object {timestamp, value }

</summary>

timestamp: string

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

value: number

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20slots">Link to this property</a>

avg: optional number

average observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20avg">Link to this property</a>

max: optional number

highest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20max">Link to this property</a>

min: optional number

lowest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20availabilityPct">Link to this property</a>

colo: string

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20colo">Link to this property</a>

hopsCount: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.http_tests.percentiles%20%3E%20(model)%20test_stat_over_time%20%3E%20(schema)">TestStatOverTime</a> { slots, avg, max, min }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20hopsCount">Link to this property</a>

<details>

<summary>

packetLossPct: object {slots, avg, max, min }

</summary>

<details>

<summary>

slots: array of object {timestamp, value }

</summary>

timestamp: string

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

value: number

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20slots%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20slots">Link to this property</a>

avg: optional number

average observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20avg">Link to this property</a>

max: optional number

highest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20max">Link to this property</a>

min: optional number

lowest observed in the time period.

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct%20%3E%20(property)%20min">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20packetLossPct">Link to this property</a>

roundTripTimeMs: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.http_tests.percentiles%20%3E%20(model)%20test_stat_over_time%20%3E%20(schema)">TestStatOverTime</a> { slots, avg, max, min }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTimeMs">Link to this property</a>

uniqueDevicesTotal: number

Count of unique devices that have run this test in the given time period.

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo%20%3E%20(items)%20%3E%20(property)%20uniqueDevicesTotal">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20tracerouteStatsByColo">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute%20%3E%20(schema)>)

<details>

<summary>

TracerouteTestPercentilesResponse object {hopsCount, packetLossPct, roundTripTimeMs }

</summary>

hopsCount: optional <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex%20%3E%20(model)%20percentiles%20%3E%20(schema)">Percentiles</a> { p50, p90, p95, p99 }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute_test_percentiles_response%20%3E%20(schema)%20%3E%20(property)%20hopsCount">Link to this property</a>

packetLossPct: optional <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex%20%3E%20(model)%20percentiles%20%3E%20(schema)">Percentiles</a> { p50, p90, p95, p99 }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute_test_percentiles_response%20%3E%20(schema)%20%3E%20(property)%20packetLossPct">Link to this property</a>

roundTripTimeMs: optional <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex%20%3E%20(model)%20percentiles%20%3E%20(schema)">Percentiles</a> { p50, p90, p95, p99 }

<a href="#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute_test_percentiles_response%20%3E%20(schema)%20%3E%20(property)%20roundTripTimeMs">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dex.traceroute_tests%20%3E%20(model)%20traceroute_test_percentiles_response%20%3E%20(schema)>)