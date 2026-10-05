---
description: New Certificate Transparency (CT) insights in Cloudflare Radar, with new API endpoints for certificate issuance trends
title: Certificate Transparency Insights in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-08-04-radar-ct-insights/og.png?v=6c5c9326ae98ad39
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 6, 2025

## Certificate Transparency Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-04-radar-ct-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now introduces Certificate Transparency (CT) insights, providing visibility into certificate issuance trends based on Certificate Transparency logs currently monitored by Cloudflare.

The following API endpoints are now available:

- [`/ct/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries/): Retrieves certificate issuance time series.
- [`/ct/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/summary/): Retrieves certificate distribution by dimension.
- [`/ct/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries_groups/): Retrieves time series of certificate distribution by dimension.
- [`/ct/authorities`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/list/): Lists certification authorities.
- [`/ct/authorities/{ca_slug}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/get/): Retrieves details about a Certification Authority (CA). CA information is derived from the [Common CA Database (CCADB) ↗︎](https://www.ccadb.org/).
- [`/ct/logs`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/list/): Lists CT logs.
- [`/ct/logs/{log_slug}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get/): Retrieves details about a CT log. CT log information is derived from the [Google Chrome log list ↗︎](https://googlechrome.github.io/CertificateTransparency/log_lists.html).

For the `summary` and `timeseries_groups` endpoints, the following dimensions are available (and also usable as filters):

- `ca`: Certification Authority (certificate issuer)
- `ca_owner`: Certification Authority Owner
- `duration`: Certificate validity duration (between NotBefore and NotAfter dates)
- `entry_type`: Entry type (certificate vs. pre-certificate)
- `expiration_status`: Expiration status (valid vs. expired)
- `has_ips`: Presence of IP addresses in certificate [Subject Alternative Names (SANs) ↗︎](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/#hostname-and-wildcard-coverage)
- `has_wildcards`: Presence of wildcard DNS names in certificate SANs
- `log`: CT log name
- `log_api`: CT log API ([RFC6962 ↗︎](https://datatracker.ietf.org/doc/html/rfc6962) vs. [Static ↗︎](https://c2sp.org/static-ct-api))
- `log_operator`: CT log operator
- `public_key_algorithm`: Public key algorithm of certificate's key
- `signature_algorithm`: Signature algorithm used by CA to sign certificate
- `tld`: Top-level domain for DNS names found in certificates SANs
- `validation_level`: [Validation level ↗︎](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)

Check out the new Certificate Transparency insights in the [new Radar page ↗︎](https://radar.cloudflare.com/certificate-transparency).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-04-radar-ct-insights/#page","headline":"Certificate Transparency Insights in Cloudflare Radar","description":"New Certificate Transparency (CT) insights in Cloudflare Radar, with new API endpoints for certificate issuance trends","url":"https://developers.cloudflare.com/changelog/post/2025-08-04-radar-ct-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-04-radar-ct-insights/og.png?v=6c5c9326ae98ad39","dateModified":"2025-08-06","datePublished":"2025-08-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
