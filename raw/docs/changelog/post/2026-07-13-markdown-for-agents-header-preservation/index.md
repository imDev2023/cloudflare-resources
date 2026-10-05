---
description: Converted responses now preserve security and cache headers, and respect your origin's content-signal.
title: Origin Content Signals for Markdown for Agents
image: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/og.png?v=432ce3dddbea92a4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 13, 2026

## Origin Content Signals for Markdown for Agents

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:

- Markdown for Agents preserves security headers such as `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Frame-Options`, `Set-Cookie`, and CORS headers (for example, `Access-Control-Allow-Origin`) on the converted response.
- Caching headers ( `Cache-Control`, `Expires`, `Age`) continue to pass through.

Your origin's [Content Signals ↗︎](https://contentsignals.org/) policy is now authoritative. If your origin sets a `content-signal` header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default `Content-Signal: ai-train=yes, search=yes, ai-input=yes`.

This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as `../page/` could resolve one path segment too high and return a `404`. Links are now resolved correctly per [RFC 3986 ↗︎](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3).

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/#page","headline":"Origin Content Signals for Markdown for Agents","description":"Converted responses now preserve security and cache headers, and respect your origin's content-signal.","url":"https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/og.png?v=432ce3dddbea92a4","dateModified":"2026-07-13","datePublished":"2026-07-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
