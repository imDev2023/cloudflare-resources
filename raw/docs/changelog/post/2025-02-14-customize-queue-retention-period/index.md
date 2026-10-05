---
description: Customize the retention period for a queue, from a minimum of 60 seconds to a maximum of 14 days.
title: Customize queue message retention periods
image: https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/og.png?v=fa186983c0d4d353
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 14, 2025

## Customize queue message retention periods

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.

![Customize a queue's message retention period](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1898,height=986,format=webp/_astro/customize-retention-period.CpK7s10q.png)

You can customize the retention period on the settings page for your queue, or using Wrangler:

*Update message retention periodbash*

```bash
$ wrangler queues update my-queue --message-retention-period-secs 600
```

This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/#page","headline":"Customize queue message retention periods","description":"Customize the retention period for a queue, from a minimum of 60 seconds to a maximum of 14 days.","url":"https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/og.png?v=fa186983c0d4d353","dateModified":"2025-02-14","datePublished":"2025-02-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
