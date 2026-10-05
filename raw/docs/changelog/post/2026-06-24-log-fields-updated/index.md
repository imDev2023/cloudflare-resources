---
description: The WebSocket Analytics Logpush dataset is now available, the Firewall events dataset is now available for account-scope Logpush, and new fields have been added to Email Security Alerts.
title: New WebSocket Analytics Logpush dataset and updated fields
image: https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/og.png?v=1bdc3560c7e4fa1c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 24, 2026

## New WebSocket Analytics Logpush dataset and updated fields

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

- **WebSocket Analytics**: A new dataset with fields including `BytesReceivedClient`, `BytesReceivedOrigin`, `BytesSentClient`, `BytesSentOrigin`, `ClientASN`, `ClientIP`, `ClientRequestHost`, `ClientRequestPath`, `ClientRequestUserAgent`, `ColoCode`, `ConnectionCloseReason`, `ConnectionCloseSource`, `ConnectionID`, `ConnectionTransportCloseCode`, `EdgeEndTimestamp`, `EdgeStartTimestamp`, and `RayID`.

#### Updated fields in existing datasets

- **Firewall events** (added): `ZoneName`. The Firewall events dataset is now also available for [account-scope Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/), in addition to the existing zone scope.
- **Email Security Alerts** (added): `BCC`, `DKIMResult`, `DMARCPolicy`, `DMARCResult`, and `SPFResult`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/#page","headline":"New WebSocket Analytics Logpush dataset and updated fields","description":"The WebSocket Analytics Logpush dataset is now available, the Firewall events dataset is now available for account-scope Logpush, and new fields have been added to Email Security Alerts.","url":"https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/og.png?v=1bdc3560c7e4fa1c","dateModified":"2026-06-24","datePublished":"2026-06-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
