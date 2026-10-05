---
title: Settings
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zones](https://developers.cloudflare.com/api/resources/zones)

[Observability](https://developers.cloudflare.com/api/resources/zones/subresources/observability)

[Tracing](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Settings

##### [View zone tracing settings](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/settings/methods/get)

GET/zones/{zone\_id}/observability/tracing/settings

##### [Update zone tracing settings](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/settings/methods/update)

PATCH/zones/{zone\_id}/observability/tracing/settings

##### [Reset zone tracing settings](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/settings/methods/delete)

DELETE/zones/{zone\_id}/observability/tracing/settings

##### ModelsExpand Collapse

<details>

<summary>

SettingGetResponse object {destinations, enabled, forward\_context, 3 more }

</summary>

destinations: array of string

Up to 100 OpenTelemetry destination identifiers that receive traces.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20destinations">Link to this property</a>

enabled: boolean

Whether Cloudflare Traces is enabled for the zone.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

forward\_context: boolean

Whether trace context is sent externally or across a zone boundary.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20forward_context">Link to this property</a>

persist: boolean

Whether traces are persisted in Cloudflare.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: "accept"or "authenticated"or "reject"

When inbound trace context may be continued. Authenticated propagation is not supported yet.

</summary>

One of the following:

"accept"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"authenticated"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

"reject"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy">Link to this property</a>

sampling\_ratio: number

The ratio of requests sampled for tracing, from 0 to 1.

maximum1

minimum0

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)%20%3E%20(property)%20sampling_ratio">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_get_response%20%3E%20(schema)>)

<details>

<summary>

SettingUpdateResponse object {destinations, enabled, forward\_context, 3 more }

</summary>

destinations: array of string

Up to 100 OpenTelemetry destination identifiers that receive traces.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20destinations">Link to this property</a>

enabled: boolean

Whether Cloudflare Traces is enabled for the zone.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

forward\_context: boolean

Whether trace context is sent externally or across a zone boundary.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20forward_context">Link to this property</a>

persist: boolean

Whether traces are persisted in Cloudflare.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: "accept"or "authenticated"or "reject"

When inbound trace context may be continued. Authenticated propagation is not supported yet.

</summary>

One of the following:

"accept"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"authenticated"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

"reject"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy">Link to this property</a>

sampling\_ratio: number

The ratio of requests sampled for tracing, from 0 to 1.

maximum1

minimum0

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)%20%3E%20(property)%20sampling_ratio">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_update_response%20%3E%20(schema)>)

<details>

<summary>

SettingDeleteResponse object {destinations, enabled, forward\_context, 3 more }

</summary>

destinations: array of string

Up to 100 OpenTelemetry destination identifiers that receive traces.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20destinations">Link to this property</a>

enabled: boolean

Whether Cloudflare Traces is enabled for the zone.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

forward\_context: boolean

Whether trace context is sent externally or across a zone boundary.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20forward_context">Link to this property</a>

persist: boolean

Whether traces are persisted in Cloudflare.

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: "accept"or "authenticated"or "reject"

When inbound trace context may be continued. Authenticated propagation is not supported yet.

</summary>

One of the following:

"accept"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"authenticated"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

"reject"

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20propagation_policy">Link to this property</a>

sampling\_ratio: number

The ratio of requests sampled for tracing, from 0 to 1.

maximum1

minimum0

<a href="#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)%20%3E%20(property)%20sampling_ratio">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zones.observability.tracing.settings%20%3E%20(model)%20setting_delete_response%20%3E%20(schema)>)