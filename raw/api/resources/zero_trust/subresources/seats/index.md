---
title: Seats
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Seats

##### [Update a user seat](https://developers.cloudflare.com/api/resources/zero_trust/subresources/seats/methods/edit)

PATCH/accounts/{account\_id}/access/seats

##### ModelsExpand Collapse

<details>

<summary>

Seat object {access\_seat, created\_at, gateway\_seat, 2 more }

</summary>

access\_seat: optional boolean

True if the seat is part of Access.

<a href="#(resource)%20zero_trust.seats%20%3E%20(model)%20seat%20%3E%20(schema)%20%3E%20(property)%20access_seat">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.seats%20%3E%20(model)%20seat%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

gateway\_seat: optional boolean

True if the seat is part of Gateway.

<a href="#(resource)%20zero_trust.seats%20%3E%20(model)%20seat%20%3E%20(schema)%20%3E%20(property)%20gateway_seat">Link to this property</a>

seat\_uid: optional string

The unique API identifier for the Zero Trust seat.

maxLength36

<a href="#(resource)%20zero_trust.seats%20%3E%20(model)%20seat%20%3E%20(schema)%20%3E%20(property)%20seat_uid">Link to this property</a>

updated\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.seats%20%3E%20(model)%20seat%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.seats%20%3E%20(model)%20seat%20%3E%20(schema)>)