---
description: Additional post delivery action log details for failures
title: Enhanced visibility for post-delivery actions
image: https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/og.png?v=cadf47ba9a26ec75
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 12, 2026

## Enhanced visibility for post-delivery actions

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.

Note

Error messages will vary depending on whether you are using Google Workspace or Microsoft 365.

![failure-log-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2348,height=1692,format=webp/_astro/enhanced-visibility-post-delivery-actions.BNiyPtJU.png)

This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.

This applies to all Email Security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/#page","headline":"Enhanced visibility for post-delivery actions","description":"Additional post delivery action log details for failures","url":"https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/og.png?v=cadf47ba9a26ec75","dateModified":"2026-01-12","datePublished":"2026-01-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
