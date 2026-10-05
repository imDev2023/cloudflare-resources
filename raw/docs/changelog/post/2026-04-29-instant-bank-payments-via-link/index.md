---
description: You can now pay for Cloudflare services directly from your bank account through Link at checkout.
title: Instant Bank Payments via Link
image: https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/og.png?v=8cb869dc8b82cd3b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 29, 2026

## Instant Bank Payments via Link

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now pay for Cloudflare services directly from your bank account using [Instant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/).

#### What changed

[Link ↗︎](https://link.co/) now supports bank account payments in addition to cards. If you have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.

![Instant Bank Payments via Link at checkout](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=413,height=562,format=webp/_astro/2026-04-29-instant-bank-payments-link.ChGd-t7M.png)

#### How to use it

1. During checkout, select your bank account from your saved Link payment methods.
2. Confirm the payment.

After your first Link authentication, your bank account is available for future purchases without re-entering details.

#### Who is eligible

Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. Your existing cards remain available at checkout.

Bank-based Link payments appear in your billing history with the payment method shown as `link` and last four digits as `0000`. For details, refer to the [Instant Bank Payments via Link documentation](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/#page","headline":"Instant Bank Payments via Link","description":"You can now pay for Cloudflare services directly from your bank account through Link at checkout.","url":"https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/og.png?v=8cb869dc8b82cd3b","dateModified":"2026-04-29","datePublished":"2026-04-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
