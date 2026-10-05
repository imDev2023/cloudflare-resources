---
description: Gateway protocol detection now supports IMAP, POP3, SMTP, MYSQL, RSYNC-DAEMON, LDAP, and NTP.
title: New protocols added for Gateway Protocol Detection (Beta)
image: https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/og.png?v=5c59c4cacdc32033
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 27, 2026

## New protocols added for Gateway Protocol Detection (Beta)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway [Protocol Detection](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/) now supports seven additional protocols in beta:

| Protocol | Notes |
| --- | --- |
| IMAP | Internet Message Access Protocol — email retrieval |
| POP3 | Post Office Protocol v3 — email retrieval |
| SMTP | Simple Mail Transfer Protocol — email sending |
| MYSQL | MySQL database wire protocol |
| RSYNC-DAEMON | rsync daemon protocol |
| LDAP | Lightweight Directory Access Protocol |
| NTP | Network Time Protocol |

These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the *Detected Protocol* selector in [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.

If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.

For more information on using Protocol Detection, refer to the [Protocol detection documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/#page","headline":"New protocols added for Gateway Protocol Detection (Beta)","description":"Gateway protocol detection now supports IMAP, POP3, SMTP, MYSQL, RSYNC-DAEMON, LDAP, and NTP.","url":"https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/og.png?v=5c59c4cacdc32033","dateModified":"2026-02-27","datePublished":"2026-02-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
