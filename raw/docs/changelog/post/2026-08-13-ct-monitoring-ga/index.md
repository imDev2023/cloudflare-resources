---
description: CT Monitoring is now GA, with automatic filtering of Cloudflare-issued certificates to reduce noise and highlight alerts about certificates Cloudflare did not issue.
title: Certificate Transparency Monitoring is now Generally Available
image: https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/og.png?v=0d0f6453bf38dc6e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 13, 2026

## Certificate Transparency Monitoring is now Generally Available

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Certificate Transparency Monitoring is now [generally available ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) across all Cloudflare plans.

Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.

Learn more in the [launch blog post ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) or the [CT Monitoring docs](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/#page","headline":"Certificate Transparency Monitoring is now Generally Available","description":"CT Monitoring is now GA, with automatic filtering of Cloudflare-issued certificates to reduce noise and highlight alerts about certificates Cloudflare did not issue.","url":"https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/og.png?v=0d0f6453bf38dc6e","dateModified":"2026-08-13","datePublished":"2026-08-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
