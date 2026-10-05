---
description: Interactive IP subtraction calculator component.
title: Subtract IP calculator
image: https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/og.png?v=8a63eae5e0c5f0d3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# Subtract IP calculator

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `SubtractIPCalculator` component is used `6` times on `5` pages.

<details>

<summary>

See all examples of pages that use SubtractIPCalculator

</summary>

Used **6** times.

**Pages**

- <a href="https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/">/cloudflare-one/networks/routes/reserved-ips/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/cloudflare-one/networks/routes/reserved-ips.mdx">Source</a>
- <a href="https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/">/style-guide/build-the-page/components/subtract-ip-calculator/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/style-guide/build-the-page/components/subtract-ip-calculator.mdx">Source</a>

**Partials**

- <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/cloudflare-one/tunnel/deployment-guides/cloud-private-ip.mdx">src/content/partials/cloudflare-one/tunnel/deployment-guides/cloud-private-ip.mdx</a>
- <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/cloudflare-one/tunnel/warp-to-tunnel-route-ips.mdx">src/content/partials/cloudflare-one/tunnel/warp-to-tunnel-route-ips.mdx</a>
- <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/cloudflare-one/warp/add-split-tunnels-route.mdx">src/content/partials/cloudflare-one/warp/add-split-tunnels-route.mdx</a>

</details>

## Import

```mdx
import { SubtractIPCalculator } from "~/components";
```

## Usage

  

Base CIDRSubtracted CIDRs

Calculate

```mdx
import { SubtractIPCalculator } from "~/components";

<SubtractIPCalculator client:load />
```

## `<SubtractIPCalculator>` Props

### `defaults`

**type:** `object`

An optional object containing `base` (`string`) and `subtract` (`string[]`) properties, to set default inputs.

**example:**

Base CIDRSubtracted CIDRs

Calculate

```mdx
import { SubtractIPCalculator } from "~/components";

<SubtractIPCalculator
	client:load
	defaults={{
		base: "10.0.0.0/8",
		subtract: ["10.0.0.0/24", "10.32.0.0/11"]
	}}
/>
```
