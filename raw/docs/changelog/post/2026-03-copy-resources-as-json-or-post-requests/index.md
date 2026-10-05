---
description: Cloudflare One resources can be easily copied from the dashboard as schema to help users more quickly adopt API and infrastructure-as-code tools.
title: Copy Cloudflare One resources as JSON or POST requests
image: https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/og.png?v=b9dadc9298ef5d71
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 2, 2026

## Copy Cloudflare One resources as JSON or POST requests

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now copy Cloudflare One resources as JSON or as a ready-to-use API POST request directly from the dashboard. This makes it simple to transition workflows into API calls, automation scripts, or infrastructure-as-code pipelines.

To use this feature, click the overflow menu (⋮) on any supported resource and select **Copy as JSON** or **Copy as POST request**. The copied output includes only the fields present on your resource, giving you a clean and minimal starting point for your own API calls.

Initially supported resources:

- Access applications
- Access policies
- Gateway policies
- Resolver policies
- Service tokens
- Identity providers

We will continue to add support for more resources throughout 2026.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/#page","headline":"Copy Cloudflare One resources as JSON or POST requests","description":"Cloudflare One resources can be easily copied from the dashboard as schema to help users more quickly adopt API and infrastructure-as-code tools.","url":"https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/og.png?v=b9dadc9298ef5d71","dateModified":"2026-03-02","datePublished":"2026-03-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
