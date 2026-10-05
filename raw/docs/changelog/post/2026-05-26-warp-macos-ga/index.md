---
description: Cloudflare One Client for macOS (version 2026.4.1390.0)
title: Cloudflare One Client for macOS (version 2026.4.1390.0)
image: https://developers.cloudflare.com/changelog/post/2026-05-26-warp-macos-ga/og.png?v=dd76cf99c69a6d93
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 26, 2026

## Cloudflare One Client for macOS (version 2026.4.1390.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-26-warp-macos-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

- Right click context menu to access the most common client actions quickly
- Built-in captive portal login experience

**Additional Changes and improvements**

- Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.
- Fixed a proxy mode connection stall issue.

**Known issues**

- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
- Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-26-warp-macos-ga/#page","headline":"Cloudflare One Client for macOS (version 2026.4.1390.0)","description":"Cloudflare One Client for macOS (version 2026.4.1390.0)","url":"https://developers.cloudflare.com/changelog/post/2026-05-26-warp-macos-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-26-warp-macos-ga/og.png?v=dd76cf99c69a6d93","dateModified":"2026-05-26","datePublished":"2026-05-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
