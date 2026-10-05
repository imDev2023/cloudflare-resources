---
description: View Container, Worker, and Durable Object logs together on a single page.
title: Container logs page now includes relevant Worker and Durable Object logs
image: https://developers.cloudflare.com/changelog/post/2026-04-21-correlated-worker-durable-object-logs/og.png?v=5f3f467933f11933
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2026

## Container logs page now includes relevant Worker and Durable Object logs

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-correlated-worker-durable-object-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Container logs page now displays related [Worker](https://developers.cloudflare.com/workers/) and [Durable Object](https://developers.cloudflare.com/durable-objects/) logs alongside container logs. This co-locates all relevant log events for a container application in one place, making it easier to trace requests and debug issues.

![Container logs page showing Worker and Durable Object logs alongside container logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1682,height=926,format=webp/_astro/container-worker-logs.BBQ7NRse.png)

You can filter to a single source when you need to isolate Container, Worker, or Durable Object output.

For information on configuring container logging, refer to [How do Container logs work?](https://developers.cloudflare.com/containers/faq/#how-do-container-logs-work).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-21-correlated-worker-durable-object-logs/#page","headline":"Container logs page now includes relevant Worker and Durable Object logs","description":"View Container, Worker, and Durable Object logs together on a single page.","url":"https://developers.cloudflare.com/changelog/post/2026-04-21-correlated-worker-durable-object-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-21-correlated-worker-durable-object-logs/og.png?v=5f3f467933f11933","dateModified":"2026-04-21","datePublished":"2026-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
