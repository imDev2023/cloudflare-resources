---
title: Projects
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Pages](https://developers.cloudflare.com/api/resources/pages)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Projects

##### [List Cloudflare Pages projects](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/list)

GET/accounts/{account\_id}/pages/projects

##### [Get a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/get)

GET/accounts/{account\_id}/pages/projects/{project\_name}

##### [Get upload token](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/get_upload_token)

GET/accounts/{account\_id}/pages/projects/{project\_name}/upload-token

##### [Create a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/create)

POST/accounts/{account\_id}/pages/projects

##### [Update a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/edit)

PATCH/accounts/{account\_id}/pages/projects/{project\_name}

##### [Delete a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/delete)

DELETE/accounts/{account\_id}/pages/projects/{project\_name}

##### [Purge the Pages build cache](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/purge_build_cache)

POST/accounts/{account\_id}/pages/projects/{project\_name}/purge\_build\_cache

##### ModelsExpand Collapse

<details>

<summary>

Deployment object {id, aliases, build\_config, 15 more }

</summary>

id: string

Id of the deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

aliases: array of string

A list of alias URLs pointing to this deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20aliases">Link to this property</a>

<details>

<summary>

build\_config: object {web\_analytics\_tag, web\_analytics\_token, build\_caching, 3 more }

Configs for the project build process.

</summary>

web\_analytics\_tag: string

The classifying tag for analytics.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20web_analytics_tag">Link to this property</a>

web\_analytics\_token: string

The auth token for analytics.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20web_analytics_token">Link to this property</a>

build\_caching: optional boolean

Enable build caching for the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20build_caching">Link to this property</a>

build\_command: optional string

Command used to build project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20build_command">Link to this property</a>

destination\_dir: optional string

Assets output directory of the build.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20destination_dir">Link to this property</a>

root\_dir: optional string

Directory to run the command.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20root_dir">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20build_config">Link to this property</a>

created\_on: string

When the deployment was created.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

<details>

<summary>

deployment\_trigger: object {metadata, type }

Info about what caused the deployment.

</summary>

<details>

<summary>

metadata: object {branch, commit\_dirty, commit\_hash, commit\_message }

Additional info about the trigger.

</summary>

branch: string

Where the trigger happened.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20metadata%20%3E%20(property)%20branch">Link to this property</a>

commit\_dirty: boolean

Whether the deployment trigger commit was dirty.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20metadata%20%3E%20(property)%20commit_dirty">Link to this property</a>

commit\_hash: string

Hash of the deployment trigger commit.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20metadata%20%3E%20(property)%20commit_hash">Link to this property</a>

commit\_message: string

Message of the deployment trigger commit.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20metadata%20%3E%20(property)%20commit_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20metadata">Link to this property</a>

<details>

<summary>

type: "github:push"or "ad\_hoc"or "deploy\_hook"

What caused the deployment.

</summary>

One of the following:

"github:push"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"ad\_hoc"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"deploy\_hook"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20deployment_trigger">Link to this property</a>

<details>

<summary>

env\_vars: map\[object {type, value } or object {type, value } ]

Environment variables used for builds and Pages Functions.

</summary>

One of the following:

<details>

<summary>

PlainText object {type, value }

A plaintext environment variable.

</summary>

type: "plain\_text"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

value: string

Environment variable value.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretText object {type, value }

An encrypted environment variable.

</summary>

type: "secret\_text"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

Secret value.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20env_vars">Link to this property</a>

<details>

<summary>

environment: "preview"or "production"

Type of deploy.

</summary>

One of the following:

"preview"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20environment%20%3E%20(member)%200">Link to this property</a>

"production"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20environment%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

is\_skipped: boolean

Whether the deployment was skipped.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20is_skipped">Link to this property</a>

latest\_stage: <a href="https://developers.cloudflare.com/api/resources/pages#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)">Stage</a> { ended\_on, name, started\_on, status }

The status of the deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20latest_stage">Link to this property</a>

modified\_on: string

When the deployment was last modified.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

project\_id: string

Id of the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20project_id">Link to this property</a>

project\_name: string

Name of the Pages project. Must begin with a lowercase letter or digit and contain only lowercase letters, digits, and hyphens.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20project_name">Link to this property</a>

short\_id: string

Short Id (8 character) of the deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20short_id">Link to this property</a>

<details>

<summary>

source: object {config, type }

Configs for the project source control.

</summary>

<details>

<summary>

config: object {deployments\_enabled, owner, owner\_id, 10 more }

</summary>

Deprecateddeployments\_enabled: boolean

Use <code>production_deployments_enabled</code> and <code>preview_deployment_setting</code> for more granular control.

Whether to enable automatic deployments when pushing to the source repository. When disabled, no deployments (production or preview) will be triggered automatically.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20deployments_enabled">Link to this property</a>

owner: string

The owner of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20owner">Link to this property</a>

owner\_id: string

The owner ID of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20owner_id">Link to this property</a>

path\_excludes: array of string

A list of paths that should be excluded from triggering a preview deployment. Wildcard syntax (<code>*</code>) is supported.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20path_excludes">Link to this property</a>

path\_includes: array of string

A list of paths that should be watched to trigger a preview deployment. Wildcard syntax (<code>*</code>) is supported.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20path_includes">Link to this property</a>

pr\_comments\_enabled: boolean

Whether to enable PR comments.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20pr_comments_enabled">Link to this property</a>

preview\_branch\_excludes: array of string

A list of branches that should not trigger a preview deployment. Wildcard syntax (<code>*</code>) is supported. Must be used with <code>preview_deployment_setting</code> set to <code>custom</code>.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_branch_excludes">Link to this property</a>

preview\_branch\_includes: array of string

A list of branches that should trigger a preview deployment. Wildcard syntax (<code>*</code>) is supported. Must be used with <code>preview_deployment_setting</code> set to <code>custom</code>.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_branch_includes">Link to this property</a>

<details>

<summary>

preview\_deployment\_setting: "all"or "none"or "custom"

Controls whether commits to preview branches trigger a preview deployment.

</summary>

One of the following:

"all"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting%20%3E%20(member)%200">Link to this property</a>

"none"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting%20%3E%20(member)%201">Link to this property</a>

"custom"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting">Link to this property</a>

production\_branch: string

The production branch of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20production_branch">Link to this property</a>

production\_deployments\_enabled: boolean

Whether to trigger a production deployment on commits to the production branch.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20production_deployments_enabled">Link to this property</a>

repo\_id: string

The ID of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20repo_id">Link to this property</a>

repo\_name: string

The name of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20repo_name">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config">Link to this property</a>

<details>

<summary>

type: "github"or "gitlab"

The source control management provider.

</summary>

One of the following:

"github"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"gitlab"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

stages: array of <a href="https://developers.cloudflare.com/api/resources/pages#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)">Stage</a> { ended\_on, name, started\_on, status }

List of past stages.

</summary>

ended\_on: string

When the stage ended.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20ended_on">Link to this property</a>

<details>

<summary>

name: "queued"or "initialize"or "clone\_repo"or 2 more

The current build stage.

</summary>

One of the following:

"queued"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%200">Link to this property</a>

"initialize"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%201">Link to this property</a>

"clone\_repo"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%202">Link to this property</a>

"build"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%203">Link to this property</a>

"deploy"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

started\_on: string

When the stage started.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20started_on">Link to this property</a>

<details>

<summary>

status: "success"or "idle"or "active"or 3 more

State of the current stage.

</summary>

One of the following:

"success"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"idle"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failure"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"canceled"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"skipped"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20stages">Link to this property</a>

url: string

The live URL to view this deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

<details>

<summary>

skip\_reason: optional "commit\_message"or "preview\_deployments\_disabled"or "production\_deployments\_disabled"or 4 more

Why the deployment was skipped.

</summary>

One of the following:

"commit\_message"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%200">Link to this property</a>

"preview\_deployments\_disabled"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%201">Link to this property</a>

"production\_deployments\_disabled"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%202">Link to this property</a>

"path\_config"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%203">Link to this property</a>

"branch\_config"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%204">Link to this property</a>

"pages\_to\_workers\_conversion"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%205">Link to this property</a>

"superseded\_queued\_build"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20skip_reason">Link to this property</a>

uses\_functions: optional boolean

Whether the deployment uses functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20uses_functions">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)>)

<details>

<summary>

Project object {id, canonical\_deployment, created\_on, 13 more }

</summary>

id: string

ID of the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

canonical\_deployment: <a href="https://developers.cloudflare.com/api/resources/pages#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)">Deployment</a> { id, aliases, build\_config, 15 more }

Most recent production deployment of the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20canonical_deployment">Link to this property</a>

created\_on: string

When the project was created.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

<details>

<summary>

deployment\_configs: object {preview, production }

Configs for deployments in a project.

</summary>

<details>

<summary>

preview: object {always\_use\_latest\_compatibility\_date, build\_image\_major\_version, compatibility\_date, 19 more }

Configs for preview deploys.

</summary>

always\_use\_latest\_compatibility\_date: boolean

Whether to always use the latest compatibility date for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20always_use_latest_compatibility_date">Link to this property</a>

build\_image\_major\_version: number

The major version of the build image to use for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20build_image_major_version">Link to this property</a>

compatibility\_date: string

Compatibility date used for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: array of string

Compatibility flags used for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20compatibility_flags">Link to this property</a>

<details>

<summary>

env\_vars: map\[object {type, value } or object {type, value } ]

Environment variables used for builds and Pages Functions.

</summary>

One of the following:

<details>

<summary>

PlainText object {type, value }

A plaintext environment variable.

</summary>

type: "plain\_text"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

value: string

Environment variable value.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretText object {type, value }

An encrypted environment variable.

</summary>

type: "secret\_text"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

Secret value.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20env_vars">Link to this property</a>

fail\_open: boolean

Whether to fail open when the deployment config cannot be applied.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20fail_open">Link to this property</a>

<details>

<summary>

Deprecatedusage\_model: "standard"or "bundled"or "unbound"

All new projects now use the Standard usage model.

The usage model for Pages Functions.

</summary>

One of the following:

"standard"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20usage_model">Link to this property</a>

<details>

<summary>

ai\_bindings: optional map\[object {project\_id } ]

Constellation bindings used for Pages Functions.

</summary>

project\_id: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20ai_bindings%20%3E%20(items)%20%3E%20(property)%20project_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20ai_bindings">Link to this property</a>

<details>

<summary>

analytics\_engine\_datasets: optional map\[object {dataset } ]

Analytics Engine bindings used for Pages Functions.

</summary>

dataset: string

Name of the dataset.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20analytics_engine_datasets%20%3E%20(items)%20%3E%20(property)%20dataset">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20analytics_engine_datasets">Link to this property</a>

browsers: optional map\[object {} ]

Browser bindings used for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20browsers">Link to this property</a>

<details>

<summary>

d1\_databases: optional map\[object {id } ]

D1 databases used for Pages Functions.

</summary>

id: string

UUID of the D1 database.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20d1_databases%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20d1_databases">Link to this property</a>

<details>

<summary>

durable\_object\_namespaces: optional map\[object {namespace\_id } ]

Durable Object namespaces used for Pages Functions.

</summary>

namespace\_id: string

ID of the Durable Object namespace.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20durable_object_namespaces%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20durable_object_namespaces">Link to this property</a>

<details>

<summary>

hyperdrive\_bindings: optional map\[object {id } ]

Hyperdrive bindings used for Pages Functions.

</summary>

id: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20hyperdrive_bindings%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20hyperdrive_bindings">Link to this property</a>

<details>

<summary>

kv\_namespaces: optional map\[object {namespace\_id } ]

KV namespaces used for Pages Functions.

</summary>

namespace\_id: string

ID of the KV namespace.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20kv_namespaces%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20kv_namespaces">Link to this property</a>

<details>

<summary>

limits: optional object {cpu\_ms }

Limits for Pages Functions.

</summary>

cpu\_ms: number

CPU time limit in milliseconds.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20limits%20%3E%20(property)%20cpu_ms">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20limits">Link to this property</a>

<details>

<summary>

mtls\_certificates: optional map\[object {certificate\_id } ]

mTLS bindings used for Pages Functions.

</summary>

certificate\_id: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20mtls_certificates%20%3E%20(items)%20%3E%20(property)%20certificate_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20mtls_certificates">Link to this property</a>

<details>

<summary>

placement: optional object {mode }

Placement setting used for Pages Functions.

</summary>

mode: string

Placement mode.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20placement%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20placement">Link to this property</a>

<details>

<summary>

queue\_producers: optional map\[object {name } ]

Queue Producer bindings used for Pages Functions.

</summary>

name: string

Name of the Queue.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20queue_producers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20queue_producers">Link to this property</a>

<details>

<summary>

r2\_buckets: optional map\[object {name, jurisdiction } ]

R2 buckets used for Pages Functions.

</summary>

name: string

Name of the R2 bucket.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20r2_buckets%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

jurisdiction: optional string

Jurisdiction of the R2 bucket.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20r2_buckets%20%3E%20(items)%20%3E%20(property)%20jurisdiction">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20r2_buckets">Link to this property</a>

<details>

<summary>

services: optional map\[object {environment, service, entrypoint } ]

Services used for Pages Functions.

</summary>

environment: string

The Service environment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20services%20%3E%20(items)%20%3E%20(property)%20environment">Link to this property</a>

service: string

The Service name.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20services%20%3E%20(items)%20%3E%20(property)%20service">Link to this property</a>

entrypoint: optional string

The entrypoint to bind to.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20services%20%3E%20(items)%20%3E%20(property)%20entrypoint">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20services">Link to this property</a>

<details>

<summary>

vectorize\_bindings: optional map\[object {index\_name } ]

Vectorize bindings used for Pages Functions.

</summary>

index\_name: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20vectorize_bindings%20%3E%20(items)%20%3E%20(property)%20index_name">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20vectorize_bindings">Link to this property</a>

wrangler\_config\_hash: optional string

Hash of the Wrangler configuration used for the deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview%20%3E%20(property)%20wrangler_config_hash">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20preview">Link to this property</a>

<details>

<summary>

production: object {always\_use\_latest\_compatibility\_date, build\_image\_major\_version, compatibility\_date, 19 more }

Configs for production deploys.

</summary>

always\_use\_latest\_compatibility\_date: boolean

Whether to always use the latest compatibility date for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20always_use_latest_compatibility_date">Link to this property</a>

build\_image\_major\_version: number

The major version of the build image to use for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20build_image_major_version">Link to this property</a>

compatibility\_date: string

Compatibility date used for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: array of string

Compatibility flags used for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20compatibility_flags">Link to this property</a>

<details>

<summary>

env\_vars: map\[object {type, value } or object {type, value } ]

Environment variables used for builds and Pages Functions.

</summary>

One of the following:

<details>

<summary>

PlainText object {type, value }

A plaintext environment variable.

</summary>

type: "plain\_text"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

value: string

Environment variable value.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretText object {type, value }

An encrypted environment variable.

</summary>

type: "secret\_text"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

value: string

Secret value.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20env_vars">Link to this property</a>

fail\_open: boolean

Whether to fail open when the deployment config cannot be applied.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20fail_open">Link to this property</a>

<details>

<summary>

Deprecatedusage\_model: "standard"or "bundled"or "unbound"

All new projects now use the Standard usage model.

The usage model for Pages Functions.

</summary>

One of the following:

"standard"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20usage_model">Link to this property</a>

<details>

<summary>

ai\_bindings: optional map\[object {project\_id } ]

Constellation bindings used for Pages Functions.

</summary>

project\_id: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20ai_bindings%20%3E%20(items)%20%3E%20(property)%20project_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20ai_bindings">Link to this property</a>

<details>

<summary>

analytics\_engine\_datasets: optional map\[object {dataset } ]

Analytics Engine bindings used for Pages Functions.

</summary>

dataset: string

Name of the dataset.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20analytics_engine_datasets%20%3E%20(items)%20%3E%20(property)%20dataset">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20analytics_engine_datasets">Link to this property</a>

browsers: optional map\[object {} ]

Browser bindings used for Pages Functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20browsers">Link to this property</a>

<details>

<summary>

d1\_databases: optional map\[object {id } ]

D1 databases used for Pages Functions.

</summary>

id: string

UUID of the D1 database.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20d1_databases%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20d1_databases">Link to this property</a>

<details>

<summary>

durable\_object\_namespaces: optional map\[object {namespace\_id } ]

Durable Object namespaces used for Pages Functions.

</summary>

namespace\_id: string

ID of the Durable Object namespace.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20durable_object_namespaces%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20durable_object_namespaces">Link to this property</a>

<details>

<summary>

hyperdrive\_bindings: optional map\[object {id } ]

Hyperdrive bindings used for Pages Functions.

</summary>

id: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20hyperdrive_bindings%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20hyperdrive_bindings">Link to this property</a>

<details>

<summary>

kv\_namespaces: optional map\[object {namespace\_id } ]

KV namespaces used for Pages Functions.

</summary>

namespace\_id: string

ID of the KV namespace.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20kv_namespaces%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20kv_namespaces">Link to this property</a>

<details>

<summary>

limits: optional object {cpu\_ms }

Limits for Pages Functions.

</summary>

cpu\_ms: number

CPU time limit in milliseconds.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20limits%20%3E%20(property)%20cpu_ms">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20limits">Link to this property</a>

<details>

<summary>

mtls\_certificates: optional map\[object {certificate\_id } ]

mTLS bindings used for Pages Functions.

</summary>

certificate\_id: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20mtls_certificates%20%3E%20(items)%20%3E%20(property)%20certificate_id">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20mtls_certificates">Link to this property</a>

<details>

<summary>

placement: optional object {mode }

Placement setting used for Pages Functions.

</summary>

mode: string

Placement mode.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20placement%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20placement">Link to this property</a>

<details>

<summary>

queue\_producers: optional map\[object {name } ]

Queue Producer bindings used for Pages Functions.

</summary>

name: string

Name of the Queue.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20queue_producers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20queue_producers">Link to this property</a>

<details>

<summary>

r2\_buckets: optional map\[object {name, jurisdiction } ]

R2 buckets used for Pages Functions.

</summary>

name: string

Name of the R2 bucket.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20r2_buckets%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

jurisdiction: optional string

Jurisdiction of the R2 bucket.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20r2_buckets%20%3E%20(items)%20%3E%20(property)%20jurisdiction">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20r2_buckets">Link to this property</a>

<details>

<summary>

services: optional map\[object {environment, service, entrypoint } ]

Services used for Pages Functions.

</summary>

environment: string

The Service environment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20services%20%3E%20(items)%20%3E%20(property)%20environment">Link to this property</a>

service: string

The Service name.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20services%20%3E%20(items)%20%3E%20(property)%20service">Link to this property</a>

entrypoint: optional string

The entrypoint to bind to.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20services%20%3E%20(items)%20%3E%20(property)%20entrypoint">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20services">Link to this property</a>

<details>

<summary>

vectorize\_bindings: optional map\[object {index\_name } ]

Vectorize bindings used for Pages Functions.

</summary>

index\_name: string

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20vectorize_bindings%20%3E%20(items)%20%3E%20(property)%20index_name">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20vectorize_bindings">Link to this property</a>

wrangler\_config\_hash: optional string

Hash of the Wrangler configuration used for the deployment.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production%20%3E%20(property)%20wrangler_config_hash">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs%20%3E%20(property)%20production">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20deployment_configs">Link to this property</a>

framework: string

Framework the project is using.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20framework">Link to this property</a>

framework\_version: string

Version of the framework the project is using.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20framework_version">Link to this property</a>

latest\_deployment: <a href="https://developers.cloudflare.com/api/resources/pages#(resource)%20pages.projects%20%3E%20(model)%20deployment%20%3E%20(schema)">Deployment</a> { id, aliases, build\_config, 15 more }

Most recent deployment of the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20latest_deployment">Link to this property</a>

name: string

Name of the Pages project. Must begin with a lowercase letter or digit and contain only lowercase letters, digits, and hyphens.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

preview\_script\_name: string

Name of the preview script.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20preview_script_name">Link to this property</a>

production\_branch: string

Production branch of the project. Used to identify production deployments.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20production_branch">Link to this property</a>

production\_script\_name: string

Name of the production script.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20production_script_name">Link to this property</a>

uses\_functions: boolean

Whether the project uses functions.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20uses_functions">Link to this property</a>

<details>

<summary>

build\_config: optional object {web\_analytics\_tag, web\_analytics\_token, build\_caching, 3 more }

Configs for the project build process.

</summary>

web\_analytics\_tag: string

The classifying tag for analytics.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20web_analytics_tag">Link to this property</a>

web\_analytics\_token: string

The auth token for analytics.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20web_analytics_token">Link to this property</a>

build\_caching: optional boolean

Enable build caching for the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20build_caching">Link to this property</a>

build\_command: optional string

Command used to build project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20build_command">Link to this property</a>

destination\_dir: optional string

Assets output directory of the build.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20destination_dir">Link to this property</a>

root\_dir: optional string

Directory to run the command.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config%20%3E%20(property)%20root_dir">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20build_config">Link to this property</a>

domains: optional array of string

A list of associated custom domains for the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20domains">Link to this property</a>

<details>

<summary>

source: optional object {config, type }

Configs for the project source control.

</summary>

<details>

<summary>

config: object {deployments\_enabled, owner, owner\_id, 10 more }

</summary>

Deprecateddeployments\_enabled: boolean

Use <code>production_deployments_enabled</code> and <code>preview_deployment_setting</code> for more granular control.

Whether to enable automatic deployments when pushing to the source repository. When disabled, no deployments (production or preview) will be triggered automatically.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20deployments_enabled">Link to this property</a>

owner: string

The owner of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20owner">Link to this property</a>

owner\_id: string

The owner ID of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20owner_id">Link to this property</a>

path\_excludes: array of string

A list of paths that should be excluded from triggering a preview deployment. Wildcard syntax (<code>*</code>) is supported.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20path_excludes">Link to this property</a>

path\_includes: array of string

A list of paths that should be watched to trigger a preview deployment. Wildcard syntax (<code>*</code>) is supported.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20path_includes">Link to this property</a>

pr\_comments\_enabled: boolean

Whether to enable PR comments.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20pr_comments_enabled">Link to this property</a>

preview\_branch\_excludes: array of string

A list of branches that should not trigger a preview deployment. Wildcard syntax (<code>*</code>) is supported. Must be used with <code>preview_deployment_setting</code> set to <code>custom</code>.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_branch_excludes">Link to this property</a>

preview\_branch\_includes: array of string

A list of branches that should trigger a preview deployment. Wildcard syntax (<code>*</code>) is supported. Must be used with <code>preview_deployment_setting</code> set to <code>custom</code>.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_branch_includes">Link to this property</a>

<details>

<summary>

preview\_deployment\_setting: "all"or "none"or "custom"

Controls whether commits to preview branches trigger a preview deployment.

</summary>

One of the following:

"all"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting%20%3E%20(member)%200">Link to this property</a>

"none"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting%20%3E%20(member)%201">Link to this property</a>

"custom"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20preview_deployment_setting">Link to this property</a>

production\_branch: string

The production branch of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20production_branch">Link to this property</a>

production\_deployments\_enabled: boolean

Whether to trigger a production deployment on commits to the production branch.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20production_deployments_enabled">Link to this property</a>

repo\_id: string

The ID of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20repo_id">Link to this property</a>

repo\_name: string

The name of the repository.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config%20%3E%20(property)%20repo_name">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20config">Link to this property</a>

<details>

<summary>

type: "github"or "gitlab"

The source control management provider.

</summary>

One of the following:

"github"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"gitlab"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

subdomain: optional string

The Cloudflare subdomain associated with the project.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)%20%3E%20(property)%20subdomain">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects%20%3E%20(model)%20project%20%3E%20(schema)>)

