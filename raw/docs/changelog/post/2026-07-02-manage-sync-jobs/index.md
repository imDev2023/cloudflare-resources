---
description: Use new Wrangler commands to trigger and monitor sync jobs for AI Search instances connected to a data source.
title: Manage AI Search sync jobs with Wrangler CLI
image: https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/og.png?v=00fa85c856367994
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 2, 2026

## Manage AI Search sync jobs with Wrangler CLI

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you connect a [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) to your [AI Search](https://developers.cloudflare.com/ai-search/) instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from [Wrangler](https://developers.cloudflare.com/ai-search/wrangler-commands/).

For example, you can trigger a sync job from your CI/CD or automated pipelines with the `jobs create` command so your index refreshes when you push a change:

```sh
wrangler ai-search jobs create my-instance
```

This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed. The following commands are available:

| Command | Description |
| --- | --- |
| `wrangler ai-search jobs create` | Trigger a new sync job |
| `wrangler ai-search jobs list` | List sync jobs for an instance |
| `wrangler ai-search jobs get` | Get details for a job |
| `wrangler ai-search jobs cancel` | Cancel a running job |
| `wrangler ai-search jobs logs` | View log entries for a job |

All commands accept `--namespace`/`-n` (defaults to `default`) and `--json` for structured output that automation and AI agents can parse directly. The `list` and `logs` commands also support `--page` and `--per-page` for pagination, and `cancel` prompts for confirmation unless you pass `-y`/`--force`.

For full usage details, refer to the [AI Search Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/#page","headline":"Manage AI Search sync jobs with Wrangler CLI","description":"Use new Wrangler commands to trigger and monitor sync jobs for AI Search instances connected to a data source.","url":"https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/og.png?v=00fa85c856367994","dateModified":"2026-07-02","datePublished":"2026-07-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
