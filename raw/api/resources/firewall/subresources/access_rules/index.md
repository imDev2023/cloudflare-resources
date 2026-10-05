---
title: Access Rules
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Firewall](https://developers.cloudflare.com/api/resources/firewall)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Access Rules

##### [List IP Access rules](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/list)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/firewall/access\_rules/rules

##### [Get an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/get)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/firewall/access\_rules/rules/{rule\_id}

##### [Create an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/create)

POST/{accounts\_or\_zones}/{account\_or\_zone\_id}/firewall/access\_rules/rules

##### [Update an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/edit)

PATCH/{accounts\_or\_zones}/{account\_or\_zone\_id}/firewall/access\_rules/rules/{rule\_id}

##### [Delete an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/delete)

DELETE/{accounts\_or\_zones}/{account\_or\_zone\_id}/firewall/access\_rules/rules/{rule\_id}

##### ModelsExpand Collapse

<details>

<summary>

AccessRuleCIDRConfiguration object {target, value }

</summary>

target: optional "ip\_range"

The configuration target. You must set the target to <code>ip_range</code> when specifying an IP address range in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address range to match. You can only use prefix lengths <code>/16</code> and <code>/24</code> for IPv4 ranges, and prefix lengths <code>/32</code>, <code>/48</code>, and <code>/64</code> for IPv6 ranges.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)>)

<details>

<summary>

AccessRuleIPConfiguration object {target, value }

</summary>

target: optional "ip"

The configuration target. You must set the target to <code>ip</code> when specifying an IP address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address to match. This address will be compared to the IP address of incoming requests.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)>)

<details>

<summary>

ASNConfiguration object {target, value }

</summary>

target: optional "asn"

The configuration target. You must set the target to <code>asn</code> when specifying an Autonomous System Number (ASN) in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The AS number to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)>)

<details>

<summary>

CountryConfiguration object {target, value }

</summary>

target: optional "country"

The configuration target. You must set the target to <code>country</code> when specifying a country code in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The two-letter ISO-3166-1 alpha-2 code to match. For more information, refer to <a href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country">IP Access rules: Parameters</a>.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)>)

<details>

<summary>

IPV6Configuration object {target, value }

</summary>

target: optional "ip6"

The configuration target. You must set the target to <code>ip6</code> when specifying an IPv6 address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IPv6 address to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)>)

<details>

<summary>

AccessRuleListResponse object {id, allowed\_modes, configuration, 5 more }

</summary>

id: string

The unique identifier of the IP Access rule.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

allowed\_modes: array of "block"or "challenge"or "whitelist"or 2 more

The available actions that a rule can apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes">Link to this property</a>

<details>

<summary>

configuration: <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">AccessRuleIPConfiguration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">IPV6Configuration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">AccessRuleCIDRConfiguration</a> { target, value } or 2 more

The rule configuration.

</summary>

One of the following:

<details>

<summary>

AccessRuleIPConfiguration object {target, value }

</summary>

target: optional "ip"

The configuration target. You must set the target to <code>ip</code> when specifying an IP address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address to match. This address will be compared to the IP address of incoming requests.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

IPV6Configuration object {target, value }

</summary>

target: optional "ip6"

The configuration target. You must set the target to <code>ip6</code> when specifying an IPv6 address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IPv6 address to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

AccessRuleCIDRConfiguration object {target, value }

</summary>

target: optional "ip\_range"

The configuration target. You must set the target to <code>ip_range</code> when specifying an IP address range in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address range to match. You can only use prefix lengths <code>/16</code> and <code>/24</code> for IPv4 ranges, and prefix lengths <code>/32</code>, <code>/48</code>, and <code>/64</code> for IPv6 ranges.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

ASNConfiguration object {target, value }

</summary>

target: optional "asn"

The configuration target. You must set the target to <code>asn</code> when specifying an Autonomous System Number (ASN) in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The AS number to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

CountryConfiguration object {target, value }

</summary>

target: optional "country"

The configuration target. You must set the target to <code>country</code> when specifying a country code in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The two-letter ISO-3166-1 alpha-2 code to match. For more information, refer to <a href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country">IP Access rules: Parameters</a>.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

<details>

<summary>

mode: "block"or "challenge"or "whitelist"or 2 more

The action to apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

created\_on: optional string

The timestamp of when the rule was created.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: optional string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

