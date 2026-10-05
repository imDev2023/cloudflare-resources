---
description: All Cloudflare plans can purge by tag, prefix, url, host, or everything to invalidate cached content on the fly.
title: All cache purge methods now available for all plans
image: https://developers.cloudflare.com/changelog/post/2025-04-01-purge-for-all/og.png?v=aaa022b46329356d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 3, 2025

## All cache purge methods now available for all plans

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-01-purge-for-all/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now access all Cloudflare cache purge methods — no matter which plan you’re on. Whether you need to update a single asset or instantly invalidate large portions of your site’s content, you now have the same powerful tools previously reserved for Enterprise customers.

**Anyone on Cloudflare can now:**

1. [Purge Everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/): Clears all cached content associated with a website.
2. [Purge by Prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/): Targets URLs sharing a common prefix.
3. [Purge by Hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/): Invalidates content by specific hostnames.
4. [Purge by URL (single-file purge)](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/): Precisely targets individual URLs.
5. [Purge by Tag](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/): Uses Cache-Tag response headers to invalidate grouped assets, offering flexibility for complex cache management scenarios.

Want to learn how each purge method works, when to use them, or what limits apply to your plan? Dive into our [purge cache documentation](https://developers.cloudflare.com/cache/how-to/purge-cache/) and [API reference ↗︎](https://developers.cloudflare.com/api/resources/cache/methods/purge/) for all the details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-01-purge-for-all/#page","headline":"All cache purge methods now available for all plans","description":"All Cloudflare plans can purge by tag, prefix, url, host, or everything to invalidate cached content on the fly.","url":"https://developers.cloudflare.com/changelog/post/2025-04-01-purge-for-all/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-01-purge-for-all/og.png?v=aaa022b46329356d","dateModified":"2025-04-03","datePublished":"2025-04-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
