---
title: Cf Interconnects
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Transit](https://developers.cloudflare.com/api/resources/magic_transit)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Cf Interconnects

##### [List interconnects](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/list)

GET/accounts/{account\_id}/magic/cf\_interconnects

##### [List interconnect Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/get)

GET/accounts/{account\_id}/magic/cf\_interconnects/{cf\_interconnect\_id}

##### [Update interconnect](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/update)

PUT/accounts/{account\_id}/magic/cf\_interconnects/{cf\_interconnect\_id}

##### [Update multiple interconnects](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/bulk_update)

PUT/accounts/{account\_id}/magic/cf\_interconnects

##### ModelsExpand Collapse

<details>

<summary>

CfInterconnectListResponse object {interconnects }

</summary>

<details>

<summary>

interconnects: optional array of object {id, automatic\_return\_routing, bgp, 12 more }

</summary>

id: optional string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

automatic\_return\_routing: optional boolean

True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the <code>coupler_integration</code> account flag to be enabled; requests setting this to <code>true</code> without that flag will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20automatic_return_routing">Link to this property</a>

<details>

<summary>

bgp: optional object {as\_no, cloudflare\_endpoint, customer\_asn, 5 more }

</summary>

Deprecatedas\_no: optional number

Deprecated. Use customer\_asn.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20as_no">Link to this property</a>

Deprecatedcloudflare\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

customer\_asn: optional number

ASN used on the customer end of the BGP session.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_asn">Link to this property</a>

Deprecatedcustomer\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_endpoint">Link to this property</a>

export\_filter\_id: optional string

ID of the BGP filter profile applied to routes advertised to the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20export_filter_id">Link to this property</a>

extra\_prefixes: optional array of string

Prefixes in this list will be advertised to the customer device, in addition to the routes in the Magic routing table.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20extra_prefixes">Link to this property</a>

import\_filter\_id: optional string

ID of the BGP filter profile applied to routes received from the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20import_filter_id">Link to this property</a>

md5\_key: optional string

MD5 key to use for session authentication.

Note that *this is not a security measure*. MD5 is not a valid security mechanism, and the key is not treated as a secret value. This is *only* supported for preventing misconfiguration, not for defending against malicious attacks.

The MD5 key, if set, must be of non-zero length and consist only of the following types of character:

- ASCII alphanumerics: <code>[a-zA-Z0-9]</code>
- Special characters in the set <code>'!@#$%^&amp;*()+[]{}&lt;&gt;/.,;:_-~</code>= |\`

In other words, MD5 keys may contain any printable ASCII character aside from newline (0x0A), quotation mark (<code>"</code>), vertical tab (0x0B), carriage return (0x0D), tab (0x09), form feed (0x0C), and the question mark (<code>?</code>). Requests specifying an MD5 key with one or more of these disallowed characters will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20md5_key">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20bgp">Link to this property</a>

colo\_name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20colo_name">Link to this property</a>

created\_on: optional string

The date and time the tunnel was created.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional description of the interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

gre: optional object {cloudflare\_endpoint }

Omitted in responses for version 1.5 interconnects.

</summary>

cloudflare\_endpoint: optional string

The IP address assigned to the Cloudflare side of the GRE tunnel created as part of the Interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20gre%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20gre">Link to this property</a>

<details>

<summary>

health\_check: optional object {direction, enabled, rate, 3 more }

</summary>

<details>

<summary>

direction: optional "unidirectional"or "bidirectional"

The direction of the flow of the healthcheck. Either unidirectional, where the probe comes to you via the interconnect and the result comes back to Cloudflare via the open Internet, or bidirectional where both the probe and result come and go via the interconnect.

</summary>

One of the following:

"unidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%200">Link to this property</a>

"bidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20direction">Link to this property</a>

enabled: optional boolean

Determines whether to run healthchecks for a tunnel.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20enabled">Link to this property</a>

rate: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_rate%20%3E%20(schema)">HealthCheckRate</a>

How frequent the health check is run. The default value is <code>mid</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20rate">Link to this property</a>

source: optional string

The source IPv4 address used for bidirectional health checks. Supported only for version 1.5 interconnects. It is required when <code>direction</code> is <code>bidirectional</code> and must be omitted (and is cleared) when <code>direction</code> is <code>unidirectional</code>. The address must be within RFC1918 space, the approved link-local range 169.254.240.0/20, or the Cloudflare reserved range 198.41.199.224/27.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

target: optional object {effective, saved } or string

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target. Must be in object form if the x-magic-new-hc-target header is set to true and string form if x-magic-new-hc-target is absent or set to false.

</summary>

One of the following:

<details>

<summary>

MagicHealthCheckTarget object {effective, saved }

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target.

</summary>

effective: optional string

The effective health check target. If ‘saved’ is empty, then this field will be populated with the calculated default value on GET requests. Ignored in POST, PUT, and PATCH requests.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20effective">Link to this property</a>

saved: optional string

The saved health check target. Setting the value to the empty string indicates that the calculated default value will be used.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20saved">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target">Link to this property</a>

type: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_type%20%3E%20(schema)">HealthCheckType</a>

The type of healthcheck to run, reply or request. The default value is <code>reply</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20health_check">Link to this property</a>

interface\_address: optional string

The IPv4 interface address for the interconnect. For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /30 or /31 prefix may be used. Version 1.5 interconnects require a /31 prefix and may also use a prefix from the account’s authorized prefixes; otherwise, select the subnet from RFC 1918 or the approved link-local ranges.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20interface_address">Link to this property</a>

interface\_address6: optional string

A 127 bit IPV6 prefix from within the virtual\_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual\_subnet6. Eg if virtual\_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface\_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20interface_address6">Link to this property</a>

modified\_on: optional string

The date and time the tunnel was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

mtu: optional number

The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum value is 576.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20mtu">Link to this property</a>

name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

version: optional string

Immutable interconnect version configured at creation time. One of:

- “1”
- “1.5”
- “2”

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20version">Link to this property</a>

virtual\_port\_reservation\_id: optional string

An identifier that correlates this interconnect with the corresponding V2 CNI interconnect resource.

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects%20%3E%20(items)%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)%20%3E%20(property)%20interconnects">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_list_response%20%3E%20(schema)>)

<details>

<summary>

CfInterconnectGetResponse object {interconnect }

</summary>

<details>

<summary>

interconnect: optional object {id, automatic\_return\_routing, bgp, 12 more }

</summary>

id: optional string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20id">Link to this property</a>

automatic\_return\_routing: optional boolean

True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the <code>coupler_integration</code> account flag to be enabled; requests setting this to <code>true</code> without that flag will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20automatic_return_routing">Link to this property</a>

<details>

<summary>

bgp: optional object {as\_no, cloudflare\_endpoint, customer\_asn, 5 more }

</summary>

Deprecatedas\_no: optional number

Deprecated. Use customer\_asn.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20as_no">Link to this property</a>

Deprecatedcloudflare\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

customer\_asn: optional number

ASN used on the customer end of the BGP session.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_asn">Link to this property</a>

Deprecatedcustomer\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_endpoint">Link to this property</a>

export\_filter\_id: optional string

ID of the BGP filter profile applied to routes advertised to the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20export_filter_id">Link to this property</a>

extra\_prefixes: optional array of string

Prefixes in this list will be advertised to the customer device, in addition to the routes in the Magic routing table.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20extra_prefixes">Link to this property</a>

import\_filter\_id: optional string

ID of the BGP filter profile applied to routes received from the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20import_filter_id">Link to this property</a>

md5\_key: optional string

MD5 key to use for session authentication.

Note that *this is not a security measure*. MD5 is not a valid security mechanism, and the key is not treated as a secret value. This is *only* supported for preventing misconfiguration, not for defending against malicious attacks.

The MD5 key, if set, must be of non-zero length and consist only of the following types of character:

- ASCII alphanumerics: <code>[a-zA-Z0-9]</code>
- Special characters in the set <code>'!@#$%^&amp;*()+[]{}&lt;&gt;/.,;:_-~</code>= |\`

In other words, MD5 keys may contain any printable ASCII character aside from newline (0x0A), quotation mark (<code>"</code>), vertical tab (0x0B), carriage return (0x0D), tab (0x09), form feed (0x0C), and the question mark (<code>?</code>). Requests specifying an MD5 key with one or more of these disallowed characters will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20md5_key">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20bgp">Link to this property</a>

colo\_name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20colo_name">Link to this property</a>

created\_on: optional string

The date and time the tunnel was created.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional description of the interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

gre: optional object {cloudflare\_endpoint }

Omitted in responses for version 1.5 interconnects.

</summary>

cloudflare\_endpoint: optional string

The IP address assigned to the Cloudflare side of the GRE tunnel created as part of the Interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20gre%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20gre">Link to this property</a>

<details>

<summary>

health\_check: optional object {direction, enabled, rate, 3 more }

</summary>

<details>

<summary>

direction: optional "unidirectional"or "bidirectional"

The direction of the flow of the healthcheck. Either unidirectional, where the probe comes to you via the interconnect and the result comes back to Cloudflare via the open Internet, or bidirectional where both the probe and result come and go via the interconnect.

</summary>

One of the following:

"unidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%200">Link to this property</a>

"bidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20direction">Link to this property</a>

enabled: optional boolean

Determines whether to run healthchecks for a tunnel.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20enabled">Link to this property</a>

rate: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_rate%20%3E%20(schema)">HealthCheckRate</a>

How frequent the health check is run. The default value is <code>mid</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20rate">Link to this property</a>

source: optional string

The source IPv4 address used for bidirectional health checks. Supported only for version 1.5 interconnects. It is required when <code>direction</code> is <code>bidirectional</code> and must be omitted (and is cleared) when <code>direction</code> is <code>unidirectional</code>. The address must be within RFC1918 space, the approved link-local range 169.254.240.0/20, or the Cloudflare reserved range 198.41.199.224/27.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

target: optional object {effective, saved } or string

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target. Must be in object form if the x-magic-new-hc-target header is set to true and string form if x-magic-new-hc-target is absent or set to false.

</summary>

One of the following:

<details>

<summary>

MagicHealthCheckTarget object {effective, saved }

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target.

</summary>

effective: optional string

The effective health check target. If ‘saved’ is empty, then this field will be populated with the calculated default value on GET requests. Ignored in POST, PUT, and PATCH requests.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20effective">Link to this property</a>

saved: optional string

The saved health check target. Setting the value to the empty string indicates that the calculated default value will be used.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20saved">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target">Link to this property</a>

type: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_type%20%3E%20(schema)">HealthCheckType</a>

The type of healthcheck to run, reply or request. The default value is <code>reply</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20health_check">Link to this property</a>

interface\_address: optional string

The IPv4 interface address for the interconnect. For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /30 or /31 prefix may be used. Version 1.5 interconnects require a /31 prefix and may also use a prefix from the account’s authorized prefixes; otherwise, select the subnet from RFC 1918 or the approved link-local ranges.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20interface_address">Link to this property</a>

interface\_address6: optional string

A 127 bit IPV6 prefix from within the virtual\_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual\_subnet6. Eg if virtual\_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface\_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20interface_address6">Link to this property</a>

modified\_on: optional string

The date and time the tunnel was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20modified_on">Link to this property</a>

mtu: optional number

The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum value is 576.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20mtu">Link to this property</a>

name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20name">Link to this property</a>

version: optional string

Immutable interconnect version configured at creation time. One of:

- “1”
- “1.5”
- “2”

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20version">Link to this property</a>

virtual\_port\_reservation\_id: optional string

An identifier that correlates this interconnect with the corresponding V2 CNI interconnect resource.

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)%20%3E%20(property)%20interconnect">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_get_response%20%3E%20(schema)>)

<details>

<summary>

CfInterconnectUpdateResponse object {modified, modified\_interconnect }

</summary>

modified: optional boolean

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

modified\_interconnect: optional object {id, automatic\_return\_routing, bgp, 12 more }

</summary>

id: optional string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20id">Link to this property</a>

automatic\_return\_routing: optional boolean

True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the <code>coupler_integration</code> account flag to be enabled; requests setting this to <code>true</code> without that flag will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20automatic_return_routing">Link to this property</a>

<details>

<summary>

bgp: optional object {as\_no, cloudflare\_endpoint, customer\_asn, 5 more }

</summary>

Deprecatedas\_no: optional number

Deprecated. Use customer\_asn.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20as_no">Link to this property</a>

Deprecatedcloudflare\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

customer\_asn: optional number

ASN used on the customer end of the BGP session.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_asn">Link to this property</a>

Deprecatedcustomer\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_endpoint">Link to this property</a>

export\_filter\_id: optional string

ID of the BGP filter profile applied to routes advertised to the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20export_filter_id">Link to this property</a>

extra\_prefixes: optional array of string

Prefixes in this list will be advertised to the customer device, in addition to the routes in the Magic routing table.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20extra_prefixes">Link to this property</a>

import\_filter\_id: optional string

ID of the BGP filter profile applied to routes received from the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20import_filter_id">Link to this property</a>

md5\_key: optional string

MD5 key to use for session authentication.

Note that *this is not a security measure*. MD5 is not a valid security mechanism, and the key is not treated as a secret value. This is *only* supported for preventing misconfiguration, not for defending against malicious attacks.

The MD5 key, if set, must be of non-zero length and consist only of the following types of character:

- ASCII alphanumerics: <code>[a-zA-Z0-9]</code>
- Special characters in the set <code>'!@#$%^&amp;*()+[]{}&lt;&gt;/.,;:_-~</code>= |\`

In other words, MD5 keys may contain any printable ASCII character aside from newline (0x0A), quotation mark (<code>"</code>), vertical tab (0x0B), carriage return (0x0D), tab (0x09), form feed (0x0C), and the question mark (<code>?</code>). Requests specifying an MD5 key with one or more of these disallowed characters will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp%20%3E%20(property)%20md5_key">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20bgp">Link to this property</a>

colo\_name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20colo_name">Link to this property</a>

created\_on: optional string

The date and time the tunnel was created.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional description of the interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

gre: optional object {cloudflare\_endpoint }

Omitted in responses for version 1.5 interconnects.

</summary>

cloudflare\_endpoint: optional string

The IP address assigned to the Cloudflare side of the GRE tunnel created as part of the Interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20gre%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20gre">Link to this property</a>

<details>

<summary>

health\_check: optional object {direction, enabled, rate, 3 more }

</summary>

<details>

<summary>

direction: optional "unidirectional"or "bidirectional"

The direction of the flow of the healthcheck. Either unidirectional, where the probe comes to you via the interconnect and the result comes back to Cloudflare via the open Internet, or bidirectional where both the probe and result come and go via the interconnect.

</summary>

One of the following:

"unidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%200">Link to this property</a>

"bidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20direction">Link to this property</a>

enabled: optional boolean

Determines whether to run healthchecks for a tunnel.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20enabled">Link to this property</a>

rate: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_rate%20%3E%20(schema)">HealthCheckRate</a>

How frequent the health check is run. The default value is <code>mid</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20rate">Link to this property</a>

source: optional string

The source IPv4 address used for bidirectional health checks. Supported only for version 1.5 interconnects. It is required when <code>direction</code> is <code>bidirectional</code> and must be omitted (and is cleared) when <code>direction</code> is <code>unidirectional</code>. The address must be within RFC1918 space, the approved link-local range 169.254.240.0/20, or the Cloudflare reserved range 198.41.199.224/27.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

target: optional object {effective, saved } or string

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target. Must be in object form if the x-magic-new-hc-target header is set to true and string form if x-magic-new-hc-target is absent or set to false.

</summary>

One of the following:

<details>

<summary>

MagicHealthCheckTarget object {effective, saved }

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target.

</summary>

effective: optional string

The effective health check target. If ‘saved’ is empty, then this field will be populated with the calculated default value on GET requests. Ignored in POST, PUT, and PATCH requests.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20effective">Link to this property</a>

saved: optional string

The saved health check target. Setting the value to the empty string indicates that the calculated default value will be used.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20saved">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20target">Link to this property</a>

type: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_type%20%3E%20(schema)">HealthCheckType</a>

The type of healthcheck to run, reply or request. The default value is <code>reply</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20health_check">Link to this property</a>

interface\_address: optional string

The IPv4 interface address for the interconnect. For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /30 or /31 prefix may be used. Version 1.5 interconnects require a /31 prefix and may also use a prefix from the account’s authorized prefixes; otherwise, select the subnet from RFC 1918 or the approved link-local ranges.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20interface_address">Link to this property</a>

interface\_address6: optional string

A 127 bit IPV6 prefix from within the virtual\_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual\_subnet6. Eg if virtual\_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface\_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20interface_address6">Link to this property</a>

modified\_on: optional string

The date and time the tunnel was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20modified_on">Link to this property</a>

mtu: optional number

The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum value is 576.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20mtu">Link to this property</a>

name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20name">Link to this property</a>

version: optional string

Immutable interconnect version configured at creation time. One of:

- “1”
- “1.5”
- “2”

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20version">Link to this property</a>

virtual\_port\_reservation\_id: optional string

An identifier that correlates this interconnect with the corresponding V2 CNI interconnect resource.

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnect">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_update_response%20%3E%20(schema)>)

<details>

<summary>

CfInterconnectBulkUpdateResponse object {modified, modified\_interconnects }

</summary>

modified: optional boolean

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

modified\_interconnects: optional array of object {id, automatic\_return\_routing, bgp, 12 more }

</summary>

id: optional string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

automatic\_return\_routing: optional boolean

True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the <code>coupler_integration</code> account flag to be enabled; requests setting this to <code>true</code> without that flag will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20automatic_return_routing">Link to this property</a>

<details>

<summary>

bgp: optional object {as\_no, cloudflare\_endpoint, customer\_asn, 5 more }

</summary>

Deprecatedas\_no: optional number

Deprecated. Use customer\_asn.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20as_no">Link to this property</a>

Deprecatedcloudflare\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

customer\_asn: optional number

ASN used on the customer end of the BGP session.

formatint32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_asn">Link to this property</a>

Deprecatedcustomer\_endpoint: optional string

Read-only for v1.5; derived from interface\_address.

formatipv4

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20customer_endpoint">Link to this property</a>

export\_filter\_id: optional string

ID of the BGP filter profile applied to routes advertised to the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20export_filter_id">Link to this property</a>

extra\_prefixes: optional array of string

Prefixes in this list will be advertised to the customer device, in addition to the routes in the Magic routing table.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20extra_prefixes">Link to this property</a>

import\_filter\_id: optional string

ID of the BGP filter profile applied to routes received from the customer.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20import_filter_id">Link to this property</a>

md5\_key: optional string

MD5 key to use for session authentication.

Note that *this is not a security measure*. MD5 is not a valid security mechanism, and the key is not treated as a secret value. This is *only* supported for preventing misconfiguration, not for defending against malicious attacks.

The MD5 key, if set, must be of non-zero length and consist only of the following types of character:

- ASCII alphanumerics: <code>[a-zA-Z0-9]</code>
- Special characters in the set <code>'!@#$%^&amp;*()+[]{}&lt;&gt;/.,;:_-~</code>= |\`

In other words, MD5 keys may contain any printable ASCII character aside from newline (0x0A), quotation mark (<code>"</code>), vertical tab (0x0B), carriage return (0x0D), tab (0x09), form feed (0x0C), and the question mark (<code>?</code>). Requests specifying an MD5 key with one or more of these disallowed characters will be rejected.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp%20%3E%20(property)%20md5_key">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20bgp">Link to this property</a>

colo\_name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20colo_name">Link to this property</a>

created\_on: optional string

The date and time the tunnel was created.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional description of the interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

gre: optional object {cloudflare\_endpoint }

Omitted in responses for version 1.5 interconnects.

</summary>

cloudflare\_endpoint: optional string

The IP address assigned to the Cloudflare side of the GRE tunnel created as part of the Interconnect.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20gre%20%3E%20(property)%20cloudflare_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20gre">Link to this property</a>

<details>

<summary>

health\_check: optional object {direction, enabled, rate, 3 more }

</summary>

<details>

<summary>

direction: optional "unidirectional"or "bidirectional"

The direction of the flow of the healthcheck. Either unidirectional, where the probe comes to you via the interconnect and the result comes back to Cloudflare via the open Internet, or bidirectional where both the probe and result come and go via the interconnect.

</summary>

One of the following:

"unidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%200">Link to this property</a>

"bidirectional"

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20direction%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20direction">Link to this property</a>

enabled: optional boolean

Determines whether to run healthchecks for a tunnel.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20enabled">Link to this property</a>

rate: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_rate%20%3E%20(schema)">HealthCheckRate</a>

How frequent the health check is run. The default value is <code>mid</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20rate">Link to this property</a>

source: optional string

The source IPv4 address used for bidirectional health checks. Supported only for version 1.5 interconnects. It is required when <code>direction</code> is <code>bidirectional</code> and must be omitted (and is cleared) when <code>direction</code> is <code>unidirectional</code>. The address must be within RFC1918 space, the approved link-local range 169.254.240.0/20, or the Cloudflare reserved range 198.41.199.224/27.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

target: optional object {effective, saved } or string

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target. Must be in object form if the x-magic-new-hc-target header is set to true and string form if x-magic-new-hc-target is absent or set to false.

</summary>

One of the following:

<details>

<summary>

MagicHealthCheckTarget object {effective, saved }

The destination address in a request type health check. After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to <code>customer_gre_endpoint address</code>. This field is ignored for bidirectional healthchecks as the interface\_address (not assigned to the Cloudflare side of the tunnel) is used as the target.

</summary>

effective: optional string

The effective health check target. If ‘saved’ is empty, then this field will be populated with the calculated default value on GET requests. Ignored in POST, PUT, and PATCH requests.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20effective">Link to this property</a>

saved: optional string

The saved health check target. Setting the value to the empty string indicates that the calculated default value will be used.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200%20%3E%20(property)%20saved">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20target">Link to this property</a>

type: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit%20%3E%20(model)%20health_check_type%20%3E%20(schema)">HealthCheckType</a>

The type of healthcheck to run, reply or request. The default value is <code>reply</code>.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20health_check">Link to this property</a>

interface\_address: optional string

The IPv4 interface address for the interconnect. For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /30 or /31 prefix may be used. Version 1.5 interconnects require a /31 prefix and may also use a prefix from the account’s authorized prefixes; otherwise, select the subnet from RFC 1918 or the approved link-local ranges.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20interface_address">Link to this property</a>

interface\_address6: optional string

A 127 bit IPV6 prefix from within the virtual\_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual\_subnet6. Eg if virtual\_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface\_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20interface_address6">Link to this property</a>

modified\_on: optional string

The date and time the tunnel was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

mtu: optional number

The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum value is 576.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20mtu">Link to this property</a>

name: optional string

The name of the interconnect. The name cannot share a name with other tunnels.

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

version: optional string

Immutable interconnect version configured at creation time. One of:

- “1”
- “1.5”
- “2”

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20version">Link to this property</a>

virtual\_port\_reservation\_id: optional string

An identifier that correlates this interconnect with the corresponding V2 CNI interconnect resource.

maxLength32

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects%20%3E%20(items)%20%3E%20(property)%20virtual_port_reservation_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_interconnects">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.cf_interconnects%20%3E%20(model)%20cf_interconnect_bulk_update_response%20%3E%20(schema)>)