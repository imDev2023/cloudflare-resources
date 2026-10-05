---
description: Precursor brings continuous, session-based behavioral detection to Cloudflare Challenges.
title: Precursor introduces session-based bot detection
image: https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/og.png?v=d28035bc2a43d8af
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 13, 2026

## Precursor introduces session-based bot detection

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.

You can [read the announcement blog ↗︎](https://blog.cloudflare.com/introducing-precursor) for background on why we built Precursor and how session-level behavioral detection works.

With Precursor enabled, Cloudflare can:

- Continuously evaluate behavioral signals across a session
- Re-validate challenge clearance as behavior changes
- Update bot scores with session context
- Provide client-side visibility where none previously existed

It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.

![Animated walkthrough of enabling Precursor in the Cloudflare dashboard](https://developers.cloudflare.com/images/precursor/enabling_precursor.gif)

To learn more, refer to the [Precursor documentation](https://developers.cloudflare.com/cloudflare-challenges/precursor/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/#page","headline":"Precursor introduces session-based bot detection","description":"Precursor brings continuous, session-based behavioral detection to Cloudflare Challenges.","url":"https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/og.png?v=d28035bc2a43d8af","dateModified":"2026-07-13","datePublished":"2026-07-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
