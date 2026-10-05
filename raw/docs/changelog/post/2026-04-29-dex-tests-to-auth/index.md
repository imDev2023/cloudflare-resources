---
description: Digital experience now supports testing applications with authentication and has enhanced test configuration
title: Digital experience tests to authenticated resources and enhanced configuration
image: https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/og.png?v=52d0886215d4a34a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 29, 2026

## Digital experience tests to authenticated resources and enhanced configuration

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital experience tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via [Cloudflare Secret Store](https://developers.cloudflare.com/secrets-store/).

Digital experience tests also have enhanced configuration options including:

- New HTTP methods (DELETE, PATCH, POST, PUT)
- Secret Store headers, custom plain text headers, and custom request bodies
- Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates

![Digital experience test configuration for Cloudflare Access applications](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1374,format=webp/_astro/dex_test_auth_config.CD3G3zb_.png)![Digital experience enhanced test configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1496,format=webp/_astro/dex_test_enhanced_config.Nsv7Vcob.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/#page","headline":"Digital experience tests to authenticated resources and enhanced configuration","description":"Digital experience now supports testing applications with authentication and has enhanced test configuration","url":"https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/og.png?v=52d0886215d4a34a","dateModified":"2026-04-29","datePublished":"2026-04-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