<details>

<summary>

Stage object {ended\_on, name, started\_on, status }

The status of the deployment.

</summary>

ended\_on: string

When the stage ended.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20ended_on">Link to this property</a>

<details>

<summary>

name: "queued"or "initialize"or "clone\_repo"or 2 more

The current build stage.

</summary>

One of the following:

"queued"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%200">Link to this property</a>

"initialize"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%201">Link to this property</a>

"clone\_repo"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%202">Link to this property</a>

"build"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%203">Link to this property</a>

"deploy"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

started\_on: string

When the stage started.

formatdate-time

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20started_on">Link to this property</a>

<details>

<summary>

status: "success"or "idle"or "active"or 3 more

State of the current stage.

</summary>

One of the following:

"success"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"idle"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failure"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"canceled"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"skipped"

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects%20%3E%20(model)%20stage%20%3E%20(schema)>)

<details>

<summary>

ProjectGetUploadTokenResponse object {jwt }

</summary>

jwt: string

Short-lived JWT used to authenticate Pages Direct Upload asset operations.

<a href="#(resource)%20pages.projects%20%3E%20(model)%20project_get_upload_token_response%20%3E%20(schema)%20%3E%20(property)%20jwt">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects%20%3E%20(model)%20project_get_upload_token_response%20%3E%20(schema)>)

