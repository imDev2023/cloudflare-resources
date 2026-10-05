---
description: Cloudflare DNSSEC supports NSEC3 for proof of non-existence.
title: NSEC3 support for DNSSEC
image: https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/og.png?v=09273b36b09d4cdd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 11, 2025

## NSEC3 support for DNSSEC

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.

What's new:

- **NSEC3 support for live-signed zones** – For both primary and secondary zones that are configured to be live-signed (also known as "on-the-fly signing"), NSEC3 can now be selected as proof of non-existence.
- **NSEC3 support for pre-signed zones** – Secondary zones that are transferred to Cloudflare in a [pre-signed setup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec) now also support NSEC3 as proof of non-existence.

For more information and how to enable NSEC3, refer to the [NSEC3 documentation](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/#page","headline":"NSEC3 support for DNSSEC","description":"Cloudflare DNSSEC supports NSEC3 for proof of non-existence.","url":"https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/og.png?v=09273b36b09d4cdd","dateModified":"2025-06-11","datePublished":"2025-06-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
