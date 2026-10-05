---
description: Simplified setup for Cloudflare's CSAM Scanning Tool, improving child safety protections for websites.
title: Fight CSAM More Easily Than Ever
image: https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/og.png?v=0b2e69e1e2960875
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 4, 2025

## Fight CSAM More Easily Than Ever

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now implement our **child safety tooling**, the **[CSAM Scanning Tool](https://developers.cloudflare.com/cache/reference/csam-scanning/)**, more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.

**How It Works**

When enabled, the tool automatically [hashes images for enabled websites as they enter the Cloudflare cache ↗︎](https://blog.cloudflare.com/the-csam-scanning-tool/). These hashes are then checked against a database of **known abusive images**.

- **Potential match detected?**
  - The **content URL is blocked**, and
  - **Cloudflare will notify you** about the found matches via the provided email address.

**Updated Service-Specific Terms**

We have also made updates to our **[Service-Specific Terms ↗︎](https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms)** to reflect these changes.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/#page","headline":"Fight CSAM More Easily Than Ever","description":"Simplified setup for Cloudflare's CSAM Scanning Tool, improving child safety protections for websites.","url":"https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/og.png?v=0b2e69e1e2960875","dateModified":"2025-02-04","datePublished":"2025-02-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
