---
description: Gateway Network policies (Layer 4) will be evaluated before HTTP (Layer 7) policies from July 14th, 2025
title: Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025
image: https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/og.png?v=376a9ece173ef4ce
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 18, 2025

## Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) will now evaluate [Network (Layer 4) policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) **before** [HTTP (Layer 7) policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/). This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.

This change will roll out progressively between **July 14–18, 2025**. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.

#### Updated order of enforcement

**Previous order:**

1. DNS policies
2. HTTP policies
3. Network policies

**New order:**

1. DNS policies
2. **Network policies**
3. **HTTP policies**

#### Action required: Review your Gateway HTTP policies

This change may affect block notifications. For example:

- You have an **HTTP policy** to block `example.com` and display a block page.
- You also have a **Network policy** to block `example.com` silently (no client notification).

With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.

To ensure users still receive a block notification, you can:

- Add a client notification to your Network policy, or
- Use only the HTTP policy for that domain.

---

#### Why we’re making this change

This update is based on user feedback and aims to:

- Create a more intuitive model by evaluating network-level policies before application-level policies.
- Minimize [526 connection errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context) by verifying the network path to an origin before attempting to establish a decrypted TLS connection.

---

To learn more, visit the [Gateway order of enforcement documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/#page","headline":"Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025","description":"Gateway Network policies (Layer 4) will be evaluated before HTTP (Layer 7) policies from July 14th, 2025","url":"https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/og.png?v=376a9ece173ef4ce","dateModified":"2025-06-18","datePublished":"2025-06-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