ProjectDeleteResponse = unknown

[Link to this property](<#(resource)%20pages.projects%20%3E%20(model)%20project_delete_response%20%3E%20(schema)>)

ProjectPurgeBuildCacheResponse = unknown

[Link to this property](<#(resource)%20pages.projects%20%3E%20(model)%20project_purge_build_cache_response%20%3E%20(schema)>)

#### ProjectsDeployments

##### [List Pages deployments](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/list)

GET/accounts/{account\_id}/pages/projects/{project\_name}/deployments

##### [Get a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/get)

GET/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}

##### [Create a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/create)

POST/accounts/{account\_id}/pages/projects/{project\_name}/deployments

##### [Delete a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/delete)

DELETE/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}

##### [Retry a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/retry)

POST/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}/retry

##### [Roll back a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/rollback)

POST/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}/rollback

##### ModelsExpand Collapse

DeploymentDeleteResponse = unknown

[Link to this property](<#(resource)%20pages.projects.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)>)

#### ProjectsDeploymentsHistory

#### ProjectsDeploymentsHistoryLogs

##### [Get Pages deployment logs](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/subresources/history/subresources/logs/methods/get)

GET/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}/history/logs

##### ModelsExpand Collapse

<details>

<summary>

LogGetResponse object {data, includes\_container\_logs, total }

