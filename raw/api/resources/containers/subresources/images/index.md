---
title: Images
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Containers](https://developers.cloudflare.com/api/resources/containers)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Images

##### [Prepare a container image](https://developers.cloudflare.com/api/resources/containers/subresources/images/methods/prepare)

POST/accounts/{account\_id}/containers/image-preparations

##### ModelsExpand Collapse

<details>

<summary>

ImagePrepareResponse object {image, status, artifact\_digest, reason }

Durable preparation state for a container image.

</summary>

image: string

Image url.

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20image">Link to this property</a>

<details>

<summary>

status: "pending"or "ready"or "error"

Current durable preparation state for a container image.

</summary>

One of the following:

"pending"

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"error"

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

artifact\_digest: optional string

Digest of the prepared runtime artifact when status is ready.

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20artifact_digest">Link to this property</a>

reason: optional string

Human-readable pending or terminal error detail.

<a href="#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)%20%3E%20(property)%20reason">Link to this property</a>

</details>

[Link to this property](<#(resource)%20containers.images%20%3E%20(model)%20image_prepare_response%20%3E%20(schema)>)