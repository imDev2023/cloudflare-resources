---
description: Newly uploaded user Worker scripts are now immediately available for dispatch upon a successful API response.
title: Workers for Platforms - Instant dispatch for newly created User Workers
image: https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/og.png?v=fcd1414f9da8809f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 20, 2025

## Workers for Platforms - Instant dispatch for newly created User Workers

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers for Platforms ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/) is an architecture wherein a centralized [dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker) processes incoming requests and routes them to isolated sub-Workers, called [User Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers).

![Workers for Platforms Requests](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=711,format=webp/_astro/wfp-request.CZmZLaYf.png)

Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.

**With this update, first-time uploads of User Workers are now deployed synchronously**. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/#page","headline":"Workers for Platforms - Instant dispatch for newly created User Workers","description":"Newly uploaded user Worker scripts are now immediately available for dispatch upon a successful API response.","url":"https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/og.png?v=fcd1414f9da8809f","dateModified":"2025-02-20","datePublished":"2025-02-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