</summary>

<details>

<summary>

data: array of object {line, ts }

</summary>

line: string

<a href="#(resource)%20pages.projects.deployments.history.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20line">Link to this property</a>

ts: string

<a href="#(resource)%20pages.projects.deployments.history.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20ts">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.deployments.history.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

includes\_container\_logs: boolean

<a href="#(resource)%20pages.projects.deployments.history.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20includes_container_logs">Link to this property</a>

total: number

<a href="#(resource)%20pages.projects.deployments.history.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)%20%3E%20(property)%20total">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.deployments.history.logs%20%3E%20(model)%20log_get_response%20%3E%20(schema)>)

#### ProjectsDeploymentsTails

##### [Create deployment tail](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/subresources/tails/methods/create)

POST/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}/tails

##### [Delete deployment tail](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/subresources/tails/methods/delete)

DELETE/accounts/{account\_id}/pages/projects/{project\_name}/deployments/{deployment\_id}/tails/{tail\_id}

##### ModelsExpand Collapse

<details>

<summary>

TailCreateResponse object {id, url }

A tail session for streaming logs from a Pages deployment.

</summary>

id: string

Identifier of the tail session.

<a href="#(resource)%20pages.projects.deployments.tails%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

url: optional string

Optional WebSocket URL to connect to for receiving tail events, when returned by the tail service.

