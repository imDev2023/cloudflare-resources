---
title: Smart Shield
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Smart Shield

##### [Get Smart Shield Settings](https://developers.cloudflare.com/api/resources/smart_shield/methods/get)

GET/zones/{zone\_id}/smart\_shield

##### [Patch Smart Shield Settings](https://developers.cloudflare.com/api/resources/smart_shield/methods/update)

PATCH/zones/{zone\_id}/smart\_shield

##### ModelsExpand Collapse

<details>

<summary>

SmartShieldGetResponse object {cache\_reserve, healthchecks\_count, regional\_tiered\_cache, 2 more }

A consolidated object containing settings from multiple APIs for partial updates.

</summary>

<details>

<summary>

cache\_reserve: object {id, editable, value }

</summary>

id: optional string

The id of the Cache Reserve setting.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20id">Link to this property</a>

editable: optional boolean

Whether the setting is editable.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: optional "on"or "off"

Specifies the enablement value of Cache Reserve.

</summary>

One of the following:

"on"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_reserve">Link to this property</a>

healthchecks\_count: number

The total number of health checks associated with the zone.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20healthchecks_count">Link to this property</a>

<details>

<summary>

regional\_tiered\_cache: object {id, editable, value }

</summary>

id: optional string

The id of the Regional Tiered Cache setting.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20regional_tiered_cache%20%3E%20(property)%20id">Link to this property</a>

editable: optional boolean

Whether the setting is editable.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20regional_tiered_cache%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: optional "on"or "off"

Specifies the enablement value of Cache Reserve.

</summary>

One of the following:

"on"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20regional_tiered_cache%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20regional_tiered_cache%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20regional_tiered_cache%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20regional_tiered_cache">Link to this property</a>

<details>

<summary>

smart\_routing: object {id, editable, value }

</summary>

id: optional string

The id of the Smart Routing setting.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_routing%20%3E%20(property)%20id">Link to this property</a>

editable: optional boolean

Whether the setting is editable.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_routing%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: optional "on"or "off"

Specifies the enablement value of Argo Smart Routing.

</summary>

One of the following:

"on"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_routing%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_routing%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_routing%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_routing">Link to this property</a>

<details>

<summary>

smart\_tiered\_cache: object {id, editable, modified\_on, value }

</summary>

id: optional string

The id of the Smart Tiered Cache setting.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20id">Link to this property</a>

editable: optional boolean

Whether the setting is editable.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: optional string

The last time the setting was modified.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

value: optional "on"or "off"

Specifies the enablement value of Tiered Cache.

</summary>

One of the following:

"on"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_get_response%20%3E%20(schema)>)

<details>

<summary>

SmartShieldUpdateResponse object {smart\_tiered\_cache }

A consolidated object containing settings from multiple APIs for partial updates.

</summary>

<details>

<summary>

smart\_tiered\_cache: object {id, editable, modified\_on, value }

</summary>

id: optional string

The id of the Smart Tiered Cache setting.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20id">Link to this property</a>

editable: optional boolean

Whether the setting is editable.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: optional string

The last time the setting was modified.

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

value: optional "on"or "off"

Specifies the enablement value of Tiered Cache.

</summary>

One of the following:

"on"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)%20%3E%20(property)%20smart_tiered_cache">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield%20%3E%20(model)%20smart_shield_update_response%20%3E%20(schema)>)

#### Smart ShieldHealth Checks

##### [List Health Checks](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/list)

GET/zones/{zone\_id}/smart\_shield/healthchecks

##### [Health Check Details](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/get)

GET/zones/{zone\_id}/smart\_shield/healthchecks/{healthcheck\_id}

##### [Create Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/create)

POST/zones/{zone\_id}/smart\_shield/healthchecks

##### [Update Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/update)

PUT/zones/{zone\_id}/smart\_shield/healthchecks/{healthcheck\_id}

##### [Patch Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/edit)

PATCH/zones/{zone\_id}/smart\_shield/healthchecks/{healthcheck\_id}

##### [Delete Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/delete)

DELETE/zones/{zone\_id}/smart\_shield/healthchecks/{healthcheck\_id}

##### ModelsExpand Collapse

<details>

<summary>

