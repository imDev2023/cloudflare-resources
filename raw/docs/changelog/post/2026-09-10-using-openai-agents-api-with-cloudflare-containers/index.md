---
description: Run Codex with Cloudflare Containers using the OpenAI Agents API
title: Use Cloudflare Containers with Codex via the OpenAI Agents API
image: https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/og.png?v=0cf24f00b344076e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 10, 2026

## Use Cloudflare Containers with Codex via the OpenAI Agents API

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.

OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.

Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source [OpenAI Agents API Workers template ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api) provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.

You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.

To get started, refer to [Run Codex on Cloudflare using the OpenAI Agents API](https://developers.cloudflare.com/sandbox/tutorials/openai-agents-api/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/#page","headline":"Use Cloudflare Containers with Codex via the OpenAI Agents API","description":"Run Codex with Cloudflare Containers using the OpenAI Agents API","url":"https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/og.png?v=0cf24f00b344076e","dateModified":"2026-09-10","datePublished":"2026-09-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
