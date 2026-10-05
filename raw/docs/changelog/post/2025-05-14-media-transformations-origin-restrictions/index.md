---
description: "Control which sources can be used for original media when requesting transformations.\n"
title: Introducing Origin Restrictions for Media Transformations
image: https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/og.png?v=472dd6e16f0c9674
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 14, 2025

## Introducing Origin Restrictions for Media Transformations

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are adding [source origin restrictions](https://developers.cloudflare.com/stream/transform-videos/sources/) to the Media Transformations beta. This allows customers to restrict what sources can be used to fetch images and video for transformations. This feature is the same as --- and uses the same settings as --- [Image Transformations sources](https://developers.cloudflare.com/images/optimization/transformations/sources/).

When transformations is first enabled, the default setting only allows transformations on images and media from the same website or domain being used to make the transformation request. In other words, by default, requests to `example.com/cdn-cgi/media` can only reference originals on `example.com`.

![Enable allowed origins from the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1664,height=872,format=webp/_astro/allowed-origins.4hu5lHws.png)

Adding access to other sources, or allowing any source, [is easy to do](https://developers.cloudflare.com/images/optimization/transformations/sources/) in the **Transformations** tab under **Stream**. Click each domain enabled for Transformations and set its sources list to match the needs of your content. The user making this change will need permission to edit zone settings.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/#page","headline":"Introducing Origin Restrictions for Media Transformations","description":"Control which sources can be used for original media when requesting transformations.","url":"https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/og.png?v=472dd6e16f0c9674","dateModified":"2025-05-14","datePublished":"2025-05-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
