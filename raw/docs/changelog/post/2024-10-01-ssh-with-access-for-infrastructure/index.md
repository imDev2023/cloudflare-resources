---
description: Use short-lived SSH certificates and fine-grained policy to secure access to your SSH servers.
title: Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure
image: https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/og.png?v=a6c855d920d19782
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2024

## Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.

SSH with [Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: [WARP-to-Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/).

SSH with Access for Infrastructure enables you to:

- **Author fine-grained policy** to control who may access your SSH servers, including specific ports, protocols, and SSH users.
- **Monitor infrastructure access** with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.
- **Preserve your end users' workflows.** SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.

![Example of an infrastructure Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1916,height=1714,format=webp/_astro/infrastructure-app.BhpJOgxs.png)

To get started, refer to [SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/#page","headline":"Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure","description":"Use short-lived SSH certificates and fine-grained policy to secure access to your SSH servers.","url":"https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/og.png?v=a6c855d920d19782","dateModified":"2024-10-01","datePublished":"2024-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
