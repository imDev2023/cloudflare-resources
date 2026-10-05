---
description: New Logpush datasets are now available, and fields have been updated across multiple Logpush datasets in Cloudflare Logs.
title: New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs
image: https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/og.png?v=49706df5bcb696c4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 20, 2026

## New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

- **Account Abuse Protection Events**: A new dataset with fields including `AuthenticationIdentityProvider`, `AuthenticationMethod`, `AuthenticationStatus`, `BotScore`, `ClientASN`, `ClientCity`, `ClientCountry`, `ClientIP`, `Email`, `EphemeralID`, `EventSource`, `EventType`, `FraudEmailRisk`, `Host`, `JA4`, `RayID`, `Timestamp`, `UserAgent`, and `UserID`.
- **Magic BGP Logs**: A new dataset with fields including `Direction`, `EventData`, `EventKind`, `EventTimestamp`, `TunnelID`, and `TunnelName`.

#### Updated fields in existing datasets

- **Firewall events** (added): `AISecurityCustomTopicCategories`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.
- **Gateway HTTP** (added): `ExperimentalFeatures` and `PackageInfo`.
- **HTTP requests** (added): `AISecurityCustomTopicCategories`, `ClientTLSKeyExchangeGroup`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/#page","headline":"New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs","description":"New Logpush datasets are now available, and fields have been updated across multiple Logpush datasets in Cloudflare Logs.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/og.png?v=49706df5bcb696c4","dateModified":"2026-08-20","datePublished":"2026-08-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
