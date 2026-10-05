---
description: Containers limits increased 15x for memory, vCPU, and disk
title: Run 15x more Containers with higher resource limits
image: https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/og.png?v=7b7c28810ecbd8e9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 25, 2026

## Run 15x more Containers with higher resource limits

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run more [Containers](https://developers.cloudflare.com/containers/) concurrently with significantly higher limits on memory, vCPU, and disk.

| Limit | Previous Limit | New Limit |
| --- | --- | --- |
| Memory for concurrent live Container instances | 400GiB | 6TiB |
| vCPU for concurrent live Container instances | 100 | 1,500 |
| Disk for concurrent live Container instances | 2TB | 30TB |

This 15x increase enables larger-scale workloads on Containers. You can now run 15,000 instances of the `lite` instance type, 6,000 instances of `basic`, over 1,500 instances of `standard-1`, or over 1,000 instances of `standard-2` concurrently.

Refer to [Limits](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/#page","headline":"Run 15x more Containers with higher resource limits","description":"Containers limits increased 15x for memory, vCPU, and disk","url":"https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/og.png?v=7b7c28810ecbd8e9","dateModified":"2026-02-25","datePublished":"2026-02-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
