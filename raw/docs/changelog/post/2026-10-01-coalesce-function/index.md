---
description: Use coalesce() in rule expressions to return the first value that is not nil.
title: Handle missing values with coalesce()
image: https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/og.png?v=9667fbbec3d194a4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Handle missing values with coalesce()

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `coalesce()` function returns the first argument that is not nil. Use it to provide a fallback in rule expressions:

```txt
http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/")
```

For details, refer to the [`coalesce()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#coalesce).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/#page","headline":"Handle missing values with coalesce()","description":"Use coalesce() in rule expressions to return the first value that is not nil.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/og.png?v=9667fbbec3d194a4","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
