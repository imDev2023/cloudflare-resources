---
description: New Container pricing changes CPU billing to be based on active usage, rather than provisioned CPU resources
title: New CPU Pricing for Containers and Sandboxes
image: https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/og.png?v=b06f33c7c8ca2778
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 21, 2025

## New CPU Pricing for Containers and Sandboxes

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) pricing for CPU time is now based on active usage only, instead of provisioned resources.

This means that you now pay less for Containers and Sandboxes.

#### An Example Before and After

Imagine running the `standard-2` instance type for one hour, which can use up to 1 vCPU, but on average you use only 20% of your CPU capacity.

CPU-time is priced at *$0.00002 per vCPU-second*.

Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.

CPU cost would have been: **$0.072** — 1 vCPU \* 3600 seconds \* $0.00002

Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.

CPU cost is now: **$0.0144** — 1 vCPU \* 3600 seconds \* $0.00002 \* 20% utilization

This can significantly reduce costs for Containers and Sandboxes.

Note

Memory cost and disk pricing remain unchanged, and is still calculated based on *provisioned* resources.

See the documentation to learn more about [Containers](https://developers.cloudflare.com/containers/get-started/), [Sandboxes](https://developers.cloudflare.com/sandbox/), and [associated pricing](https://developers.cloudflare.com/containers/platform/pricing).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/#page","headline":"New CPU Pricing for Containers and Sandboxes","description":"New Container pricing changes CPU billing to be based on active usage, rather than provisioned CPU resources","url":"https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/og.png?v=b06f33c7c8ca2778","dateModified":"2025-11-21","datePublished":"2025-11-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
