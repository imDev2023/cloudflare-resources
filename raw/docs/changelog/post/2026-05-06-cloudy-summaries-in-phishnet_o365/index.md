---
description: Cloudy email summaries are now available in PhishNet for Office 365 environments.
title: Cloudy Summaries in PhishNet O365
image: https://developers.cloudflare.com/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/og.png?v=dddb9398cf10e0b9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 6, 2026

## Cloudy Summaries in PhishNet O365

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

PhishNet users can now access **Cloudy summaries** directly within the email investigation experience. When reviewing a message in PhishNet, users will see an AI-generated summary that provides additional context and key details about the email.

These summaries help users quickly understand the nature of a message without needing to manually parse through headers, body content, and detection signals. Cloudy surfaces the most relevant information so users can make faster, more informed decisions about suspicious emails.

**These summaries are not trained on customer data.** They are generated using the outputs of our existing detection models and analysis systems.

This feature is available for PhishNet with Office 365. Support for Gmail will be available by the end of the quarter.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/#page","headline":"Cloudy Summaries in PhishNet O365","description":"Cloudy email summaries are now available in PhishNet for Office 365 environments.","url":"https://developers.cloudflare.com/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/og.png?v=dddb9398cf10e0b9","dateModified":"2026-05-06","datePublished":"2026-05-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
