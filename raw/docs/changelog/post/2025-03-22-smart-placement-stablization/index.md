---
description: Workers and Pages Functions with Smart Placement enabled will not unexpectedly return to default locations if request traffic dips.
title: Smart Placement is smarter about running Workers and Pages Functions in the best locations
image: https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/og.png?v=00b8cc4349af8c47
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 22, 2025

## Smart Placement is smarter about running Workers and Pages Functions in the best locations

[Workers](https://developers.cloudflare.com/workers/) [Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/) is a unique Cloudflare feature that can make decisions to move your Worker to run in a more optimal location (such as closer to a database). Instead of always running in the default location (the one closest to where the request is received), Smart Placement uses certain “heuristics” (rules and thresholds) to decide if a different location might be faster or more efficient.

Previously, if these heuristics weren't consistently met, your Worker would revert to running in the default location—even after it had been optimally placed. This meant that if your Worker received minimal traffic for a period of time, the system would reset to the default location, rather than remaining in the optimal one.

Now, once Smart Placement has identified and assigned an optimal location, temporarily dropping below the heuristic thresholds will not force a return to default locations. For example in the previous algorithm, a drop in requests for a few days might return to default locations and heuristics would have to be met again. This was problematic for workloads that made requests to a geographically located resource every few days or longer. In this scenario, your Worker would never get placed optimally. This is no longer the case.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/#page","headline":"Smart Placement is smarter about running Workers and Pages Functions in the best locations","description":"Workers and Pages Functions with Smart Placement enabled will not unexpectedly return to default locations if request traffic dips.","url":"https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/og.png?v=00b8cc4349af8c47","dateModified":"2025-03-22","datePublished":"2025-03-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
