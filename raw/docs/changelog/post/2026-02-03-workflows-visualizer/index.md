---
description: Visualize your Workflow's step sequence, loops, and branching logic directly in the Cloudflare dashboard
title: Visualize your Workflows in the Cloudflare dashboard
image: https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/og.png?v=c1df2f560881fb71
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 4, 2026

## Visualize your Workflows in the Cloudflare dashboard

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Workflows now automatically generates visual diagrams from your code

Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:

- Understand how steps connect and execute
- Visualize loops and nested logic
- Follow branching paths for conditional logic

![Example diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1927,height=1530,format=webp/_astro/2026-02-03-workflows-diagram.BfQAnWL3.png)

You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.

Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/workflows) to see their diagrams.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/#page","headline":"Visualize your Workflows in the Cloudflare dashboard","description":"Visualize your Workflow's step sequence, loops, and branching logic directly in the Cloudflare dashboard","url":"https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/og.png?v=c1df2f560881fb71","dateModified":"2026-02-04","datePublished":"2026-02-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
