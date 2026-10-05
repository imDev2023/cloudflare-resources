---
description: Control which users see bookmark applications in the App Launcher by assigning Access policies.
title: Policies for bookmark applications
image: https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/og.png?v=918c3331499486cf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 17, 2026

## Policies for bookmark applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now assign [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) to [bookmark applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/bookmarks/). This lets you control which users see a bookmark in the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/) based on identity, device posture, and other policy rules.

Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:

- **Tailor the App Launcher to each user** — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.
- **Restrict visibility of sensitive bookmarks** — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.

Bookmarks support all [Access policy configurations](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).

For more information, refer to [Add bookmarks](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/bookmarks/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/#page","headline":"Policies for bookmark applications","description":"Control which users see bookmark applications in the App Launcher by assigning Access policies.","url":"https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/og.png?v=918c3331499486cf","dateModified":"2026-02-17","datePublished":"2026-02-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
