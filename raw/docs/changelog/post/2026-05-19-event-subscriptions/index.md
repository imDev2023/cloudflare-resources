---
description: Subscribe to Artifacts events for repository creates, deletes, forks, imports, pushes, clones, and fetches.
title: Event subscriptions for Artifacts lifecycle events
image: https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/og.png?v=eb0b031b5c4d650d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 19, 2026

## Event subscriptions for Artifacts lifecycle events

[Artifacts](https://developers.cloudflare.com/artifacts/) [Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now receive [event notifications](https://developers.cloudflare.com/queues/event-subscriptions/) for [Artifacts](https://developers.cloudflare.com/artifacts/) repository changes and consume them from a Worker to build commit-driven automation.

This allows you to:

- Run custom workflows when a repository is created or imported
- Kick off a build and deploy a change when an agent pushes to a repo
- Trigger a review agent on every push

Available events include:

- **Account-level events** ( `artifacts` source) — `repo.created`, `repo.deleted`, `repo.forked`, `repo.imported`
- **Repository-level events** ( `artifacts.repo` source) — `pushed`, `cloned`, `fetched`

To learn more, refer to [Artifacts documentation](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/#page","headline":"Event subscriptions for Artifacts lifecycle events","description":"Subscribe to Artifacts events for repository creates, deletes, forks, imports, pushes, clones, and fetches.","url":"https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/og.png?v=eb0b031b5c4d650d","dateModified":"2026-05-19","datePublished":"2026-05-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
