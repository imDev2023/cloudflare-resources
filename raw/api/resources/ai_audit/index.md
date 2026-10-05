---
title: AI Audit
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# AI Audit

#### AI AuditRobots

##### [Get robots.txt rules](https://developers.cloudflare.com/api/resources/ai_audit/subresources/robots/methods/get)

GET/zones/{zone\_id}/ai-audit/robots

##### [Bulk get robots.txt rules](https://developers.cloudflare.com/api/resources/ai_audit/subresources/robots/methods/bulk_get)

POST/zones/{zone\_id}/ai-audit/robots/bulk

##### ModelsExpand Collapse

<details>

<summary>

RobotGetResponse object {userAgents, sitemaps, status }

Parsed robots.txt rules for a single domain.

</summary>

<details>

<summary>

userAgents: map\[object {allow, disallow, contentSignals, crawlDelay } ]

Map of user-agent string to its parsed rules.

</summary>

allow: array of string

List of allowed path patterns.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20allow">Link to this property</a>

disallow: array of string

List of disallowed path patterns.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20disallow">Link to this property</a>

<details>

<summary>

contentSignals: optional object {"ai-input", "ai-train", search }

Content signal directives from robots.txt.

</summary>

<details>

<summary>

"ai-input": optional "yes"or "no"

Whether AI input usage is permitted.

</summary>

One of the following:

"yes"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-input%20%3E%20(member)%200">Link to this property</a>

"no"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-input%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-input">Link to this property</a>

<details>

<summary>

"ai-train": optional "yes"or "no"

Whether AI training is permitted.

</summary>

One of the following:

"yes"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-train%20%3E%20(member)%200">Link to this property</a>

"no"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-train%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-train">Link to this property</a>

<details>

<summary>

search: optional "yes"or "no"

Whether search indexing is permitted.

</summary>

One of the following:

"yes"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20search%20%3E%20(member)%200">Link to this property</a>

"no"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20search%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20search">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals">Link to this property</a>

crawlDelay: optional number

Crawl delay in seconds.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20crawlDelay">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20userAgents">Link to this property</a>

sitemaps: optional array of string

List of sitemap URLs found in robots.txt.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20sitemaps">Link to this property</a>

status: optional number

HTTP status code from fetching the robots.txt file.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_get_response%20%3E%20(schema)>)

<details>

<summary>

RobotBulkGetResponse = map\[object {userAgents, sitemaps, status } ]

Map of hostname to parsed robots.txt rules.

</summary>

<details>

<summary>

userAgents: map\[object {allow, disallow, contentSignals, crawlDelay } ]

Map of user-agent string to its parsed rules.

</summary>

allow: array of string

List of allowed path patterns.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20allow">Link to this property</a>

disallow: array of string

List of disallowed path patterns.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20disallow">Link to this property</a>

<details>

<summary>

contentSignals: optional object {"ai-input", "ai-train", search }

Content signal directives from robots.txt.

</summary>

<details>

<summary>

"ai-input": optional "yes"or "no"

Whether AI input usage is permitted.

</summary>

One of the following:

"yes"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-input%20%3E%20(member)%200">Link to this property</a>

"no"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-input%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-input">Link to this property</a>

<details>

<summary>

"ai-train": optional "yes"or "no"

Whether AI training is permitted.

</summary>

One of the following:

"yes"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-train%20%3E%20(member)%200">Link to this property</a>

"no"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-train%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20ai-train">Link to this property</a>

<details>

<summary>

search: optional "yes"or "no"

Whether search indexing is permitted.

</summary>

One of the following:

"yes"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20search%20%3E%20(member)%200">Link to this property</a>

"no"

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20search%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals%20%3E%20(property)%20search">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20contentSignals">Link to this property</a>

crawlDelay: optional number

Crawl delay in seconds.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents%20%3E%20(items)%20%3E%20(property)%20crawlDelay">Link to this property</a>

</details>

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20userAgents">Link to this property</a>

sitemaps: optional array of string

List of sitemap URLs found in robots.txt.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20sitemaps">Link to this property</a>

status: optional number

HTTP status code from fetching the robots.txt file.

<a href="#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_audit.robots%20%3E%20(model)%20robot_bulk_get_response%20%3E%20(schema)>)