---
description: Workers running in separate dev commands can now communicate with each other using the Cloudflare Vite plugin.
title: Run and connect Workers in separate dev commands with the Cloudflare Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/og.png?v=8770923e35be01c3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 26, 2025

## Run and connect Workers in separate dev commands with the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with `vite dev` or `wrangler dev`.

Simply start each Worker in its own terminal:

```sh
# Terminal 1
vite dev

# Terminal 2
wrangler dev
```

This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.

Check out the [Developing with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers) guide to learn more about the different approaches and when to use each one.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/#page","headline":"Run and connect Workers in separate dev commands with the Cloudflare Vite plugin","description":"Workers running in separate dev commands can now communicate with each other using the Cloudflare Vite plugin.","url":"https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/og.png?v=8770923e35be01c3","dateModified":"2025-06-26","datePublished":"2025-06-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
