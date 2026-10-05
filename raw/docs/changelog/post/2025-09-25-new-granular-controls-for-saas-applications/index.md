---
description: Gateway now provides granular control over File Sharing and AI Chat applications
title: Application granular controls for operations in SaaS applications
image: https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/og.png?v=7f29399825cb057d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2025

## Application granular controls for operations in SaaS applications

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway users can now apply granular controls to their file sharing and AI chat applications through [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies).

The new feature offers two methods of controlling SaaS applications:

- **Application Controls** are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include *Upload*, *Download*, *Prompt*, *Voice*, and *Share* depending on the application.
- **Operations** are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.

Get started using [Application Granular Controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls) and refer to the list of [supported applications](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/#page","headline":"Application granular controls for operations in SaaS applications","description":"Gateway now provides granular control over File Sharing and AI Chat applications","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/og.png?v=7f29399825cb057d","dateModified":"2025-09-30","datePublished":"2025-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
