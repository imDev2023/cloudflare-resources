---
description: Display Cloudflare CLI namespace documentation.
title: CfNamespace
image: https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/og.png?v=da3cef88a710f7c8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# CfNamespace

Last updated Sep 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `CfNamespace` component is used `0` times on `0` pages.

<details>

<summary>

See all examples of pages that use CfNamespace

</summary>

Used **0** times.

**Pages**

**Partials**

</details>

The `CfNamespace` component documents every visible command in a Cloudflare CLI namespace using metadata from the version of `cf` installed in the [`cloudflare-docs` repository ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/package.json).

## Import

```mdx
import { CfNamespace } from "~/components";
```

## Usage

```mdx
import { CfNamespace } from "~/components";

<CfNamespace namespace="hyperdrive" />
```

## Arguments

`namespace` `string` required is the namespace without the `cf` prefix, such as `hyperdrive`.

`headingLevel` `number` (default: 2) optional sets the heading level for each command name.
