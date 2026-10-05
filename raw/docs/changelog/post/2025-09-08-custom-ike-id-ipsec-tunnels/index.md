---
description: Customers can now set a custom IKE ID for their IPsec Tunnels
title: Custom IKE ID for IPsec Tunnels
image: https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/og.png?v=16c5ae8f924a9fbd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 8, 2025

## Custom IKE ID for IPsec Tunnels

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.

This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the [Custom IKE ID feature and the API call to configure it](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/#page","headline":"Custom IKE ID for IPsec Tunnels","description":"Customers can now set a custom IKE ID for their IPsec Tunnels","url":"https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/og.png?v=16c5ae8f924a9fbd","dateModified":"2025-09-08","datePublished":"2025-09-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
