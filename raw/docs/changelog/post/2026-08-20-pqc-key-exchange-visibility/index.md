---
description: The http_requests dataset now includes ClientTLSKeyExchangeGroup, exposing the TLS key exchange negotiated on every client-to-Cloudflare connection.
title: Per-zone post-quantum visibility in Logpush and Log Explorer
image: https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/og.png?v=abd5ef1463ee8d57
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 20, 2026

## Per-zone post-quantum visibility in Logpush and Log Explorer

[Logs](https://developers.cloudflare.com/logs/) [Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Radar ↗︎](https://radar.cloudflare.com/post-quantum) publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the [`http_requests`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) Logpush dataset — also queryable in [Log Explorer](https://developers.cloudflare.com/log-explorer/) — includes a new `ClientTLSKeyExchangeGroup` field.

The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as `X25519MLKEM768`, and classical connections appear as `X25519`, `P-256`, or another named group. A value of `UNK` means the group could not be determined, and `NONE` means either RSA key exchange was used or TLS was not used.

With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/#page","headline":"Per-zone post-quantum visibility in Logpush and Log Explorer","description":"The http_requests dataset now includes ClientTLSKeyExchangeGroup, exposing the TLS key exchange negotiated on every client-to-Cloudflare connection.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/og.png?v=abd5ef1463ee8d57","dateModified":"2026-08-20","datePublished":"2026-08-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
