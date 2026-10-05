---
description: You can now debug your workers tests with the Workers <> Vitest integration
title: Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers
image: https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/og.png?v=58d229bc96eb10f0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 13, 2025

## Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now debug your Workers tests with our [Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) by running the following command:

```sh
vitest --inspect --no-file-parallelism
```

Attach a debugger to the port 9229 and you can start stepping through your Workers tests. This is available with `@cloudflare/vitest-pool-workers` v0.7.5 or later.

Learn more in our [documentation](https://developers.cloudflare.com/workers/testing/vitest-integration/debugging/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/#page","headline":"Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers","description":"You can now debug your workers tests with the Workers \u003c> Vitest integration","url":"https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/og.png?v=58d229bc96eb10f0","dateModified":"2025-03-13","datePublished":"2025-03-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
