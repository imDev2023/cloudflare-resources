---
description: Add tags to targets and define infrastructure applications based on tag values.
title: Access for Infrastructure now supports tagged targets and tag-based target criteria
image: https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/og.png?v=465c76db3af468a8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 15, 2026

## Access for Infrastructure now supports tagged targets and tag-based target criteria

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now integrates with [Resource Tagging](https://developers.cloudflare.com/resource-tagging/). You can attach key-value tags to [infrastructure targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target) and use them in access policies.

You can manage tags on targets inline when you create or edit a target or through the central [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/). Cloudflare keeps tags in sync across both methods.

Infrastructure applications also support a target criteria model with `include`, `require`, and `exclude` operators. Each operator can match targets by hostname, tag, or both.

- **Include** matches targets that have any of the specified values.
- **Require** matches targets that have all of the specified values.
- **Exclude** rejects targets that have any of the specified values.

![Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=1616,format=webp/_astro/tags-in-infra-app.ja2Tp-Gq.png)

For more information, refer to [Add an infrastructure application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/#page","headline":"Access for Infrastructure now supports tagged targets and tag-based target criteria","description":"Add tags to targets and define infrastructure applications based on tag values.","url":"https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/og.png?v=465c76db3af468a8","dateModified":"2026-09-15","datePublished":"2026-09-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
