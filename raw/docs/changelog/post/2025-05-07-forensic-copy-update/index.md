---
description: HTTP policies can now be configured to send forensic copies for all allow and block policies.
title: Send forensic copies to storage without DLP profiles
image: https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/og.png?v=92a6415979c95e99
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2025

## Send forensic copies to storage without DLP profiles

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now [send DLP forensic copies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination) to third-party storage for any HTTP policy with an `Allow` or `Block` action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.

By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1324,height=636,format=webp/_astro/forensic-copies-for-all.fxeFrCY4.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/#page","headline":"Send forensic copies to storage without DLP profiles","description":"HTTP policies can now be configured to send forensic copies for all allow and block policies.","url":"https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/og.png?v=92a6415979c95e99","dateModified":"2025-05-07","datePublished":"2025-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
