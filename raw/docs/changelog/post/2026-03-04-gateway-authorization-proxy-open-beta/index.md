---
description: Authorization proxy endpoints and Cloudflare-hosted PAC files are now in open beta for all plan types, enabling identity-aware Gateway policies without a device client.
title: Gateway Authorization Proxy and hosted PAC files (open beta)
image: https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/og.png?v=5683faade7fac8d9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 4, 2026

## Gateway Authorization Proxy and hosted PAC files (open beta)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [PAC file hosting](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now in open beta for all plan types.

Previously, [proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) relied on static source IP addresses to authorize traffic, providing no user-level identity in logs or policies. The new authorization proxy replaces IP-based authorization with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication, verifying who a user is before applying Gateway filtering without installing the WARP client.

This is ideal for environments where you cannot deploy a device client, such as virtual desktops (VDI), mergers and acquisitions, or compliance-restricted endpoints.

#### Key capabilities

- **Identity-aware proxy traffic** — Users authenticate through your identity provider (Okta, Microsoft Entra ID, Google Workspace, and others) via Cloudflare Access. Logs now show exactly which user accessed which site, and you can write [identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/) like "only the Finance team can access this accounting tool."
- **Multiple identity providers** — Display one or multiple login methods simultaneously, giving flexibility for organizations managing users across different identity systems.
- **Cloudflare-hosted PAC files** — Create and host [PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) directly in Cloudflare One with pre-configured templates for Okta and Azure, hosted at `https://pac.cloudflare-gateway.com/<account-id>/<slug>` on Cloudflare's global network.
- **Simplified billing** — Each user occupies a seat, exactly like they do with the Cloudflare One Client. No new metrics to track.

#### Get started

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Networks** > **Resolvers & Proxies** > **Proxy endpoints**.
2. [Create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and configure Access policies.
3. [Create a hosted PAC file](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) or write your own.
4. [Configure browsers](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#3b-configure-browser-to-use-pac-file) to use the PAC file URL.
5. [Install the Cloudflare certificate](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/) for HTTPS inspection.

For more details, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and the [announcement blog post ↗︎](https://blog.cloudflare.com/gateway-authorization-proxy-identity-aware-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/#page","headline":"Gateway Authorization Proxy and hosted PAC files (open beta)","description":"Authorization proxy endpoints and Cloudflare-hosted PAC files are now in open beta for all plan types, enabling identity-aware Gateway policies without a device client.","url":"https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/og.png?v=5683faade7fac8d9","dateModified":"2026-03-04","datePublished":"2026-03-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
