---
description: Purge cached image variants created by Vary for Images.
title: P​urge varied images
image: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-varied-images/og.png?v=7525c09a2f614910
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# P​urge varied images

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-varied-images/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Purging varied images instantly purges all content variants for that URL. This behavior occurs so that if an image changes, you can easily update the cache with a single purge request instead of trying to determine the potential number of out-of-date variants. The behavior is true regardless of [purge type](https://developers.cloudflare.com/cache/how-to/purge-cache/) used, such as [single file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/), [tag](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/), or [hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).
