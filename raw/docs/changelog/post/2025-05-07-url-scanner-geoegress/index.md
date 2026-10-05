---
description: Enterprise users can now choose the location from which URL scans are performed.
title: URL Scanner now supports geo-specific scanning
image: https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/og.png?v=6785e8403adb018c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 8, 2025

## URL Scanner now supports geo-specific scanning

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now choose the geographic location from which a URL scan is performed — either via [Security Center](https://developers.cloudflare.com/security-center/investigate/) in the Cloudflare dashboard or via the [URL Scanner API](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/create/).

This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.

**What’s new:**

- Location Picker: Select a location for the scan via **Security Center → Investigate** in the dashboard or through the API.
- Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.
- Default behavior: If no location is set, scans default to the user’s current geographic region.

Learn more in the [Security Center documentation](https://developers.cloudflare.com/security-center/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/#page","headline":"URL Scanner now supports geo-specific scanning","description":"Enterprise users can now choose the location from which URL scans are performed.","url":"https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/og.png?v=6785e8403adb018c","dateModified":"2025-05-08","datePublished":"2025-05-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
