---
description: AI Search now supports the Workers AI GLM-5.3 Flash model for text generation.
title: AI Search now supports GLM-5.3 Flash
image: https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/og.png?v=c59399ea6b316718
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 30, 2026

## AI Search now supports GLM-5.3 Flash

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [`@cf/zai-org/glm-5.3-flash`](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) for text generation. The model has a 1,048,576-token context window and runs on Workers AI.

To configure the model for an AI Search instance, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/#page","headline":"AI Search now supports GLM-5.3 Flash","description":"AI Search now supports the Workers AI GLM-5.3 Flash model for text generation.","url":"https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/og.png?v=c59399ea6b316718","dateModified":"2026-08-30","datePublished":"2026-08-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
