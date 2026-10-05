---
description: Create, edit, and delete custom applications for Cloudflare One Appliance — matched by hostname, IP subnet, or source subnet.
title: Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard
image: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/og.png?v=4a48985379af636c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now define [custom applications](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application) for [breakout](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [prioritized](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/) traffic on the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard, without calling the API.

![Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-custom-application-traffic-steering.D25Ga9-d.gif)

- In **Traffic Steering** > **Breakout traffic** or **Prioritized traffic**, select **Assign application traffic** > **Add** to create a custom application matched by **Hostnames**, **IP subnets**, and/or the new **Source subnets** field, alongside Cloudflare-managed applications.
- Edit or delete an existing custom application from the same panel, no API round-trip required.
- **Source subnets** lets you match traffic by its source IP range, complementing the existing [source LAN interface breakout criteria](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).

This complements the existing API and Terraform workflow for managing applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [Prioritized traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/#page","headline":"Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard","description":"Create, edit, and delete custom applications for Cloudflare One Appliance — matched by hostname, IP subnet, or source subnet.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/og.png?v=4a48985379af636c","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
