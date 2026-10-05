---
description: Enterprise customers can now raise a zone's maximum CDN request body size to 5 GB from the Cloudflare dashboard without contacting Support.
title: Enterprise customers can self-serve CDN upload limits up to 5 GB
image: https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/og.png?v=817e2f3a26a36e8e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 4, 2026

## Enterprise customers can self-serve CDN upload limits up to 5 GB

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now configure a zone's CDN **Maximum Upload Size** up to 5 GB directly from the **Network** page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.

The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.

Refer to [Cache upload limits](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits) and [Workers request body size limits](https://developers.cloudflare.com/workers/platform/limits/#request-and-response-limits) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/#page","headline":"Enterprise customers can self-serve CDN upload limits up to 5 GB","description":"Enterprise customers can now raise a zone's maximum CDN request body size to 5 GB from the Cloudflare dashboard without contacting Support.","url":"https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/og.png?v=817e2f3a26a36e8e","dateModified":"2026-09-04","datePublished":"2026-09-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
