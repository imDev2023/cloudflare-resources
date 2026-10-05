---
description: You can now capture up to 256 KB of log events per Workers Invocation helping you gain better visibility into application behavior.
title: Capture up to 256 KB of log events in each Workers Invocation
image: https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/og.png?v=dc3c2947f154050a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## Capture up to 256 KB of log events in each Workers Invocation

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now capture a maximum of 256 KB of log events per Workers invocation, helping you gain better visibility into application behavior.

All console.log() statements, exceptions, request metadata, and headers are automatically captured during the Worker invocation and emitted as [JSON object](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events). [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs) deserializes this object before indexing the fields and storing them. You can also capture, transform, and export the JSON object in a [Tail Worker](https://developers.cloudflare.com/workers/observability/logs/tail-workers).

256 KB is a 2x increase from the previous 128 KB limit. After you exceed this limit, further context associated with the request will not be recorded in your logs.

This limit is automatically applied to all Workers.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/#page","headline":"Capture up to 256 KB of log events in each Workers Invocation","description":"You can now capture up to 256 KB of log events per Workers Invocation helping you gain better visibility into application behavior.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/og.png?v=dc3c2947f154050a","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
