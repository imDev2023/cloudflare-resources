---
description: Markdown for Agents now supports content encoding and larger responses.
title: Content encoding support for Markdown for Agents and other improvements
image: https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/og.png?v=6b49752f741ca2e0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 16, 2026

## Content encoding support for Markdown for Agents and other improvements

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When AI systems request pages from any website that uses Cloudflare and has [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) enabled, they can express the preference for `text/markdown` in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

This release adds the following improvements:

- The origin response limit was raised from 1 MB to 2 MB (2,097,152 bytes).
- We no longer require the origin to send the `content-length` header.
- We now support content encoded responses from the origin.

If you haven’t enabled automatic Markdown conversion yet, visit the [AI Crawl Control ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ai) section of the Cloudflare dashboard and enable **Markdown for Agents**.

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/#page","headline":"Content encoding support for Markdown for Agents and other improvements","description":"Markdown for Agents now supports content encoding and larger responses.","url":"https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/og.png?v=6b49752f741ca2e0","dateModified":"2026-02-16","datePublished":"2026-02-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
