---
description: Constrain content width for layout control.
title: Width
image: https://developers.cloudflare.com/style-guide/build-the-page/components/width/og.png?v=8f64ec9ca93040a1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# Width

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/width/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `Width` component is used `8` times on `4` pages.

<details>

<summary>

See all examples of pages that use Width

</summary>

Used **8** times.

**Pages**

- <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/">/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only.mdx">Source</a>
- <a href="https://developers.cloudflare.com/magic-transit/network-flow/">/magic-transit/network-flow/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/magic-transit/network-flow.mdx">Source</a>

**Partials**

- <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/networking-services/mnm-magic-transit-integration.mdx">src/content/partials/networking-services/mnm-magic-transit-integration.mdx</a>
- <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/style-guide/llms-txt.mdx">src/content/partials/style-guide/llms-txt.mdx</a>

</details>

This component can be used to constrain the width of content, such as text or images.

## Import

```mdx
import { Width } from "~/components";
```

## Usage

```mdx
import { Width } from "~/components";

<Width size="large">This content will take up 75% of the container width</Width>

<Width size="medium">
	This content will take up 50% of the container width
</Width>

<Width size="small">This content will take up 25% of the container width</Width>

<Width size="small" center>
	This content will take up 25% of the container width and be centered
</Width>
```

## `<Width>` Props

### `size`

**required**

**type:** `"large" | "medium" | "small"`

Controls the width of the container:

- `large`: 75% of container width
- `medium`: 50% of container width
- `small`: 25% of container width

### `center`

**type:** `boolean`

Whether to horizontally center the content.
