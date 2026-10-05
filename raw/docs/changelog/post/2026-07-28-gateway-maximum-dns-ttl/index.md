---
description: Cloudflare One admins can now set a maximum time-to-live (TTL) for DNS responses at the account level and override it per DNS location.
title: Control Cloudflare Gateway DNS caching with a maximum TTL setting
image: https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/og.png?v=0f555e9c17dd7017
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 28, 2026

## Control Cloudflare Gateway DNS caching with a maximum TTL setting

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.

![The maximum DNS TTL setting in Traffic policies > Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2170,height=294,format=webp/_astro/gateway-max-ttl-traffic-settings.BRF3NUMp.png)

The setting is available at two levels:

- **Account level** - In **Traffic Policies** > **Traffic Settings**, under **Proxy and inspection**. This sets the default cap for all DNS locations.
- **Per-location** - Each [DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-proxies/) can inherit the account setting, disable the cap, or override it with a custom value.

Two new fields are also available in DNS logs: `upstream_record_ttls` (the original TTL from the upstream response) and `applied_max_ttl` (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.

For more information, refer to [Maximum DNS TTL](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/#page","headline":"Control Cloudflare Gateway DNS caching with a maximum TTL setting","description":"Cloudflare One admins can now set a maximum time-to-live (TTL) for DNS responses at the account level and override it per DNS location.","url":"https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/og.png?v=0f555e9c17dd7017","dateModified":"2026-07-28","datePublished":"2026-07-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
