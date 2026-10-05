---
description: You can now apply HTTP Isolate policies to traffic routed through authorization proxy endpoints.
title: Browser Isolation support for authorization proxy endpoints
image: https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/og.png?v=02a6c48f624e51ec
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 7, 2026

## Browser Isolation support for authorization proxy endpoints

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) now supports Gateway [authorization proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint). You can apply [HTTP Isolate policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.

Previously, only [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.

To get started, [create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [build an Isolate policy](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/#page","headline":"Browser Isolation support for authorization proxy endpoints","description":"You can now apply HTTP Isolate policies to traffic routed through authorization proxy endpoints.","url":"https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/og.png?v=02a6c48f624e51ec","dateModified":"2026-07-07","datePublished":"2026-07-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
