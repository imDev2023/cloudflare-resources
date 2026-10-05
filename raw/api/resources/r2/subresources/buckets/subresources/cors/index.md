---
title: CORS
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[R2](https://developers.cloudflare.com/api/resources/r2)

[Buckets](https://developers.cloudflare.com/api/resources/r2/subresources/buckets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# CORS

##### [Get Bucket CORS Policy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/cors/methods/get)

GET/accounts/{account\_id}/r2/buckets/{bucket\_name}/cors

##### [Set Bucket CORS Policy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/cors/methods/update)

PUT/accounts/{account\_id}/r2/buckets/{bucket\_name}/cors

##### [Delete Bucket CORS Policy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/cors/methods/delete)

DELETE/accounts/{account\_id}/r2/buckets/{bucket\_name}/cors

##### ModelsExpand Collapse

<details>

<summary>

CORSGetResponse object {rules }

</summary>

<details>

<summary>

rules: optional array of object {allowed, id, exposeHeaders, maxAgeSeconds }

</summary>

<details>

<summary>

allowed: object {methods, origins, headers }

Object specifying allowed origins, methods and headers for this CORS rule.

</summary>

<details>

<summary>

methods: array of "GET"or "PUT"or "POST"or 2 more

Specifies the value for the Access-Control-Allow-Methods header R2 sets when requesting objects in a bucket from a browser.

</summary>

One of the following:

"GET"

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20methods%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"PUT"

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20methods%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"POST"

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20methods%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"DELETE"

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20methods%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"HEAD"

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20methods%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20methods">Link to this property</a>

origins: array of string

Specifies the value for the Access-Control-Allow-Origin header R2 sets when requesting objects in a bucket from a browser.

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20origins">Link to this property</a>

headers: optional array of string

Specifies the value for the Access-Control-Allow-Headers header R2 sets when requesting objects in this bucket from a browser. Cross-origin requests that include custom headers (e.g. x-user-id) should specify these headers as AllowedHeaders.

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allowed">Link to this property</a>

id: optional string

Identifier for this rule.

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

exposeHeaders: optional array of string

Specifies the headers that can be exposed back, and accessed by, the JavaScript making the cross-origin request. If you need to access headers beyond the safelisted response headers, such as Content-Encoding or cf-cache-status, you must specify it here.

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20exposeHeaders">Link to this property</a>

maxAgeSeconds: optional number

Specifies the amount of time (in seconds) browsers are allowed to cache CORS preflight responses. Browsers may limit this to 2 hours or less, even if the maximum value (86400) is specified.

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20maxAgeSeconds">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)%20%3E%20(property)%20rules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_get_response%20%3E%20(schema)>)

CORSUpdateResponse = unknown

[Link to this property](<#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_update_response%20%3E%20(schema)>)

CORSDeleteResponse = unknown

[Link to this property](<#(resource)%20r2.buckets.cors%20%3E%20(model)%20cors_delete_response%20%3E%20(schema)>)