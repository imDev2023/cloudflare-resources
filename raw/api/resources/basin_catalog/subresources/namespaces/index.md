---
title: Namespaces
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Basin Catalog](https://developers.cloudflare.com/api/resources/basin_catalog)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Namespaces

##### [List namespaces in catalog](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/methods/list)

GET/accounts/{account\_id}/basin-catalog/{bucket\_name}/namespaces

##### ModelsExpand Collapse

<details>

<summary>

NamespaceListResponse object {namespaces, details, namespace\_uuids, next\_page\_token }

Contains the list of namespaces with optional pagination.

</summary>

namespaces: array of array of string

Lists namespaces in the catalog.

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20namespaces">Link to this property</a>

<details>

<summary>

details: optional array of object {namespace, namespace\_uuid, created\_at, updated\_at }

Contains detailed metadata for each namespace when return\_details is true. Each object includes the namespace, UUID, and timestamps.

</summary>

namespace: array of string

Specifies the hierarchical namespace parts as an array of strings. For example, \[“bronze”, “analytics”] represents the namespace “bronze.analytics”.

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20namespace">Link to this property</a>

namespace\_uuid: string

Contains the UUID that persists across renames.

formatuuid

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20namespace_uuid">Link to this property</a>

created\_at: optional string

Indicates the creation timestamp in ISO 8601 format.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

updated\_at: optional string

Shows the last update timestamp in ISO 8601 format. Null if never updated.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20details">Link to this property</a>

namespace\_uuids: optional array of string

Contains UUIDs for each namespace when return\_uuids is true. The order corresponds to the namespaces array.

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20namespace_uuids">Link to this property</a>

next\_page\_token: optional string

Use this opaque token to fetch the next page of results. A null or absent value indicates the last page.

<a href="#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)%20%3E%20(property)%20next_page_token">Link to this property</a>

</details>

[Link to this property](<#(resource)%20basin_catalog.namespaces%20%3E%20(model)%20namespace_list_response%20%3E%20(schema)>)

#### NamespacesTables

##### [List tables in namespace](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/subresources/tables/methods/list)

GET/accounts/{account\_id}/basin-catalog/{bucket\_name}/namespaces/{namespace}/tables

##### ModelsExpand Collapse

<details>

<summary>

TableListResponse object {identifiers, details, next\_page\_token, table\_uuids }

Contains the list of tables with optional pagination.

</summary>

<details>

<summary>

identifiers: array of object {name, namespace }

Lists tables in the namespace.

</summary>

name: string

Specifies the table name.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20identifiers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

namespace: array of string

Specifies the hierarchical namespace parts as an array of strings. For example, \[“bronze”, “analytics”] represents the namespace “bronze.analytics”.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20identifiers%20%3E%20(items)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20identifiers">Link to this property</a>

<details>

<summary>

details: optional array of object {identifier, table\_uuid, created\_at, 3 more }

Contains detailed metadata for each table when return\_details is true. Each object includes identifier, UUID, timestamps, and locations.

</summary>

<details>

<summary>

identifier: object {name, namespace }

Specifies a unique table identifier within a catalog.

</summary>

name: string

Specifies the table name.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20identifier%20%3E%20(property)%20name">Link to this property</a>

namespace: array of string

Specifies the hierarchical namespace parts as an array of strings. For example, \[“bronze”, “analytics”] represents the namespace “bronze.analytics”.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20identifier%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20identifier">Link to this property</a>

table\_uuid: string

Contains the UUID that persists across renames.

formatuuid

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20table_uuid">Link to this property</a>

created\_at: optional string

Indicates the creation timestamp in ISO 8601 format.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

location: optional string

Specifies the base S3 URI for table storage location.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20location">Link to this property</a>

metadata\_location: optional string

Contains the S3 URI to table metadata file. Null for staged tables.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20metadata_location">Link to this property</a>

updated\_at: optional string

Shows the last update timestamp in ISO 8601 format. Null if never updated.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20details">Link to this property</a>

next\_page\_token: optional string

Use this opaque token to fetch the next page of results. A null or absent value indicates the last page.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20next_page_token">Link to this property</a>

table\_uuids: optional array of string

Contains UUIDs for each table when return\_uuids is true. The order corresponds to the identifiers array.

<a href="#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)%20%3E%20(property)%20table_uuids">Link to this property</a>

</details>

[Link to this property](<#(resource)%20basin_catalog.namespaces.tables%20%3E%20(model)%20table_list_response%20%3E%20(schema)>)

#### NamespacesTablesMaintenance Configs

##### [Get table maintenance configuration](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/get)

GET/accounts/{account\_id}/basin-catalog/{bucket\_name}/namespaces/{namespace}/tables/{table\_name}/maintenance-configs

##### [Update table maintenance configuration](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/update)

POST/accounts/{account\_id}/basin-catalog/{bucket\_name}/namespaces/{namespace}/tables/{table\_name}/maintenance-configs

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

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

target\_size\_mb: "64"or "128"or "256"or "512"

Sets the target file size for compaction in megabytes. Defaults to “128”.

</summary>

One of the following:

"64"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%200">Link to this property</a>

"128"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%201">Link to this property</a>

"256"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%202">Link to this property</a>

"512"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20compaction">Link to this property</a>

interval: optional string

Scheduling interval between normal table maintenance runs.

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20interval">Link to this property</a>

<details>

<summary>

snapshot\_expiration: optional object {max\_snapshot\_age, min\_snapshots\_to\_keep, state, next\_eligible\_at }

</summary>

max\_snapshot\_age: string

Specifies the maximum age for snapshots.

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20max_snapshot_age">Link to this property</a>

min\_snapshots\_to\_keep: number

Specifies the minimum number of snapshots to retain. Defaults to 100.

formatint64

minimum1

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20min_snapshots_to_keep">Link to this property</a>

<details>

<summary>

state: "enabled"or "disabled"

Specifies the state of maintenance operations.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config%20%3E%20(property)%20snapshot_expiration">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)%20%3E%20(property)%20maintenance_config">Link to this property</a>

</details>

[Link to this property](<#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_get_response%20%3E%20(schema)>)

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

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

target\_size\_mb: "64"or "128"or "256"or "512"

Sets the target file size for compaction in megabytes. Defaults to “128”.

</summary>

One of the following:

"64"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%200">Link to this property</a>

"128"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%201">Link to this property</a>

"256"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%202">Link to this property</a>

"512"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20target_size_mb">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20compaction">Link to this property</a>

interval: optional string

Scheduling interval between normal table maintenance runs.

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

<details>

<summary>

snapshot\_expiration: optional object {max\_snapshot\_age, min\_snapshots\_to\_keep, state, next\_eligible\_at }

</summary>

max\_snapshot\_age: string

Specifies the maximum age for snapshots.

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20max_snapshot_age">Link to this property</a>

min\_snapshots\_to\_keep: number

Specifies the minimum number of snapshots to retain. Defaults to 100.

formatint64

minimum1

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20min_snapshots_to_keep">Link to this property</a>

<details>

<summary>

state: "enabled"or "disabled"

Specifies the state of maintenance operations.

</summary>

One of the following:

"enabled"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"disabled"

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20state">Link to this property</a>

next\_eligible\_at: optional string

Earliest time when the scheduler can claim this operation. Null when disabled.

formatdate-time

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration%20%3E%20(property)%20next_eligible_at">Link to this property</a>

</details>

<a href="#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)%20%3E%20(property)%20snapshot_expiration">Link to this property</a>

</details>

[Link to this property](<#(resource)%20basin_catalog.namespaces.tables.maintenance_configs%20%3E%20(model)%20maintenance_config_update_response%20%3E%20(schema)>)