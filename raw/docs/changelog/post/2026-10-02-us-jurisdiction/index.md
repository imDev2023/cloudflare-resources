---
description: Create D1 databases that remain within the United States.
title: United States jurisdiction
image: https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/og.png?v=d30d6bbc9df715e5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## United States jurisdiction

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:

```sh
npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us
```

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/#page","headline":"United States jurisdiction","description":"Create D1 databases that remain within the United States.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/og.png?v=d30d6bbc9df715e5","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
