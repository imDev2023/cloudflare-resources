---
description: Rather than generating the SSH CA using Cloudflare's API, you can now generate it directly from the dashboard.
title: Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard
image: https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/og.png?v=7a1e3cf5b4961956
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 14, 2025

## Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

SSH with [Cloudflare Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.

Previously, users had to generate this certificate by using the [Cloudflare API ↗︎](https://developers.cloudflare.com/api/) directly. With this update, you can now create and manage this certificate in the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com) from the **Access controls** > **Service credentials** page.

![Navigate to Access controls and then Service credentials to see where you can generate an SSH CA](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2710,height=1180,format=webp/_astro/SSH-CA-generation.DYa9RnX1.png)

For more details, refer to [Generate a Cloudflare SSH CA](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/#page","headline":"Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard","description":"Rather than generating the SSH CA using Cloudflare's API, you can now generate it directly from the dashboard.","url":"https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/og.png?v=7a1e3cf5b4961956","dateModified":"2025-11-14","datePublished":"2025-11-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