HealthCheckListResponse object {id, address, check\_regions, 15 more }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

The hostname or IP address of the origin server to run health checks on.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

<details>

<summary>

check\_regions: optional array of "WNAM"or "ENAM"or "WEU"or 11 more

A list of regions from which to run health checks. Null means Cloudflare will pick a default region.

</summary>

One of the following:

"WNAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"ENAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"WEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"EEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"NSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"SSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"OC"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"ME"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

"NAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%208">Link to this property</a>

"SAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%209">Link to this property</a>

"IN"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2010">Link to this property</a>

"SEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2011">Link to this property</a>

"NEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2012">Link to this property</a>

"ALL\_REGIONS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2013">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20check_regions">Link to this property</a>

consecutive\_fails: optional number

The number of consecutive fails required from a health check before changing the health to unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_fails">Link to this property</a>

consecutive\_successes: optional number

The number of consecutive successes required from a health check before changing the health to healthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_successes">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

A human-readable description of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

failure\_reason: optional string

The current failure reason if status is unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20failure_reason">Link to this property</a>

<details>

<summary>

http\_config: optional object {allow\_insecure, expected\_body, expected\_codes, 5 more }

Parameters specific to an HTTP or HTTPS health check.

</summary>

allow\_insecure: optional boolean

Do not validate the certificate when the health check uses HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20allow_insecure">Link to this property</a>

expected\_body: optional string

A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_body">Link to this property</a>

expected\_codes: optional array of string

The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_codes">Link to this property</a>

follow\_redirects: optional boolean

Follow redirects if the origin returns a 3xx status code.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20follow_redirects">Link to this property</a>

header: optional map\[array of string]

The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20header">Link to this property</a>

<details>

<summary>

method: optional "GET"or "HEAD"

The HTTP method to use for the health check.

</summary>

One of the following:

"GET"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"HEAD"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method">Link to this property</a>

path: optional string

The endpoint path to health check against.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20path">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80 if type is HTTP or 443 if type is HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20http_config">Link to this property</a>

interval: optional number

The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

modified\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: optional string

A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

retries: optional number

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

status: optional "unknown"or "healthy"or "unhealthy"or "suspended"

The current status of the origin server according to the health check.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"healthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"unhealthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"suspended"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

suspended: optional boolean

If suspended, no health checks are sent to the origin.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20suspended">Link to this property</a>

<details>

<summary>

tcp\_config: optional object {method, port }

Parameters specific to TCP health check.

</summary>

method: optional "connection\_established"

The TCP connection method to use for the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20method">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config">Link to this property</a>

timeout: optional number

The timeout (in seconds) before marking the health check as failed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20timeout">Link to this property</a>

type: optional string

The protocol to use for the health check. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_list_response%20%3E%20(schema)>)

<details>

<summary>

HealthCheckGetResponse object {id, address, check\_regions, 15 more }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

The hostname or IP address of the origin server to run health checks on.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

<details>

<summary>

check\_regions: optional array of "WNAM"or "ENAM"or "WEU"or 11 more

A list of regions from which to run health checks. Null means Cloudflare will pick a default region.

</summary>

One of the following:

"WNAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"ENAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"WEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"EEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"NSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"SSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"OC"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"ME"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

"NAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%208">Link to this property</a>

"SAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%209">Link to this property</a>

"IN"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2010">Link to this property</a>

"SEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2011">Link to this property</a>

"NEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2012">Link to this property</a>

"ALL\_REGIONS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2013">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20check_regions">Link to this property</a>

consecutive\_fails: optional number

The number of consecutive fails required from a health check before changing the health to unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_fails">Link to this property</a>

consecutive\_successes: optional number

The number of consecutive successes required from a health check before changing the health to healthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_successes">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

A human-readable description of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

failure\_reason: optional string

The current failure reason if status is unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20failure_reason">Link to this property</a>

<details>

<summary>

http\_config: optional object {allow\_insecure, expected\_body, expected\_codes, 5 more }

Parameters specific to an HTTP or HTTPS health check.

</summary>

allow\_insecure: optional boolean

Do not validate the certificate when the health check uses HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20allow_insecure">Link to this property</a>

expected\_body: optional string

