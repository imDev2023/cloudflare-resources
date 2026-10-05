---
title: Variants
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cache](https://developers.cloudflare.com/api/resources/cache)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Variants

##### [Get variants setting](https://developers.cloudflare.com/api/resources/cache/subresources/variants/methods/get)

GET/zones/{zone\_id}/cache/variants

##### [Change variants setting](https://developers.cloudflare.com/api/resources/cache/subresources/variants/methods/edit)

PATCH/zones/{zone\_id}/cache/variants

##### [Delete variants setting](https://developers.cloudflare.com/api/resources/cache/subresources/variants/methods/delete)

DELETE/zones/{zone\_id}/cache/variants

##### ModelsExpand Collapse

<details>

<summary>

VariantGetResponse object {id, editable, value, modified\_on }

</summary>

id: "variants"

The identifier of the caching setting.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: object {avif, bmp, gif, 8 more }

Value of the zone setting.

</summary>

avif: optional array of string

List of strings with the MIME types of all the variants that should be served for avif.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20avif">Link to this property</a>

bmp: optional array of string

List of strings with the MIME types of all the variants that should be served for bmp.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20bmp">Link to this property</a>

gif: optional array of string

List of strings with the MIME types of all the variants that should be served for gif.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20gif">Link to this property</a>

jp2: optional array of string

List of strings with the MIME types of all the variants that should be served for jp2.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jp2">Link to this property</a>

jpeg: optional array of string

List of strings with the MIME types of all the variants that should be served for jpeg.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jpeg">Link to this property</a>

jpg: optional array of string

List of strings with the MIME types of all the variants that should be served for jpg.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jpg">Link to this property</a>

jpg2: optional array of string

List of strings with the MIME types of all the variants that should be served for jpg2.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jpg2">Link to this property</a>

png: optional array of string

List of strings with the MIME types of all the variants that should be served for png.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20png">Link to this property</a>

tif: optional array of string

List of strings with the MIME types of all the variants that should be served for tif.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20tif">Link to this property</a>

tiff: optional array of string

List of strings with the MIME types of all the variants that should be served for tiff.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20tiff">Link to this property</a>

webp: optional array of string

List of strings with the MIME types of all the variants that should be served for webp.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20webp">Link to this property</a>

</details>

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)>)

<details>

<summary>

VariantEditResponse object {id, editable, value, modified\_on }

</summary>

id: "variants"

The identifier of the caching setting.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: object {avif, bmp, gif, 8 more }

Value of the zone setting.

</summary>

avif: optional array of string

List of strings with the MIME types of all the variants that should be served for avif.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20avif">Link to this property</a>

bmp: optional array of string

List of strings with the MIME types of all the variants that should be served for bmp.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20bmp">Link to this property</a>

gif: optional array of string

List of strings with the MIME types of all the variants that should be served for gif.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20gif">Link to this property</a>

jp2: optional array of string

List of strings with the MIME types of all the variants that should be served for jp2.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jp2">Link to this property</a>

jpeg: optional array of string

List of strings with the MIME types of all the variants that should be served for jpeg.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jpeg">Link to this property</a>

jpg: optional array of string

List of strings with the MIME types of all the variants that should be served for jpg.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jpg">Link to this property</a>

jpg2: optional array of string

List of strings with the MIME types of all the variants that should be served for jpg2.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20jpg2">Link to this property</a>

png: optional array of string

List of strings with the MIME types of all the variants that should be served for png.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20png">Link to this property</a>

tif: optional array of string

List of strings with the MIME types of all the variants that should be served for tif.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20tif">Link to this property</a>

tiff: optional array of string

List of strings with the MIME types of all the variants that should be served for tiff.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20tiff">Link to this property</a>

webp: optional array of string

List of strings with the MIME types of all the variants that should be served for webp.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(property)%20webp">Link to this property</a>

</details>

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)>)

<details>

<summary>

VariantDeleteResponse object {id, editable, modified\_on }

</summary>

id: "variants"

The identifier of the caching setting.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20cache.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cache.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)>)