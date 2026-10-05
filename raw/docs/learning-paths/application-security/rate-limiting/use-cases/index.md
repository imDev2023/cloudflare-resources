---
description: Explore common use cases and configurations.
title: Use cases
image: https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/use-cases/og.png?v=215a09d42df3bf95
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Use cases

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/use-cases/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The most common uses cases are:

- [Enforce granular access control](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/#enforcing-granular-access-control) to resources. Includes access control based on criteria such as user agent, IP address, referrer, host, country, and world region.
- [Protect against credential stuffing](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/#protecting-against-credential-stuffing) and account takeover attacks.
- [Limit the number of operations](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/#limiting-the-number-of-operations) performed by individual clients. Includes preventing scraping by bots, accessing sensitive data, bulk creation of new accounts, and programmatic buying in ecommerce platforms.
- [Protect REST APIs](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/#protecting-rest-apis) from resource exhaustion (targeted DDoS attacks) and resources from abuse in general.
- [Protect GraphQL APIs](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/#protecting-graphql-apis) by preventing server overload and limiting the number of operations.
