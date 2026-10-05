---
description: WARP client for Windows (version 2026.1.89.1)
title: WARP client for Windows (version 2026.1.89.1)
image: https://developers.cloudflare.com/changelog/post/2026-01-27-warp-windows-beta/og.png?v=9e54ce975d4ee553
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 27, 2026

## WARP client for Windows (version 2026.1.89.1)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-27-warp-windows-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new Beta release for the Windows WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes, improvements, and new features.

**Changes and improvements**

- Improvements to [multi-user mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/). Fixed an issue where when switching from a pre-login registration to a user registration, Mobile Device Management (MDM) configuration association could be lost.
- Added a new feature to [manage NetBIOS over TCP/IP](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#netbios-over-tcpip) functionality on the Windows client. NetBIOS over TCP/IP on the Windows client is now disabled by default and can be enabled in [device profile settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/).
- Fixed an issue causing failure of the [local network exclusion](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion) feature when configured with a timeout of `0`.
- Improvement for the Windows [client certificate posture check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/warp-client-checks/client-certificate/) to ensure logged results are from checks that run once users log in.
- Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.
- DNS resolution may be broken when the following conditions are all true:
  - WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while WARP is connected.

  To work around this issue, reconnect the WARP client by toggling off and back on.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-27-warp-windows-beta/#page","headline":"WARP client for Windows (version 2026.1.89.1)","description":"WARP client for Windows (version 2026.1.89.1)","url":"https://developers.cloudflare.com/changelog/post/2026-01-27-warp-windows-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-27-warp-windows-beta/og.png?v=9e54ce975d4ee553","dateModified":"2026-01-27","datePublished":"2026-01-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
