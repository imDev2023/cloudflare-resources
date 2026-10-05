---
title: Network Path
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DEX](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex)

[Traceroute Test Results](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_test_results)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Network Path

##### [Get details for a specific traceroute test run](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_test_results/subresources/network_path/methods/get)

GET/accounts/{account\_id}/dex/traceroute-test-results/{test\_result\_id}/network-path

##### ModelsExpand Collapse

<details>

<summary>

NetworkPathGetResponse object {hops, resultId, colo, 6 more }

</summary>

<details>

<summary>

hops: array of object {ttl, asn, aso, 6 more }

An array of the hops taken by the device to reach the end destination.

</summary>

ttl: number

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20aso">Link to this property</a>

ipAddress: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20ipAddress">Link to this property</a>

<details>

<summary>

location: optional object {city, state, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

state: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20state">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20location">Link to this property</a>

<details>

<summary>

mile: optional "client-to-app"or "client-to-cf-egress"or "client-to-cf-ingress"or "client-to-isp"

</summary>

One of the following:

"client-to-app"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20mile%20%3E%20(member)%200">Link to this property</a>

"client-to-cf-egress"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20mile%20%3E%20(member)%201">Link to this property</a>

"client-to-cf-ingress"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20mile%20%3E%20(member)%202">Link to this property</a>

"client-to-isp"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20mile%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20mile">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

packetLossPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20packetLossPct">Link to this property</a>

rttMs: optional number

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20rttMs">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20hops">Link to this property</a>

resultId: string

API Resource UUID tag.

maxLength36

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20resultId">Link to this property</a>

colo: optional string

Cloudflare colo airport code.

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20colo">Link to this property</a>

deviceName: optional string

Name of the device associated with this network path response.

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceName">Link to this property</a>

<details>

<summary>

execution\_context: optional "EXECUTION\_CONTEXT\_INVALID"or "OUT\_OF\_TUNNEL"or "IN\_TUNNEL"

Whether the test was run inside or outside of the WARP tunnel.

</summary>

One of the following:

"EXECUTION\_CONTEXT\_INVALID"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20execution_context%20%3E%20(member)%200">Link to this property</a>

"OUT\_OF\_TUNNEL"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20execution_context%20%3E%20(member)%201">Link to this property</a>

"IN\_TUNNEL"

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20execution_context%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20execution_context">Link to this property</a>

testId: optional string

API Resource UUID tag.

maxLength36

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20testId">Link to this property</a>

testName: optional string

Name of the traceroute test.

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20testName">Link to this property</a>

time\_start: optional string

Timestamp indicating when the traceroute test execution began.

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20time_start">Link to this property</a>

tunnel\_type: optional string

<a href="#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnel_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dex.traceroute_test_results.network_path%20%3E%20(model)%20network_path_get_response%20%3E%20(schema)>)