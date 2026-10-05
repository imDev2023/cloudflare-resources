---
description: Connect to internal Windows servers via a web browser — no VPN or RDP client required.
title: Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!
image: https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/og.png?v=122700e73f23b865
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 22, 2025

## Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/) with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.

Since we announced our [open beta](https://developers.cloudflare.com/changelog/access/#2025-06-30), we've made a few improvements:

- Support for targets with IPv6.
- Support for [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/) and [WARP Connector](https://developers.cloudflare.com/mesh/) as on-ramps.
- More robust error messaging on the login page to help you if you encounter an issue.
- Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.
- Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.

As a refresher, here are some benefits browser-based RDP provides:

- **Control how users authenticate to internal RDP resources** with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.
- **Record who is accessing which servers and when** to support regulatory compliance requirements and to gain greater visibility in the event of a security event.
- **Eliminate the need to install and manage software on user devices**. You will only need a web browser.
- **Reduce your attack surface** by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.

![Example of a browser-based RDP Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2132,height=1814,format=webp/_astro/browser-based-rdp-access-app.BNXce1JL.png)

To get started, refer to [Connect to RDP in a browser](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/#page","headline":"Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!","description":"Connect to internal Windows servers via a web browser — no VPN or RDP client required.","url":"https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/og.png?v=122700e73f23b865","dateModified":"2025-09-22","datePublished":"2025-09-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
