---
description: Query matched operation IDs and managed labels per request using the httpRequestsAdaptive and httpRequestsAdaptiveGroups GraphQL datasets.
title: Web Assets fields now available in GraphQL Analytics API
image: https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/og.png?v=70221221da06fb47
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 23, 2026

## Web Assets fields now available in GraphQL Analytics API

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Two new fields are now available in the `httpRequestsAdaptive` and `httpRequestsAdaptiveGroups` [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) datasets:

- `webAssetsOperationId` — the ID of the [saved endpoint](https://developers.cloudflare.com/api-shield/management-and-monitoring/) that matched the incoming request.
- `webAssetsLabelsManaged` — the [managed labels](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#managed-labels) mapped to the matched operation at the time of the request (for example, `cf-llm`, `cf-log-in`). At most 10 labels are returned per request.

Both fields are empty when no operation matched. `webAssetsLabelsManaged` is also empty when no managed labels are assigned to the matched operation.

These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) did or did not flag a request.

Refer to [Endpoint labeling service](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#analytics) for GraphQL query examples.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/#page","headline":"Web Assets fields now available in GraphQL Analytics API","description":"Query matched operation IDs and managed labels per request using the httpRequestsAdaptive and httpRequestsAdaptiveGroups GraphQL datasets.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/og.png?v=70221221da06fb47","dateModified":"2026-03-23","datePublished":"2026-03-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
