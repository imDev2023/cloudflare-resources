---
description: The Google Bard application has been fully replaced with Gemini
title: Google Bard Application replaced by Gemini
image: https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/og.png?v=19e15d2da095eb96
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 22, 2025

## Google Bard Application replaced by Gemini

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Google Bard** application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the **Gemini** application (ID: 1340). Any existing Gateway policies that reference the old Google Bard application will no longer function. To ensure your policies continue to work as intended, you should update them to use the new Gemini application. We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies. For more information about application policies, please see the [Cloudflare Gateway documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/#page","headline":"Google Bard Application replaced by Gemini","description":"The Google Bard application has been fully replaced with Gemini","url":"https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/og.png?v=19e15d2da095eb96","dateModified":"2025-07-22","datePublished":"2025-07-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
