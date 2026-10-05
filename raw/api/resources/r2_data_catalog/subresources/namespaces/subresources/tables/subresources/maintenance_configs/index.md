---
title: Maintenance Configs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[R2 Data Catalog](https://developers.cloudflare.com/api/resources/r2_data_catalog)

[Namespaces](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces)

[Tables](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Maintenance Configs

##### [Get table maintenance configuration](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/get)

Deprecated

GET/accounts/{account\_id}/r2-catalog/{bucket\_name}/namespaces/{namespace}/tables/{table\_name}/maintenance-configs

##### [Update table maintenance configuration](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/update)

Deprecated

POST/accounts/{account\_id}/r2-catalog/{bucket\_name}/namespaces/{namespace}/tables/{table\_name}/maintenance-configs

##### ModelsExpand Collapse

<details>

<summary>

MaintenanceConfigGetResponse object {maintenance\_config }

Contains table maintenance configuration.

</summary>

<details>

<summary>

maintenance\_config: object {compaction, interval, snapshot\_expiration }

Configures maintenance for the table.

</summary>

<details>

<summary>

compaction: optional object {state, target\_size\_mb, next\_eligible\_at }

Configures compaction settings for table optimization.

</summary>

<details>

<summary>

state: "enabled"or "disabled"

Specifies the state of maintenance operations.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

target\_size\_mb: "64"or "128"or "256"or "512"

Sets the target file size for compaction in megabytes. Defaults to “128”.

</summary>

One of the following:

"64"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%200">Link to this property</a>

"128"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%201">Link to this property</a>

"256"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%202">Link to this property</a>

"512"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction">Link to this property</a>

interval: optional string

Scheduling interval between normal table maintenance runs.

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20interval">Link to this property</a>

<details>

<summary>

snapshot\_expiration: optional object {max\_snapshot\_age, min\_snapshots\_to\_keep, state, next\_eligible\_at }

</summary>

max\_snapshot\_age: string

Specifies the maximum age for snapshots.

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20max_snapshot_age">Link to this property</a>

min\_snapshots\_to\_keep: number

Specifies the minimum number of snapshots to retain. Defaults to 100.

formatint64

minimum1

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20min_snapshots_to_keep">Link to this property</a>

<details>

<summary>

state: "enabled"or "disabled"

Specifies the state of maintenance operations.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)>)

<details>

<summary>

MaintenanceConfigUpdateResponse object {compaction, interval, snapshot\_expiration }

Configures maintenance for the table.

</summary>

<details>

<summary>

compaction: optional object {state, target\_size\_mb, next\_eligible\_at }

Configures compaction settings for table optimization.

</summary>

<details>

<summary>

state: "enabled"or "disabled"

Specifies the state of maintenance operations.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

target\_size\_mb: "64"or "128"or "256"or "512"

Sets the target file size for compaction in megabytes. Defaults to “128”.

</summary>

One of the following:

"64"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%200">Link to this property</a>

"128"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%201">Link to this property</a>

"256"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%202">Link to this property</a>

"512"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction">Link to this property</a>

interval: optional string

Scheduling interval between normal table maintenance runs.

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

<details>

<summary>

snapshot\_expiration: optional object {max\_snapshot\_age, min\_snapshots\_to\_keep, state, next\_eligible\_at }

</summary>

max\_snapshot\_age: string

Specifies the maximum age for snapshots.

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20max_snapshot_age">Link to this property</a>

min\_snapshots\_to\_keep: number

Specifies the minimum number of snapshots to retain. Defaults to 100.

formatint64

minimum1

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20min_snapshots_to_keep">Link to this property</a>

<details>

<summary>

state: "enabled"or "disabled"

Specifies the state of maintenance operations.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2_data_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)>)