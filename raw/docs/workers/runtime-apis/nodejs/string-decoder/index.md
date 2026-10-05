---
description: Use the Node.js string_decoder module in Cloudflare Workers for decoding buffer objects into strings.
title: StringDecoder
image: https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/og.png?v=7b306f06686a610f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# StringDecoder

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:string_decoder` ↗︎](https://nodejs.org/api/string_decoder.html) is a legacy utility module that predates the WHATWG standard [TextEncoder](https://developers.cloudflare.com/workers/runtime-apis/encoding/#textencoder) and [TextDecoder](https://developers.cloudflare.com/workers/runtime-apis/encoding/#textdecoder) API. In most cases, you should use `TextEncoder` and `TextDecoder` instead. `StringDecoder` is available in the Workers runtime primarily for compatibility with existing npm packages that rely on it. `StringDecoder` can be accessed using:

```js
const { StringDecoder } = require("node:string_decoder");
const decoder = new StringDecoder("utf8");

const cent = Buffer.from([0xc2, 0xa2]);
console.log(decoder.write(cent));

const euro = Buffer.from([0xe2, 0x82, 0xac]);
console.log(decoder.write(euro));
```

Refer to the [Node.js documentation for `string_decoder` ↗︎](https://nodejs.org/dist/latest-v20.x/docs/api/string_decoder.html) for more information.
