---
description: Find DNS records shadowed by a delegation.
title: Shadowed record warnings are now available for all zones
image: https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/og.png?v=37389350437c264b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 14, 2026

## Shadowed record warnings are now available for all zones

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.

Shadow metadata is also available in DNS records API responses when you set `include_shadow_metadata=true`. The metadata identifies the delegating `NS` records and, when applicable, whether an `A` or `AAAA` record is glue. For more information, refer to [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/#page","headline":"Shadowed record warnings are now available for all zones","description":"Find DNS records shadowed by a delegation.","url":"https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/og.png?v=37389350437c264b","dateModified":"2026-09-14","datePublished":"2026-09-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
