---
description: Scan GraphQL traffic and block queries that could overload your origin.
title: GraphQL malicious query protection
image: https://developers.cloudflare.com/api-shield/security/graphql-protection/og.png?v=28a2d411af4a980b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/api-shield/llms.txt  
> Use this file to discover all available pages before exploring further.

# GraphQL malicious query protection

Last updated Sep 29, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/api-shield/security/graphql-protection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

GraphQL is a query language for APIs. In addition to protecting RESTful APIs, Cloudflare can also protect GraphQL APIs.

GraphQL malicious query protection scans your GraphQL traffic for queries that could overload your origin and result in a denial of service. Query size is the number of terminal fields, or leaves, in a query. You can build rules that limit the query depth and size of incoming GraphQL queries in order to block suspiciously large or complex queries.

## Availability

GraphQL malicious query protection is available for all API Shield customers. Enterprise customers who have not purchased API Shield can preview [API Shield as a non-contract service ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield) in the Cloudflare dashboard or by contacting your account team.

## Limitations

The following limitations apply:

- Parsing is limited to GraphQL `POST` bodies up to 20 KiB. This limit will be raised in a future release.
- Only `POST` requests with content types of `application/json` or `application/graphql` are inspected.
- Queries containing fragments or multiple operations are not supported.
- Parsing and rules are limited to paths with the case-sensitive `/graphql` suffix.
