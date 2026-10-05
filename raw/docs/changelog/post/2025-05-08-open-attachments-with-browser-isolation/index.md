---
description: A new attachment section in Email security allows you to safely open attachments to view and investigate.
title: Open email attachments with Browser Isolation
image: https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/og.png?v=1d7ec645f085b9f6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 15, 2025

## Open email attachments with Browser Isolation

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now safely open email attachments to view and investigate them.

What this means is that messages now have a **Attachments** section. Here, you can view processed attachments and their classifications (for example, *Malicious*, *Suspicious*, *Encrypted*). Next to each attachment, a **Browser Isolation** icon allows your team to safely open the file in a **clientless, isolated browser** with no risk to the analyst or your environment.

![Attachment-RBI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=517,height=155,format=webp/_astro/Attachment-RBI.U9Dp8dJO.png)

To use this feature, you must:

- Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
- Have **Browser Isolation (BISO)** seats assigned.

For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/#page","headline":"Open email attachments with Browser Isolation","description":"A new attachment section in Email security allows you to safely open attachments to view and investigate.","url":"https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/og.png?v=1d7ec645f085b9f6","dateModified":"2025-05-15","datePublished":"2025-05-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
