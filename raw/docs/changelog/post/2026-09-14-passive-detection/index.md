---
description: Learn from your Gateway traffic with Passive Detection. Explore sensitive data and its destinations to decide where a data protection policy can help.
title: Discover where sensitive data goes before you create a Data Loss Prevention policy
image: https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/og.png?v=378ddbb5cee5b740
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 14, 2026

## Discover where sensitive data goes before you create a Data Loss Prevention policy

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Passive Detection** for [Cloudflare Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) lets you learn from your Gateway traffic before deciding what to log or block. Discover the sensitive data types in sampled traffic, explore their destinations, and use the findings to build policies around your organization's needs.

The dashboard brings together detections from sampled HTTP request and response bodies. Select an entry to follow its detections over time, review destinations, and check policy coverage. You do not need a Gateway DLP policy to get these insights, and existing Gateway policies continue to apply.

![Passive Detection dashboard showing detection totals, data type distribution, policy coverage, and detection entries](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=593,format=webp/_astro/passive-detection.B_-_POtg.gif)

Passive Detection is generally available. The detection entries available to your account depend on your [Zero Trust plan](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

To get started, refer to the [Passive Detection documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/#page","headline":"Discover where sensitive data goes before you create a Data Loss Prevention policy","description":"Learn from your Gateway traffic with Passive Detection. Explore sensitive data and its destinations to decide where a data protection policy can help.","url":"https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/og.png?v=378ddbb5cee5b740","dateModified":"2026-09-14","datePublished":"2026-09-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
