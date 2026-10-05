---
description: Use the Node.js path module in Cloudflare Workers for file and directory path manipulation utilities.
title: path
image: https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/og.png?v=f490ad333e09357b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# path

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:path` ↗︎](https://nodejs.org/api/path.html) module provides utilities for working with file and directory paths. The `node:path` module can be accessed using:

```js
import path from "node:path";
path.join("/foo", "bar", "baz/asdf", "quux", "..");
// Returns: '/foo/bar/baz/asdf'
```

Refer to the [Node.js documentation for `path` ↗︎](https://nodejs.org/api/path.html) for more information.
