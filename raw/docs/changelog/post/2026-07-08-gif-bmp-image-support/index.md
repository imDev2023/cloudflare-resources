---
description: Convert GIF and BMP image files to searchable text with Workers AI Markdown conversion (toMarkdown), so AI Search can index them automatically.
title: Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion
image: https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/og.png?v=19b4e1f17e11d473
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 8, 2026

## Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion

[Workers AI](https://developers.cloudflare.com/workers-ai/) [AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers AI [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) (`toMarkdown`) now supports `.gif` and `.bmp` image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.

GIF and BMP files run through the same [image pipeline](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/#images) as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.

[AI Search](https://developers.cloudflare.com/ai-search/) uses `toMarkdown` automatically to process the files it ingests, so any `.gif` and `.bmp` files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.

Learn more about [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) and the full list of [AI Search's supported file types](https://developers.cloudflare.com/ai-search/configuration/data-source/#supported-file-types).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/#page","headline":"Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion","description":"Convert GIF and BMP image files to searchable text with Workers AI Markdown conversion (toMarkdown), so AI Search can index them automatically.","url":"https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/og.png?v=19b4e1f17e11d473","dateModified":"2026-07-08","datePublished":"2026-07-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
