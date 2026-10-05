---
description: Access administrators can control whether self-hosted applications preemptively set authorization cookies across their public hostnames.
title: Control authorization cookies for multi-domain Access applications
image: https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/og.png?v=c13c94b7c6511b21
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## Control authorization cookies for multi-domain Access applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.

Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.

The new **Eager redirect cookie** setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a `CF_Authorization` cookie. This supports applications that need to make requests across hostnames before the user visits each one.

For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.

To configure the setting, refer to [Authorization cookie](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/#page","headline":"Control authorization cookies for multi-domain Access applications","description":"Access administrators can control whether self-hosted applications preemptively set authorization cookies across their public hostnames.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/og.png?v=c13c94b7c6511b21","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
