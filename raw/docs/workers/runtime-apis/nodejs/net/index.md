---
description: Use the Node.js net module in Cloudflare Workers to create TCP socket connections to external servers.
title: net
image: https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/og.png?v=a5bfada4c28c15c3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# net

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

You can use [`node:net` ↗︎](https://nodejs.org/api/net.html) to create a direct connection to servers via a TCP sockets with [`net.Socket` ↗︎](https://nodejs.org/api/net.html#class-netsocket).

These functions use [`connect`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#connect) functionality from the built-in `cloudflare:sockets` module.

*index.jsjs*

```js
import net from "node:net";

const exampleIP = "127.0.0.1";

export default {
	async fetch(req) {
		const socket = new net.Socket();
		socket.connect(4000, exampleIP, function () {
			console.log("Connected");
		});

		socket.write("Hello, Server!");
		socket.end();

		return new Response("Wrote to server", { status: 200 });
	},
};
```

*index.tsts*

```ts
import net from "node:net";

const exampleIP = "127.0.0.1";

export default {
  async fetch(req): Promise<Response> {
    const socket = new net.Socket();
    socket.connect(4000, exampleIP, function () {
      console.log("Connected");
    });

    socket.write("Hello, Server!");
    socket.end();

    return new Response("Wrote to server", { status: 200 });

},
} satisfies ExportedHandler;
```

Additionally, other APIs such as [`net.BlockList` ↗︎](https://nodejs.org/api/net.html#class-netblocklist) and [`net.SocketAddress` ↗︎](https://nodejs.org/api/net.html#class-netsocketaddress) are available.

Note that the [`net.Server` ↗︎](https://nodejs.org/api/net.html#class-netserver) class is not supported by Workers.

The full `node:net` API is documented in the [Node.js documentation for `node:net` ↗︎](https://nodejs.org/api/net.html).

```plaintext

```
