---
description: New Managed IP List, Cloudflare IP Ranges
title: Cloudflare IP Ranges List
image: https://developers.cloudflare.com/changelog/post/2025-03-13-new-managed-iplist/og.png?v=e54c1bc79296b6b2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 13, 2025

## Cloudflare IP Ranges List

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-13-new-managed-iplist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic Firewall now supports a new managed list of Cloudflare IP ranges. This list is available as an option when creating a Magic Firewall policy based on IP source/destination addresses. When selecting "is in list" or "is not in list", the option "**Cloudflare IP Ranges**" will appear in the dropdown menu.

This list is based on the IPs listed in the Cloudflare [IP ranges ↗︎](https://www.cloudflare.com/en-gb/ips/). Updates to this managed list are applied automatically.

![Cloudflare IPs Managed List](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1102,height=677,format=webp/_astro/cloudflare-ips.DetyOndL.png)

Note: IP Lists require a Cloudflare Advanced Network Firewall subscription. For more details about Cloudflare Network Firewall plans, refer to [Plans](https://developers.cloudflare.com/cloudflare-network-firewall/plans).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-13-new-managed-iplist/#page","headline":"Cloudflare IP Ranges List","description":"New Managed IP List, Cloudflare IP Ranges","url":"https://developers.cloudflare.com/changelog/post/2025-03-13-new-managed-iplist/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-13-new-managed-iplist/og.png?v=e54c1bc79296b6b2","dateModified":"2025-03-13","datePublished":"2025-03-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
