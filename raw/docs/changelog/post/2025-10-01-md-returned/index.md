---
description: Users can now retrieve markdown, rather than HTML, from Cloudflare documentation
title: Return markdown
image: https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/og.png?v=84adac08635861a0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2025

## Return markdown

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.

```sh
curl https://developers.cloudflare.com/workers/ -H 'Accept: text/markdown'  -v
```

If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example [here ↗︎](https://github.com/cloudflare/cloudflare-docs/pull/25493).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/#page","headline":"Return markdown","description":"Users can now retrieve markdown, rather than HTML, from Cloudflare documentation","url":"https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/og.png?v=84adac08635861a0","dateModified":"2025-10-01","datePublished":"2025-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
