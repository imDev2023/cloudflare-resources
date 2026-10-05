---
description: Trigger a Workflow on push to run CI checks and deploy your Artifacts repo to a Worker or User Worker.
title: Build and deploy Artifacts repos on every push
image: https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/og.png?v=467e8c5d93051a20
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2026

## Build and deploy Artifacts repos on every push

[Artifacts](https://developers.cloudflare.com/artifacts/) [Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run your CI/CD pipeline on your [Artifacts](https://developers.cloudflare.com/artifacts/) repo by defining a CI [Workflow](https://developers.cloudflare.com/workflows/) with the [CI SDK ↗︎](https://github.com/cloudflare/ci), automatically triggered on Artifacts push events.

This allows you to:

- Automatically build and deploy application code stored in Artifacts.
- Run linting, type checking, tests, and other checks on every push.
- Reuse dependencies when the lockfile (i.e. `pnpm-lock.yaml`) has not changed.
- Stop deployment when a check or build fails.
- Restrict API token access to the deployment step.
- Deploy the output to a [Worker](https://developers.cloudflare.com/workers/) or a [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) User Worker.

Define your CI steps with `@cloudflare/ci`. Each `ci.runner()` spins up an isolated sandbox, and the `cache` option reuses installed dependencies across each sandboxed step in your CI job.

Point `cache.inputs` at your lockfile (i.e. `pnpm-lock.yaml`, `bun.lock`), and the install step only runs again when that lockfile changes:

*src/index.jsjs*

```js
const deps = await ci.runner({
	name: "install",
	command: "bun install --frozen-lockfile",
	cache: { inputs: ["package.json", "bun.lock"] },
});

await Promise.all([
	deps.runner({ name: "lint", command: "bun run lint" }),
	deps.runner({ name: "test", command: "bun run test" }),
	deps.runner({ name: "typecheck", command: "bun run typecheck" }),
	deps.runner({ name: "build", command: "bun run build" }),
]);

await deps.runner({ name: "deploy", command: "bun wrangler deploy" });
```

*src/index.tsts*

```ts
const deps = await ci.runner({
	name: "install",
	command: "bun install --frozen-lockfile",
	cache: { inputs: ["package.json", "bun.lock"] },
});

await Promise.all([
	deps.runner({ name: "lint", command: "bun run lint" }),
	deps.runner({ name: "test", command: "bun run test" }),
	deps.runner({ name: "typecheck", command: "bun run typecheck" }),
	deps.runner({ name: "build", command: "bun run build" }),
]);

await deps.runner({ name: "deploy", command: "bun wrangler deploy" });
```

To start the Workflow automatically after each push, add a `cf.artifacts.repo.pushed` trigger to your Wrangler configuration:

```jsonc
{
	"triggers": {
		"events": [
			{
				"type": "cf.artifacts.repo.pushed",
				"filter": {
					"namespace": "CI",
					"repoName": "my-repo",
				},
				"target": {
					"scriptName": "my-ci-worker",
					"workflowName": "ci-workflow",
				},
			},
		],
	},
}
```

```toml
[[triggers.events]]
type = "cf.artifacts.repo.pushed"

  [triggers.events.filter]
  namespace = "CI"
  repoName = "my-repo"

  [triggers.events.target]
  scriptName = "my-ci-worker"
  workflowName = "ci-workflow"
```

To learn more, refer to [Build and deploy Artifacts repos](https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/#page","headline":"Build and deploy Artifacts repos on every push","description":"Trigger a Workflow on push to run CI checks and deploy your Artifacts repo to a Worker or User Worker.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/og.png?v=467e8c5d93051a20","dateModified":"2026-08-04","datePublished":"2026-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
