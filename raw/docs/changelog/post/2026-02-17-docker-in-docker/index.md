---
description: Run Docker in Docker inside Containers and Sandboxes
title: Docker-in-Docker support added to Containers and Sandboxes
image: https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/og.png?v=2bd7a7c7476a55b6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 17, 2026

## Docker-in-Docker support added to Containers and Sandboxes

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) and [Containers](https://developers.cloudflare.com/containers/) now support running Docker for "Docker-in-Docker" setups. This is particularly useful when your end users or [agents](https://developers.cloudflare.com/agents) want to run a full sandboxed development environment.

This allows you to:

- Develop containerized applications with your Sandbox
- Run isolated test environments for images
- Build container images as part of CI/CD workflows
- Deploy arbitrary images supplied at runtime within a container

For [Sandbox SDK](https://developers.cloudflare.com/sandbox/) users, see the [Docker-in-Docker guide](https://developers.cloudflare.com/sandbox/guides/docker-in-docker/) for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the [Containers FAQ](https://developers.cloudflare.com/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/#page","headline":"Docker-in-Docker support added to Containers and Sandboxes","description":"Run Docker in Docker inside Containers and Sandboxes","url":"https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/og.png?v=2bd7a7c7476a55b6","dateModified":"2026-02-17","datePublished":"2026-02-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
