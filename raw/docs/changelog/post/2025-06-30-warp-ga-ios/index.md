---
description: Cloudflare One Agent for iOS (version 1.11)
title: Cloudflare One Agent for iOS (version 1.11)
image: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/og.png?v=4a97d7a6c0b14e6c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 30, 2025

## Cloudflare One Agent for iOS (version 1.11)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the iOS Cloudflare One Agent is now available in the [iOS App Store ↗︎](https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

- QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
- DNS over HTTPS traffic is now included in the WARP tunnel by default.
- The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/#page","headline":"Cloudflare One Agent for iOS (version 1.11)","description":"Cloudflare One Agent for iOS (version 1.11)","url":"https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/og.png?v=4a97d7a6c0b14e6c","dateModified":"2025-06-30","datePublished":"2025-06-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