A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_body">Link to this property</a>

expected\_codes: optional array of string

The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_codes">Link to this property</a>

follow\_redirects: optional boolean

Follow redirects if the origin returns a 3xx status code.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20follow_redirects">Link to this property</a>

header: optional map\[array of string]

The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20header">Link to this property</a>

<details>

<summary>

method: optional "GET"or "HEAD"

The HTTP method to use for the health check.

</summary>

One of the following:

"GET"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"HEAD"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method">Link to this property</a>

path: optional string

The endpoint path to health check against.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20path">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80 if type is HTTP or 443 if type is HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20http_config">Link to this property</a>

interval: optional number

The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

modified\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: optional string

A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

retries: optional number

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

status: optional "unknown"or "healthy"or "unhealthy"or "suspended"

The current status of the origin server according to the health check.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"healthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"unhealthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"suspended"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

suspended: optional boolean

If suspended, no health checks are sent to the origin.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20suspended">Link to this property</a>

<details>

<summary>

tcp\_config: optional object {method, port }

Parameters specific to TCP health check.

</summary>

method: optional "connection\_established"

The TCP connection method to use for the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20method">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config">Link to this property</a>

timeout: optional number

The timeout (in seconds) before marking the health check as failed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20timeout">Link to this property</a>

type: optional string

The protocol to use for the health check. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_get_response%20%3E%20(schema)>)

<details>

<summary>

HealthCheckCreateResponse object {id, address, check\_regions, 15 more }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

The hostname or IP address of the origin server to run health checks on.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

<details>

<summary>

check\_regions: optional array of "WNAM"or "ENAM"or "WEU"or 11 more

A list of regions from which to run health checks. Null means Cloudflare will pick a default region.

</summary>

One of the following:

"WNAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"ENAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"WEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"EEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"NSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"SSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"OC"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"ME"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

"NAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%208">Link to this property</a>

"SAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%209">Link to this property</a>

"IN"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2010">Link to this property</a>

"SEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2011">Link to this property</a>

"NEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2012">Link to this property</a>

"ALL\_REGIONS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2013">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20check_regions">Link to this property</a>

consecutive\_fails: optional number

The number of consecutive fails required from a health check before changing the health to unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_fails">Link to this property</a>

consecutive\_successes: optional number

The number of consecutive successes required from a health check before changing the health to healthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_successes">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

A human-readable description of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

failure\_reason: optional string

The current failure reason if status is unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20failure_reason">Link to this property</a>

<details>

<summary>

http\_config: optional object {allow\_insecure, expected\_body, expected\_codes, 5 more }

Parameters specific to an HTTP or HTTPS health check.

</summary>

allow\_insecure: optional boolean

Do not validate the certificate when the health check uses HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20allow_insecure">Link to this property</a>

expected\_body: optional string

A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_body">Link to this property</a>

expected\_codes: optional array of string

The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_codes">Link to this property</a>

follow\_redirects: optional boolean

Follow redirects if the origin returns a 3xx status code.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20follow_redirects">Link to this property</a>

header: optional map\[array of string]

The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20header">Link to this property</a>

<details>

<summary>

method: optional "GET"or "HEAD"

The HTTP method to use for the health check.

</summary>

One of the following:

"GET"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"HEAD"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method">Link to this property</a>

path: optional string

The endpoint path to health check against.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20path">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80 if type is HTTP or 443 if type is HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20http_config">Link to this property</a>

interval: optional number

The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

modified\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: optional string

A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

retries: optional number

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

status: optional "unknown"or "healthy"or "unhealthy"or "suspended"

The current status of the origin server according to the health check.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"healthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"unhealthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"suspended"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

suspended: optional boolean

If suspended, no health checks are sent to the origin.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20suspended">Link to this property</a>

<details>

<summary>

tcp\_config: optional object {method, port }

Parameters specific to TCP health check.

</summary>

method: optional "connection\_established"

The TCP connection method to use for the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20method">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config">Link to this property</a>

timeout: optional number

The timeout (in seconds) before marking the health check as failed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20timeout">Link to this property</a>

type: optional string

The protocol to use for the health check. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_create_response%20%3E%20(schema)>)

<details>

