---
description: Assign read-only access to AI Crawl Control for team members who need to monitor crawler activity without edit permissions.
title: AI Crawl Control Read Only role now available
image: https://developers.cloudflare.com/changelog/post/2026-01-13-ai-crawl-control-read-only-role/og.png?v=48a911b21d4ab2d0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 13, 2026

## AI Crawl Control Read Only role now available

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-13-ai-crawl-control-read-only-role/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Account administrators can now assign the **AI Crawl Control Read Only** role to provide read-only access to AI Crawl Control at the domain level.

Users with this role can view the **Overview**, **Crawlers**, **Metrics**, **Robots.txt**, and **Settings** tabs but cannot modify crawler actions or settings.

This role is specific for AI Crawl Control. You still require correct permissions to access other areas / features of the dashboard.

To assign, go to **Manage Account** > **Members** and add a policy with the **AI Crawl Control Read Only** role scoped to the desired domain.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-13-ai-crawl-control-read-only-role/#page","headline":"AI Crawl Control Read Only role now available","description":"Assign read-only access to AI Crawl Control for team members who need to monitor crawler activity without edit permissions.","url":"https://developers.cloudflare.com/changelog/post/2026-01-13-ai-crawl-control-read-only-role/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-13-ai-crawl-control-read-only-role/og.png?v=48a911b21d4ab2d0","dateModified":"2026-01-13","datePublished":"2026-01-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
