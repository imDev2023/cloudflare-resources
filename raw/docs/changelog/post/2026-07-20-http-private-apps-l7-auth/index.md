---
description: Plaintext HTTP private apps now use the same in-browser Access login flow as HTTPS apps, instead of the Cloudflare One Client notification.
title: Browser-based login for plaintext HTTP private applications
image: https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/og.png?v=fe9f46c2317c4540
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 20, 2026

## Browser-based login for plaintext HTTP private applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now uses the standard browser-based login flow for [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) served over plaintext HTTP on port `80`.

Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an `Authentication required` pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access [application token](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) on success.

This brings the HTTP experience in line with HTTPS apps (with [Gateway TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.

Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/#page","headline":"Browser-based login for plaintext HTTP private applications","description":"Plaintext HTTP private apps now use the same in-browser Access login flow as HTTPS apps, instead of the Cloudflare One Client notification.","url":"https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/og.png?v=fe9f46c2317c4540","dateModified":"2026-07-20","datePublished":"2026-07-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
