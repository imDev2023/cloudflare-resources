---
description: Configure your AI Gateway to automatically retry failed requests to upstream providers with customizable delay and backoff settings.
title: Automatically retry on upstream provider failures on AI Gateway
image: https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/og.png?v=b5db836d31263a84
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 2, 2026

## Automatically retry on upstream provider failures on AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.

You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.

![Retry Requests settings in the AI Gateway dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2344,height=502,format=webp/_astro/auto-retry-changelog.DoCXZnDy.png)

This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use [Dynamic Routing](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/).

For more information, refer to [Manage gateways](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#retry-requests).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/#page","headline":"Automatically retry on upstream provider failures on AI Gateway","description":"Configure your AI Gateway to automatically retry failed requests to upstream providers with customizable delay and backoff settings.","url":"https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/og.png?v=b5db836d31263a84","dateModified":"2026-04-02","datePublished":"2026-04-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
