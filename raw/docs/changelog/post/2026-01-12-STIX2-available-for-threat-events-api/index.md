---
description: Customers can now export threat events in STIX2 format for seamless integration with TIP, SIEM, and SOAR platforms.
title: Cloudflare Threat Events now support STIX2 format
image: https://developers.cloudflare.com/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/og.png?v=aa6b32cb1ddd48c4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 12, 2026

## Cloudflare Threat Events now support STIX2 format

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are excited to announce that **Cloudflare Threat Events** now supports the **STIX2 (Structured Threat Information Expression)** format. This was a highly requested feature designed to streamline how security teams consume and act upon our threat intelligence.

By adopting this industry-standard format, you can now integrate Cloudflare's threat events data more effectively into your existing security ecosystem.

#### Key benefits

- Eliminate the need for custom parsers, as STIX2 allows for "out of the box" ingestion into major **Threat Intel Platforms (TIPs)**, **SIEMs**, and **SOAR** tools.
- STIX2 provides a standardized way to represent relationships between indicators, sightings, and threat actors, giving your analysts a clearer picture of the threat landscape.

For technical details on how to query events using this format, please refer to our [Threat Events API Documentation ↗︎](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/).

---

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/#page","headline":"Cloudflare Threat Events now support STIX2 format","description":"Customers can now export threat events in STIX2 format for seamless integration with TIP, SIEM, and SOAR platforms.","url":"https://developers.cloudflare.com/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/og.png?v=aa6b32cb1ddd48c4","dateModified":"2026-01-12","datePublished":"2026-01-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
