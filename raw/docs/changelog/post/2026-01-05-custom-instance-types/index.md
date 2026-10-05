---
description: Configure custom vCPU, memory, and disk allocations for your container instances
title: Custom container instance types now available for all users
image: https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/og.png?v=3edcdab2e7ef8ecf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 5, 2026

## Custom container instance types now available for all users

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Custom instance types are now enabled for all [Cloudflare Containers](https://developers.cloudflare.com/containers) users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined [instance types](https://developers.cloudflare.com/containers/platform/limits/#instance-types). Previously, only select Enterprise customers were able to customize their instance type.

To use a custom instance type, specify the `instance_type` property as an object with `vcpu`, `memory_mib`, and `disk_mb` fields in your Wrangler configuration:

```toml
[[containers]]
image = "./Dockerfile"
instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }
```

Individual limits for custom instance types are based on the `standard-4` instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like `lite` or `basic`.

See the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types) for the full list of constraints on custom instance types. See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container,

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/#page","headline":"Custom container instance types now available for all users","description":"Configure custom vCPU, memory, and disk allocations for your container instances","url":"https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/og.png?v=3edcdab2e7ef8ecf","dateModified":"2026-01-05","datePublished":"2026-01-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
