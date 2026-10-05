---
description: Stop a service token from authenticating without deleting its configuration.
title: Temporarily turn off Access service tokens
image: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/og.png?v=1d766c5b8b39d9f7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## Temporarily turn off Access service tokens

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.

Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.

For configuration instructions, refer to [Turn a service token on or off](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/#page","headline":"Temporarily turn off Access service tokens","description":"Stop a service token from authenticating without deleting its configuration.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/og.png?v=1d766c5b8b39d9f7","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
