---
description: API Shield now automatically labels inactive saved endpoints with the cf-risk-zombie risk label.
title: New Zombie API detection for API Shield
image: https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/og.png?v=5b8c5146d781f91f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 25, 2025

## New Zombie API detection for API Shield

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the `cf-risk-zombie` [risk label](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#risk-labels) is applied.

The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.

Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a [fallthrough rule](https://developers.cloudflare.com/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule) to prevent communication with endpoints removed from Endpoint Management.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/#page","headline":"New Zombie API detection for API Shield","description":"API Shield now automatically labels inactive saved endpoints with the cf-risk-zombie risk label.","url":"https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/og.png?v=5b8c5146d781f91f","dateModified":"2025-11-25","datePublished":"2025-11-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
