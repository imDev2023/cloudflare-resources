---
description: Node.js APIs from the node:crypto and node:tls modules are now available when using nodejs_compat.
title: Improved support for Node.js Crypto and TLS APIs in Workers
image: https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/og.png?v=50475a7f11eb0a0b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2025

## Improved support for Node.js Crypto and TLS APIs in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When using a Worker with the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag enabled, the following Node.js APIs are now available:

- [`node:crypto`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/)
- [`node:tls`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/)

This make it easier to reuse existing Node.js code in Workers or use npm packages that depend on these APIs.

#### node:crypto

The full [`node:crypto` ↗︎](https://nodejs.org/api/crypto.html) API is now available in Workers.

You can use it to verify and sign data:

```js
import { sign, verify } from "node:crypto";

const signature = sign("sha256", "-data to sign-", env.PRIVATE_KEY);
const verified = verify("sha256", "-data to sign-", env.PUBLIC_KEY, signature);
```

Or, to encrypt and decrypt data:

```js
import { publicEncrypt, privateDecrypt } from "node:crypto";

const encrypted = publicEncrypt(env.PUBLIC_KEY, "some data");
const plaintext = privateDecrypt(env.PRIVATE_KEY, encrypted);
```

See the [`node:crypto` documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/) for more information.

#### node:tls

The following APIs from `node:tls` are now available:

- [`connect` ↗︎](https://nodejs.org/api/tls.html#tlsconnectoptions-callback)
- [`TLSSocket` ↗︎](https://nodejs.org/api/tls.html#class-tlstlssocket)
- [`checkServerIdentity` ↗︎](https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert)
- [`createSecureContext` ↗︎](https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions)

This enables secure connections over TLS (Transport Layer Security) to external services.

```js
import { connect } from "node:tls";

// ... in a request handler ...
const connectionOptions = { key: env.KEY, cert: env.CERT };
const socket = connect(url, connectionOptions, () => {
	if (socket.authorized) {
		console.log("Connection authorized");
	}
});

socket.on("data", (data) => {
	console.log(data);
});

socket.on("end", () => {
	console.log("server ends connection");
});
```

See the [`node:tls` documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/#page","headline":"Improved support for Node.js Crypto and TLS APIs in Workers","description":"Node.js APIs from the node:crypto and node:tls modules are now available when using nodejs_compat.","url":"https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/og.png?v=50475a7f11eb0a0b","dateModified":"2025-04-08","datePublished":"2025-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
