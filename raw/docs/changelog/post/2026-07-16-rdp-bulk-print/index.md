---
description: Users can print multiple PDF files from a browser-based RDP session as a single print job.
title: Bulk print PDFs for browser-based RDP
image: https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/og.png?v=eef1daf7592172c0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 16, 2026

## Bulk print PDFs for browser-based RDP

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select **Print all PDFs** in the clipboard panel. The files are combined into one PDF and sent to your local printer.

![The clipboard panel showing the Print all PDFs option for multiple selected PDF files.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=768,height=432,format=webp/_astro/rdp-bulk-print.DT4sCcI-.png)

Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to [Print PDFs for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/#page","headline":"Bulk print PDFs for browser-based RDP","description":"Users can print multiple PDF files from a browser-based RDP session as a single print job.","url":"https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/og.png?v=eef1daf7592172c0","dateModified":"2026-07-16","datePublished":"2026-07-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
