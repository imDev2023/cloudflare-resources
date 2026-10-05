---
description: Customers can now choose their preferred mail processing location to be Germany, India, or Australia during onboarding
title: Regional Email Processing for Germany, India, or Australia
image: https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/og.png?v=08a4b38f134ff8a9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2025

## Regional Email Processing for Germany, India, or Australia

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: **MX**, **BCC**, and **Journaling**.

#### What’s new

Customers can now select where their email is processed. The following regions are supported:

- **Germany**
- **India**
- **Australia**

Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.

#### How to use it

When onboarding a domain with MX, BCC, or Journaling:

1. Select the desired processing location (Germany, India, or Australia).
2. The UI will display updated processing addresses specific to that region.
3. For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.

#### Availability

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

#### What’s next

We’re expanding the list of processing locations to match our [Data Localization Suite (DLS)](https://developers.cloudflare.com/data-localization/) footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/#page","headline":"Regional Email Processing for Germany, India, or Australia","description":"Customers can now choose their preferred mail processing location to be Germany, India, or Australia during onboarding","url":"https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/og.png?v=08a4b38f134ff8a9","dateModified":"2025-09-11","datePublished":"2025-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
