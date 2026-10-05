---
description: Preview potential logo matches and adjust similarity thresholds before saving your Brand Protection queries
title: Real-time logo match preview
image: https://developers.cloudflare.com/changelog/post/2026-03-18-brand-protection-logo-match-preview/og.png?v=85b3b9717dc2b25d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2026

## Real-time logo match preview

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-18-brand-protection-logo-match-preview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are introducing **Logo Match Preview**, bringing the same pre-save visibility to visual assets that was previously only available for string-based queries. This update allows you to fine-tune your brand detection strategy before committing to a live monitor.

#### What’s new:

- Upload your brand logo and immediately see a sample of potential matches from recently detected sites before finalizing the query
- Adjust your similarity score (from 75% to 100%) and watch the results refresh in real-time to find the balance between broad detection and noise reduction
- Review the specific logos triggered by your current settings to ensure your query is capturing the right level of brand infringement

If you are ready to test your brand assets, go to the [Brand Protection dashboard ↗︎](https://developers.cloudflare.com/security-center/brand-protection/) to try the new preview tool.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-18-brand-protection-logo-match-preview/#page","headline":"Real-time logo match preview","description":"Preview potential logo matches and adjust similarity thresholds before saving your Brand Protection queries","url":"https://developers.cloudflare.com/changelog/post/2026-03-18-brand-protection-logo-match-preview/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-18-brand-protection-logo-match-preview/og.png?v=85b3b9717dc2b25d","dateModified":"2026-03-18","datePublished":"2026-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
