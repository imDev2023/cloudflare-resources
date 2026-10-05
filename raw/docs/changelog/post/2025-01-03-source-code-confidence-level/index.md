---
description: Added source code confidence levels to Data Loss Prevention
title: Detect source code leaks with Data Loss Prevention
image: https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/og.png?v=8d2ea6e96d7e6859
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2025

## Detect source code leaks with Data Loss Prevention

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now detect source code leaks with Data Loss Prevention (DLP) with predefined checks against common programming languages.

The following programming languages are validated with natural language processing (NLP).

- C
- C++
- C#
- Go
- Haskell
- Java
- JavaScript
- Lua
- Python
- R
- Rust
- Swift

DLP also supports confidence level for [source code profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code).

For more details, refer to [DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/#page","headline":"Detect source code leaks with Data Loss Prevention","description":"Added source code confidence levels to Data Loss Prevention","url":"https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/og.png?v=8d2ea6e96d7e6859","dateModified":"2025-01-20","datePublished":"2025-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
