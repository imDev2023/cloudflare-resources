---
description: Workers VPC now trusts Cloudflare Origin CA certificates for HTTPS connections to private services.
title: Origin CA certificate support for Workers VPC
image: https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/og.png?v=51146e116fb28090
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 13, 2026

## Origin CA certificate support for Workers VPC

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers VPC now supports [Cloudflare Origin CA certificates](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/) when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).

With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the `https` scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.

For more information, refer to [Supported TLS certificates](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/#supported-tls-certificates).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/#page","headline":"Origin CA certificate support for Workers VPC","description":"Workers VPC now trusts Cloudflare Origin CA certificates for HTTPS connections to private services.","url":"https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/og.png?v=51146e116fb28090","dateModified":"2026-02-13","datePublished":"2026-02-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
