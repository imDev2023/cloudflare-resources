---
description: Review detailed logs of cache purge requests to track activity and verify content revalidation targets.
title: Audit Logs for Cache Purge Events
image: https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/og.png?v=f3b2fda3d47f2ce9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 25, 2025

## Audit Logs for Cache Purge Events

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now review detailed audit logs for cache purge events, giving you visibility into what purge requests were sent, what they contained, and by whom. Audit your purge requests via the Dashboard or API for all purge methods:

- Purge everything
- List of prefixes
- List of tags
- List of hosts
- List of files

#### Example

The detailed audit payload is visible within the Cloudflare Dashboard (under **Manage Account** > **Audit Logs**) and via the API. Below is an example of the Audit Logs v2 payload structure:

```json
{
  "action": {
    "result": "success",
    "type": "create"
  },
  "actor": {
    "id": "1234567890abcdef",
    "email": "user@example.com",
    "type": "user"
  },
  "resource": {
    "product": "purge_cache",
    "request": {
      "files": [
        "https://example.com/images/logo.png",
        "https://example.com/css/styles.css"
      ]
    }
  },
  "zone": {
    "id": "023e105f4ecef8ad9ca31a8372d0c353",
    "name": "example.com"
  }
}
```

#### Get started

To get started, refer to the [Audit Logs documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/#page","headline":"Audit Logs for Cache Purge Events","description":"Review detailed logs of cache purge requests to track activity and verify content revalidation targets.","url":"https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/og.png?v=f3b2fda3d47f2ce9","dateModified":"2025-11-25","datePublished":"2025-11-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
