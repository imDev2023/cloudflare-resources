---
description: Create URL redirects with expression-based Single Redirect rules.
title: Single Redirects
image: https://developers.cloudflare.com/rules/url-forwarding/single-redirects/og.png?v=9a4afcd92bb4d952
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Single Redirects

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Single Redirects allow you to create static or dynamic URL redirects. Static redirects send users to a fixed target URL, while dynamic redirects build the target URL from components of the original request. A [wildcard-based](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#wildcard-matching) interface allows you to define source and target URL patterns without complex functions or regular expressions, efficiently handling thousands of URLs with a single rule. Dynamic URL redirects also support advanced features such as string replacement operations and [regular expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/values/#string-values-and-regular-expressions) (depending on your Cloudflare plan).

For more complex and customized redirect logic, consider using [Snippets](https://developers.cloudflare.com/rules/snippets/).

---

## Related resources

- [Availability](https://developers.cloudflare.com/rules/url-forwarding/#availability): Information on the Single Redirects quotas and features per Cloudflare plan.
- [Execution order](https://developers.cloudflare.com/rules/url-forwarding/#execution-order): Execution order of the different Rules products.
- [Trace a request](https://developers.cloudflare.com/rules/trace-request/): Use Cloudflare Trace to determine if a redirect rule is triggering for a specific URL.
