---
description: Containers limits have been increased to allow for more concurrent instances
title: Run more Containers with higher resource limits
image: https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/og.png?v=7bb65beee3ce161c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2025

## Run more Containers with higher resource limits

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run more Containers concurrently with higher limits on CPU, memory, and disk.

| Limit | New Limit | Previous Limit |
| --- | --- | --- |
| Memory for concurrent live Container instances | 400GiB | 40GiB |
| vCPU for concurrent live Container instances | 100 | 20 |
| Disk for concurrent live Container instances | 2TB | 100GB |

You can now run 1000 instances of the `dev` instance type, 400 instances of `basic`, or 100 instances of `standard` concurrently.

This opens up new possibilities for running larger-scale workloads on Containers.

See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container, and the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/#page","headline":"Run more Containers with higher resource limits","description":"Containers limits have been increased to allow for more concurrent instances","url":"https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/og.png?v=7bb65beee3ce161c","dateModified":"2025-09-25","datePublished":"2025-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
