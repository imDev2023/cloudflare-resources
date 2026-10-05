---
description: Cloudflare One Client for Linux (version 2026.7.1343.0)
title: Cloudflare One Client for Linux (version 2026.7.1343.0)
image: https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/og.png?v=8828135e87d918da
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 19, 2026

## Cloudflare One Client for Linux (version 2026.7.1343.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
- When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.

**Additional changes and improvements**

- Fixed the client not allowing login to another organization when currently showing "Device not in organization."
- A DNS search domain parsing failure no longer prevents connection.
- Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
- Fixed missing certificate error display due to a race condition.
- Fixed empty black window after transitioning from docked dual displays to undocked/internal display.
- Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.

**Known issues**

- When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/#page","headline":"Cloudflare One Client for Linux (version 2026.7.1343.0)","description":"Cloudflare One Client for Linux (version 2026.7.1343.0)","url":"https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/og.png?v=8828135e87d918da","dateModified":"2026-08-19","datePublished":"2026-08-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
