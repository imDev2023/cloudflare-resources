---
description: Workers can now be deployed and rolled back to their most recent 100 versions, up from the previous limit of 10.
title: Worker version rollback limit increased from 10 to 100
image: https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/og.png?v=aa5d60844ac91857
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2025

## Worker version rollback limit increased from 10 to 100

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The number of recent versions available for a Worker rollback has been increased from 10 to 100.

This allows you to:

- Promote any of the 100 most recent versions to be the active deployment.
- Split traffic using [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/) between your latest code and any of the 100 most recent versions.

You can do this through the Cloudflare dashboard or with [Wrangler's rollback command](https://developers.cloudflare.com/workers/wrangler/commands/general/#rollback)

Learn more about [versioned deployments](https://developers.cloudflare.com/workers/versions-and-deployments/) and [rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/#page","headline":"Worker version rollback limit increased from 10 to 100","description":"Workers can now be deployed and rolled back to their most recent 100 versions, up from the previous limit of 10.","url":"https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/og.png?v=aa5d60844ac91857","dateModified":"2025-09-11","datePublished":"2025-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
