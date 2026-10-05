---
title: Datasets
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DLP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Datasets

##### [Fetch all datasets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/list)

GET/accounts/{account\_id}/dlp/datasets

##### [Fetch a specific dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/get)

GET/accounts/{account\_id}/dlp/datasets/{dataset\_id}

##### [Create a new dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/create)

POST/accounts/{account\_id}/dlp/datasets

##### [Update details about a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/update)

PUT/accounts/{account\_id}/dlp/datasets/{dataset\_id}

##### [Delete a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/delete)

DELETE/accounts/{account\_id}/dlp/datasets/{dataset\_id}

##### ModelsExpand Collapse

<details>

<summary>

Dataset object {id, columns, created\_at, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

columns: array of object {entry\_id, header\_name, num\_cells, upload\_status }

</summary>

entry\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20entry_id">Link to this property</a>

header\_name: string

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20header_name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

upload\_status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

encoding\_version: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20encoding_version">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20num_cells">Link to this property</a>

secret: boolean

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20secret">Link to this property</a>

<details>

<summary>

status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

Stores when the dataset was last updated.

This includes name or description changes as well as uploads.

formatdate-time

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

<details>

<summary>

uploads: array of object {num\_cells, status, version }

</summary>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

version: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads">Link to this property</a>

case\_sensitive: optional boolean

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20case_sensitive">Link to this property</a>

description: optional string

The description of the dataset.

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)>)

<details>

<summary>

DatasetArray = array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)">Dataset</a> { id, columns, created\_at, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

columns: array of object {entry\_id, header\_name, num\_cells, upload\_status }

</summary>

entry\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20entry_id">Link to this property</a>

header\_name: string

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20header_name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

upload\_status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns%20%3E%20(items)%20%3E%20(property)%20upload_status">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20columns">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

encoding\_version: number

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20encoding_version">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20num_cells">Link to this property</a>

secret: boolean

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20secret">Link to this property</a>

<details>

<summary>

status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

Stores when the dataset was last updated.

This includes name or description changes as well as uploads.

formatdate-time

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

<details>

<summary>

uploads: array of object {num\_cells, status, version }

</summary>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

version: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads%20%3E%20(items)%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20uploads">Link to this property</a>

case\_sensitive: optional boolean

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20case_sensitive">Link to this property</a>

description: optional string

The description of the dataset.

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_array%20%3E%20(schema)>)

<details>

<summary>

DatasetCreation object {dataset, encoding\_version, max\_cells, 2 more }

</summary>

dataset: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)">Dataset</a> { id, columns, created\_at, 9 more }

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_creation%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

encoding\_version: number

Encoding version to use for dataset.

formatint32

minimum0

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_creation%20%3E%20(schema)%20%3E%20(property)%20encoding_version">Link to this property</a>

max\_cells: number

formatint64

minimum0

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_creation%20%3E%20(schema)%20%3E%20(property)%20max_cells">Link to this property</a>

version: number

The version to use when uploading the dataset.

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_creation%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

secret: optional string

The secret to use for Exact Data Match datasets.

This is not present in Custom Wordlists.

formatpassword

<a href="#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_creation%20%3E%20(schema)%20%3E%20(property)%20secret">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.datasets%20%3E%20(model)%20dataset_creation%20%3E%20(schema)>)

#### DatasetsUpload

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

#### DatasetsVersions

##### [Sets the column information for a multi-column upload](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/versions/methods/create)

POST/accounts/{account\_id}/dlp/datasets/{dataset\_id}/versions/{version}

##### ModelsExpand Collapse

<details>

<summary>

VersionCreateResponse object {entry\_id, header\_name, num\_cells, upload\_status }

</summary>

entry\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20entry_id">Link to this property</a>

header\_name: string

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20header_name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

upload\_status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.datasets.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)>)

#### DatasetsVersionsEntries

##### [Upload a new version of a multi-column dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/versions/subresources/entries/methods/create)

POST/accounts/{account\_id}/dlp/datasets/{dataset\_id}/versions/{version}/entries/{entry\_id}

##### ModelsExpand Collapse

<details>

<summary>

EntryCreateResponse object {entry\_id, header\_name, num\_cells, upload\_status }

</summary>

entry\_id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20entry_id">Link to this property</a>

header\_name: string

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20header_name">Link to this property</a>

num\_cells: number

formatint64

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20num_cells">Link to this property</a>

<details>

<summary>

upload\_status: "empty"or "uploading"or "pending"or 3 more

</summary>

One of the following:

"empty"

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%200">Link to this property</a>

"uploading"

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%201">Link to this property</a>

"pending"

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%202">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%203">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)%20%3E%20(property)%20upload_status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.datasets.versions.entries%20%3E%20(model)%20entry_create_response%20%3E%20(schema)>)