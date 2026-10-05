---
description: View tunnel diagnostic logs
title: Troubleshoot tunnels with diagnostic logs
image: https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/og.png?v=6d43a5d92be28811
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 19, 2024

## Troubleshoot tunnels with diagnostic logs

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest `cloudflared` build [2024.12.2 ↗︎](https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2) introduces the ability to collect all the diagnostic logs needed to troubleshoot a `cloudflared` instance.

A diagnostic report collects data from a single instance of `cloudflared` running on the local machine and outputs it to a `cloudflared-diag` file.

For more information, refer to [Diagnostic logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/#page","headline":"Troubleshoot tunnels with diagnostic logs","description":"View tunnel diagnostic logs","url":"https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/og.png?v=6d43a5d92be28811","dateModified":"2024-12-19","datePublished":"2024-12-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