notes: optional string

An informative summary of the rule, typically used as a reminder or explanation.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20notes">Link to this property</a>

<details>

<summary>

scope: optional object {id, email, type }

All zones owned by the user will have the rule applied.

</summary>

id: optional string

Defines an identifier.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20email">Link to this property</a>

<details>

<summary>

type: optional "user"or "organization"

Defines the scope of the rule.

</summary>

One of the following:

"user"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_list_response%20%3E%20(schema)>)

<details>

<summary>

AccessRuleGetResponse object {id, allowed\_modes, configuration, 5 more }

</summary>

id: string

The unique identifier of the IP Access rule.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

allowed\_modes: array of "block"or "challenge"or "whitelist"or 2 more

The available actions that a rule can apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes">Link to this property</a>

<details>

<summary>

configuration: <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">AccessRuleIPConfiguration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">IPV6Configuration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">AccessRuleCIDRConfiguration</a> { target, value } or 2 more

The rule configuration.

</summary>

One of the following:

<details>

<summary>

AccessRuleIPConfiguration object {target, value }

</summary>

target: optional "ip"

The configuration target. You must set the target to <code>ip</code> when specifying an IP address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address to match. This address will be compared to the IP address of incoming requests.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

IPV6Configuration object {target, value }

</summary>

target: optional "ip6"

The configuration target. You must set the target to <code>ip6</code> when specifying an IPv6 address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IPv6 address to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

AccessRuleCIDRConfiguration object {target, value }

</summary>

target: optional "ip\_range"

The configuration target. You must set the target to <code>ip_range</code> when specifying an IP address range in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address range to match. You can only use prefix lengths <code>/16</code> and <code>/24</code> for IPv4 ranges, and prefix lengths <code>/32</code>, <code>/48</code>, and <code>/64</code> for IPv6 ranges.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

ASNConfiguration object {target, value }

</summary>

target: optional "asn"

The configuration target. You must set the target to <code>asn</code> when specifying an Autonomous System Number (ASN) in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The AS number to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

CountryConfiguration object {target, value }

</summary>

target: optional "country"

The configuration target. You must set the target to <code>country</code> when specifying a country code in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The two-letter ISO-3166-1 alpha-2 code to match. For more information, refer to <a href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country">IP Access rules: Parameters</a>.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

<details>

<summary>

mode: "block"or "challenge"or "whitelist"or 2 more

The action to apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

created\_on: optional string

The timestamp of when the rule was created.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: optional string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

notes: optional string

An informative summary of the rule, typically used as a reminder or explanation.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20notes">Link to this property</a>

<details>

<summary>

scope: optional object {id, email, type }

All zones owned by the user will have the rule applied.

</summary>

id: optional string

Defines an identifier.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20email">Link to this property</a>

<details>

<summary>

type: optional "user"or "organization"

Defines the scope of the rule.

</summary>

One of the following:

"user"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_get_response%20%3E%20(schema)>)

<details>

<summary>

AccessRuleCreateResponse object {id, allowed\_modes, configuration, 5 more }

</summary>

id: string

The unique identifier of the IP Access rule.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

allowed\_modes: array of "block"or "challenge"or "whitelist"or 2 more

The available actions that a rule can apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes">Link to this property</a>

<details>

<summary>

configuration: <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">AccessRuleIPConfiguration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">IPV6Configuration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">AccessRuleCIDRConfiguration</a> { target, value } or 2 more

The rule configuration.

</summary>

One of the following:

<details>

<summary>

AccessRuleIPConfiguration object {target, value }

</summary>

target: optional "ip"

The configuration target. You must set the target to <code>ip</code> when specifying an IP address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address to match. This address will be compared to the IP address of incoming requests.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

IPV6Configuration object {target, value }

</summary>

target: optional "ip6"

The configuration target. You must set the target to <code>ip6</code> when specifying an IPv6 address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IPv6 address to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

AccessRuleCIDRConfiguration object {target, value }

</summary>

target: optional "ip\_range"

The configuration target. You must set the target to <code>ip_range</code> when specifying an IP address range in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address range to match. You can only use prefix lengths <code>/16</code> and <code>/24</code> for IPv4 ranges, and prefix lengths <code>/32</code>, <code>/48</code>, and <code>/64</code> for IPv6 ranges.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

ASNConfiguration object {target, value }

</summary>

