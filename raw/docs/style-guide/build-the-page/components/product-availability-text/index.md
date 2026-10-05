---
description: Show product availability by plan type.
title: Product availability text
image: https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/og.png?v=78e799bdde824554
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# Product availability text

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `ProductAvailabilityText` component is used `2` times on `2` pages.

<details>

<summary>

See all examples of pages that use ProductAvailabilityText

</summary>

Used **2** times.

**Pages**

- <a href="https://developers.cloudflare.com/rules/cloud-connector/">/rules/cloud-connector/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/rules/cloud-connector/index.mdx">Source</a>
- <a href="https://developers.cloudflare.com/rules/trace-request/">/rules/trace-request/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/rules/trace-request/index.mdx">Source</a>

**Partials**

</details>

The `ProductAvailabilityText` component dynamically renders a product's lifecycle status (such as "Beta" or "Alpha") inline with the product name. It renders nothing for generally available (GA) products, so it is safe to leave in place as a product matures.

The `product` prop must match a file in `src/content/directory/`.

```mdx
import { ProductAvailabilityText } from "~/components";

Cloud Connector <ProductAvailabilityText product="cloud-connector" /> allows you to route matching traffic to a public cloud provider.
```

## Props

| Prop | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product` | `string` | Yes | — | Product slug matching a file in `src/content/directory/`. |
| `parentheses` | `string` | No | `"true"` | When `"true"`, wraps the output in parentheses (for example, `(Beta)`). Set to `"false"` for the raw text. |

## Behavior

- If the product availability is **GA**, the component renders nothing.
- If the product or its availability data is not found, the component renders nothing (and logs a warning at build time).
