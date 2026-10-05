---
description: Enterprise accounts now have a single DNS records quota across all of their zones.
title: Account-level DNS records quota
image: https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/og.png?v=ae62f15a756cbe4a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 10, 2026

## Account-level DNS records quota

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.

Accounts without an account-level quota are unaffected: existing per-zone quotas behave exactly as before.

For more details, refer to [DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/#page","headline":"Account-level DNS records quota","description":"Enterprise accounts now have a single DNS records quota across all of their zones.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/og.png?v=ae62f15a756cbe4a","dateModified":"2026-06-10","datePublished":"2026-06-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
