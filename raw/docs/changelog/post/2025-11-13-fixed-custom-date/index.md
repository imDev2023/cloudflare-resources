---
description: Log Explorer now correctly handles custom SQL date field filters.
title: Fixed custom SQL date picker inconsistencies
image: https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/og.png?v=47fc30340e0dfcbc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 13, 2025

## Fixed custom SQL date picker inconsistencies

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've resolved a bug in Log Explorer that caused inconsistencies between the custom SQL date field filters and the date picker dropdown. Previously, users attempting to filter logs based on a custom date field via a SQL query sometimes encountered unexpected results or mismatching dates when using the interactive date picker.

This fix ensures that the custom SQL date field filters now align correctly with the selection made in the date picker dropdown, providing a reliable and predictable filtering experience for your log data. This is particularly important for users creating custom log views based on time-sensitive fields.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/#page","headline":"Fixed custom SQL date picker inconsistencies","description":"Log Explorer now correctly handles custom SQL date field filters.","url":"https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/og.png?v=47fc30340e0dfcbc","dateModified":"2025-11-13","datePublished":"2025-11-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
