---
description: You can now manage all of your load balancers in one place with the new Load Balancing UI.
title: New Account-Level Load Balancing UI and Private Load Balancers
image: https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/og.png?v=1797632c8395a9d7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 4, 2025

## New Account-Level Load Balancing UI and Private Load Balancers

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've made two large changes to load balancing:

- Redesigned the user interface, now centralized at the **account level**.
- Introduced [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.

This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.

![Load Balancing UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=822,format=webp/_astro/account-load-balancing-ui.CoCi7gPb.png)

**Key Enhancements:**

- **Account-Level UI Consolidation:**
  - **Unified Management:** Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.
  - **Improved Efficiency:** This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.
- **Private Network Load Balancing:**
  - **Secure Internal Application Access:** Create [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.
  - **WARP & Magic WAN Integration:** Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.
  - **Enhanced Security for Internal Resources:** Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.

![Private Load Balancers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=744,format=webp/_astro/private-load-balancer.yti20m_p.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/#page","headline":"New Account-Level Load Balancing UI and Private Load Balancers","description":"You can now manage all of your load balancers in one place with the new Load Balancing UI.","url":"https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/og.png?v=1797632c8395a9d7","dateModified":"2025-06-04","datePublished":"2025-06-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
