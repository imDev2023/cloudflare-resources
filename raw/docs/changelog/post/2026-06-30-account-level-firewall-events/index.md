---
description: Stream firewall events for every zone in an account through a single Logpush job, with a new ZoneName field to identify the source zone.
title: Account-scoped firewall events dataset in Logpush
image: https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/og.png?v=6bc91ad872c78ab7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 30, 2026

## Account-scoped firewall events dataset in Logpush

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush now supports [firewall events as an account-scoped dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/). Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.

The dataset includes a new [`ZoneName`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename) field so you can identify which zone each event came from when consuming logs in your downstream pipeline.

#### What's available

- A new account-scoped `firewall_events` dataset, configurable via the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/) or the Cloudflare dashboard.
- The same fields and filter expressions supported by the existing [zone-scoped firewall events dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/), plus the new `ZoneName` field.
- Support for all existing Logpush destinations.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/#page","headline":"Account-scoped firewall events dataset in Logpush","description":"Stream firewall events for every zone in an account through a single Logpush job, with a new ZoneName field to identify the source zone.","url":"https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/og.png?v=6bc91ad872c78ab7","dateModified":"2026-06-30","datePublished":"2026-06-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