target: optional "asn"

The configuration target. You must set the target to <code>asn</code> when specifying an Autonomous System Number (ASN) in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The AS number to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

CountryConfiguration object {target, value }

</summary>

target: optional "country"

The configuration target. You must set the target to <code>country</code> when specifying a country code in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The two-letter ISO-3166-1 alpha-2 code to match. For more information, refer to <a href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country">IP Access rules: Parameters</a>.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

<details>

<summary>

mode: "block"or "challenge"or "whitelist"or 2 more

The action to apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

created\_on: optional string

The timestamp of when the rule was created.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: optional string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

notes: optional string

An informative summary of the rule, typically used as a reminder or explanation.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20notes">Link to this property</a>

<details>

<summary>

scope: optional object {id, email, type }

All zones owned by the user will have the rule applied.

</summary>

id: optional string

Defines an identifier.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20email">Link to this property</a>

<details>

<summary>

type: optional "user"or "organization"

Defines the scope of the rule.

</summary>

One of the following:

"user"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_create_response%20%3E%20(schema)>)

<details>

<summary>

AccessRuleEditResponse object {id, allowed\_modes, configuration, 5 more }

</summary>

id: string

The unique identifier of the IP Access rule.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

allowed\_modes: array of "block"or "challenge"or "whitelist"or 2 more

The available actions that a rule can apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20allowed_modes">Link to this property</a>

<details>

<summary>

configuration: <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">AccessRuleIPConfiguration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">IPV6Configuration</a> { target, value } or <a href="https://developers.cloudflare.com/api/resources/firewall#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">AccessRuleCIDRConfiguration</a> { target, value } or 2 more

The rule configuration.

</summary>

One of the following:

<details>

<summary>

AccessRuleIPConfiguration object {target, value }

</summary>

target: optional "ip"

The configuration target. You must set the target to <code>ip</code> when specifying an IP address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address to match. This address will be compared to the IP address of incoming requests.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_ip_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

IPV6Configuration object {target, value }

</summary>

target: optional "ip6"

The configuration target. You must set the target to <code>ip6</code> when specifying an IPv6 address in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IPv6 address to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20ipv6_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

AccessRuleCIDRConfiguration object {target, value }

</summary>

target: optional "ip\_range"

The configuration target. You must set the target to <code>ip_range</code> when specifying an IP address range in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The IP address range to match. You can only use prefix lengths <code>/16</code> and <code>/24</code> for IPv4 ranges, and prefix lengths <code>/32</code>, <code>/48</code>, and <code>/64</code> for IPv6 ranges.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_cidr_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

ASNConfiguration object {target, value }

</summary>

target: optional "asn"

The configuration target. You must set the target to <code>asn</code> when specifying an Autonomous System Number (ASN) in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The AS number to match.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20asn_configuration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

CountryConfiguration object {target, value }

</summary>

target: optional "country"

The configuration target. You must set the target to <code>country</code> when specifying a country code in the rule.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

value: optional string

The two-letter ISO-3166-1 alpha-2 code to match. For more information, refer to <a href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country">IP Access rules: Parameters</a>.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20country_configuration%20%3E%20(schema)">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

<details>

<summary>

mode: "block"or "challenge"or "whitelist"or 2 more

The action to apply to a matched request.

</summary>

One of the following:

"block"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"whitelist"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

"js\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%203">Link to this property</a>

"managed\_challenge"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20mode">Link to this property</a>

created\_on: optional string

The timestamp of when the rule was created.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: optional string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

notes: optional string

An informative summary of the rule, typically used as a reminder or explanation.

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20notes">Link to this property</a>

<details>

<summary>

scope: optional object {id, email, type }

All zones owned by the user will have the rule applied.

</summary>

id: optional string

Defines an identifier.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20id">Link to this property</a>

email: optional string

The contact email address of the user.

maxLength90

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20email">Link to this property</a>

<details>

<summary>

type: optional "user"or "organization"

Defines the scope of the rule.

</summary>

One of the following:

"user"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"organization"

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)%20%3E%20(property)%20scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_edit_response%20%3E%20(schema)>)

<details>

<summary>

AccessRuleDeleteResponse object {id }

</summary>

id: string

Defines an identifier.

maxLength32

<a href="#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20firewall.access_rules%20%3E%20(model)%20access_rule_delete_response%20%3E%20(schema)>)