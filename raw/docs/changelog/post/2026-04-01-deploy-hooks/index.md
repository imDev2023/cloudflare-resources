---
description: Trigger a build for a specific branch by sending a POST request to a unique URL.
title: Deploy Hooks are now available for Workers Builds
image: https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/og.png?v=8cb91fbb46899fd5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 1, 2026

## Deploy Hooks are now available for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.

Each Deploy Hook is a unique URL tied to a specific branch. Send it a `POST` and your Worker builds and deploys.

```sh
curl -X POST "https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/<DEPLOY_HOOK_ID>"
```

To create one, go to **Workers & Pages** > your Worker > **Settings** > **Builds** > **Deploy Hooks**.

Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/) can rebuild your project on a schedule:

```js
export default {
	async scheduled(event, env, ctx) {
		ctx.waitUntil(fetch(env.DEPLOY_HOOK_URL, { method: "POST" }));
	},
};
```

```ts
export default {
  async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void> {
    ctx.waitUntil(fetch(env.DEPLOY_HOOK_URL, { method: "POST" }));
  },
} satisfies ExportedHandler<Env>;
```

You can also use Deploy Hooks to [rebuild when your CMS publishes new content](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/#cms-integration) or [deploy from a Slack slash command](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command).

#### Built-in optimizations

- **Automatic deduplication**: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.
- **Last triggered**: The dashboard shows when each hook was last triggered.
- **Build source**: Your Worker's build history shows which Deploy Hook started each build by name.

Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see [Limits & pricing](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/).

To get started, read the [Deploy Hooks documentation](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/#page","headline":"Deploy Hooks are now available for Workers Builds","description":"Trigger a build for a specific branch by sending a POST request to a unique URL.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/og.png?v=8cb91fbb46899fd5","dateModified":"2026-04-01","datePublished":"2026-04-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
