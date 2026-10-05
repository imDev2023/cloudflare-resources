---
title: Groups
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Firewall](https://developers.cloudflare.com/api/resources/firewall)

[WAF](https://developers.cloudflare.com/api/resources/firewall/subresources/waf)

[Packages](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Groups

##### [List WAF rule groups](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/list)

Deprecated

GET/zones/{zone\_id}/firewall/waf/packages/{package\_id}/groups

##### [Get a WAF rule group](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/get)

Deprecated

GET/zones/{zone\_id}/firewall/waf/packages/{package\_id}/groups/{group\_id}

##### [Update a WAF rule group](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/edit)

Deprecated

PATCH/zones/{zone\_id}/firewall/waf/packages/{package\_id}/groups/{group\_id}

##### ModelsExpand Collapse

<details>

<summary>

Group object {id, description, mode, 5 more }

</summary>

id: string

Defines the unique identifier of the rule group.

maxLength32

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: string

Defines an informative summary of what the rule group does.

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

mode: "on"or "off"

Defines the state of the rules contained in the rule group. When <code>on</code>, the rules in the group are configurable/usable.

</summary>

One of the following:

"on"

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

name: string

Defines the name of the rule group.

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

rules\_count: number

Defines the number of rules in the current rule group.

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20rules_count">Link to this property</a>

<details>

<summary>

allowed\_modes: optional array of "on"or "off"

Defines the available states for the rule group.

</summary>

One of the following:

"on"

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20allowed_modes">Link to this property</a>

modified\_rules\_count: optional number

Defines the number of rules within the group that have been modified from their default configuration.

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20modified_rules_count">Link to this property</a>

package\_id: optional string

Defines the unique identifier of a WAF package.

maxLength32

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)%20%3E%20(property)%20package_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group%20%3E%20(schema)>)

<details>

<summary>

GroupGetResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group_get_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group_get_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group_get_response%20%3E%20(schema)>)

<details>

<summary>

GroupEditResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group_edit_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group_edit_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.waf.packages.groups%20%3E%20(model)%20group_edit_response%20%3E%20(schema)>)