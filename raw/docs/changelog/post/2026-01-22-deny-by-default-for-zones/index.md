---
description: Block traffic to zones that do not have an Access application configured.
title: Require Access protection for zones
image: https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/og.png?v=c1f2a353338f40fd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 22, 2026

## Require Access protection for zones

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.

This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.

![Require Cloudflare Access protection in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2160,height=738,format=webp/_astro/require-cloudflare-access-protection.BAUmTYOs.png)

#### How it works

- **Blocked by default**: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.
- **Explicit access required**: To allow traffic, create an Access application with an Allow or Bypass policy.
- **Hostname exemptions**: You can exempt specific hostnames from this requirement.

To turn on this feature, refer to [Require Access protection](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/#page","headline":"Require Access protection for zones","description":"Block traffic to zones that do not have an Access application configured.","url":"https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/og.png?v=c1f2a353338f40fd","dateModified":"2026-01-22","datePublished":"2026-01-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
