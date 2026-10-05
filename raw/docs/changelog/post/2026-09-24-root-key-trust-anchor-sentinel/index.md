---
description: 1.1.1.1 supports RFC 8509 root key trust anchor sentinels to help diagnose DNSSEC root key rollovers.
title: RFC 8509 root key trust anchor sentinel support
image: https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/og.png?v=5822cd630b2b5d4f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 24, 2026

## RFC 8509 root key trust anchor sentinel support

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

1.1.1.1 now supports [RFC 8509 ↗︎](https://datatracker.ietf.org/doc/html/rfc8509) root key trust anchor sentinels. They let you check whether the responding resolver trusts a DNSSEC root key ahead of a key rollover.

To check for KSK-2024 (key tag 38696), query DNSSEC-signed names in `dnstest.dev`:

```sh
# On a sentinel-aware resolver that trusts KSK-2024:

# Returns NOERROR with an A answer.
dig @1.1.1.1 root-key-sentinel-is-ta-38696.dnstest.dev. A +noall +comments +answer

# Returns SERVFAIL without an answer.
dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +noall +comments +answer

# CD bypasses sentinel processing and returns the original A answer.
dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +cdflag +noall +comments +answer
```

For background on DNSSEC validation, refer to [DNSKEY](https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/#page","headline":"RFC 8509 root key trust anchor sentinel support","description":"1.1.1.1 supports RFC 8509 root key trust anchor sentinels to help diagnose DNSSEC root key rollovers.","url":"https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/og.png?v=5822cd630b2b5d4f","dateModified":"2026-09-24","datePublished":"2026-09-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
