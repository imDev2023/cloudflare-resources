---
description: New Access service token secrets include a recognizable prefix and checksum for credential scanning tools.
title: Access service token secrets use a scannable format
image: https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/og.png?v=5fd7390183551167
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## Access service token secrets use a scannable format

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format `cfast_[40 alphanumeric characters][8-character checksum]`. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.

Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same `CF-Access-Client-Id` and `CF-Access-Client-Secret` authentication headers.

For more information, refer to [Service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/#page","headline":"Access service token secrets use a scannable format","description":"New Access service token secrets include a recognizable prefix and checksum for credential scanning tools.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/og.png?v=5fd7390183551167","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
