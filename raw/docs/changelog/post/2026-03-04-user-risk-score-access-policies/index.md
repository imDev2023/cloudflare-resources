---
description: Use user risk scores to control access to your applications.
title: User risk score selector in Access policies
image: https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/og.png?v=f18c9288e6e0321c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 4, 2026

## User risk score selector in Access policies

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use [user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) in your [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). The new **User Risk Score** selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.

For more information, refer to [Use risk scores in Access policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/#page","headline":"User risk score selector in Access policies","description":"Use user risk scores to control access to your applications.","url":"https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/og.png?v=f18c9288e6e0321c","dateModified":"2026-03-04","datePublished":"2026-03-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
