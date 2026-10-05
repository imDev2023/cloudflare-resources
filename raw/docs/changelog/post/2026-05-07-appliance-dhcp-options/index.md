---
description: Configure DHCP options on the appliance's DHCP server, including options for PXE / iPXE boot.
title: Custom DHCP options on Cloudflare One Appliance
image: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/og.png?v=e3542ffcd08a066a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2026

## Custom DHCP options on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.

Each option is defined by `option_number`, `value`, and one of four value types: `text`, `integer`, `hex`, or `ip`. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.

For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/#page","headline":"Custom DHCP options on Cloudflare One Appliance","description":"Configure DHCP options on the appliance's DHCP server, including options for PXE / iPXE boot.","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/og.png?v=e3542ffcd08a066a","dateModified":"2026-05-07","datePublished":"2026-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
