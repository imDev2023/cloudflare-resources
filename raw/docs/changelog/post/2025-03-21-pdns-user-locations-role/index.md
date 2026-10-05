---
description: Create secure DNS locations using the new Cloudflare Zero Trust Locations Write role.
title: Secure DNS Locations Management User Role
image: https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/og.png?v=a721ee4ff781386c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 21, 2025

## Secure DNS Locations Management User Role

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to introduce the [**Cloudflare Zero Trust Secure DNS Locations Write role**](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations), designed to provide DNS filtering customers with granular control over third-party access when configuring their Protective DNS (PDNS) solutions.

Many DNS filtering customers rely on external service partners to manage their DNS location endpoints. This role allows you to grant access to external parties to administer DNS locations without overprovisioning their permissions.

**Secure DNS Location Requirements:**

- Mandate usage of [Bring your own DNS resolver IP addresses ↗︎](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip) if available on the account.
- Require source network filtering for IPv4/IPv6/DoT endpoints; token authentication or source network filtering for the DoH endpoint.

You can assign the new role via Cloudflare Dashboard (`Manage Accounts > Members`) or via API. For more information, refer to the [Secure DNS Locations documentation ↗︎](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/#page","headline":"Secure DNS Locations Management User Role","description":"Create secure DNS locations using the new Cloudflare Zero Trust Locations Write role.","url":"https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/og.png?v=a721ee4ff781386c","dateModified":"2025-03-21","datePublished":"2025-03-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
