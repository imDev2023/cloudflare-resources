---
title: Threat Signals
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Threat Signals

Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

## Prerequisites

1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.

#### Threat SignalsSearch

##### [Search Threat Signals articles using AI Search](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/search/methods/search)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/search

##### ModelsExpand Collapse

<details>

<summary>

SearchSearchResponse object {count, results }

</summary>

count: number

Number of unique article candidates returned in this response. Equal to results.length.

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

results: array of object {article\_id, dataset\_id, event\_id, 3 more }

</summary>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20article_id">Link to this property</a>

dataset\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

event\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20event_id">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

score: number

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

text: string

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.search%20%3E%20(model)%20search_search_response%20%3E%20(schema)>)

#### Threat SignalsCategories

##### [List Threat Signals feed categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/categories/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/categories

##### ModelsExpand Collapse

<details>

<summary>

CategoryListResponse object {categories }

</summary>

<details>

<summary>

categories: array of object {id, description, name }

</summary>

id: string

Wire value accepted by the feed <code>category_id</code> field.

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

description: string

Plain-language description of the category.

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

name: string

Human-readable display label.

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.categories%20%3E%20(model)%20category_list_response%20%3E%20(schema)>)

#### Threat SignalsFeeds

##### [List Threat Signals feeds](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds

##### [Create Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds

##### [Update Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}

##### [Delete Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}

##### [Trigger Threat Signals feed poll](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/poll)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/poll

##### ModelsExpand Collapse

<details>

<summary>

FeedListResponse object {count, feeds, page, 2 more }

</summary>

count: number

Number of feeds on this page.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

feeds: array of object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20feeds">Link to this property</a>

page: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20per_page">Link to this property</a>

total\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_list_response%20%3E%20(schema)>)

<details>

<summary>

FeedCreateResponse object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_create_response%20%3E%20(schema)>)

<details>

<summary>

FeedEditResponse object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_edit_response%20%3E%20(schema)>)

<details>

<summary>

FeedDeleteResponse object {id, category\_id, category\_name, 12 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

category\_id: string

Feed category identifier. Null when unset.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20category_id">Link to this property</a>

category\_name: string

Display name of the feed category. Null when unset or unresolvable.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20category_name">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

curated\_feed\_id: string

Curated catalog feed this subscription was created from. Null for custom feeds.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20curated_feed_id">Link to this property</a>

display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

enabled: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

last\_polled\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_polled_at">Link to this property</a>

poll\_interval\_s: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20poll_interval_s">Link to this property</a>

source\_type: string

<code>custom</code> for a feed added by URL, <code>curated</code> for a curated catalog feed.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20source_type">Link to this property</a>

status: string

Polling health: <code>active</code>, or <code>error</code> after a failed poll.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

subscribed\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20subscribed_at">Link to this property</a>

title: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_delete_response%20%3E%20(schema)>)

<details>

<summary>

FeedPollResponse object {errors, feeds, triggered }

</summary>

errors: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

feeds: array of object {feed\_id, status, workflow\_id, feed\_enabled }

</summary>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

<details>

<summary>

status: "workflow\_created"or "error"

</summary>

One of the following:

"workflow\_created"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"error"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

workflow\_id: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20workflow_id">Link to this property</a>

feed\_enabled: optional boolean

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds%20%3E%20(items)%20%3E%20(property)%20feed_enabled">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20feeds">Link to this property</a>

triggered: number

<a href="#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)%20%3E%20(property)%20triggered">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds%20%3E%20(model)%20feed_poll_response%20%3E%20(schema)>)

#### Threat SignalsFeedsRaw

##### [Get Threat Signals feed XML](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/raw/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}/raw

##### ModelsExpand Collapse

RawGetResponse = string

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds.raw%20%3E%20(model)%20raw_get_response%20%3E%20(schema)>)

#### Threat SignalsFeedsSkills

##### [Get Threat Signals feed skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/skills/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}/skills

##### [Set Threat Signals feed skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/skills/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/v2/threat-signals/feeds/{feed\_id}/skills

##### ModelsExpand Collapse

<details>

<summary>

SkillGetResponse object {feed\_id, skills }

</summary>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

<details>

<summary>

skills: array of object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20skills">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)>)

<details>

<summary>

SkillUpdateResponse object {feed\_id, skills }

</summary>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20feed_id">Link to this property</a>

<details>

<summary>

skills: array of object {position, skill\_id }

</summary>

position: number

Zero-based pipeline position.

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20position">Link to this property</a>

skill\_id: string

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20skill_id">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)%20%3E%20(property)%20skills">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.feeds.skills%20%3E%20(model)%20skill_update_response%20%3E%20(schema)>)

#### Threat SignalsArticles

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

#### Threat SignalsArticlesContent

