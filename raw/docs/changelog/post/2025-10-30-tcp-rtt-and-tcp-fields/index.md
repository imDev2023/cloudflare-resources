---
description: Cloudflare Rulesets now support evaluating TCP connections and TCP RTT as part of request logic.
title: New TCP-based fields available in Rulesets
image: https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/og.png?v=2a76e1584c107ae9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 30, 2025

## New TCP-based fields available in Rulesets

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Build rules based on TCP transport and latency

Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.

---

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `cf.edge.client_tcp` | Boolean | Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC. |
| `cf.timings.client_tcp_rtt_msec` | Number | Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT. |

Example filter expression:

```plaintext
cf.edge.client_tcp && cf.timings.client_tcp_rtt_msec < 100
```

More information can be found in the Rules language [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/#page","headline":"New TCP-based fields available in Rulesets","description":"Cloudflare Rulesets now support evaluating TCP connections and TCP RTT as part of request logic.","url":"https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/og.png?v=2a76e1584c107ae9","dateModified":"2025-10-30","datePublished":"2025-10-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
