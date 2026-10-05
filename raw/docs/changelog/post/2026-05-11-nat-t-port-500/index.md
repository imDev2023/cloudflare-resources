---
description: IPsec tunnels can now use the standard NAT traversal flow, starting IKE on UDP port 500 and switching to port 4500 after NAT detection.
title: NAT-T support for IKE on UDP port 500
image: https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/og.png?v=d3fec56e40afe739
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 11, 2026

## NAT-T support for IKE on UDP port 500

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare IPsec now supports the standard NAT traversal (NAT-T) flow, where IKE begins on UDP port `500` and switches to UDP port `4500` after NAT is detected.

Previously, devices behind NAT had to be configured to initiate IKE on UDP port `4500` directly. Devices that started on UDP port `500` could not complete the IKE handshake when NAT was in the path. This required custom configuration on devices such as VeloCloud SD-WAN edges, Cisco IOS-XE routers, and Juniper SRX firewalls, and was not possible on every platform.

What changed:

- Devices behind NAT can now initiate IKE on either UDP port `500` or UDP port `4500`.
- Devices that start IKE on UDP port `500` and switch to UDP port `4500` after NAT detection now complete the handshake successfully.
- No configuration change is required on Cloudflare. The change is available for all IPsec tunnels on Cloudflare WAN and Magic Transit.

This change does not affect existing tunnels:

- Tunnels using UDP port `500` with no NAT detected continue to operate as before.
- Tunnels configured to start IKE on UDP port `4500` continue to operate as before.
- NAT detection logic is unchanged.

For configuration details, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/#page","headline":"NAT-T support for IKE on UDP port 500","description":"IPsec tunnels can now use the standard NAT traversal flow, starting IKE on UDP port 500 and switching to port 4500 after NAT detection.","url":"https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/og.png?v=d3fec56e40afe739","dateModified":"2026-05-11","datePublished":"2026-05-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
