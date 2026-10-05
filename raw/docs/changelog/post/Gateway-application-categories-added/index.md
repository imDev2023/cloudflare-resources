---
description: Manage outbound traffic with more granular application categories
title: New Application Categories added for HTTP Traffic Management
image: https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/og.png?v=eee2ced376b445ed
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 28, 2025

## New Application Categories added for HTTP Traffic Management

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To give you precision and flexibility while creating policies to block unwanted traffic, we are introducing new, more granular application categories in the Gateway product.

We have added the following categories to provide more precise organization and allow for finer-grained policy creation, designed around how users interact with different types of applications:

- Business
- Education
- Entertainment & Events
- Food & Drink
- Health & Fitness
- Lifestyle
- Navigation
- Photography & Graphic Design
- Travel

The new categories are live now, but we are providing a transition period for existing applications to be fully remapped to these new categories.

The full remapping will be completed by January 30, 2026.

We encourage you to use this time to:

- Review the new category structure.
- Identify and adjust any existing HTTP policies that reference older categories to ensure a smooth transition.

For more information on creating HTTP policies, refer to [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/#page","headline":"New Application Categories added for HTTP Traffic Management","description":"Manage outbound traffic with more granular application categories","url":"https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/og.png?v=eee2ced376b445ed","dateModified":"2025-10-28","datePublished":"2025-10-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