<a href="#(resource)%20pages.projects.deployments.tails%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.deployments.tails%20%3E%20(model)%20tail_create_response%20%3E%20(schema)>)

TailDeleteResponse = unknown

[Link to this property](<#(resource)%20pages.projects.deployments.tails%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)>)

#### ProjectsDomains

##### [List Pages custom domains](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/list)

GET/accounts/{account\_id}/pages/projects/{project\_name}/domains

##### [Get a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/get)

GET/accounts/{account\_id}/pages/projects/{project\_name}/domains/{domain\_name}

##### [Add a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/create)

POST/accounts/{account\_id}/pages/projects/{project\_name}/domains

##### [Retry custom domain validation](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/edit)

PATCH/accounts/{account\_id}/pages/projects/{project\_name}/domains/{domain\_name}

##### [Delete a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/delete)

DELETE/accounts/{account\_id}/pages/projects/{project\_name}/domains/{domain\_name}

##### ModelsExpand Collapse

<details>

<summary>

DomainListResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_list_response%20%3E%20(schema)>)

<details>

<summary>

DomainGetResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_get_response%20%3E%20(schema)>)

<details>

<summary>

DomainCreateResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_create_response%20%3E%20(schema)>)

<details>

<summary>

DomainEditResponse object {id, certificate\_authority, created\_on, 6 more }

