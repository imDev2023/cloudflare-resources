---
title: Skills
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Signals](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals)

[Feeds](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Skills

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