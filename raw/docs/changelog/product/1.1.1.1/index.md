---
title: 1.1.1.1 (DNS Resolver) Changelog
image: https://developers.cloudflare.com/og-changelog.png
---

[Skip to content](#main-content)

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

Sep 24, 2026

[<h2>RFC 8509 root key trust anchor sentinel support</h2>](https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/)

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

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

Jul 28, 2026

[<h2>Improved DoH JSON formatting for additional record types</h2>](https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/)

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

Cloudflare is rolling out updated formatting for the `data` field in the 1.1.1.1 [DoH JSON API](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/) (`application/dns-json`). During the roll out responses may use either the old or new format.

Note

These are breaking changes. The DoH JSON format has no formal RFC and its schema is not guaranteed to be stable. If you need a stable format, use the [DoH wireformat](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-wireformat/) instead.

#### Human-readable display for additional record types

Several record types previously returned their `data` field in [RFC 3597 ↗︎](https://datatracker.ietf.org/doc/html/rfc3597) generic hex encoding (`\# <length> <hex>`). These now use standard presentation format:

```txt
CAA:        0 issue "letsencrypt.org"
NAPTR:      100 10 "s" "SIP+D2U" "" _sip._udp.example.com.
RP:         admin.example.com. txt.example.com.
IPSECKEY:   10 1 2 192.0.2.1 AwEA...
SVCB:       1 target.example.com. alpn=h2
HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1
TLSA:       3 1 1 aabbccdd...
SSHFP:      1 2 aabbccdd...
OPENPGPKEY: AwEA...
```

#### Numeric DNSSEC algorithm identifiers

DNSSEC-related records now use numeric algorithm identifiers as defined in [RFC 4034 ↗︎](https://datatracker.ietf.org/doc/html/rfc4034) instead of mnemonic names. This affects `RRSIG`, `DS`, `CDS`, `DNSKEY`, and `CDNSKEY` records. For example, `RSASHA256` becomes `8`, `ECDSAP256SHA256` becomes `13`, and `ED25519` becomes `15`. DS digest types also change from mnemonic to numeric: `SHA-256` becomes `2`.

*Beforetxt*

```txt
RRSIG:  A RSASHA256 2 300 ...
DS:     12345 RSASHA256 SHA-256 aabb...
DNSKEY: 257 3 RSASHA256 AwEA...
```

*Aftertxt*

```txt
RRSIG:  A 8 2 300 ...
DS:     12345 8 2 aabb...
DNSKEY: 257 3 8 AwEA...
```

#### Other formatting changes

`HINFO` character-strings are now individually quoted to remove ambiguity when values contain spaces:

*Beforetxt*

```txt
"data": "Intel Xeon Linux"
```

*Aftertxt*

```txt
"data": "\"Intel Xeon\" \"Linux\""
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/1.1.1.1/#page","headline":"1.1.1.1 (DNS Resolver) Changelog","url":"https://developers.cloudflare.com/changelog/product/1.1.1.1/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
