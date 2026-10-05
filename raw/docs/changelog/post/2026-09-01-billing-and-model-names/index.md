---
description: AI Gateway monthly usage invoices now show the total cost per model, while invoices and logs use consistent model names.
title: AI Gateway consolidates monthly usage invoice line items and standardizes model names
image: https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/og.png?v=3413985c49befaf8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 1, 2026

## AI Gateway consolidates monthly usage invoice line items and standardizes model names

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.

For example, an invoice that previously included these separate line items:

- `anthropic claude-haiku-4-5-20251001 Input Tokens`: 40,000 tokens at $0.000001 ($0.04)
- `anthropic claude-haiku-4-5-20251001 Output Tokens`: 24,000 tokens at $0.000005 ($0.12)

The updated invoice includes one line item: `anthropic/claude-haiku-4.5`: $0.16.

AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent `provider/model` identifier.

For more information, refer to the [Unified Billing documentation](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) and [AI Gateway logging documentation](https://developers.cloudflare.com/ai-gateway/observability/logging/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/#page","headline":"AI Gateway consolidates monthly usage invoice line items and standardizes model names","description":"AI Gateway monthly usage invoices now show the total cost per model, while invoices and logs use consistent model names.","url":"https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/og.png?v=3413985c49befaf8","dateModified":"2026-09-01","datePublished":"2026-09-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
