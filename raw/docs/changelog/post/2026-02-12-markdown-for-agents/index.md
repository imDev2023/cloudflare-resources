---
description: Cloudflare's network supports real-time content conversion to markdown at the source.
title: Introducing Markdown for Agents
image: https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/og.png?v=db5639391a571cb2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2026

## Introducing Markdown for Agents

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's network now supports real-time content conversion at the source, for enabled zones using [content negotiation ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation) headers. When AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for `text/markdown` in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

Here is a curl example with the `Accept` negotiation header requesting this page from our developer documentation:

```bash
curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \
  -H "Accept: text/markdown"
```

The response to this request is now formatted in markdown:

```http
HTTP/2 200
date: Wed, 11 Feb 2026 11:44:48 GMT
content-type: text/markdown; charset=utf-8
content-length: 2899
vary: accept
x-markdown-tokens: 725
content-signal: ai-train=yes, search=yes, ai-input=yes

---
title: Markdown for Agents · Cloudflare Agents docs
---

## What is Markdown for Agents

Markdown has quickly become the lingua franca for agents and AI systems
as a whole. The format’s explicit structure makes it ideal for AI processing,
ultimately resulting in better results while minimizing token waste.
...
```

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) and our [blog announcement ↗︎](https://blog.cloudflare.com/markdown-for-agents/) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/#page","headline":"Introducing Markdown for Agents","description":"Cloudflare's network supports real-time content conversion to markdown at the source.","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/og.png?v=db5639391a571cb2","dateModified":"2026-02-12","datePublished":"2026-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
