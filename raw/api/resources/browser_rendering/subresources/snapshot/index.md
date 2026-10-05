---
title: Snapshot
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Snapshot

##### [Get HTML content and screenshot.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/snapshot/methods/create)

POST/accounts/{account\_id}/browser-rendering/snapshot

##### ModelsExpand Collapse

<details>

<summary>

SnapshotCreateResponse object {accessibilityTree, content, markdown, screenshot }

</summary>

<details>

<summary>

accessibilityTree: optional object {role, autocomplete, checked, 23 more }

Accessibility tree node

</summary>

role: string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20role">Link to this property</a>

autocomplete: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20autocomplete">Link to this property</a>

<details>

<summary>

checked: optional booleanor "mixed"

</summary>

One of the following:

boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20checked%20%3E%20(variant)%200">Link to this property</a>

"mixed"

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20checked%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20checked">Link to this property</a>

children: optional array of unknown

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20children">Link to this property</a>

description: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20description">Link to this property</a>

disabled: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20disabled">Link to this property</a>

expanded: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20expanded">Link to this property</a>

focused: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20focused">Link to this property</a>

haspopup: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20haspopup">Link to this property</a>

invalid: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20invalid">Link to this property</a>

keyshortcuts: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20keyshortcuts">Link to this property</a>

level: optional number

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20level">Link to this property</a>

modal: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20modal">Link to this property</a>

multiline: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20multiline">Link to this property</a>

multiselectable: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20multiselectable">Link to this property</a>

name: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20name">Link to this property</a>

orientation: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20orientation">Link to this property</a>

<details>

<summary>

pressed: optional booleanor "mixed"

</summary>

One of the following:

boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20pressed%20%3E%20(variant)%200">Link to this property</a>

"mixed"

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20pressed%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20pressed">Link to this property</a>

readonly: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20readonly">Link to this property</a>

required: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20required">Link to this property</a>

roledescription: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20roledescription">Link to this property</a>

selected: optional boolean

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20selected">Link to this property</a>

<details>

<summary>

value: optional stringor number

</summary>

One of the following:

string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20value">Link to this property</a>

valuemax: optional number

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20valuemax">Link to this property</a>

valuemin: optional number

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20valuemin">Link to this property</a>

valuetext: optional string

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree%20%3E%20(property)%20valuetext">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20accessibilityTree">Link to this property</a>

content: optional string

HTML content.

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20content">Link to this property</a>

markdown: optional string

Markdown content. Prefixed with YAML frontmatter (e.g. <code>title</code>) when the page provides that metadata.

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20markdown">Link to this property</a>

screenshot: optional string

Base64 encoded image.

<a href="#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)%20%3E%20(property)%20screenshot">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.snapshot%20%3E%20(model)%20snapshot_create_response%20%3E%20(schema)>)