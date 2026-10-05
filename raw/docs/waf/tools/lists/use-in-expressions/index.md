---
description: Learn how to use lists in rule expressions.
title: Use lists in expressions
image: https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/og.png?v=04136c8f49fe3bb6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Use lists in expressions

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In the Cloudflare dashboard, there are two options for editing [expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/):

- [Expression Builder](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder): Allows you to create expressions using drop-down lists, emphasizing a visual approach to defining an expression.
- [Expression Editor](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor): A text-only interface that supports advanced features, such as grouping symbols and functions for transforming and validating values.

## Use a list in the Expression Builder

To use a list in the Expression Builder:

1. From the **Operator** drop-down list, select *is in list* or *is not in list*. Note that not all fields support these operators.![Selecting an IP list from the Value drop-down list when configuring the expression of a WAF custom rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=979,height=739,format=webp/_astro/cf-open-proxies-list.DYcEfIK7.png)
2. Select a list from the **Value** drop-down list. Depending on your plan, you may be able to select a [Managed IP List](https://developers.cloudflare.com/waf/tools/lists/managed-lists/#managed-ip-lists).
3. To commit your changes and enable the rule, select **Deploy**. If you are not ready to enable the rule, select **Save as Draft**.

## Use a list in the Expression Editor

To use a list in the Expression Editor, specify the `in` operator and use `$<list_name>` to specify the name of the list.

Examples:

- Expression matching requests from IP addresses that are in an IP list named `office_network`:

  ```txt
  ip.src in $office_network
  ```


- Expression matching requests with a source IP address different from IP addresses in the `office_network` IP list:

  ```txt
  not ip.src in $office_network
  ```


- Expression matching requests from IP addresses in the Cloudflare Open Proxies [Managed IP List](https://developers.cloudflare.com/waf/tools/lists/managed-lists/#managed-ip-lists):

  ```txt
  ip.src in $cf.open_proxies
  ```
