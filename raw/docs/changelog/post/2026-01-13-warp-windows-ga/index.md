---
description: WARP client for Windows (version 2025.10.186.0)
title: WARP client for Windows (version 2025.10.186.0)
image: https://developers.cloudflare.com/changelog/post/2026-01-13-warp-windows-ga/og.png?v=3fcc0c0f587e60e1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 13, 2026

## WARP client for Windows (version 2025.10.186.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-13-warp-windows-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Windows WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes, improvements, and new features. New features include the ability to manage WARP client connectivity for all devices in your fleet using an [external signal](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect), and a new WARP client device posture check for [Antivirus](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/).

**Changes and improvements**

- Added a new feature to manage WARP client connectivity for all devices using an [external signal](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect). This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.
- Fixed an issue that caused occasional audio degradation and increased CPU usage on Windows by optimizing route configurations for large [domain-based split tunnel rules](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#domain-based-split-tunnels).
- The [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.
- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) now supports transparent HTTP proxying in addition to CONNECT-based proxying.
- Fixed an issue where sending large messages to the daemon by Inter-Process Communication (IPC) could cause the daemon to fail and result in service interruptions.
- Added support for a new WARP client device posture check for [Antivirus](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/). The check confirms the presence of an antivirus program on a Windows device with the option to check if the antivirus is up to date.

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.
- DNS resolution may be broken when the following conditions are all true:
  - WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while WARP is connected.

  To work around this issue, reconnect the WARP client by toggling off and back on.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-13-warp-windows-ga/#page","headline":"WARP client for Windows (version 2025.10.186.0)","description":"WARP client for Windows (version 2025.10.186.0)","url":"https://developers.cloudflare.com/changelog/post/2026-01-13-warp-windows-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-13-warp-windows-ga/og.png?v=3fcc0c0f587e60e1","dateModified":"2026-01-13","datePublished":"2026-01-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
