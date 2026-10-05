---
description: A button component for RSS feed subscriptions.
title: RSSButton
image: https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/og.png?v=235cc9dade3fa109
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# RSSButton

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Example

```mdx
import { RSSButton } from "~/components";

<RSSButton changelog="Workers" />
<br />
<RSSButton href="/custom/feed.xml" text="Custom Feed" icon="ph:arrow-square-out" />
```

## Props

### `text`

**type:** `string`

**default:** `"Subscribe to RSS"`

The text to display in the button.

### `icon`

**type:** `string`

**default:** `"rss"`

The icon to display next to the text. Renders via the Nimbus `Icon` component; accepts any iconify icon name (for example, `ph:rss-simple`). The default `"rss"` maps to `ph:rss-simple`.

### `changelog` or `href`

You must provide either `changelog` or `href`, but not both:

#### `changelog`

**type:** `string`

The name of the changelog to link to. This will be transformed into a lowercase, hyphen-separated string and used to construct the RSS feed URL in the format `/changelog/rss/{changelog}.xml`.

#### `href`

**type:** `string`

A custom URL to link to. Use this when you need to link to an RSS feed that doesn't follow the standard changelog URL pattern.
