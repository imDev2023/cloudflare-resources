---
description: We have upgraded and streamlined limits for Cloudflare Rules products for everyone.
title: Increased Cloudflare Rules limits
image: https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/og.png?v=48dcce32c1ebcc7c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2025

## Increased Cloudflare Rules limits

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have upgraded and streamlined [Cloudflare Rules](https://developers.cloudflare.com/rules/) limits across all plans, simplifying rule management and improving scalability for everyone.

**New limits by product:**

- [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)
  - Free: **20** → **10,000** URL redirects across lists
  - Pro: **500** → **25,000** URL redirects across lists
  - Business: **500** → **50,000** URL redirects across lists
  - Enterprise: **10,000** → **1,000,000** URL redirects across lists
- [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)
  - Free: **5** → **10** connectors
  - Enterprise: **125** → **300** connectors
- [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)
  - Pro: **5** → **25** error assets and rules
  - Business: **20** → **50** error assets and rules
  - Enterprise: **50** → **300** error assets and rules
- [Snippets](https://developers.cloudflare.com/rules/snippets/)
  - Pro: **10** → **25** code snippets and rules
  - Business: **25** → **50** code snippets and rules
  - Enterprise: **50** → **300** code snippets and rules
- [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/), [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/), [Compression Rules](https://developers.cloudflare.com/rules/compression-rules/), [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/), [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/), and [Transform Rules](https://developers.cloudflare.com/rules/transform/)
  - Enterprise: **125** → **300** rules

Gradual rollout

Limits are updated gradually. Some customers may still see previous limits until the rollout is fully completed in the first half of 2025.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/#page","headline":"Increased Cloudflare Rules limits","description":"We have upgraded and streamlined limits for Cloudflare Rules products for everyone.","url":"https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/og.png?v=48dcce32c1ebcc7c","dateModified":"2025-02-12","datePublished":"2025-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
