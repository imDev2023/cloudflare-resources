---
description: Paid plans can now deploy Pages sites with up to 100,000 files, increased from the previous limit of 20,000 files.
title: Increased Pages file limit to 100,000 for paid plans
image: https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/og.png?v=29299fd21b6ecf8c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 23, 2026

## Increased Pages file limit to 100,000 for paid plans

[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Paid plans can now have up to 100,000 files per Pages site, increased from the previous limit of 20,000 files.

To enable this increased limit, set the environment variable `PAGES_WRANGLER_MAJOR_VERSION=4` in your Pages project settings.

The Free plan remains at 20,000 files per site.

For more details, refer to the [Pages limits documentation](https://developers.cloudflare.com/pages/platform/limits/#files).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/#page","headline":"Increased Pages file limit to 100,000 for paid plans","description":"Paid plans can now deploy Pages sites with up to 100,000 files, increased from the previous limit of 20,000 files.","url":"https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/og.png?v=29299fd21b6ecf8c","dateModified":"2026-01-23","datePublished":"2026-01-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
