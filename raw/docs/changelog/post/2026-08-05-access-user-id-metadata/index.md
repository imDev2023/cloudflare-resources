---
description: Use Cloudflare Access identity in AI Gateway to set spend limits, control model access, filter logs, and more.
title: Identity-aware controls are now available in AI Gateway
image: https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/og.png?v=be6a7e696d6c9dba
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 5, 2026

## Identity-aware controls are now available in AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:

- **Protect your gateway endpoint.** Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.
- **Identity-aware controls.** When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.

With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as `cf.user_id`.

For setup instructions, refer to [Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/#page","headline":"Identity-aware controls are now available in AI Gateway","description":"Use Cloudflare Access identity in AI Gateway to set spend limits, control model access, filter logs, and more.","url":"https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/og.png?v=be6a7e696d6c9dba","dateModified":"2026-08-05","datePublished":"2026-08-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
