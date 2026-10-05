---
title: Overrides
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Firewall](https://developers.cloudflare.com/api/resources/firewall)

[WAF](https://developers.cloudflare.com/api/resources/firewall/subresources/waf)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Overrides

##### [List WAF overrides](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/list)

Deprecated

GET/zones/{zone\_id}/firewall/waf/overrides

##### [Get a WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/get)

Deprecated

GET/zones/{zone\_id}/firewall/waf/overrides/{overrides\_id}

##### [Create a WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/create)

Deprecated

POST/zones/{zone\_id}/firewall/waf/overrides

##### [Update WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/update)

Deprecated

PUT/zones/{zone\_id}/firewall/waf/overrides/{overrides\_id}

##### [Delete a WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/delete)

Deprecated

DELETE/zones/{zone\_id}/firewall/waf/overrides/{overrides\_id}

##### ModelsExpand Collapse

OverrideURL = string

[Link to this property](<#(resource)%20firewall.waf.overrides%20%3E%20(model)%20override_url%20%3E%20(schema)>)

<details>

<summary>

RewriteAction object {block, challenge, default, 2 more }

Specifies that, when a WAF rule matches, its configured action will be replaced by the action configured in this object.

</summary>

<details>

<summary>

block: optional "challenge"or "block"or "simulate"or 2 more

The WAF rule action to apply.

</summary>

One of the following:

"challenge"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20block%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20block%20%3E%20(member)%201">Link to this property</a>

"simulate"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20block%20%3E%20(member)%202">Link to this property</a>

"disable"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20block%20%3E%20(member)%203">Link to this property</a>

"default"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20block%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20block">Link to this property</a>

<details>

<summary>

challenge: optional "challenge"or "block"or "simulate"or 2 more

The WAF rule action to apply.

</summary>

One of the following:

"challenge"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20challenge%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20challenge%20%3E%20(member)%201">Link to this property</a>

"simulate"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20challenge%20%3E%20(member)%202">Link to this property</a>

"disable"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20challenge%20%3E%20(member)%203">Link to this property</a>

"default"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20challenge%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20challenge">Link to this property</a>

<details>

<summary>

default: optional "challenge"or "block"or "simulate"or 2 more

The WAF rule action to apply.

</summary>

One of the following:

"challenge"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20default%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20default%20%3E%20(member)%201">Link to this property</a>

"simulate"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20default%20%3E%20(member)%202">Link to this property</a>

"disable"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20default%20%3E%20(member)%203">Link to this property</a>

"default"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20default%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

<details>

<summary>

disable: optional "challenge"or "block"or "simulate"or 2 more

The WAF rule action to apply.

</summary>

One of the following:

"challenge"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20disable%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20disable%20%3E%20(member)%201">Link to this property</a>

"simulate"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20disable%20%3E%20(member)%202">Link to this property</a>

"disable"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20disable%20%3E%20(member)%203">Link to this property</a>

"default"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20disable%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20disable">Link to this property</a>

<details>

<summary>

simulate: optional "challenge"or "block"or "simulate"or 2 more

The WAF rule action to apply.

</summary>

One of the following:

"challenge"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20simulate%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20simulate%20%3E%20(member)%201">Link to this property</a>

"simulate"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20simulate%20%3E%20(member)%202">Link to this property</a>

"disable"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20simulate%20%3E%20(member)%203">Link to this property</a>

"default"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20simulate%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)%20%3E%20(property)%20simulate">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.waf.overrides%20%3E%20(model)%20rewrite_action%20%3E%20(schema)>)

<details>

<summary>

WAFRule = map\["challenge"or "block"or "simulate"or 2 more]

An object that allows you to override the action of specific WAF rules. Each key of this object must be the ID of a WAF rule, and each value must be a valid WAF action. Unless you are disabling a rule, ensure that you also enable the rule group that this WAF rule belongs to. When creating a new URI-based WAF override, you must provide a <code>groups</code> object or a <code>rules</code> object.

</summary>

One of the following:

"challenge"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20waf_rule%20%3E%20(schema)%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"block"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20waf_rule%20%3E%20(schema)%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"simulate"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20waf_rule%20%3E%20(schema)%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"disable"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20waf_rule%20%3E%20(schema)%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"default"

<a href="#(resource)%20firewall.waf.overrides%20%3E%20(model)%20waf_rule%20%3E%20(schema)%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.waf.overrides%20%3E%20(model)%20waf_rule%20%3E%20(schema)>)