##### [Get Threat Signals article content](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/content/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/content

##### ModelsExpand Collapse

ContentGetResponse = string

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.content%20%3E%20(model)%20content_get_response%20%3E%20(schema)>)

#### Threat SignalsArticlesTags

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

#### Threat SignalsArticlesSkill Outputs

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

#### Threat SignalsIndicators

##### [List Threat Signals article indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/indicators/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/indicators

##### ModelsExpand Collapse

<details>

<summary>

IndicatorListResponse object {indicators, pagination }

</summary>

<details>

<summary>

indicators: array of object {id, article\_id, article\_title, 5 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

article\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20article_id">Link to this property</a>

article\_title: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20article_title">Link to this property</a>

dataset\_id: string

Threat Events dataset identifier for navigating from this indicator. Null when the account feeds dataset mapping is unavailable.

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20dataset_id">Link to this property</a>

feed\_display\_name: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20feed_display_name">Link to this property</a>

feed\_id: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20feed_id">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20indicators">Link to this property</a>

<details>

<summary>

pagination: object {count, cursor, has\_more, 4 more }

</summary>

count: number

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20count">Link to this property</a>

cursor: string

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20cursor">Link to this property</a>

has\_more: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20has_more">Link to this property</a>

page: number

Ordinal of this cursor page; not a total-results offset.

minimum1

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

maximum100

minimum1

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20per_page">Link to this property</a>

total\_count: number

minimum0

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count">Link to this property</a>

total\_count\_is\_exact: boolean

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count_is_exact">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.indicators%20%3E%20(model)%20indicator_list_response%20%3E%20(schema)>)

#### Threat SignalsSkills

##### [List Threat Signals skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/list)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills

##### [Create Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills

##### [Get Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}

##### [Update Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}

##### [Delete Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}

##### ModelsExpand Collapse

<details>

<summary>

SkillListResponse object {count, custom\_skills\_available, page, 3 more }

</summary>

count: number

Number of skills on this page.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

custom\_skills\_available: boolean

Whether the authenticated account may access custom-skill capabilities under Stakeout’s Threat Signals access-mode policy. This is a policy availability indicator, not a row-existence indicator. False for threat\_signals\_only mode; true for entitled, allowlisted, cfone\_internal, and service modes.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20custom_skills_available">Link to this property</a>

page: number

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

skills: array of object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20skills">Link to this property</a>

total\_count: number

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)%20%3E%20(property)%20total_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_list_response%20%3E%20(schema)>)

<details>

<summary>

SkillCreateResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_create_response%20%3E%20(schema)>)

<details>

<summary>

SkillGetResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_get_response%20%3E%20(schema)>)

<details>

<summary>

SkillEditResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_edit_response%20%3E%20(schema)>)

<details>

<summary>

SkillDeleteResponse object {id, config, created\_at, 7 more }

</summary>

id: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

config: string

JSON-encoded skill configuration. Always null for default skills.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

created\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_active: number

1 when active, 0 when inactive.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

name: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

output\_schema: string

JSON-encoded JSON Schema the skill output must satisfy.

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20output_schema">Link to this property</a>

prompt: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20prompt">Link to this property</a>

<details>

<summary>

source: "default"or "custom"

<code>default</code> for Cloudforce One managed skills (read-only), <code>custom</code> for account skills.

</summary>

One of the following:

"default"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"custom"

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

type: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

<a href="#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills%20%3E%20(model)%20skill_delete_response%20%3E%20(schema)>)

#### Threat SignalsSkillsTag Categories

##### [Get Threat Signals skill tag categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/subresources/tag_categories/methods/get)

GET/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}/tag-categories

##### [Replace Threat Signals skill tag categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/subresources/tag_categories/methods/update)

PUT/accounts/{account\_id}/cloudforce-one/v2/threat-signals/skills/{skill\_id}/tag-categories

##### ModelsExpand Collapse

<details>

<summary>

TagCategoryGetResponse object {category\_uuids, skill\_id }

</summary>

category\_uuids: array of string

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_get_response%20%3E%20(schema)%20%3E%20(property)%20category_uuids">Link to this property</a>

skill\_id: "default-tagging-skill"

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_get_response%20%3E%20(schema)%20%3E%20(property)%20skill_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_get_response%20%3E%20(schema)>)

<details>

<summary>

TagCategoryUpdateResponse object {category\_uuids, skill\_id }

</summary>

category\_uuids: array of string

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_update_response%20%3E%20(schema)%20%3E%20(property)%20category_uuids">Link to this property</a>

skill\_id: "default-tagging-skill"

<a href="#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_update_response%20%3E%20(schema)%20%3E%20(property)%20skill_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.skills.tag_categories%20%3E%20(model)%20tag_category_update_response%20%3E%20(schema)>)