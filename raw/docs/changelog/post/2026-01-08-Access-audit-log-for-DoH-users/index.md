---
description: Cloudflare admin activity logs display when a DoH user is created.
title: Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users
image: https://developers.cloudflare.com/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/og.png?v=7a8f1b68e3ec0fe6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 8, 2026

## Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare [admin activity logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/) now capture each time a [DNS over HTTP (DoH) user](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/) is created.

These logs can be viewed from the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com/), pulled via the [Cloudflare API](https://developers.cloudflare.com/api/), and exported through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/#page","headline":"Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users","description":"Cloudflare admin activity logs display when a DoH user is created.","url":"https://developers.cloudflare.com/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/og.png?v=7a8f1b68e3ec0fe6","dateModified":"2026-01-08","datePublished":"2026-01-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
