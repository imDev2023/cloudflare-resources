---
title: Routes
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Transit](https://developers.cloudflare.com/api/resources/magic_transit)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Routes

##### [List Routes](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/list)

GET/accounts/{account\_id}/magic/routes

##### [Route Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/get)

GET/accounts/{account\_id}/magic/routes/{route\_id}

##### [Create a Route](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/create)

POST/accounts/{account\_id}/magic/routes

##### [Update Route](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/update)

PUT/accounts/{account\_id}/magic/routes/{route\_id}

##### [Delete Route](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/delete)

DELETE/accounts/{account\_id}/magic/routes/{route\_id}

##### [Update Many Routes](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/bulk_update)

PUT/accounts/{account\_id}/magic/routes

##### [Delete Many Routes](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/empty)

DELETE/accounts/{account\_id}/magic/routes

##### ModelsExpand Collapse

<details>

<summary>

Scope object {colo\_names, colo\_regions }

Used only for ECMP routes.

</summary>

colo\_names: optional array of string

List of colo names for the ECMP scope.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)%20%3E%20(property)%20colo_names">Link to this property</a>

colo\_regions: optional array of string

List of colo regions for the ECMP scope.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)%20%3E%20(property)%20colo_regions">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)>)

<details>

<summary>

RouteListResponse object {routes }

</summary>

<details>

<summary>

routes: optional array of object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)%20%3E%20(property)%20routes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_list_response%20%3E%20(schema)>)

<details>

<summary>

RouteGetResponse object {route }

</summary>

<details>

<summary>

route: optional object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)%20%3E%20(property)%20route">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_get_response%20%3E%20(schema)>)

<details>

<summary>

RouteCreateResponse object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)%20%3E%20(property)%20weight">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_create_response%20%3E%20(schema)>)

<details>

<summary>

RouteUpdateResponse object {modified, modified\_route }

</summary>

modified: optional boolean

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

modified\_route: optional object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_route">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_update_response%20%3E%20(schema)>)

<details>

<summary>

RouteDeleteResponse object {deleted, deleted\_route }

</summary>

deleted: optional boolean

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted">Link to this property</a>

<details>

<summary>

deleted\_route: optional object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)%20%3E%20(property)%20deleted_route">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_delete_response%20%3E%20(schema)>)

<details>

<summary>

RouteBulkUpdateResponse object {modified, modified\_routes }

</summary>

modified: optional boolean

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

<details>

<summary>

modified\_routes: optional array of object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes%20%3E%20(items)%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_routes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_bulk_update_response%20%3E%20(schema)>)

<details>

<summary>

RouteEmptyResponse object {deleted, deleted\_routes }

</summary>

deleted: optional boolean

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted">Link to this property</a>

<details>

<summary>

deleted\_routes: optional array of object {id, nexthop, prefix, 6 more }

</summary>

id: string

Identifier

maxLength32

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

nexthop: string

The next-hop IP Address for the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20nexthop">Link to this property</a>

prefix: string

IP Prefix in Classless Inter-Domain Routing format.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20prefix">Link to this property</a>

priority: number

Priority of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

created\_on: optional string

When the route was created.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

description: optional string

An optional human provided description of the static route.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

modified\_on: optional string

When the route was last modified.

formatdate-time

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

scope: optional <a href="https://developers.cloudflare.com/api/resources/magic_transit#(resource)%20magic_transit.routes%20%3E%20(model)%20scope%20%3E%20(schema)">Scope</a> { colo\_names, colo\_regions }

Used only for ECMP routes.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

weight: optional number

Optional weight of the ECMP scope - if provided.

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes%20%3E%20(items)%20%3E%20(property)%20weight">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)%20%3E%20(property)%20deleted_routes">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.routes%20%3E%20(model)%20route_empty_response%20%3E%20(schema)>)