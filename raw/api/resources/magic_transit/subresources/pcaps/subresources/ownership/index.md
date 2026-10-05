---
title: Ownership
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Transit](https://developers.cloudflare.com/api/resources/magic_transit)

[PCAPs](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Ownership

##### [List PCAPs Bucket Ownership](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/get)

GET/accounts/{account\_id}/pcaps/ownership

##### [Add buckets for full packet captures](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/create)

POST/accounts/{account\_id}/pcaps/ownership

##### [Delete buckets for full packet captures](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/delete)

DELETE/accounts/{account\_id}/pcaps/ownership/{ownership\_id}

##### [Validate buckets for full packet captures](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/validate)

POST/accounts/{account\_id}/pcaps/ownership/validate

##### ModelsExpand Collapse

<details>

<summary>

Ownership object {id, destination\_conf, filename, 3 more }

</summary>

id: string

The bucket ID associated with the packet captures API.

maxLength32

minLength32

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

destination\_conf: string

The full URI for the bucket. This field only applies to <code>full</code> packet captures.

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20destination_conf">Link to this property</a>

filename: string

The ownership challenge filename stored in the bucket.

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20filename">Link to this property</a>

<details>

<summary>

status: "pending"or "success"or "failed"

The status of the ownership challenge. Can be pending, success or failed.

</summary>

One of the following:

"pending"

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"success"

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

submitted: string

The RFC 3339 timestamp when the bucket was added to packet captures API.

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20submitted">Link to this property</a>

validated: optional string

The RFC 3339 timestamp when the bucket was validated.

<a href="#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)%20%3E%20(property)%20validated">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.pcaps.ownership%20%3E%20(model)%20ownership%20%3E%20(schema)>)