---
description: A new setting simplifies clientless access for self-hosted applications with private destinations.
title: Streamlined clientless browser isolation for private applications
image: https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/og.png?v=a996ecac025cac56
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 17, 2026

## Streamlined clientless browser isolation for private applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new **Allow clientless access** setting makes it easier to connect users without a device client to internal applications, without using public DNS.

![Allow clientless access setting in the Cloudflare One dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1117,height=206,format=webp/_astro/allow-clientless-access.BHKwQuVt.png)

Previously, to provide clientless access to a private hostname or IP without a [published application](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route), you had to create a separate [bookmark application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/bookmarks/) pointing to a prefixed [Clientless Web Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) URL (for example, `https://<your-teamname>.cloudflareaccess.com/browser/https://10.0.0.1/`). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.

Now, you can manage clientless access directly within your [private self-hosted application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/). When **Allow clientless access** is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have [remote browser permissions](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) to open the link.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/#page","headline":"Streamlined clientless browser isolation for private applications","description":"A new setting simplifies clientless access for self-hosted applications with private destinations.","url":"https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/og.png?v=a996ecac025cac56","dateModified":"2026-02-17","datePublished":"2026-02-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
