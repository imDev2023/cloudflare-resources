---
description: Bidirectional tunnel health check return packets are accepted by any Magic on-ramp
title: Bidirectional tunnel health checks are compatible with all Magic on-ramps
image: https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/og.png?v=584ad67f07ea4d56
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 5, 2025

## Bidirectional tunnel health checks are compatible with all Magic on-ramps

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.

Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.

There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.

Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/#page","headline":"Bidirectional tunnel health checks are compatible with all Magic on-ramps","description":"Bidirectional tunnel health check return packets are accepted by any Magic on-ramp","url":"https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/og.png?v=584ad67f07ea4d56","dateModified":"2025-09-05","datePublished":"2025-09-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
