---
description: Local console access for bootstrapping Magic WAN Connector
title: Configure your Magic WAN Connector to connect via static IP assignment
image: https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/og.png?v=29d93b2263d25cd2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 14, 2025

## Configure your Magic WAN Connector to connect via static IP assignment

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now locally configure your [Magic WAN Connector](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) to work in a static IP configuration.

This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.

For more details, refer to [WAN with a static IP address](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/#page","headline":"Configure your Magic WAN Connector to connect via static IP assignment","description":"Local console access for bootstrapping Magic WAN Connector","url":"https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/og.png?v=29d93b2263d25cd2","dateModified":"2025-02-14","datePublished":"2025-02-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
