---
description: Allocate up to 20 GB of disk to any custom Container instance type, independent of its memory.
title: Custom Container instance types no longer have a disk to memory ratio limit
image: https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/og.png?v=55f24f5293ed20da
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 29, 2026

## Custom Container instance types no longer have a disk to memory ratio limit

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) custom instance types no longer limit disk based on memory. Previously, a custom instance type could have a maximum of 2 GB of disk for each 1 GiB of memory. You can now allocate up to the 20 GB disk maximum to any custom instance type.

Use this to run workloads that need more disk than memory, such as workloads with large container images, datasets, or build caches. The maximum image size is the same as the instance disk space, so more disk also lets you deploy larger images.

For example, a custom instance type with 1 vCPU and 3 GiB of memory was previously limited to 6 GB of disk. It can now use 20 GB:

```jsonc
{
	"containers": [
		{
			"image": "./Dockerfile",
			"instance_type": {
				"vcpu": 1,
				"memory_mib": 3072,
				"disk_mb": 20000,
			},
		},
	],
}
```

```toml
[[containers]]
image = "./Dockerfile"

  [containers.instance_type]
  vcpu = 1
  memory_mib = 3_072
  disk_mb = 20_000
```

The other custom instance type constraints do not change, including the minimum of 3 GiB of memory per vCPU. For the full list, refer to [Custom Instance Types](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/#page","headline":"Custom Container instance types no longer have a disk to memory ratio limit","description":"Allocate up to 20 GB of disk to any custom Container instance type, independent of its memory.","url":"https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/og.png?v=55f24f5293ed20da","dateModified":"2026-09-29","datePublished":"2026-09-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
