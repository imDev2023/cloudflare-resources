---
title: Entries
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DLP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp)

[Datasets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets)

[Versions](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/versions)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Entries

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