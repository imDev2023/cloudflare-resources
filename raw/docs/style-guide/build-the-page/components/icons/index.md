---
description: Browse available product and UI icons.
title: Icons
image: https://developers.cloudflare.com/style-guide/build-the-page/components/icons/og.png?v=42c9b960a5808d8c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# Icons

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/icons/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

There are two icon components which pull from two different icon sets.

## Icon

The `Icon` component from Nimbus is available as a standalone component.

Primarily, this is used for Cloudflare product icons which are stored in `/src/icons/*.svg`.

```mdx
import { Icon } from "~/components";

<Icon name="workers" class="text-5xl text-orange-400" />
```

## Card and LinkCard

Components like `Card` and `LinkCard` accept a plain `icon` string prop — any [iconify ↗︎](https://icon-sets.iconify.design/) icon name.

```mdx
import { Card, LinkCard } from "~/components";

<Card title="Example" icon="ph:rocket-launch" />
<LinkCard title="Example" href="/workers/" icon="ph:rocket-launch" />
```

Content authored before the Nimbus migration may still use Starlight-style icon names (for example `icon="ph:terminal-window"`). These are automatically mapped to an equivalent iconify icon at build time. New content should use iconify names directly.

## Icon library

Optionally, you can choose a corresponding icon from Starlight’s [Icons ↗︎](https://starlight.astro.build/reference/icons/#all-icons) for cards or tabs.
