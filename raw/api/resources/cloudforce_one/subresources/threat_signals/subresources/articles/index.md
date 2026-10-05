---
title: Articles
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Signals](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Articles

##### [List Threat Signals articles](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles

##### [Bulk update Threat Signals article read status](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/bulk_edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles

##### [Get Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}

##### [Update Threat Signals article read status](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}

##### ModelsExpand Collapse

<details>

<summary>

ArticleListResponse object {articles, has\_more, next\_cursor, 2 more }

</summary>

<details>

<summary>

articles: array of object {id, dataset\_id, event\_id, 10 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

dataset\_id: string

Threat Events dataset identifier for the article redirect. Null when the account feeds dataset mapping is unavailable.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

event\_id: string

Threat Events event identifier associated with this article for a UI redirect. Null when no event has been linked.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20event_id">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

fetched\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20fetched_at">Link to this property</a>

link: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20link">Link to this property</a>

published\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20published_at">Link to this property</a>

read: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20read">Link to this property</a>

read\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20read_at">Link to this property</a>

summary: string

Persisted enrichment summary. Null until enrichment produces a summary.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20summary">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20articles">Link to this property</a>

has\_more: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20has_more">Link to this property</a>

next\_cursor: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20next_cursor">Link to this property</a>

total\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count">Link to this property</a>

total\_count\_is\_exact: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_list_response%20%3E%20(schema)>)

<details>

<summary>

ArticleBulkEditResponse object {updated\_count }

</summary>

updated\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_bulk_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_bulk_edit_response%20%3E%20(schema)>)

<details>

<summary>

ArticleGetResponse object {id, bullet\_points, content\_r2\_key, 16 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

bullet\_points: object {impact, what\_happened, who\_affected }

</summary>

impact: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20impact">Link to this property</a>

what\_happened: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20what_happened">Link to this property</a>

who\_affected: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20who_affected">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points">Link to this property</a>

content\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20content_r2_key">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

fetched\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20fetched_at">Link to this property</a>

<details>

<summary>

indicator\_extraction\_status: "in\_progress"or "complete"or "failed"or "unknown"

Progress of the article’s indicator extraction and IOC contextualization run. complete and failed are terminal; unknown means no run has been recorded.

</summary>

One of the following:

"in\_progress"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%200">Link to this property</a>

"complete"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%202">Link to this property</a>

"unknown"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status">Link to this property</a>

link: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20link">Link to this property</a>

metadata: map\[unknown]

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

published\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20published_at">Link to this property</a>

read: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20read">Link to this property</a>

read\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20read_at">Link to this property</a>

source\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20source_count">Link to this property</a>

summary: string

Persisted enrichment summary. Null until enrichment produces a summary.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20summary">Link to this property</a>

summary\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20summary_r2_key">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20skill_version">Link to this property</a>

tag\_skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_get_response%20%3E%20(schema)>)

<details>

<summary>

ArticleEditResponse object {id, bullet\_points, content\_r2\_key, 16 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

bullet\_points: object {impact, what\_happened, who\_affected }

</summary>

impact: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20impact">Link to this property</a>

what\_happened: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20what_happened">Link to this property</a>

who\_affected: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points%20%3E%20(property)%20who_affected">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20bullet_points">Link to this property</a>

content\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20content_r2_key">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

fetched\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20fetched_at">Link to this property</a>

<details>

<summary>

indicator\_extraction\_status: "in\_progress"or "complete"or "failed"or "unknown"

Progress of the article’s indicator extraction and IOC contextualization run. complete and failed are terminal; unknown means no run has been recorded.

</summary>

One of the following:

"in\_progress"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%200">Link to this property</a>

"complete"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%201">Link to this property</a>

"failed"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%202">Link to this property</a>

"unknown"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20indicator_extraction_status">Link to this property</a>

link: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20link">Link to this property</a>

metadata: map\[unknown]

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

published\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20published_at">Link to this property</a>

read: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20read">Link to this property</a>

read\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20read_at">Link to this property</a>

source\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20source_count">Link to this property</a>

summary: string

Persisted enrichment summary. Null until enrichment produces a summary.

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20summary">Link to this property</a>

summary\_r2\_key: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20summary_r2_key">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20skill_version">Link to this property</a>

tag\_skill\_version: optional string

<a href="#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles%20%3E%20(model)%20article_edit_response%20%3E%20(schema)>)

#### ArticlesContent

##### [Get Threat Signals article content](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/content/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/content

##### ModelsExpand Collapse

ContentGetResponse = string

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.content%20%3E%20(model)%20content_get_response%20%3E%20(schema)>)

#### ArticlesTags

##### [Add tag to Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tags

##### [Remove tag from Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tags/{tag\_id}

##### [Generate Threat Signals article AI tags](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/generate)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tag

##### ModelsExpand Collapse

<details>

<summary>

TagCreateResponse object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)>)

<details>

<summary>

TagDeleteResponse object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)>)

<details>

<summary>

TagGenerateResponse object {tag\_skill\_version, tags }

</summary>

tag\_skill\_version: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

Final hydrated assignment set; may be empty when no applicable tags are selected.

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)>)

#### ArticlesSkill Outputs

##### [Get Threat Signals article skill output](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/skill_outputs/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/skills/{skill\_id}/output

##### ModelsExpand Collapse

<details>

<summary>

SkillOutputGetResponse object {article\_id, custom\_skill\_version, output\_schema, 2 more }

</summary>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20article_id">Link to this property</a>

custom\_skill\_version: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_skill_version">Link to this property</a>

output\_schema: string

JSON-encoded output schema of the skill. Null when the skill no longer exists.

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

skill\_id: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20skill_id">Link to this property</a>

custom\_output: optional unknown

Skill output. Parsed JSON when the stored output is valid JSON, otherwise the raw string.

<a href="#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_output">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.skill_outputs%20%3E%20(model)%20skill_output_get_response%20%3E%20(schema)>)