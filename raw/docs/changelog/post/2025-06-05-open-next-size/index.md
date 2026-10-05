---
description: Update to the latest version of `@opennextjs/cloudflare` to automatically benefit from these improvements.
title: Performance and size optimization for the Cloudflare adapter for Open Next
image: https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/og.png?v=5cd05d34e15e99c6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 5, 2025

## Performance and size optimization for the Cloudflare adapter for Open Next

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans [to improve performance and size ↗︎](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead).

`@opennextjs/cloudflare` v1.2 released on June 5, 2025 delivers on these enhancements. By removing `babel` from the app code and dropping a dependency on `@ampproject/toolbox-optimizer`, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.

This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.

Users only need to update to the latest version of `@opennextjs/cloudflare` to automatically benefit from these improvements.

Note that we published [CVE-2005-6087 ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m) for a SSRF vulnerability in the `@opennextjs/cloudflare` package. The vulnerability has been fixed from `@opennextjs/cloudflare` v1.3.0 onwards. Please update to any version after this one.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/#page","headline":"Performance and size optimization for the Cloudflare adapter for Open Next","description":"Update to the latest version of @opennextjs/cloudflare to automatically benefit from these improvements.","url":"https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/og.png?v=5cd05d34e15e99c6","dateModified":"2025-06-05","datePublished":"2025-06-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
