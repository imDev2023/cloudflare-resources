---
description: More steps per Workflow + pause/resume now supported
title: Increased Workflows limits and improved instance queueing.
image: https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/og.png?v=d1276e5a71b6f238
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 15, 2025

## Increased Workflows limits and improved instance queueing.

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) (beta) now allows you to define up to 1024 [steps](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstep). `sleep` steps do not count against this limit.

We've also added:

- `instanceId` as property to the [`WorkflowEvent`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowevent) type, allowing you to retrieve the current instance ID from within a running Workflow instance
- Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.
- Support for [`pause` and `resume`](https://developers.cloudflare.com/workflows/build/workers-api/#pause) for Workflow instances in a queued state.

We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new `waitForEvent` API over the coming weeks.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/#page","headline":"Increased Workflows limits and improved instance queueing.","description":"More steps per Workflow + pause/resume now supported","url":"https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/og.png?v=d1276e5a71b6f238","dateModified":"2025-01-15","datePublished":"2025-01-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
