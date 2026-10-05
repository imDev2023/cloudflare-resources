---
description: Deploy Workers from AI agents with `wrangler deploy --temporary`, then claim the temporary account within 60 minutes.
title: Temporary accounts for AI agent deployments
image: https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/og.png?v=0897a122226002dd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2026

## Temporary accounts for AI agent deployments

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI agents can now deploy Workers to Cloudflare without first requiring a user to sign up, open a browser-based OAuth flow, click through the dashboard, or create an API token. When an agent tries to deploy without Cloudflare credentials, Wrangler can tell it to rerun with `--temporary`, then deploy the Worker to a temporary preview account.

To try this with your agent, update to Wrangler 4.102.0 or later, make sure you are logged out (`wrangler logout`), and then ask your agent to build something and deploy it to Cloudflare. The agent should follow Wrangler's output and deploy using the `--temporary` flag.

![Diagram showing an AI agent deploying, verifying, and redeploying a Worker to a temporary account, then claiming it after authentication and moving it to a permanent account](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1748,height=368,format=webp/_astro/claim-deployments-flow.Co0tUHG4.png)

```sh
wrangler deploy --temporary
```

The temporary deployment stays live for 60 minutes. During that window, the agent can verify the Worker, redeploy changes, and return both the live Worker URL and claim URL. Opening the claim URL lets you sign in to or create a Cloudflare account and make the temporary account permanent.

Temporary preview accounts currently support a limited set of products, including Workers, Workers Static Assets, Workers KV, D1, Durable Objects, Hyperdrive, Queues, and SSL/TLS certificates. For supported products, limits, and claim behavior, refer to [Claim deployments (temporary accounts)](https://developers.cloudflare.com/workers/platform/claim-deployments/).

For more context, refer to [Temporary Cloudflare Accounts for Agents ↗︎](https://blog.cloudflare.com/temporary-accounts/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/#page","headline":"Temporary accounts for AI agent deployments","description":"Deploy Workers from AI agents with wrangler deploy --temporary, then claim the temporary account within 60 minutes.","url":"https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/og.png?v=0897a122226002dd","dateModified":"2026-06-19","datePublished":"2026-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
