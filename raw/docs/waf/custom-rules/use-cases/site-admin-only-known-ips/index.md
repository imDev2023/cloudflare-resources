---
description: Restrict admin area access to known IP addresses.
title: Require known IP addresses in site admin area
image: https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/og.png?v=17e66c82ee5519a6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Require known IP addresses in site admin area

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If an attack compromises the administrative area of your website, the consequences can be severe. With custom rules, you can protect your site's admin area by blocking requests for access to admin paths that do not come from a known IP address.

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) limits access to the WordPress admin area, `/wp-admin/`, by blocking requests that do not originate from a specified set of IP addresses:

- **When incoming requests match**:

  | Field | Operator | Value | Logic |
  | --- | --- | --- | --- |
  | IP Source Address | is not in | `10.20.30.40` `192.168.1.0/24` | And |
  | URI Path | wildcard | `/wp-admin/*` |  |

  If you are using the expression editor:  
  `(not ip.src in {10.20.30.40 192.168.1.0/24} and http.request.uri.path wildcard "/wp-admin/*")`
- **Then take action**: *Block*

## Other resources

- [Use case: Allow traffic from IP addresses in allowlist only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/)
