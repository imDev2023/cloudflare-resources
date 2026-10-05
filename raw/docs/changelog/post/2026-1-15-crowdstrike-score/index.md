---
description: Cloudflare One now supports two new risk scoring behaviors based on CrowdStrike device posture attributes.
title: Support for CrowdStrike device scores in User Risk Scoring
image: https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/og.png?v=90bb621d6b580a2b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 15, 2026

## Support for CrowdStrike device scores in User Risk Scoring

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One has expanded its \[User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the \[CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).

Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.

New risk behaviors The following risk scoring behaviors are now available:

- CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a "Low" score from CrowdStrike.
- CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a "Medium" score from CrowdStrike.

These scores are derived from \[CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/#page","headline":"Support for CrowdStrike device scores in User Risk Scoring","description":"Cloudflare One now supports two new risk scoring behaviors based on CrowdStrike device posture attributes.","url":"https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/og.png?v=90bb621d6b580a2b","dateModified":"2026-01-15","datePublished":"2026-01-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