<summary>

HealthCheckUpdateResponse object {id, address, check\_regions, 15 more }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

The hostname or IP address of the origin server to run health checks on.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

<details>

<summary>

check\_regions: optional array of "WNAM"or "ENAM"or "WEU"or 11 more

A list of regions from which to run health checks. Null means Cloudflare will pick a default region.

</summary>

One of the following:

"WNAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"ENAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"WEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"EEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"NSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"SSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"OC"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"ME"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

"NAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%208">Link to this property</a>

"SAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%209">Link to this property</a>

"IN"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2010">Link to this property</a>

"SEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2011">Link to this property</a>

"NEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2012">Link to this property</a>

"ALL\_REGIONS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2013">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20check_regions">Link to this property</a>

consecutive\_fails: optional number

The number of consecutive fails required from a health check before changing the health to unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_fails">Link to this property</a>

consecutive\_successes: optional number

The number of consecutive successes required from a health check before changing the health to healthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_successes">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

A human-readable description of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

failure\_reason: optional string

The current failure reason if status is unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20failure_reason">Link to this property</a>

<details>

<summary>

http\_config: optional object {allow\_insecure, expected\_body, expected\_codes, 5 more }

Parameters specific to an HTTP or HTTPS health check.

</summary>

allow\_insecure: optional boolean

Do not validate the certificate when the health check uses HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20allow_insecure">Link to this property</a>

expected\_body: optional string

A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_body">Link to this property</a>

expected\_codes: optional array of string

The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_codes">Link to this property</a>

follow\_redirects: optional boolean

Follow redirects if the origin returns a 3xx status code.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20follow_redirects">Link to this property</a>

header: optional map\[array of string]

The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20header">Link to this property</a>

<details>

<summary>

method: optional "GET"or "HEAD"

The HTTP method to use for the health check.

</summary>

One of the following:

"GET"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"HEAD"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method">Link to this property</a>

path: optional string

The endpoint path to health check against.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20path">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80 if type is HTTP or 443 if type is HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20http_config">Link to this property</a>

interval: optional number

The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

modified\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: optional string

A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

retries: optional number

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

status: optional "unknown"or "healthy"or "unhealthy"or "suspended"

The current status of the origin server according to the health check.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"healthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"unhealthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"suspended"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

suspended: optional boolean

If suspended, no health checks are sent to the origin.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20suspended">Link to this property</a>

<details>

<summary>

tcp\_config: optional object {method, port }

Parameters specific to TCP health check.

</summary>

method: optional "connection\_established"

The TCP connection method to use for the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20method">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config">Link to this property</a>

timeout: optional number

The timeout (in seconds) before marking the health check as failed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20timeout">Link to this property</a>

type: optional string

The protocol to use for the health check. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_update_response%20%3E%20(schema)>)

<details>

<summary>

HealthCheckEditResponse object {id, address, check\_regions, 15 more }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

The hostname or IP address of the origin server to run health checks on.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

<details>

<summary>

check\_regions: optional array of "WNAM"or "ENAM"or "WEU"or 11 more

A list of regions from which to run health checks. Null means Cloudflare will pick a default region.

</summary>

One of the following:

"WNAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"ENAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"WEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"EEU"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"NSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"SSAM"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"OC"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"ME"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

"NAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%208">Link to this property</a>

"SAF"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%209">Link to this property</a>

"IN"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2010">Link to this property</a>

"SEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2011">Link to this property</a>

"NEAS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2012">Link to this property</a>

"ALL\_REGIONS"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions%20%3E%20(items)%20%3E%20(member)%2013">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20check_regions">Link to this property</a>

consecutive\_fails: optional number

The number of consecutive fails required from a health check before changing the health to unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_fails">Link to this property</a>

consecutive\_successes: optional number

The number of consecutive successes required from a health check before changing the health to healthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20consecutive_successes">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

A human-readable description of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

failure\_reason: optional string

The current failure reason if status is unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20failure_reason">Link to this property</a>

<details>

<summary>

http\_config: optional object {allow\_insecure, expected\_body, expected\_codes, 5 more }

Parameters specific to an HTTP or HTTPS health check.

</summary>

allow\_insecure: optional boolean

