---
description: Logpush expands to all plans with included monthly usage and usage-based pricing for exports and transformations.
title: Logpush is now available on all plans with usage-based pricing
image: https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/og.png?v=7979d5002e60a7e2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## Logpush is now available on all plans with usage-based pricing

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

- **Internal exports**: 25 GB per month, then $0.03 per additional GB.
- **External exports**: 25 GB per month, then $0.10 per additional GB.
- **Transformations**: 1 GB per month, then $0.04 per additional GB.

R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/#page","headline":"Logpush is now available on all plans with usage-based pricing","description":"Logpush expands to all plans with included monthly usage and usage-based pricing for exports and transformations.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/og.png?v=7979d5002e60a7e2","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
