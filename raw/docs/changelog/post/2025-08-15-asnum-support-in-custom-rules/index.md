---
description: You can now create Load Balancing custom rules to steer traffic based on the incoming request's Autonomous System Number (ASN).
title: Steer Traffic by AS Number in Load Balancing Custom Rules
image: https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/og.png?v=c8be2551d47d172b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 15, 2025

## Steer Traffic by AS Number in Load Balancing Custom Rules

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.

This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.

![Create a Load Balancing Custom Rule using AS Num](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2554,height=1472,format=webp/_astro/asnum-custom-rule.CtcHu_zj.png)

To get started, create a [Custom Rule ↗︎](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/) in your Load Balancer and select **AS Num** from the **Field** dropdown.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/#page","headline":"Steer Traffic by AS Number in Load Balancing Custom Rules","description":"You can now create Load Balancing custom rules to steer traffic based on the incoming request's Autonomous System Number (ASN).","url":"https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/og.png?v=c8be2551d47d172b","dateModified":"2025-08-15","datePublished":"2025-08-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
