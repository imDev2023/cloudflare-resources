---
title: Fleet Status
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Devices](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Fleet Status

##### [Get the latest status of a device.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/fleet_status/methods/get)

GET/accounts/{account\_id}/dex/devices/{device\_id}/fleet-status/live

##### ModelsExpand Collapse

<details>

<summary>

FleetStatusGetResponse object {colo, deviceId, mode, 40 more }

</summary>

colo: string

Cloudflare colo airport code.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20colo">Link to this property</a>

deviceId: string

Device identifier (UUID v4)

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceId">Link to this property</a>

mode: string

The mode under which the WARP client is run.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

platform: string

Operating system.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20platform">Link to this property</a>

status: string

Network status.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

timestamp: string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20timestamp">Link to this property</a>

version: string

WARP client version.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

alwaysOn: optional boolean

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20alwaysOn">Link to this property</a>

batteryCharging: optional boolean

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20batteryCharging">Link to this property</a>

batteryCycles: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20batteryCycles">Link to this property</a>

batteryPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20batteryPct">Link to this property</a>

connectionType: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20connectionType">Link to this property</a>

cpuPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20cpuPct">Link to this property</a>

<details>

<summary>

cpuPctByApp: optional array of object {cpu\_pct, name }

</summary>

cpu\_pct: optional number

CPU usage percentage, on a scale of 0 to 100.

formatfloat

maximum100

minimum0

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20cpuPctByApp%20%3E%20(items)%20%3E%20(property)%20cpu_pct">Link to this property</a>

name: optional string

Application name.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20cpuPctByApp%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20cpuPctByApp">Link to this property</a>

<details>

<summary>

deviceIpv4: optional object {address, asn, aso, 4 more }

</summary>

address: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20address">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20aso">Link to this property</a>

<details>

<summary>

location: optional object {city, country\_iso, state\_iso, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

country\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20location%20%3E%20(property)%20country_iso">Link to this property</a>

state\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20location%20%3E%20(property)%20state_iso">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20location">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20name">Link to this property</a>

netmask: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20netmask">Link to this property</a>

version: optional number

IP version (<code>1</code> for IPv4, <code>2</code> for IPv6, <code>0</code> if unknown).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv4">Link to this property</a>

<details>

<summary>

deviceIpv6: optional object {address, asn, aso, 4 more }

</summary>

address: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20address">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20aso">Link to this property</a>

<details>

<summary>

location: optional object {city, country\_iso, state\_iso, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

country\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20location%20%3E%20(property)%20country_iso">Link to this property</a>

state\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20location%20%3E%20(property)%20state_iso">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20location">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20name">Link to this property</a>

netmask: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20netmask">Link to this property</a>

version: optional number

IP version (<code>1</code> for IPv4, <code>2</code> for IPv6, <code>0</code> if unknown).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceIpv6">Link to this property</a>

deviceName: optional string

Device identifier (human readable).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceName">Link to this property</a>

DeprecateddeviceRegistration: optional string

Use <code>registrationId</code> instead.

Deprecated: use registrationId. Device registration identifier (UUID).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20deviceRegistration">Link to this property</a>

diskReadBps: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20diskReadBps">Link to this property</a>

diskUsagePct: optional number

formatfloat

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20diskUsagePct">Link to this property</a>

diskWriteBps: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20diskWriteBps">Link to this property</a>

dohSubdomain: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20dohSubdomain">Link to this property</a>

estimatedLossPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20estimatedLossPct">Link to this property</a>

firewallEnabled: optional boolean

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20firewallEnabled">Link to this property</a>

<details>

<summary>

gatewayIpv4: optional object {address, asn, aso, 4 more }

</summary>

address: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20address">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20aso">Link to this property</a>

<details>

<summary>

location: optional object {city, country\_iso, state\_iso, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

country\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20location%20%3E%20(property)%20country_iso">Link to this property</a>

state\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20location%20%3E%20(property)%20state_iso">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20location">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20name">Link to this property</a>

netmask: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20netmask">Link to this property</a>

version: optional number

IP version (<code>1</code> for IPv4, <code>2</code> for IPv6, <code>0</code> if unknown).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv4">Link to this property</a>

<details>

<summary>

gatewayIpv6: optional object {address, asn, aso, 4 more }

</summary>

address: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20address">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20aso">Link to this property</a>

<details>

<summary>

location: optional object {city, country\_iso, state\_iso, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

country\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20location%20%3E%20(property)%20country_iso">Link to this property</a>

state\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20location%20%3E%20(property)%20state_iso">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20location">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20name">Link to this property</a>

netmask: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20netmask">Link to this property</a>

version: optional number

IP version (<code>1</code> for IPv4, <code>2</code> for IPv6, <code>0</code> if unknown).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20gatewayIpv6">Link to this property</a>

handshakeLatencyMs: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20handshakeLatencyMs">Link to this property</a>

<details>

<summary>

ispIpv4: optional object {address, asn, aso, 4 more }

</summary>

address: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20address">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20aso">Link to this property</a>

<details>

<summary>

location: optional object {city, country\_iso, state\_iso, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

country\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20location%20%3E%20(property)%20country_iso">Link to this property</a>

state\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20location%20%3E%20(property)%20state_iso">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20location">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20name">Link to this property</a>

netmask: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20netmask">Link to this property</a>

version: optional number

IP version (<code>1</code> for IPv4, <code>2</code> for IPv6, <code>0</code> if unknown).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv4">Link to this property</a>

<details>

<summary>

ispIpv6: optional object {address, asn, aso, 4 more }

</summary>

address: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20address">Link to this property</a>

asn: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20asn">Link to this property</a>

aso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20aso">Link to this property</a>

<details>

<summary>

location: optional object {city, country\_iso, state\_iso, zip }

</summary>

city: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20location%20%3E%20(property)%20city">Link to this property</a>

country\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20location%20%3E%20(property)%20country_iso">Link to this property</a>

state\_iso: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20location%20%3E%20(property)%20state_iso">Link to this property</a>

zip: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20location%20%3E%20(property)%20zip">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20location">Link to this property</a>

name: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20name">Link to this property</a>

netmask: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20netmask">Link to this property</a>

version: optional number

IP version (<code>1</code> for IPv4, <code>2</code> for IPv6, <code>0</code> if unknown).

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ispIpv6">Link to this property</a>

metal: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20metal">Link to this property</a>

networkRcvdBps: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20networkRcvdBps">Link to this property</a>

networkSentBps: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20networkSentBps">Link to this property</a>

networkSsid: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20networkSsid">Link to this property</a>

personEmail: optional string

User contact email address

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20personEmail">Link to this property</a>

ramAvailableKb: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ramAvailableKb">Link to this property</a>

ramUsedPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ramUsedPct">Link to this property</a>

<details>

<summary>

ramUsedPctByApp: optional array of object {name, ram\_used\_pct }

</summary>

name: optional string

Application name.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ramUsedPctByApp%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

ram\_used\_pct: optional number

RAM usage percentage, on a scale of 0 to 100.

formatfloat

maximum100

minimum0

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ramUsedPctByApp%20%3E%20(items)%20%3E%20(property)%20ram_used_pct">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20ramUsedPctByApp">Link to this property</a>

registrationId: optional string

Device registration identifier (UUID v4). On multi-user devices, this uniquely identifies a user’s registration on the device.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20registrationId">Link to this property</a>

<details>

<summary>

rtt: optional object {minRttUs, rttUs, rttVarUs }

Round-trip time statistics for the WARP tunnel.

</summary>

<details>

<summary>

minRttUs: optional object {downstream, upstream }

Minimum round-trip time in microseconds.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20minRttUs%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20minRttUs%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20minRttUs">Link to this property</a>

<details>

<summary>

rttUs: optional object {downstream, upstream }

Round-trip time in microseconds.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20rttUs%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20rttUs%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20rttUs">Link to this property</a>

<details>

<summary>

rttVarUs: optional object {downstream, upstream }

Round-trip time variance in microseconds.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20rttVarUs%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20rttVarUs%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt%20%3E%20(property)%20rttVarUs">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20rtt">Link to this property</a>

switchLocked: optional boolean

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20switchLocked">Link to this property</a>

<details>

<summary>

tunnelStats: optional object {bytesLost, bytesReceived, bytesRetransmitted, 6 more }

WARP tunnel packet and byte counters.

</summary>

<details>

<summary>

bytesLost: optional object {downstream, upstream }

Number of bytes lost, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesLost%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesLost%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesLost">Link to this property</a>

<details>

<summary>

bytesReceived: optional object {downstream, upstream }

Number of bytes received, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesReceived%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesReceived%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesReceived">Link to this property</a>

<details>

<summary>

bytesRetransmitted: optional object {downstream, upstream }

Number of bytes retransmitted, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesRetransmitted%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesRetransmitted%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesRetransmitted">Link to this property</a>

<details>

<summary>

bytesSent: optional object {downstream, upstream }

Number of bytes sent, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesSent%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesSent%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20bytesSent">Link to this property</a>

<details>

<summary>

packetsLost: optional object {downstream, upstream }

Number of packets lost, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsLost%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsLost%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsLost">Link to this property</a>

<details>

<summary>

packetsReceived: optional object {downstream, upstream }

Number of packets received, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsReceived%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsReceived%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsReceived">Link to this property</a>

<details>

<summary>

packetsRetransmitted: optional object {downstream, upstream }

Number of packets retransmitted, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsRetransmitted%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsRetransmitted%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsRetransmitted">Link to this property</a>

<details>

<summary>

packetsSent: optional object {downstream, upstream }

Number of packets sent, split by direction.

</summary>

downstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsSent%20%3E%20(property)%20downstream">Link to this property</a>

upstream: optional number

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsSent%20%3E%20(property)%20upstream">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20packetsSent">Link to this property</a>

statsWindowMs: optional number

The measurement window duration in milliseconds.

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats%20%3E%20(property)%20statsWindowMs">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelStats">Link to this property</a>

tunnelType: optional string

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20tunnelType">Link to this property</a>

wifiStrengthDbm: optional number

formatint64

<a href="#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)%20%3E%20(property)%20wifiStrengthDbm">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.fleet_status%20%3E%20(model)%20fleet_status_get_response%20%3E%20(schema)>)