Do not validate the certificate when the health check uses HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20allow_insecure">Link to this property</a>

expected\_body: optional string

A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_body">Link to this property</a>

expected\_codes: optional array of string

The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20expected_codes">Link to this property</a>

follow\_redirects: optional boolean

Follow redirects if the origin returns a 3xx status code.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20follow_redirects">Link to this property</a>

header: optional map\[array of string]

The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20header">Link to this property</a>

<details>

<summary>

method: optional "GET"or "HEAD"

The HTTP method to use for the health check.

</summary>

One of the following:

"GET"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"HEAD"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20method">Link to this property</a>

path: optional string

The endpoint path to health check against.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20path">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80 if type is HTTP or 443 if type is HTTPS.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20http_config">Link to this property</a>

interval: optional number

The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

modified\_on: optional string

formatdate-time

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: optional string

A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

retries: optional number

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

status: optional "unknown"or "healthy"or "unhealthy"or "suspended"

The current status of the origin server according to the health check.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"healthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"unhealthy"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"suspended"

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

suspended: optional boolean

If suspended, no health checks are sent to the origin.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20suspended">Link to this property</a>

<details>

<summary>

tcp\_config: optional object {method, port }

Parameters specific to TCP health check.

</summary>

method: optional "connection\_established"

The TCP connection method to use for the health check.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20method">Link to this property</a>

port: optional number

Port number to connect to for the health check. Defaults to 80.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20tcp_config">Link to this property</a>

timeout: optional number

The timeout (in seconds) before marking the health check as failed.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20timeout">Link to this property</a>

type: optional string

The protocol to use for the health check. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’.

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_edit_response%20%3E%20(schema)>)

<details>

<summary>

HealthCheckDeleteResponse object {id }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.health_checks%20%3E%20(model)%20health_check_delete_response%20%3E%20(schema)>)

#### Smart ShieldCache Reserve Clear

##### [Get Cache Reserve Clear](https://developers.cloudflare.com/api/resources/smart_shield/subresources/cache_reserve_clear/methods/status)

GET/zones/{zone\_id}/smart\_shield/cache\_reserve\_clear

##### [Start Cache Reserve Clear](https://developers.cloudflare.com/api/resources/smart_shield/subresources/cache_reserve_clear/methods/clear)

POST/zones/{zone\_id}/smart\_shield/cache\_reserve\_clear

##### ModelsExpand Collapse

<details>

<summary>

CacheReserveClearStatusResponse object {id, start\_ts, state, 2 more }

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

</summary>

id: <a href="https://developers.cloudflare.com/api/resources/cache#(resource)%20cache.cache_reserve%20%3E%20(model)%20cache_reserve_clear%20%3E%20(schema)">CacheReserveClear</a>

ID of the zone setting.

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

start\_ts: string

The time that the latest Cache Reserve Clear operation started.

formatdate-time

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20start_ts">Link to this property</a>

<details>

<summary>

state: "In-progress"or "Completed"

The current state of the Cache Reserve Clear operation.

</summary>

One of the following:

"In-progress"

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"Completed"

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

end\_ts: optional string

The time that the latest Cache Reserve Clear operation completed.

formatdate-time

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20end_ts">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_status_response%20%3E%20(schema)>)

<details>

<summary>

CacheReserveClearClearResponse object {id, start\_ts, state, 2 more }

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

</summary>

id: <a href="https://developers.cloudflare.com/api/resources/cache#(resource)%20cache.cache_reserve%20%3E%20(model)%20cache_reserve_clear%20%3E%20(schema)">CacheReserveClear</a>

ID of the zone setting.

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

start\_ts: string

The time that the latest Cache Reserve Clear operation started.

formatdate-time

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20start_ts">Link to this property</a>

<details>

<summary>

state: "In-progress"or "Completed"

The current state of the Cache Reserve Clear operation.

</summary>

One of the following:

"In-progress"

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"Completed"

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

end\_ts: optional string

The time that the latest Cache Reserve Clear operation completed.

formatdate-time

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20end_ts">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20smart_shield.cache_reserve_clear%20%3E%20(model)%20cache_reserve_clear_clear_response%20%3E%20(schema)>)