---
description: Privacy Proxy metrics are now queryable through the GraphQL Analytics API, the new default method for accessing observability data. Four nodes cover requests, ingress connections, egress connections, and authentication.
title: Privacy Proxy metrics now available via GraphQL Analytics API
image: https://developers.cloudflare.com/changelog/post/2026-04-15-graphql-analytics-api/og.png?v=bfc29550e8768558
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2026

## Privacy Proxy metrics now available via GraphQL Analytics API

[Privacy Proxy](https://developers.cloudflare.com/privacy-proxy/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-graphql-analytics-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Privacy Proxy metrics are now queryable through Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/), the new default method for accessing Privacy Proxy observability data. All metrics are available through a single endpoint:

```bash
curl https://api.cloudflare.com/client/v4/graphql \
  --header "Authorization: Bearer <API_TOKEN>" \
  --header "Content-Type: application/json" \
  --data '{
    "query": "{ viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }",
    "variables": {
      "accountTag": "<YOUR_ACCOUNT_TAG>",
      "startDate": "2026-04-04",
      "endDate": "2026-04-06"
    }
  }'
```

#### Available nodes

Four GraphQL nodes are now live, providing aggregate metrics across all key dimensions of your Privacy Proxy deployment:

- **`privacyProxyRequestMetricsAdaptiveGroups`** — Request volume, error rates, status codes, and proxy status breakdowns.
- **`privacyProxyIngressConnMetricsAdaptiveGroups`** — Client-to-proxy connection counts, bytes transferred, and latency percentiles.
- **`privacyProxyEgressConnMetricsAdaptiveGroups`** — Proxy-to-origin connection counts, bytes transferred, and latency percentiles.
- **`privacyProxyAuthMetricsAdaptiveGroups`** — Authentication attempt counts by method and result.

All nodes support filtering by time, data center (`coloCode`), and endpoint, with additional node-specific dimensions such as transport protocol and authentication method.

#### What this means for existing OpenTelemetry users

OpenTelemetry-based metrics export remains available. The GraphQL Analytics API is now the recommended default method — a plug-and-play method that requires no collector infrastructure, saving engineering overhead.

#### Learn more

- [GraphQL Analytics API for Privacy Proxy](https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/)
- [GraphQL Analytics API — getting started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-graphql-analytics-api/#page","headline":"Privacy Proxy metrics now available via GraphQL Analytics API","description":"Privacy Proxy metrics are now queryable through the GraphQL Analytics API, the new default method for accessing observability data. Four nodes cover requests, ingress connections, egress connections, and authentication.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-graphql-analytics-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-15-graphql-analytics-api/og.png?v=bfc29550e8768558","dateModified":"2026-04-15","datePublished":"2026-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
