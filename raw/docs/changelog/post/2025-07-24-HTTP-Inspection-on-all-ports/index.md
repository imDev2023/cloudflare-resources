---
description: Gateway can now apply HTTP filtering to all HTTP requests proxied!
title: Gateway HTTP Filtering on all ports available in open BETA
image: https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/og.png?v=d51af0aade2da94f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 24, 2025

## Gateway HTTP Filtering on all ports available in open BETA

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) can now apply [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) to all proxied HTTP requests, not just traffic on standard HTTP (`80`) and HTTPS (`443`) ports. This means all requests can now be filtered by [A/V scanning](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/), [file sandboxing](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/file-sandboxing/), [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/#data-in-transit), and more.

You can turn this [setting](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports) on by going to **Settings** > **Network** > **Firewall** and choosing *Inspect on all ports*.

![HTTP Inspection on all ports setting](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=535,format=webp/_astro/Gateway-Inspection-all-ports.CCmwX6D0.png)

To learn more, refer to [Inspect on all ports (Beta)](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/#page","headline":"Gateway HTTP Filtering on all ports available in open BETA","description":"Gateway can now apply HTTP filtering to all HTTP requests proxied!","url":"https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/og.png?v=d51af0aade2da94f","dateModified":"2025-07-24","datePublished":"2025-07-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
