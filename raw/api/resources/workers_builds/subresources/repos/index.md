---
title: Repos
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workers Builds](https://developers.cloudflare.com/api/resources/workers_builds)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Repos

#### ReposConnections

##### [Create or update a repository connection](https://developers.cloudflare.com/api/resources/workers_builds/subresources/repos/subresources/connections/methods/upsert)

PUT/accounts/{account\_id}/builds/repos/connections

##### [Delete a repository connection](https://developers.cloudflare.com/api/resources/workers_builds/subresources/repos/subresources/connections/methods/delete)

DELETE/accounts/{account\_id}/builds/repos/connections/{repo\_connection\_uuid}

##### ModelsExpand Collapse

<details>

<summary>

ConnectionUpsertResponse object {created\_on, deleted\_on, modified\_on, 6 more }

</summary>

created\_on: optional string

formatdate-time

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

deleted\_on: optional string

formatdate-time

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20deleted_on">Link to this property</a>

modified\_on: optional string

formatdate-time

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

provider\_account\_id: optional string

Provider-specific identifier of the account or namespace that owns the repository.

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_account_id">Link to this property</a>

provider\_account\_name: optional string

Human-readable name of the account or namespace that owns the repository.

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_account_name">Link to this property</a>

<details>

<summary>

provider\_type: optional "github"or "gitlab"or "gitlab\_internal"or "origin"

Source control provider.

</summary>

One of the following:

"github"

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_type%20%3E%20(member)%200">Link to this property</a>

"gitlab"

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_type%20%3E%20(member)%201">Link to this property</a>

"gitlab\_internal"

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_type%20%3E%20(member)%202">Link to this property</a>

"origin"

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20provider_type">Link to this property</a>

repo\_connection\_uuid: optional string

Repository connection UUID.

formatuuid

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20repo_connection_uuid">Link to this property</a>

repo\_id: optional string

Provider-specific repository identifier.

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20repo_id">Link to this property</a>

repo\_name: optional string

Human-readable repository name.

<a href="#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)%20%3E%20(property)%20repo_name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_upsert_response%20%3E%20(schema)>)

ConnectionDeleteResponse = unknown

[Link to this property](<#(resource)%20workers_builds.repos.connections%20%3E%20(model)%20connection_delete_response%20%3E%20(schema)>)

#### ReposConfig Autofill

##### [Get repository configuration autofill](https://developers.cloudflare.com/api/resources/workers_builds/subresources/repos/subresources/config_autofill/methods/get)

GET/accounts/{account\_id}/builds/repos/{provider\_type}/{provider\_account\_id}/{repo\_id}/config\_autofill

##### ModelsExpand Collapse

<details>

<summary>

ConfigAutofillGetResponse object {config\_file, default\_worker\_name, env\_worker\_names, 2 more }

</summary>

config\_file: optional string

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20config_file">Link to this property</a>

default\_worker\_name: optional string

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20default_worker_name">Link to this property</a>

env\_worker\_names: optional map\[string]

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20env_worker_names">Link to this property</a>

<details>

<summary>

package\_manager: optional "npm"or "yarn"or "pnpm"or 2 more

Package manager inferred from repository lockfiles; defaults to npm when none is detected.

</summary>

One of the following:

"npm"

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20package_manager%20%3E%20(member)%200">Link to this property</a>

"yarn"

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20package_manager%20%3E%20(member)%201">Link to this property</a>

"pnpm"

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20package_manager%20%3E%20(member)%202">Link to this property</a>

"bun"

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20package_manager%20%3E%20(member)%203">Link to this property</a>

"uv"

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20package_manager%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20package_manager">Link to this property</a>

scripts: optional map\[string]

<a href="#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)%20%3E%20(property)%20scripts">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers_builds.repos.config_autofill%20%3E%20(model)%20config_autofill_get_response%20%3E%20(schema)>)