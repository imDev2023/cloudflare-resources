---
description: Cloudflare has introduced new fields to Gateway-related datasets in Cloudflare Logs.
title: New fields added to Gateway-related datasets in Cloudflare Logs
image: https://developers.cloudflare.com/changelog/post/2024-10-08-new-gateway-fields/og.png?v=caf61b5784af8970
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 8, 2024

## New fields added to Gateway-related datasets in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-10-08-new-gateway-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has introduced new fields to two Gateway-related datasets in Cloudflare Logs:

- **Gateway HTTP**: `ApplicationIDs`, `ApplicationNames`, `CategoryIDs`, `CategoryNames`, `DestinationIPContinentCode`, `DestinationIPCountryCode`, `ProxyEndpoint`, `SourceIPContinentCode`, `SourceIPCountryCode`, `VirtualNetworkID`, and `VirtualNetworkName`.
- **Gateway Network**: `ApplicationIDs`, `ApplicationNames`, `DestinationIPContinentCode`, `DestinationIPCountryCode`, `ProxyEndpoint`, `SourceIPContinentCode`, `SourceIPCountryCode`, `TransportProtocol`, `VirtualNetworkID`, and `VirtualNetworkName`.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-10-08-new-gateway-fields/#page","headline":"New fields added to Gateway-related datasets in Cloudflare Logs","description":"Cloudflare has introduced new fields to Gateway-related datasets in Cloudflare Logs.","url":"https://developers.cloudflare.com/changelog/post/2024-10-08-new-gateway-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-10-08-new-gateway-fields/og.png?v=caf61b5784af8970","dateModified":"2024-10-08","datePublished":"2024-10-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
