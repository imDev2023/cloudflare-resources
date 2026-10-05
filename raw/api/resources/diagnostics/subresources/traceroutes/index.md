---
title: Traceroutes
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Diagnostics](https://developers.cloudflare.com/api/resources/diagnostics)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Traceroutes

##### [Traceroute](https://developers.cloudflare.com/api/resources/diagnostics/subresources/traceroutes/methods/create)

POST/accounts/{account\_id}/diagnostics/traceroute

##### ModelsExpand Collapse

<details>

<summary>

Traceroute object {colos, target }

</summary>

<details>

<summary>

colos: optional array of object {colo, error, hops, 2 more }

</summary>

<details>

<summary>

colo: optional object {city, name }

</summary>

city: optional string

Source colo city.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20colo%20%3E%20(property)%20city">Link to this property</a>

name: optional string

Source colo name.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20colo%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20colo">Link to this property</a>

<details>

<summary>

error: optional ""or "Could not gather traceroute data: Code 1"or "Could not gather traceroute data: Code 2"or 2 more

Errors resulting from collecting traceroute from colo to target.

</summary>

One of the following:

""

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(member)%200">Link to this property</a>

"Could not gather traceroute data: Code 1"

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(member)%201">Link to this property</a>

"Could not gather traceroute data: Code 2"

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(member)%202">Link to this property</a>

"Could not gather traceroute data: Code 3"

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(member)%203">Link to this property</a>

"Could not gather traceroute data: Code 4"

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

hops: optional array of object {nodes, packets\_lost, packets\_sent, packets\_ttl }

</summary>

<details>

<summary>

nodes: optional array of object {asn, ip, labels, 6 more }

An array of node objects.

</summary>

asn: optional string

AS number associated with the node object.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

ip: optional string

IP address of the node.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20ip">Link to this property</a>

labels: optional array of string

Field appears if there is an additional annotation printed when the probe returns. Field also appears when running a GRE+ICMP traceroute to denote which traceroute a node comes from.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20labels">Link to this property</a>

max\_rtt\_ms: optional number

Maximum RTT in ms.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20max_rtt_ms">Link to this property</a>

mean\_rtt\_ms: optional number

Mean RTT in ms.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20mean_rtt_ms">Link to this property</a>

min\_rtt\_ms: optional number

Minimum RTT in ms.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20min_rtt_ms">Link to this property</a>

name: optional string

Host name of the address, this may be the same as the IP address.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

packet\_count: optional number

Number of packets with a response from this node.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20packet_count">Link to this property</a>

std\_dev\_rtt\_ms: optional number

Standard deviation of the RTTs in ms.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(property)%20std_dev_rtt_ms">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20nodes">Link to this property</a>

packets\_lost: optional number

Number of packets where no response was received.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_sent: optional number

Number of packets sent with specified TTL.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

packets\_ttl: optional number

The time to live (TTL).

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops%20%3E%20(items)%20%3E%20(property)%20packets_ttl">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20hops">Link to this property</a>

target\_summary: optional unknown

Aggregated statistics from all hops about the target.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20target_summary">Link to this property</a>

traceroute\_time\_ms: optional number

Total time of traceroute in ms.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos%20%3E%20(items)%20%3E%20(property)%20traceroute_time_ms">Link to this property</a>

</details>

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20colos">Link to this property</a>

target: optional string

The target hostname, IPv6, or IPv6 address.

<a href="#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

</details>

[Link to this property](<#(resource)%20diagnostics.traceroutes%20%3E%20(model)%20traceroute%20%3E%20(schema)>)