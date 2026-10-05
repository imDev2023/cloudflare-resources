---
description: New visual match scores and threshold controls to better identify brand impersonation.
title: Enhanced Logo Matching for Brand Protection
image: https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/og.png?v=75033bdc1120f371
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2026

## Enhanced Logo Matching for Brand Protection

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have significantly upgraded our Logo Matching capabilities within Brand Protection. While previously limited to approximately 100% matches, users can now detect a wider range of brand assets through a redesigned matching model and UI.

#### What's new

- **Configurable match thresholds**: Users can set a minimum match score (starting at 75%) when creating a logo query to capture subtle variations or high-quality impersonations.
- **Visual match scores**: Allow users to see the exact percentage of the match directly in the results table, highlighted with color-coded lozenges to indicate severity.
- **Direct logo previews**: Available in the Cloudflare dashboard — similar to string matches — to verify infringements at a glance.

#### Key benefits

- **Expose sophisticated impersonators** who use slightly altered logos to bypass basic detection filters.
- **Faster triage** of the most relevant threats immediately using visual indicators, reducing the time spent manually reviewing matches.

Ready to protect your visual identity? Learn more in our [Brand Protection documentation](https://developers.cloudflare.com/security-center/brand-protection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/#page","headline":"Enhanced Logo Matching for Brand Protection","description":"New visual match scores and threshold controls to better identify brand impersonation.","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/og.png?v=75033bdc1120f371","dateModified":"2026-02-12","datePublished":"2026-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
