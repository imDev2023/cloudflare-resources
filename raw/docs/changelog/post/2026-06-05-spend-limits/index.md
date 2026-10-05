---
description: Set cost-based budgets on your AI Gateway scoped by model, provider, or custom metadata like user or team.
title: Control AI costs with spend limits
image: https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/og.png?v=1b41f7bafea97168
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 5, 2026

## Control AI costs with spend limits

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.

You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.

Spend limits work with both [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) and [BYOK](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) requests for models with known pricing.

For more details, refer to the [Spend limits documentation](https://developers.cloudflare.com/ai-gateway/features/spend-limits/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/#page","headline":"Control AI costs with spend limits","description":"Set cost-based budgets on your AI Gateway scoped by model, provider, or custom metadata like user or team.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/og.png?v=1b41f7bafea97168","dateModified":"2026-06-05","datePublished":"2026-06-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
