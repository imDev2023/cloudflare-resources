---
description: AI Gateway logs now capture the user agent of the client that made each request.
title: View the user agent of requests in AI Gateway logs
image: https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/og.png?v=9c1d9af369735167
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 12, 2026

## View the user agent of requests in AI Gateway logs

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from `openai-python` versus a custom application or a Cloudflare Worker.

The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.

For more information, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/#page","headline":"View the user agent of requests in AI Gateway logs","description":"AI Gateway logs now capture the user agent of the client that made each request.","url":"https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/og.png?v=9c1d9af369735167","dateModified":"2026-06-12","datePublished":"2026-06-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
