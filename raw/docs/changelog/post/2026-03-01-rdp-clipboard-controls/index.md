---
description: Administrators can now restrict copy and paste actions between a user's local machine and their browser-based RDP session.
title: Clipboard controls for browser-based RDP
image: https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/og.png?v=bd4f4bef0ca51407
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 1, 2026

## Clipboard controls for browser-based RDP

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure clipboard controls for browser-based RDP with Cloudflare Access. Clipboard controls allow administrators to restrict whether users can copy or paste text between their local machine and the remote Windows server.

![Enable users to copy and paste content from their local machine to remote RDP sessions in the Cloudflare One dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2000,height=546,format=webp/_astro/rdp-clipboard-controls.B0ZmliDb.png)

This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting clipboard access, you can prevent sensitive data from being transferred out of the remote session to a user's personal device.

#### Configuration options

Clipboard controls are configured per policy within your Access application. For each policy, you can independently allow or deny:

- **Copy from local client to remote RDP session** — Users can copy/paste text from their local machine into the browser-based RDP session.
- **Copy from remote RDP session to local client** — Users can copy/paste text from the browser-based RDP session to their local machine.

By default, both directions are denied for new policies. For existing Access applications created before this feature was available, clipboard access remains enabled to preserve backwards compatibility.

When a user attempts a restricted clipboard action, the clipboard content is replaced with an error message informing them that the action is not allowed.

For more information, refer to [Clipboard controls for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#clipboard-controls).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/#page","headline":"Clipboard controls for browser-based RDP","description":"Administrators can now restrict copy and paste actions between a user's local machine and their browser-based RDP session.","url":"https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/og.png?v=bd4f4bef0ca51407","dateModified":"2026-03-01","datePublished":"2026-03-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
