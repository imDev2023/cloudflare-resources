---
description: Block uploads and downloads of Apple Disk Images (DMG), Microsoft Application Installers (MSIX), and macOS Installer Packages (MPKG) to prevent the transfer of unauthorized software.
title: Expanded File Type Controls for Executables and Disk Images
image: https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/og.png?v=0bf0848fffd9ab8e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2025

## Expanded File Type Controls for Executables and Disk Images

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.

We have expanded Gateway's file type controls to include:

- Apple Disk Image (dmg)
- Microsoft Software Installer (msix, appx)
- Apple Software Package (pkg)

You can find these new options within the [*Upload File Types* and *Download File Types* selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) when creating or editing an HTTP policy. The file types are categorized as follows:

- **System**: *Apple Disk Image (dmg)*
- **Executable**: *Microsoft Software Installer (msix)*, *Microsoft Software Installer (appx)*, *Apple Software Package (pkg)*

To ensure these file types are blocked effectively, please note the following behaviors:

- DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.
- MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type *Unscannable*. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.

To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to [supported file types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#supported-file-types).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/#page","headline":"Expanded File Type Controls for Executables and Disk Images","description":"Block uploads and downloads of Apple Disk Images (DMG), Microsoft Application Installers (MSIX), and macOS Installer Packages (MPKG) to prevent the transfer of unauthorized software.","url":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/og.png?v=0bf0848fffd9ab8e","dateModified":"2025-10-01","datePublished":"2025-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
