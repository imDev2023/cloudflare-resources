---
description: Select your egress IP depending on your upstream fully qualified domain name (FQDN), application, or category
title: FQDN Filtering For Gateway Egress Policies
image: https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/og.png?v=2e79d4feed499fd2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 28, 2025

## FQDN Filtering For Gateway Egress Policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.

- Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.
- During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
  - For WARP client support, additional configuration is required. For more information, refer to the [WARP client configuration documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#limitations).

![Egress by FQDN and Hostname](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=841,height=1045,format=webp/_astro/Gateway-Egress-FQDN-Policy-preview.Civon5p8.png)

This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/#page","headline":"FQDN Filtering For Gateway Egress Policies","description":"Select your egress IP depending on your upstream fully qualified domain name (FQDN), application, or category","url":"https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/og.png?v=2e79d4feed499fd2","dateModified":"2025-04-28","datePublished":"2025-04-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
