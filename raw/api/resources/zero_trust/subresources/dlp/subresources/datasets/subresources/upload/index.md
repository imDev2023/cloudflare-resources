---
title: Upload
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DLP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp)

[Datasets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Upload

##### [Prepare to upload a new version of a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/upload/methods/create)

POST/accounts/{account\_id}/dlp/datasets/{dataset\_id}/upload

##### [Upload a new version of a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/upload/methods/edit)

POST/accounts/{account\_id}/dlp/datasets/{dataset\_id}/upload/{version}

##### ModelsExpand Collapse

<details>

<summary>

NewVersion object {encoding\_version, max\_cells, version, 3 more }

</summary>

encoding\_version: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20encoding_version">Link to this property</a>

max\_cells: number

formatint64

minimum0

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20max_cells">Link to this property</a>

version: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

case\_sensitive: optional boolean

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20case_sensitive">Link to this property</a>

<details>

<summary>

columns: optional array of object {entry\_id, header\_name, num\_cells, upload\_status }

</summary>

entry\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20entry_id">Link to this property</a>

header\_name: string

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20header_name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

upload\_status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20columns">Link to this property</a>

secret: optional string

formatpassword

<a href="#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)%20%3E%20(property)%20secret">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.datasets.upload%20%3E%20(model)%20new_version%20%3E%20(schema)>)