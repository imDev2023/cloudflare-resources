---
description: Build and ship AI Agents on Cloudflare using the Agents SDK
title: Introducing the Agents SDK
image: https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/og.png?v=aa403bab1e575fea
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 25, 2025

## Introducing the Agents SDK

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've released the [Agents SDK ↗︎](http://blog.cloudflare.com/build-ai-agents-on-cloudflare/), a package and set of tools that help you build and ship AI Agents.

You can get up and running with a [chat-based AI Agent ↗︎](https://github.com/cloudflare/agents-starter) (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:

```sh
npm create cloudflare@latest agents-starter -- --template="cloudflare/agents-starter"
# open up README.md and follow the instructions
```

You can also add an Agent to any existing Workers application by installing the `agents` package directly

```sh
npm i agents
```

... and then define your first Agent:

```ts
import { Agent } from "agents";

export class YourAgent extends Agent<Env> {
	// Build it out
	// Access state on this.state or query the Agent's database via this.sql
	// Handle WebSocket events with onConnect and onMessage
	// Run tasks on a schedule with this.schedule
	// Call AI models
	// ... and/or call other Agents.
}
```

Head over to the [Agents documentation](https://developers.cloudflare.com/agents/) to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/#page","headline":"Introducing the Agents SDK","description":"Build and ship AI Agents on Cloudflare using the Agents SDK","url":"https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/og.png?v=aa403bab1e575fea","dateModified":"2025-02-25","datePublished":"2025-02-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
