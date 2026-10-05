---
title: Variants
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Images](https://developers.cloudflare.com/api/resources/images)

[V1](https://developers.cloudflare.com/api/resources/images/subresources/v1)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Variants

##### [List variants](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/list)

GET/accounts/{account\_id}/images/v1/variants

##### [Variant details](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/get)

GET/accounts/{account\_id}/images/v1/variants/{variant\_id}

##### [Create a variant](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/create)

POST/accounts/{account\_id}/images/v1/variants

##### [Update a variant](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit)

PATCH/accounts/{account\_id}/images/v1/variants/{variant\_id}

##### [Delete a variant](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/delete)

DELETE/accounts/{account\_id}/images/v1/variants/{variant\_id}

##### ModelsExpand Collapse

<details>

<summary>

Variant object {variants }

</summary>

<details>

<summary>

variants: optional object {hero }

</summary>

<details>

<summary>

hero: optional object {id, options, neverRequireSignedURLs }

</summary>

id: string

maxLength99

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

options: object {fit, height, metadata, width }

Allows you to define image resizing sizes for different use cases.

</summary>

<details>

<summary>

fit: "scale-down"or "contain"or "cover"or 2 more

The fit property describes how the width and height dimensions should be interpreted.

</summary>

One of the following:

"scale-down"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%200">Link to this property</a>

"contain"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%201">Link to this property</a>

"cover"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%202">Link to this property</a>

"crop"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%203">Link to this property</a>

"pad"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20fit">Link to this property</a>

height: number

Maximum height in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20height">Link to this property</a>

<details>

<summary>

metadata: "keep"or "copyright"or "none"

What EXIF data should be preserved in the output image.

</summary>

One of the following:

"keep"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%200">Link to this property</a>

"copyright"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20metadata">Link to this property</a>

width: number

Maximum width in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options%20%3E%20(property)%20width">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20options">Link to this property</a>

neverRequireSignedURLs: optional boolean

Indicates whether the variant can access an image without a signature, regardless of image access control.

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero%20%3E%20(property)%20neverRequireSignedURLs">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants%20%3E%20(property)%20hero">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)%20%3E%20(property)%20variants">Link to this property</a>

</details>

[Link to this property](<#(resource)%20images.v1.variants%20%3E%20(model)%20variant%20%3E%20(schema)>)

<details>

<summary>

VariantGetResponse object {variant }

</summary>

<details>

<summary>

variant: optional object {id, options, neverRequireSignedURLs }

</summary>

id: string

maxLength99

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

options: object {fit, height, metadata, width }

Allows you to define image resizing sizes for different use cases.

</summary>

<details>

<summary>

fit: "scale-down"or "contain"or "cover"or 2 more

The fit property describes how the width and height dimensions should be interpreted.

</summary>

One of the following:

"scale-down"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%200">Link to this property</a>

"contain"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%201">Link to this property</a>

"cover"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%202">Link to this property</a>

"crop"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%203">Link to this property</a>

"pad"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit">Link to this property</a>

height: number

Maximum height in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20height">Link to this property</a>

<details>

<summary>

metadata: "keep"or "copyright"or "none"

What EXIF data should be preserved in the output image.

</summary>

One of the following:

"keep"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%200">Link to this property</a>

"copyright"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata">Link to this property</a>

width: number

Maximum width in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20width">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options">Link to this property</a>

neverRequireSignedURLs: optional boolean

Indicates whether the variant can access an image without a signature, regardless of image access control.

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20neverRequireSignedURLs">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)%20%3E%20(property)%20variant">Link to this property</a>

</details>

[Link to this property](<#(resource)%20images.v1.variants%20%3E%20(model)%20variant_get_response%20%3E%20(schema)>)

<details>

<summary>

VariantCreateResponse object {variant }

</summary>

<details>

<summary>

variant: optional object {id, options, neverRequireSignedURLs }

</summary>

id: string

maxLength99

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

options: object {fit, height, metadata, width }

Allows you to define image resizing sizes for different use cases.

</summary>

<details>

<summary>

fit: "scale-down"or "contain"or "cover"or 2 more

The fit property describes how the width and height dimensions should be interpreted.

</summary>

One of the following:

"scale-down"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%200">Link to this property</a>

"contain"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%201">Link to this property</a>

"cover"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%202">Link to this property</a>

"crop"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%203">Link to this property</a>

"pad"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit">Link to this property</a>

height: number

Maximum height in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20height">Link to this property</a>

<details>

<summary>

metadata: "keep"or "copyright"or "none"

What EXIF data should be preserved in the output image.

</summary>

One of the following:

"keep"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%200">Link to this property</a>

"copyright"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata">Link to this property</a>

width: number

Maximum width in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20width">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options">Link to this property</a>

neverRequireSignedURLs: optional boolean

Indicates whether the variant can access an image without a signature, regardless of image access control.

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20neverRequireSignedURLs">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)%20%3E%20(property)%20variant">Link to this property</a>

</details>

[Link to this property](<#(resource)%20images.v1.variants%20%3E%20(model)%20variant_create_response%20%3E%20(schema)>)

<details>

<summary>

VariantEditResponse object {variant }

</summary>

<details>

<summary>

variant: optional object {id, options, neverRequireSignedURLs }

</summary>

id: string

maxLength99

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

options: object {fit, height, metadata, width }

Allows you to define image resizing sizes for different use cases.

</summary>

<details>

<summary>

fit: "scale-down"or "contain"or "cover"or 2 more

The fit property describes how the width and height dimensions should be interpreted.

</summary>

One of the following:

"scale-down"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%200">Link to this property</a>

"contain"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%201">Link to this property</a>

"cover"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%202">Link to this property</a>

"crop"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%203">Link to this property</a>

"pad"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20fit">Link to this property</a>

height: number

Maximum height in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20height">Link to this property</a>

<details>

<summary>

metadata: "keep"or "copyright"or "none"

What EXIF data should be preserved in the output image.

</summary>

One of the following:

"keep"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%200">Link to this property</a>

"copyright"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20metadata">Link to this property</a>

width: number

Maximum width in image pixels.

minimum1

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options%20%3E%20(property)%20width">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20options">Link to this property</a>

neverRequireSignedURLs: optional boolean

Indicates whether the variant can access an image without a signature, regardless of image access control.

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant%20%3E%20(property)%20neverRequireSignedURLs">Link to this property</a>

</details>

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)%20%3E%20(property)%20variant">Link to this property</a>

</details>

[Link to this property](<#(resource)%20images.v1.variants%20%3E%20(model)%20variant_edit_response%20%3E%20(schema)>)

<details>

<summary>

VariantDeleteResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20images.v1.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20images.v1.variants%20%3E%20(model)%20variant_delete_response%20%3E%20(schema)>)