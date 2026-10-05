---
title: Pools
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Load Balancers](https://developers.cloudflare.com/api/resources/load_balancers)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Pools

##### [List Pools](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/list)

GET/accounts/{account\_id}/load\_balancers/pools

##### [Pool Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/get)

GET/accounts/{account\_id}/load\_balancers/pools/{pool\_id}

##### [Create Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/create)

POST/accounts/{account\_id}/load\_balancers/pools

##### [Update Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/update)

PUT/accounts/{account\_id}/load\_balancers/pools/{pool\_id}

##### [Patch Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/edit)

PATCH/accounts/{account\_id}/load\_balancers/pools/{pool\_id}

##### [Delete Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/delete)

DELETE/accounts/{account\_id}/load\_balancers/pools/{pool\_id}

##### [Patch Pools](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/bulk_edit)

PATCH/accounts/{account\_id}/load\_balancers/pools

##### ModelsExpand Collapse

<details>

<summary>

Pool object {id, check\_regions, created\_on, 17 more }

</summary>

id: optional string

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

check\_regions: optional array of <a href="https://developers.cloudflare.com/api/resources/load_balancers#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)">CheckRegion</a>

A list of regions from which to run health checks. Null means every Cloudflare data center.

</summary>

One of the following:

"WNAM"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"ENAM"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"WEU"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

"EEU"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%203">Link to this property</a>

"NSAM"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%204">Link to this property</a>

"SSAM"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%205">Link to this property</a>

"OC"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%206">Link to this property</a>

"ME"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%207">Link to this property</a>

"NAF"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%208">Link to this property</a>

"SAF"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%209">Link to this property</a>

"SAS"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%2010">Link to this property</a>

"SEAS"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%2011">Link to this property</a>

"NEAS"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%2012">Link to this property</a>

"CHINA"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%2013">Link to this property</a>

"ALL\_REGIONS"

<a href="#(resource)%20load_balancers%20%3E%20(model)%20check_region%20%3E%20(schema)%20%3E%20(member)%2014">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20check_regions">Link to this property</a>

created\_on: optional string

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

A human-readable description of the pool.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

disabled\_at: optional string

This field shows up only if the pool is disabled. This field is set with the time the pool was disabled at.

formatdate-time

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20disabled_at">Link to this property</a>

enabled: optional boolean

Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

health\_sources: optional array of "local"or "regional"or "global"

A list of health sources, ordered from highest to lowest priority, used to evaluate individual origin health and overall pool health. The load balancer uses the first source that has data and falls back to the next. Currently accepted values are null or the exact array \[“regional”, “global”]; any other combination is rejected. Null (the default) behaves like \[“local”, “global”]. \[“regional”, “global”] makes each region steer on its own health, falling back to the global decision when a region has no fresh data. Setting regional requires at least one region in check\_regions.

</summary>

One of the following:

"local"

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20health_sources%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"regional"

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20health_sources%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"global"

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20health_sources%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20health_sources">Link to this property</a>

latitude: optional number

The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20latitude">Link to this property</a>

load\_shedding: optional <a href="https://developers.cloudflare.com/api/resources/load_balancers#(resource)%20load_balancers%20%3E%20(model)%20load_shedding%20%3E%20(schema)">LoadShedding</a> { default\_percent, default\_policy, session\_percent, session\_policy }

Configures load shedding policies and percentages for the pool.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20load_shedding">Link to this property</a>

longitude: optional number

The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20longitude">Link to this property</a>

minimum\_origins: optional number

The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20minimum_origins">Link to this property</a>

modified\_on: optional string

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

monitor: optional string

The ID of the Monitor to use for checking the health of origins within this pool.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20monitor">Link to this property</a>

monitor\_group: optional string

The ID of the Monitor Group to use for checking the health of origins within this pool.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20monitor_group">Link to this property</a>

name: optional string

A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

networks: optional array of string

List of networks where Load Balancer or Pool is enabled.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20networks">Link to this property</a>

notification\_email: optional string

This field is now deprecated. It has been moved to Cloudflare’s Centralized Notification service <a href="https://developers.cloudflare.com/fundamentals/notifications/">https://developers.cloudflare.com/fundamentals/notifications/</a>. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20notification_email">Link to this property</a>

notification\_filter: optional <a href="https://developers.cloudflare.com/api/resources/load_balancers#(resource)%20load_balancers%20%3E%20(model)%20notification_filter%20%3E%20(schema)">NotificationFilter</a> { origin, pool }

Filter pool and origin health notifications by resource type or health status. Use null to reset.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20notification_filter">Link to this property</a>

origin\_steering: optional <a href="https://developers.cloudflare.com/api/resources/load_balancers#(resource)%20load_balancers%20%3E%20(model)%20origin_steering%20%3E%20(schema)">OriginSteering</a> { policy }

Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity.

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20origin_steering">Link to this property</a>

<details>

<summary>

origins: optional array of <a href="https://developers.cloudflare.com/api/resources/load_balancers#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)">Origin</a> { address, disabled\_at, enabled, 6 more }

The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy.

</summary>

address: optional string

The IP address (IPv4 or IPv6) of the origin, or its publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare. To set an internal/reserved address, virtual\_network\_id must also be set.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

disabled\_at: optional string

This field shows up only if the origin is disabled. This field is set with the time the origin was disabled.

formatdate-time

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20disabled_at">Link to this property</a>

enabled: optional boolean

Whether to enable (the default) this origin within the pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

flatten\_cname: optional boolean

Whether to flatten CNAME records for this origin, resolving them to A/AAAA records before returning to the client. When true (the default), the director resolves CNAME addresses to their underlying A/AAAA records. When false, the origin address is returned as a raw CNAME record without resolution. This setting mirrors the DNS API record flatten\_cname setting.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20flatten_cname">Link to this property</a>

header: optional <a href="https://developers.cloudflare.com/api/resources/load_balancers#(resource)%20load_balancers%20%3E%20(model)%20header%20%3E%20(schema)">Header</a> { Host }

The request header is used to pass additional information with an HTTP request. Currently supported header is ‘Host’.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20header">Link to this property</a>

name: optional string

A human-identifiable name for the origin.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

port: optional number

The port for upstream connections. A value of 0 means the default port for the protocol will be used.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20port">Link to this property</a>

virtual\_network\_id: optional string

The virtual network subnet ID the origin belongs in. Virtual network must also belong to the account.

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20virtual_network_id">Link to this property</a>

weight: optional number

The weight of this origin relative to other origins in the pool. Based on the configured weight the total traffic is distributed among origins within the pool.

- <code>origin_steering.policy="least_outstanding_requests"</code>: Use weight to scale the origin’s outstanding requests.
- <code>origin_steering.policy="least_connections"</code>: Use weight to scale the origin’s open connections.

maximum1

minimum0

multipleOf0.01

<a href="#(resource)%20load_balancers%20%3E%20(model)%20origin%20%3E%20(schema)%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)%20%3E%20(property)%20origins">Link to this property</a>

</details>

[Link to this property](<#(resource)%20load_balancers.pools%20%3E%20(model)%20pool%20%3E%20(schema)>)

<details>

<summary>

PoolDeleteResponse object {id }

</summary>

id: optional string

<a href="#(resource)%20load_balancers.pools%20%3E%20(model)%20pool_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20load_balancers.pools%20%3E%20(model)%20pool_delete_response%20%3E%20(schema)>)

#### PoolsHealth

##### [Pool Health Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/get)

GET/accounts/{account\_id}/load\_balancers/pools/{pool\_id}/health

##### [Preview Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/create)

POST/accounts/{account\_id}/load\_balancers/pools/{pool\_id}/preview

##### ModelsExpand Collapse

<details>

<summary>

HealthGetResponse object {pool\_id, pop\_health }

A list of regions from which to run health checks. Null means every Cloudflare data center.

</summary>

pool\_id: optional string

Pool ID.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pool_id">Link to this property</a>

<details>

<summary>

pop\_health: optional object {healthy, origins }

List of regions and associated health status.

</summary>

healthy: optional boolean

Whether health check in region is healthy.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20healthy">Link to this property</a>

<details>

<summary>

origins: optional array of object {ip }

</summary>

<details>

<summary>

ip: optional object {failure\_reason, healthy, response\_code, rtt }

</summary>

failure\_reason: optional string

Failure reason.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20ip%20%3E%20(property)%20failure_reason">Link to this property</a>

healthy: optional boolean

Origin health status.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20ip%20%3E%20(property)%20healthy">Link to this property</a>

response\_code: optional number

Response code from origin health check.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20ip%20%3E%20(property)%20response_code">Link to this property</a>

rtt: optional string

Origin RTT (Round Trip Time) response.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20ip%20%3E%20(property)%20rtt">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20origins%20%3E%20(items)%20%3E%20(property)%20ip">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health%20%3E%20(property)%20origins">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)%20%3E%20(property)%20pop_health">Link to this property</a>

</details>

[Link to this property](<#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_get_response%20%3E%20(schema)>)

<details>

<summary>

HealthCreateResponse object {pools, preview\_id }

</summary>

pools: optional map\[string]

Monitored pool IDs mapped to their respective names.

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_create_response%20%3E%20(schema)%20%3E%20(property)%20pools">Link to this property</a>

preview\_id: optional string

<a href="#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_create_response%20%3E%20(schema)%20%3E%20(property)%20preview_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20load_balancers.pools.health%20%3E%20(model)%20health_create_response%20%3E%20(schema)>)

#### PoolsReferences

##### [List Pool References](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/references/methods/get)

GET/accounts/{account\_id}/load\_balancers/pools/{pool\_id}/references

##### ModelsExpand Collapse

<details>

<summary>

ReferenceGetResponse object {reference\_type, resource\_id, resource\_name, resource\_type }

</summary>

<details>

<summary>

reference\_type: optional "\*"or "referral"or "referrer"

</summary>

One of the following:

"\*"

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20reference_type%20%3E%20(member)%200">Link to this property</a>

"referral"

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20reference_type%20%3E%20(member)%201">Link to this property</a>

"referrer"

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20reference_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20reference_type">Link to this property</a>

resource\_id: optional string

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_id">Link to this property</a>

resource\_name: optional string

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_name">Link to this property</a>

resource\_type: optional string

<a href="#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20load_balancers.pools.references%20%3E%20(model)%20reference_get_response%20%3E%20(schema)>)