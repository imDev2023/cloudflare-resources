---
description: Unscannable files for Download and Upload File Types selectors
title: Block files that are password-protected, compressed, or otherwise unscannable.
image: https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/og.png?v=582959c0576bd3d7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 3, 2025

## Block files that are password-protected, compressed, or otherwise unscannable.

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.

These unscannable files are now matched with the [Download and Upload File Types traffic selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) for HTTP policies:

- Password-protected Microsoft Office document
- Password-protected PDF
- Password-protected ZIP archive
- Unscannable ZIP archive

To get started inspecting and modifying behavior based on these and other rules, refer to [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/#page","headline":"Block files that are password-protected, compressed, or otherwise unscannable.","description":"Unscannable files for Download and Upload File Types selectors","url":"https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/og.png?v=582959c0576bd3d7","dateModified":"2025-02-03","datePublished":"2025-02-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
