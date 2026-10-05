---
title: Sippy
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[R2](https://developers.cloudflare.com/api/resources/r2)

[Buckets](https://developers.cloudflare.com/api/resources/r2/subresources/buckets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Sippy

##### [Get Sippy Configuration](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/sippy/methods/get)

GET/accounts/{account\_id}/r2/buckets/{bucket\_name}/sippy

##### [Enable Sippy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/sippy/methods/update)

PUT/accounts/{account\_id}/r2/buckets/{bucket\_name}/sippy

##### [Disable Sippy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/sippy/methods/delete)

DELETE/accounts/{account\_id}/r2/buckets/{bucket\_name}/sippy

##### ModelsExpand Collapse

Provider = "r2"

[Link to this property](<#(resource)%20r2.buckets.sippy%20%3E%20(model)%20provider%20%3E%20(schema)>)

<details>

<summary>

Sippy object {destination, enabled, source }

</summary>

<details>

<summary>

destination: optional object {accessKeyId, account, bucket, provider }

Details about the configured destination bucket.

</summary>

accessKeyId: optional string

ID of the Cloudflare API token used when writing objects to this bucket.

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20accessKeyId">Link to this property</a>

account: optional string

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20account">Link to this property</a>

bucket: optional string

Name of the bucket on the provider.

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20bucket">Link to this property</a>

provider: optional <a href="https://developers.cloudflare.com/api/resources/r2#(resource)%20r2.buckets.sippy%20%3E%20(model)%20provider%20%3E%20(schema)">Provider</a>

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20provider">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

enabled: optional boolean

State of Sippy for this bucket.

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

source: optional object {bucket, bucketUrl, container, 2 more }

Details about the configured source bucket.

</summary>

bucket: optional string

Name of the bucket on the provider (AWS, GCS only).

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20bucket">Link to this property</a>

bucketUrl: optional string

S3-compatible URL (Generic S3-compatible providers only).

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20bucketUrl">Link to this property</a>

container: optional string

Name of the Azure Blob Storage container (Azure only).

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20container">Link to this property</a>

<details>

<summary>

provider: optional "aws"or "gcs"or "s3"or "azure"

</summary>

One of the following:

"aws"

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20provider%20%3E%20(member)%200">Link to this property</a>

"gcs"

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20provider%20%3E%20(member)%201">Link to this property</a>

"s3"

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20provider%20%3E%20(member)%202">Link to this property</a>

"azure"

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20provider%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20provider">Link to this property</a>

region: optional string

Region where the bucket resides (AWS only).

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy%20%3E%20(schema)>)

<details>

<summary>

SippyDeleteResponse object {enabled }

</summary>

enabled: optional false

<a href="#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.buckets.sippy%20%3E%20(model)%20sippy_delete_response%20%3E%20(schema)>)