---
description: Display a prompt that readers can copy into their AI coding agent.
title: CopyPrompt
image: https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/og.png?v=4b01e9bd2e069c8b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# CopyPrompt

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `CopyPrompt` component is used `1` times on `1` pages.

<details>

<summary>

See all examples of pages that use CopyPrompt

</summary>

Used **1** times.

**Pages**

- <a href="https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/">/style-guide/build-the-page/components/copy-prompt/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/style-guide/build-the-page/components/copy-prompt.mdx">Source</a>

**Partials**

</details>

The `CopyPrompt` component displays a one-line prompt next to a **Copy prompt** button. Use it when readers can complete a task by pasting a prompt into an AI coding agent, such as a quickstart that an agent can run for them.

Build a Cloudflare Worker that returns Hello World, then deploy it with Wrangler.

Copy promptCopied!

## Import

```mdx
import { CopyPrompt } from "~/components";
```

## Usage

```mdx
import { CopyPrompt } from "~/components";

<CopyPrompt text="Build a Cloudflare Worker that returns Hello World, then deploy it with Wrangler." />
```

The prompt displays on a single line and is truncated if it does not fit, but the full text is always copied. Keep prompts short so readers can see what they are copying. For longer prompts, use a [code block](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/code-block-guidelines/) with `txt` as the language instead.

## `<CopyPrompt>` Props

### `text`

**type:** `string`

The prompt to display. Selecting **Copy prompt** copies this text to the clipboard.
