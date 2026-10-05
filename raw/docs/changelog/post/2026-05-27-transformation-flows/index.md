---
description: "Set up automated rules to optimize remote images across your zone without writing code or changing URLs.\n"
title: Transformation flows in Images
image: https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/og.png?v=b492c458f3da53ee
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 27, 2026

## Transformation flows in Images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

![Custom flow configuration panel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1654,height=1398,format=webp/_astro/custom-flow.DeAGR8BY.png)

Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.

There are two modes for transformation flows:

- **[Provider flows](https://developers.cloudflare.com/images/optimization/transformations/flows/#set-up-a-provider-flow)** — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.
- **[Custom flows](https://developers.cloudflare.com/images/optimization/transformations/flows/#set-up-a-custom-flow)** — Define your own conditions and actions for use cases like automatic format conversion, [responsive sizing](https://developers.cloudflare.com/images/optimization/make-responsive-images/#using-widthauto) with `width=auto`, or directory-based optimization.

To get started, go to **Images** > **Transformations** > **Automation** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/images/transformations).

Learn more about [transformation flows](https://developers.cloudflare.com/images/optimization/transformations/flows/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/#page","headline":"Transformation flows in Images","description":"Set up automated rules to optimize remote images across your zone without writing code or changing URLs.","url":"https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/og.png?v=b492c458f3da53ee","dateModified":"2026-05-27","datePublished":"2026-05-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
