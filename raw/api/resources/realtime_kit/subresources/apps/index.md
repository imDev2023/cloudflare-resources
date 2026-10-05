---
title: Apps
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Realtime Kit](https://developers.cloudflare.com/api/resources/realtime_kit)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Apps

##### [Fetch all apps](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps/methods/get)

GET/accounts/{account\_id}/realtime/kit/apps

##### [Create App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps/methods/post)

POST/accounts/{account\_id}/realtime/kit/apps

##### ModelsExpand Collapse

<details>

<summary>

AppGetResponse object {data, paging, success }

</summary>

<details>

<summary>

data: optional array of object {id, created\_at, name }

</summary>

id: optional string

formatuuid

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

name: optional string

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

<details>

<summary>

paging: optional object {end\_offset, start\_offset, total\_count }

</summary>

end\_offset: optional number

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20paging%20%3E%20(property)%20end_offset">Link to this property</a>

start\_offset: optional number

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20paging%20%3E%20(property)%20start_offset">Link to this property</a>

total\_count: optional number

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20paging%20%3E%20(property)%20total_count">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20paging">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_get_response%20%3E%20(schema)>)

<details>

<summary>

AppPostResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {app }

</summary>

<details>

<summary>

app: optional object {id, created\_at, name }

</summary>

id: optional string

formatuuid

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20app%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20app%20%3E%20(property)%20created_at">Link to this property</a>

name: optional string

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20app%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20app">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.apps%20%3E%20(model)%20app_post_response%20%3E%20(schema)>)