---
description: Cloudflare Access for private hostname applications can now secure traffic on all ports and protocols. 🔒
title: Access private hostname applications support all ports/protocols
image: https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/og.png?v=9def404d3b77ecc0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 28, 2025

## Access private hostname applications support all ports/protocols

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Access for private hostname applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) can now secure traffic on all ports and protocols.

Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port `443` and support Server Name Indicator (SNI).

This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.

![Example private application on non-443 port](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1283,height=496,format=webp/_astro/internal_private_app_any_port.DNXnEy0u.png)

For example, you can now create a self-hosted application in Access for `ssh.testapp.local` running on port `22`. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.

This feature is generally available across all plans.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/#page","headline":"Access private hostname applications support all ports/protocols","description":"Cloudflare Access for private hostname applications can now secure traffic on all ports and protocols. 🔒","url":"https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/og.png?v=9def404d3b77ecc0","dateModified":"2025-10-28","datePublished":"2025-10-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
