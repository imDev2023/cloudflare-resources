---
description: Cloudflare DLP now includes Data Classification, a new capability for organizing and labeling sensitive content with labels, templates, and reusable data classes.
title: Classify sensitive content with Data Classification
image: https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/og.png?v=b9d5aa1249be82d8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2026

## Classify sensitive content with Data Classification

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare DLP now includes **Data Classification**, which lets administrators organize and label sensitive content using labels, templates, and reusable data classes.

With Data Classification, administrators can define labels such as sensitivity schemas and levels, and data tag groups and tags. Administrators can also build from Cloudflare-managed templates and create reusable data classes that combine detection entries, other data classes, sensitivity levels, and data tags.

You can then use those classifications in custom DLP profiles to identify the severity of sensitive content, understand where it exists, and apply that logic consistently across DLP profiles.

For more information, refer to [Data Classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/#page","headline":"Classify sensitive content with Data Classification","description":"Cloudflare DLP now includes Data Classification, a new capability for organizing and labeling sensitive content with labels, templates, and reusable data classes.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/og.png?v=b9d5aa1249be82d8","dateModified":"2026-04-30","datePublished":"2026-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
