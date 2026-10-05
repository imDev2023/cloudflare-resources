---
description: DNS Analytics and DNS Firewall Analytics now support accounts with Customer Metadata Boundary set to EU.
title: DNS Analytics for Customer Metadata Boundary set to EU region
image: https://developers.cloudflare.com/changelog/post/2026-03-20-dns-analytics-cmb-eu/og.png?v=e769a9b9d6dbb822
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 20, 2026

## DNS Analytics for Customer Metadata Boundary set to EU region

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-20-dns-analytics-cmb-eu/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

DNS Analytics is now available for customers with [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/) (CMB) set to EU. Query your DNS analytics data while keeping metadata stored in the EU region.

This update includes:

- **DNS Analytics** — Access the same DNS analytics experience for zones in CMB=EU accounts.
- **EU data residency** — Analytics data is stored and queried from the EU region, meeting data localization requirements.
- **DNS Firewall Analytics** — DNS Firewall analytics is now supported for CMB=EU customers.

#### Availability

Available to customers with the [Data Localization Suite](https://developers.cloudflare.com/data-localization/) who have Customer Metadata Boundary configured for the EU region.

#### Where to find it

- **Authoritative DNS:** In the Cloudflare dashboard, select your zone and go to the **Analytics** page. [Go to **Analytics** ↗](https://dash.cloudflare.com/?to=/:account/:zone/dns/analytics)
- **DNS Firewall:** In the Cloudflare dashboard, go to the **DNS Firewall Analytics** page. [Go to **Analytics** ↗](https://dash.cloudflare.com/?to=/:account/dns-firewall/analytics)

For more information, refer to [DNS Analytics](https://developers.cloudflare.com/dns/additional-options/analytics/) and [DNS Firewall Analytics](https://developers.cloudflare.com/dns/dns-firewall/analytics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-20-dns-analytics-cmb-eu/#page","headline":"DNS Analytics for Customer Metadata Boundary set to EU region","description":"DNS Analytics and DNS Firewall Analytics now support accounts with Customer Metadata Boundary set to EU.","url":"https://developers.cloudflare.com/changelog/post/2026-03-20-dns-analytics-cmb-eu/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-20-dns-analytics-cmb-eu/og.png?v=e769a9b9d6dbb822","dateModified":"2026-03-20","datePublished":"2026-03-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
