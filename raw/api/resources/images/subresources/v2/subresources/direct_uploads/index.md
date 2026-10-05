---
title: Direct Uploads
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Images](https://developers.cloudflare.com/api/resources/images)

[V2](https://developers.cloudflare.com/api/resources/images/subresources/v2)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Direct Uploads

##### [Create authenticated direct upload URL V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/subresources/direct_uploads/methods/create)

POST/accounts/{account\_id}/images/v2/direct\_upload

##### ModelsExpand Collapse

<details>

<summary>

DirectUploadCreateResponse object {id, uploadURL }

</summary>

id: optional string

Image unique identifier.

maxLength32

<a href="#(resource)%20images.v2.direct_uploads%20%3E%20(model)%20direct_upload_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

uploadURL: optional string

The URL the unauthenticated upload can be performed to using a single HTTP POST (multipart/form-data) request.

<a href="#(resource)%20images.v2.direct_uploads%20%3E%20(model)%20direct_upload_create_response%20%3E%20(schema)%20%3E%20(property)%20uploadURL">Link to this property</a>

</details>

[Link to this property](<#(resource)%20images.v2.direct_uploads%20%3E%20(model)%20direct_upload_create_response%20%3E%20(schema)>)