---
title: Precursor
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Precursor

##### [Get Zone Precursor Config](https://developers.cloudflare.com/api/resources/precursor/methods/get)

GET/zones/{zone\_id}/precursor

##### [Update Zone Precursor Config](https://developers.cloudflare.com/api/resources/precursor/methods/update)

PUT/zones/{zone\_id}/precursor

##### ModelsExpand Collapse

<details>

<summary>

EnforcementRule object {expression, mode, id, 2 more }

</summary>

expression: string

The filter expression that determines which requests the rule matches.

maxLength4000

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

mode: "min-friction"or "max-security"

The override mode Precursor applies to requests matching an enforcement rule. Unlike <code>default_mode</code>, this cannot be <code>off</code>.

</summary>

One of the following:

"min-friction"

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"max-security"

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

id: optional string

The read-only identifier that Cloudflare assigns to the rule.

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule is active.

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)>)

<details>

<summary>

PrecursorConfig object {default\_mode, enforcement\_rules }

</summary>

<details>

<summary>

Deprecateddefault\_mode: optional "off"or "min-friction"or "max-security"

The zone-level Precursor enforcement mode applied to requests that do not match a more specific enforcement rule.

</summary>

One of the following:

"off"

<a href="#(resource)%20precursor%20%3E%20(model)%20precursor_config%20%3E%20(schema)%20%3E%20(property)%20default_mode%20%3E%20(member)%200">Link to this property</a>

"min-friction"

<a href="#(resource)%20precursor%20%3E%20(model)%20precursor_config%20%3E%20(schema)%20%3E%20(property)%20default_mode%20%3E%20(member)%201">Link to this property</a>

"max-security"

<a href="#(resource)%20precursor%20%3E%20(model)%20precursor_config%20%3E%20(schema)%20%3E%20(property)%20default_mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20precursor%20%3E%20(model)%20precursor_config%20%3E%20(schema)%20%3E%20(property)%20default_mode">Link to this property</a>

<details>

<summary>

Deprecatedenforcement\_rules: optional array of <a href="https://developers.cloudflare.com/api/resources/precursor#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)">EnforcementRule</a> { expression, mode, id, 2 more }

The ordered list of enforcement rules for the zone.

</summary>

expression: string

The filter expression that determines which requests the rule matches.

maxLength4000

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

mode: "min-friction"or "max-security"

The override mode Precursor applies to requests matching an enforcement rule. Unlike <code>default_mode</code>, this cannot be <code>off</code>.

</summary>

One of the following:

"min-friction"

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"max-security"

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

id: optional string

The read-only identifier that Cloudflare assigns to the rule.

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule is active.

<a href="#(resource)%20precursor%20%3E%20(model)%20enforcement_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20precursor%20%3E%20(model)%20precursor_config%20%3E%20(schema)%20%3E%20(property)%20enforcement_rules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20precursor%20%3E%20(model)%20precursor_config%20%3E%20(schema)>)