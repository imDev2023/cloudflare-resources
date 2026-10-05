---
description: See how much your organization spends on AI, attribute it to identities, and flag anomalous usage that can signal a security risk.
title: Track AI spend and catch anomalous usage with User Insights
image: https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/og.png?v=7918459bb1c0d047
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 5, 2026

## Track AI spend and catch anomalous usage with User Insights

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now includes User Insights, a dashboard that gives you two things at once: clear visibility into how much your organization spends on AI, and a security signal that surfaces users whose usage suddenly looks abnormal. It works on the traffic already flowing through your gateway, so there is no additional setup.

On the spend side, User Insights shows organization-wide totals for cost, requests, tokens, and adoption, and lets you drill into an individual user to see their spend, top models and providers, cache hit rate, and more. To attribute usage to individual users, add a user identifier with custom metadata or put your gateway behind Cloudflare Access.

On the security side, User Insights baselines each user's normal usage from their 95th percentile (p95) session cost over the last 30 days, then flags sessions that exceed both that baseline and an organization-level threshold. A sudden jump above a user's own pattern is often the first sign of a compromised credential or a misbehaving agent, so you can investigate before it shows up on your bill.

User Insights is available to all AI Gateway customers at no additional cost.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/#page","headline":"Track AI spend and catch anomalous usage with User Insights","description":"See how much your organization spends on AI, attribute it to identities, and flag anomalous usage that can signal a security risk.","url":"https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/og.png?v=7918459bb1c0d047","dateModified":"2026-08-05","datePublished":"2026-08-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