</summary>

id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificate\_authority: "google"or "lets\_encrypt"

</summary>

One of the following:

"google"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

created\_on: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

domain\_id: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20domain_id">Link to this property</a>

name: string

Fully qualified domain name for the Pages project, such as <code>example.com</code>.

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 3 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

validation\_data: object {method, status, error\_message, 2 more }

</summary>

<details>

<summary>

method: "http"or "txt"

</summary>

One of the following:

"http"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%200">Link to this property</a>

"txt"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending"or "active"or 2 more

</summary>

One of the following:

"initializing"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20error_message">Link to this property</a>

txt\_name: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_data">Link to this property</a>

<details>

<summary>

verification\_data: object {status, error\_message }

</summary>

<details>

<summary>

status: "pending"or "active"or "deactivated"or 2 more

</summary>

One of the following:

"pending"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"active"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"deactivated"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"blocked"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"error"

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20status">Link to this property</a>

error\_message: optional string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data%20%3E%20(property)%20error_message">Link to this property</a>

</details>

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20verification_data">Link to this property</a>

zone\_tag: string

<a href="#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_edit_response%20%3E%20(schema)>)

DomainDeleteResponse = unknown

[Link to this property](<#(resource)%20pages.projects.domains%20%3E%20(model)%20domain_delete_response%20%3E%20(schema)>)