---
description: Display a single Cloudflare CLI command with details.
title: CfCommand
image: https://developers.cloudflare.com/style-guide/build-the-page/components/cf-command/og.png?v=bdcd4fdd54919fe6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# CfCommand

Last updated Sep 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-command/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `CfCommand` component is used `0` times on `0` pages.

<details>

<summary>

See all examples of pages that use CfCommand

</summary>

Used **0** times.

**Pages**

**Partials**

</details>

The `CfCommand` component documents one Cloudflare CLI command using metadata from the version of `cf` installed in the [`cloudflare-docs` repository ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/package.json).

## Import

```mdx
import { CfCommand } from "~/components";
```

## Usage

```mdx
import { CfCommand } from "~/components";

<CfCommand command="deploy" />
<CfCommand command="auth whoami" headingLevel={3} />
```

## Arguments

`command` `string` required is the command without the `cf` prefix, such as `deploy` or `auth whoami`.

`headingLevel` `number` (default: 2) optional sets the heading level for the command name.
