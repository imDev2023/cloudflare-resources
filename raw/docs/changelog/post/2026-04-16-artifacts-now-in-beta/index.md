---
description: Artifacts is now available in beta as a versioned filesystem for Workers, APIs, and Git-compatible workflows.
title: "Artifacts now in beta: versioned filesystem with Git access"
image: https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/og.png?v=9241e0baef156878
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 16, 2026

## Artifacts now in beta: versioned filesystem with Git access

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Artifacts](https://developers.cloudflare.com/artifacts/) is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.

You can [read the announcement blog ↗︎](https://blog.cloudflare.com/artifacts-git-for-agents-beta/) to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.

Artifacts has three API surfaces:

- Workers bindings (for creating and managing repositories)
- REST API (for creating and managing repos from any other compute platform)
- Git protocol (for interacting with repos)

As an example: you can use the Workers binding to create a repo and read back its remote URL:

```ts
# Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.
const created = await env.PROD_ARTIFACTS.create("agent-007");
const remote = (await created.repo.info())?.remote;
```

Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:

```bash
curl --request POST "https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos" --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" --header "Content-Type: application/json" --data '{"name":"agent-007"}'
```

Any Git client that speaks smart HTTP can use the returned remote URL:

```bash
# Agents know git.
# Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.
git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git
```

To learn more, refer to [Get started](https://developers.cloudflare.com/artifacts/get-started/), [Workers binding](https://developers.cloudflare.com/artifacts/api/workers-binding/), and [Git protocol](https://developers.cloudflare.com/artifacts/api/git-protocol/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/#page","headline":"Artifacts now in beta: versioned filesystem with Git access","description":"Artifacts is now available in beta as a versioned filesystem for Workers, APIs, and Git-compatible workflows.","url":"https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/og.png?v=9241e0baef156878","dateModified":"2026-04-16","datePublished":"2026-04-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
