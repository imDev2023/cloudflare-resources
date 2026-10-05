---
description: Zero Trust Network Session Logs are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type.
title: Network Session Logs now available for all on-ramps
image: https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/og.png?v=a58a9fdfc84cd96b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 24, 2026

## Network Session Logs now available for all on-ramps

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from [proxy endpoints (PAC files)](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) egress — on-ramps that previously did not generate session logs.

Customers who already consume the `zero_trust_network_sessions` dataset via [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) or [Log Explorer](https://developers.cloudflare.com/log-explorer/) may see increased log volume if they use these on-ramps.

For field definitions, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/). For traffic analysis, refer to [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/#page","headline":"Network Session Logs now available for all on-ramps","description":"Zero Trust Network Session Logs are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type.","url":"https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/og.png?v=a58a9fdfc84cd96b","dateModified":"2026-04-24","datePublished":"2026-04-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
