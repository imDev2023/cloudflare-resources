---
description: Charge for access to protected resources.
title: Monetization Gateway closed beta
image: https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/og.png?v=80fcf6b57d16238b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## Monetization Gateway closed beta

[Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Monetization Gateway is now available in closed beta. Sellers can use it to charge agents for access to APIs, Model Context Protocol (MCP) tools, sites, and datasets.

Sellers (domain owners) define which requests require payment, the cost, and where the payment should be sent. Buyers receive the payment instructions, sign an authorization, and receive the resource after the payment has been settled. The Monetization Gateway uses the x402 protocol to handle payment authorization within the HTTP request flow.

To learn more, request access in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway), review the [Monetization Gateway documentation](https://developers.cloudflare.com/monetization-gateway/), or read the [blog ↗︎](https://blog.cloudflare.com/monetization-gateway-beta/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/#page","headline":"Monetization Gateway closed beta","description":"Charge for access to protected resources.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/og.png?v=80fcf6b57d16238b","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
