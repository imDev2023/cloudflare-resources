---
description: Artifacts is now in open beta with Workers Builds integration, programmable repository workflows, event subscriptions, data localization, and metrics.
title: Artifacts is now in open beta
image: https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/og.png?v=326b7b145b3ea731
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Artifacts is now in open beta

[Artifacts](https://developers.cloudflare.com/artifacts/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Artifacts](https://developers.cloudflare.com/artifacts/), Cloudflare's versioned file system that speaks Git, is now in open beta. Artifacts is built for scale, so you can create a repository per project, user, session, or task.

With Artifacts, you can:

- **Deploy repositories to Workers** — Connect an Artifacts repository through [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/). Pushes to the production branch deploy the updated Worker, while other branches create or update [Worker Previews](https://developers.cloudflare.com/workers/previews/).
- **Programmatically manage repositories** — Use an [Artifacts binding](https://developers.cloudflare.com/artifacts/api/workers-binding/) from a Worker to create or fork repos, inspect files and commits, read files by path, and issue repo-scoped Git tokens.
- **React to repository changes** — [Subscribe to events](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/) when a repository is created, imported, forked, deleted, pushed to, cloned, or fetched.
- **Control where repository data is stored** — Choose to [store and process](https://developers.cloudflare.com/artifacts/guides/data-localization/) your data in the US or EU.
- **Monitor repository usage** — View total operations, pulls, pushes, errors, and error rates in the Cloudflare dashboard or [via API for analytics](https://developers.cloudflare.com/artifacts/observability/metrics/).

Artifacts is available for customers on the Workers Paid plan. Cloudflare will begin [billing](https://developers.cloudflare.com/artifacts/platform/pricing/) for Artifacts on October 14, 2026.

#### Build the next GitHub on Cloudflare

We are hosting a competition to see who can build the next GitHub on Cloudflare using Workers and Artifacts.

[Apply today ↗︎](https://www.cloudflare.com/git-competition/) — submissions are open until October 14, 2026.

The first-place team will receive $25,000 in Cloudflare credits. The top three teams will be flown to San Francisco to present what they built at Cloudflare Connect.

Get started with the [Artifacts documentation](https://developers.cloudflare.com/artifacts/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/#page","headline":"Artifacts is now in open beta","description":"Artifacts is now in open beta with Workers Builds integration, programmable repository workflows, event subscriptions, data localization, and metrics.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/og.png?v=326b7b145b3ea731","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
