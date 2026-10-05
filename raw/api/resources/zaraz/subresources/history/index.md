---
title: History
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zaraz](https://developers.cloudflare.com/api/resources/zaraz)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# History

##### [List Zaraz historical configuration records](https://developers.cloudflare.com/api/resources/zaraz/subresources/history/methods/list)

GET/zones/{zone\_id}/settings/zaraz/history

##### [Restore Zaraz historical configuration by ID](https://developers.cloudflare.com/api/resources/zaraz/subresources/history/methods/update)

PUT/zones/{zone\_id}/settings/zaraz/history

##### ModelsExpand Collapse

<details>

<summary>

HistoryListResponse object {id, createdAt, description, 2 more }

</summary>

id: number

ID of the configuration.

<a href="#(resource)%20zaraz.history%20%3E%20(model)%20history_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

createdAt: string

Date and time the configuration was created.

formatdate-time

<a href="#(resource)%20zaraz.history%20%3E%20(model)%20history_list_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

description: string

Configuration description provided by the user who published this configuration.

<a href="#(resource)%20zaraz.history%20%3E%20(model)%20history_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

updatedAt: string

Date and time the configuration was last updated.

formatdate-time

<a href="#(resource)%20zaraz.history%20%3E%20(model)%20history_list_response%20%3E%20(schema)%20%3E%20(property)%20updatedAt">Link to this property</a>

userId: string

Alpha-numeric ID of the account user who published the configuration.

<a href="#(resource)%20zaraz.history%20%3E%20(model)%20history_list_response%20%3E%20(schema)%20%3E%20(property)%20userId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zaraz.history%20%3E%20(model)%20history_list_response%20%3E%20(schema)>)

#### HistoryConfigs

##### [Get Zaraz historical configurations by ID(s)](https://developers.cloudflare.com/api/resources/zaraz/subresources/history/subresources/configs/methods/get)

GET/zones/{zone\_id}/settings/zaraz/history/configs

##### ModelsExpand Collapse

<details>

<summary>

ConfigGetResponse = map\[object {id, config, createdAt, 2 more } ]

Object where keys are numeric configuration IDs.

</summary>

id: number

ID of the configuration.

<a href="#(resource)%20zaraz.history.configs%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

config: <a href="https://developers.cloudflare.com/api/resources/zaraz#(resource)%20zaraz.config%20%3E%20(model)%20configuration%20%3E%20(schema)">Configuration</a> { dataLayer, debugKey, settings, 7 more }

Zaraz configuration.

<a href="#(resource)%20zaraz.history.configs%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20config">Link to this property</a>

createdAt: string

Date and time the configuration was created.

formatdate-time

<a href="#(resource)%20zaraz.history.configs%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20createdAt">Link to this property</a>

updatedAt: string

Date and time the configuration was last updated.

formatdate-time

<a href="#(resource)%20zaraz.history.configs%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20updatedAt">Link to this property</a>

userId: string

Alpha-numeric ID of the account user who published the configuration.

<a href="#(resource)%20zaraz.history.configs%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zaraz.history.configs%20%3E%20(model)%20config_get_response%20%3E%20(schema)>)