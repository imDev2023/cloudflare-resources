---
description: The Workers Quick Editor devtools inspector has been deprecated and replaced with a lightweight log viewer.
title: Quick Editor devtools replaced with log viewer
image: https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/og.png?v=e861a61e3cf23875
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 16, 2026

## Quick Editor devtools replaced with log viewer

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has deprecated the Workers Quick Editor dev tools inspector and replaced it with a lightweight log viewer.

This aligns our logging with `wrangler tail` and gives us the opportunity to focus our efforts on bringing benefits from the work we have invested in observability, which would not be possible otherwise.

We have made improvements to this logging viewer based on your feedback such that you can log object and array types, and easily clear the list of logs. This does not include class instances. Limitations are documented in the [Workers Playground docs](https://developers.cloudflare.com/workers/playground/).

If you do need to develop your Worker with a remote inspector, you can still do this using Wrangler locally. Cloning a project from your quick editor to your computer for local development can be done with the `wrangler init --from-dash` command. For more information, refer to [Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/general/#init).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/#page","headline":"Quick Editor devtools replaced with log viewer","description":"The Workers Quick Editor devtools inspector has been deprecated and replaced with a lightweight log viewer.","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/og.png?v=e861a61e3cf23875","dateModified":"2026-02-16","datePublished":"2026-02-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
