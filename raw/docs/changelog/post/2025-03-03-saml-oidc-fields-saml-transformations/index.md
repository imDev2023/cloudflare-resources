---
description: Access for SaaS new SAML and OIDC Fields and SAML transforms
title: New SAML and OIDC Fields and SAML transforms for Access for SaaS
image: https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/og.png?v=d478116472589eec
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 3, 2025

## New SAML and OIDC Fields and SAML transforms for Access for SaaS

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Access for SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/) now include more configuration options to support a wider array of SaaS applications.

**SAML and OIDC Field Additions**

OIDC apps now include:

- Group Filtering via RegEx
- OIDC Claim mapping from an IdP
- OIDC token lifetime control
- Advanced OIDC auth flows including hybrid and implicit flows

![OIDC field additions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1021,height=192,format=webp/_astro/oidc-claims.2di8l9Lv.png)

SAML apps now include improved SAML attribute mapping from an IdP.

![SAML field additions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1051,height=202,format=webp/_astro/saml-attribute-statements.CW45j5Qi.png)

**SAML transformations**

SAML identities sent to Access applications can be fully customized using JSONata expressions. This allows admins to configure the precise identity SAML statement sent to a SaaS application.

![Configured SAML statement sent to application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1030,height=254,format=webp/_astro/transformation-box.DyKn-DdN.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/#page","headline":"New SAML and OIDC Fields and SAML transforms for Access for SaaS","description":"Access for SaaS new SAML and OIDC Fields and SAML transforms","url":"https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/og.png?v=d478116472589eec","dateModified":"2025-03-03","datePublished":"2025-03-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
