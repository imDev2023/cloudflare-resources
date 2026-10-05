---
description: Cloudflare Advanced Network Firewall Country rules now work with Unified Routing mode.
title: Country rules supported in Unified Routing
image: https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/og.png?v=ca46e6bd1e446937
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2026

## Country rules supported in Unified Routing

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Country rules are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. This feature requires a Cloudflare Advanced Network Firewall subscription.

You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.

This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/#page","headline":"Country rules supported in Unified Routing","description":"Cloudflare Advanced Network Firewall Country rules now work with Unified Routing mode.","url":"https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/og.png?v=ca46e6bd1e446937","dateModified":"2026-04-21","datePublished":"2026-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
