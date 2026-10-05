---
title: Transformations Allowed Origins
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zones](https://developers.cloudflare.com/api/resources/zones)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Transformations Allowed Origins

##### [Get Image Transformations Allowed Origins setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_allowed_origins/methods/get)

GET/zones/{zone\_id}/settings/transformations\_allowed\_origins

##### [Change Image Transformations Allowed Origins setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_allowed_origins/methods/edit)

PATCH/zones/{zone\_id}/settings/transformations\_allowed\_origins

##### ModelsExpand Collapse

<details>

<summary>

TransformationsAllowedOrigins object {id, editable, modified\_on, value }

Controls which origins are allowed to request image and video transformations.

</summary>

id: optional "image\_resizing\_allowed\_origins"

ID of the zone setting.

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

editable: optional trueor false

Whether or not this setting can be modified for this zone (based on your Cloudflare plan level).

</summary>

One of the following:

true

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20editable%20%3E%20(member)%200">Link to this property</a>

false

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20editable%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: optional string

last time this setting was modified.

formatdate-time

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

value: optional "on"or "off"

Comma-separated list of allowed origin domains for image and video transformations. Use ”\*” to allow all origins (default).

</summary>

One of the following:

"on"

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zones.transformations_allowed_origins%20%3E%20(model)%20transformations_allowed_origins%20%3E%20(schema)>)