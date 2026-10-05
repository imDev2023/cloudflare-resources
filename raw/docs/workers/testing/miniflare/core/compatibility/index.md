---
description: Configure compatibility dates and flags in Miniflare to match Cloudflare Workers runtime behavior.
title: Compatibility Dates
image: https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/og.png?v=67f291bf4d98026d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Compatibility Dates

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

- [Compatibility Dates Reference](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

## Compatibility Dates

Miniflare uses compatibility dates to opt-into backwards-incompatible changes from a specific date. If one isn't set, it will default to some time far in the past.

```js
const mf = new Miniflare({
	compatibilityDate: "2021-11-12",
});
```

## Compatibility Flags

Miniflare also lets you opt-in/out of specific changes using compatibility flags:

```js
const mf = new Miniflare({
	compatibilityFlags: [
		"formdata_parser_supports_files",
		"durable_object_fetch_allows_relative_url",
	],
});
```
