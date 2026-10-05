---
description: Authorization proxy endpoints and Cloudflare-hosted PAC files are now generally available for all plan types, enabling identity-aware Gateway policies without a device client.
title: Gateway Authorization Proxy and hosted PAC files are now generally available
image: https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/og.png?v=3ba18f4d8af32d29
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 29, 2026

## Gateway Authorization Proxy and hosted PAC files are now generally available

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [hosted PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now generally available for all plan types.

Authorization proxy endpoints add an identity-aware option alongside the existing [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint), using [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication to verify who a user is before applying Gateway filtering — without installing the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.

These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.

To get started, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/#page","headline":"Gateway Authorization Proxy and hosted PAC files are now generally available","description":"Authorization proxy endpoints and Cloudflare-hosted PAC files are now generally available for all plan types, enabling identity-aware Gateway policies without a device client.","url":"https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/og.png?v=3ba18f4d8af32d29","dateModified":"2026-04-29","datePublished":"2026-04-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
