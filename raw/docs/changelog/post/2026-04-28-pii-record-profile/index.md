---
description: A new predefined DLP profile detects records that contain multiple types of personal data, reducing false positives from isolated matches.
title: Detect PII records with a new predefined DLP profile
image: https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/og.png?v=02eba0708a891d10
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 28, 2026

## Detect PII records with a new predefined DLP profile

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: **Personally Identifiable Information (PII) Record**.

Most predefined and custom DLP profiles match when any enabled detection entry matches. The **Personally Identifiable Information (PII) Record** profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.

Detection entries included in the profile:

- AU Passport Number
- American Express Card Number
- Diners Club Card Number
- US Driver's License Number
- Email Address
- Full Name
- US Mailing Address
- Mastercard Card Number
- US Individual Tax Identification Number (ITIN)
- US Passport Number
- US Phone Number
- Union Pay Card Number
- United States SSN Numeric Detection
- Visa Card Number

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/#page","headline":"Detect PII records with a new predefined DLP profile","description":"A new predefined DLP profile detects records that contain multiple types of personal data, reducing false positives from isolated matches.","url":"https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/og.png?v=02eba0708a891d10","dateModified":"2026-04-28","datePublished":"2026-04-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
