---
description: Run Cursor Cloud Agents on Cloudflare, with each session in an isolated self-hosted machine backed by Cloudflare Containers.
title: Run Cursor Cloud Agents on Cloudflare via self-hosted machines
image: https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/og.png?v=81855f1c6964cee8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## Run Cursor Cloud Agents on Cloudflare via self-hosted machines

[Sandboxes](https://developers.cloudflare.com/sandbox/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cursor self-hosted machines ↗︎](https://cursor.com/docs/cloud-agent/self-hosted) let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by [Cloudflare Containers](https://developers.cloudflare.com/containers/).

![Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3308,height=1916,format=webp/_astro/cursor-cloud-agents-self-hosted-pool.XNeWCXB2.png)

Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source [Cursor Cloudflare Workers template ↗︎](https://github.com/anysphere/cloudflare-workers) deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.

To get started, refer to [Run Cursor Cloud Agents on Cloudflare via self-hosted machines](https://developers.cloudflare.com/sandbox/coding-agents/cursor/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/#page","headline":"Run Cursor Cloud Agents on Cloudflare via self-hosted machines","description":"Run Cursor Cloud Agents on Cloudflare, with each session in an isolated self-hosted machine backed by Cloudflare Containers.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/og.png?v=81855f1c6964cee8","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
