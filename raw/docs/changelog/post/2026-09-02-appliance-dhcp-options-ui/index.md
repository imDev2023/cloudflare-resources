---
description: Add custom DHCP options to a LAN's DHCP server directly from the dashboard, no API or Terraform required.
title: Configure DHCP options from the dashboard on Cloudflare One Appliance
image: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/og.png?v=06c5f4dfb08343fe
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## Configure DHCP options from the dashboard on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure [custom DHCP options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/) directly from the dashboard when the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) is acting as the DHCP server for a LAN.

![Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-dhcp-options-ui.B5OEZmib.gif)

- In **LAN configuration**, under **DHCP server options**, select **Add DHCP option** to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select **Add custom option** to enter your own option code, type, and value.
- This complements the existing [API and Terraform workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options) for configuring DHCP options.

For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/#page","headline":"Configure DHCP options from the dashboard on Cloudflare One Appliance","description":"Add custom DHCP options to a LAN's DHCP server directly from the dashboard, no API or Terraform required.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/og.png?v=06c5f4dfb08343fe","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
