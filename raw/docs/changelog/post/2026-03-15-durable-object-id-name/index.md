---
description: Retrieve the name of a named Durable Object from within the object itself.
title: Access Durable Object name via `ctx.id.name`
image: https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/og.png?v=54a41f9e6f7f3763
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 15, 2026

## Access Durable Object name via \`ctx.id.name\`

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When your Worker accesses a Durable Object via `idFromName()` or `getByName()`, the same name is now available on `ctx.id.name` inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the [Workers runtime types](https://developers.cloudflare.com/workers/languages/typescript/).

This is especially useful for [alarms](https://developers.cloudflare.com/durable-objects/api/alarms/), where there is no calling client to pass the name as an argument. When an alarm handler runs, `ctx.id.name` will hold the same name the object was originally accessed with.

```js
import { DurableObject } from "cloudflare:workers";

export class ChatRoom extends DurableObject {
  async getRoomName() {
    // ctx.id.name returns the name passed to getByName() or idFromName()
    return this.ctx.id.name;
  }
}

// Worker
export default {
  async fetch(request, env) {
    const stub = env.CHAT_ROOM.getByName("general");
    const roomName = await stub.getRoomName();
    return new Response(`Welcome to ${roomName}!`);
  },
};
```

`ctx.id.name` is `undefined` in the following cases:

- For Durable Objects created with `newUniqueId()`.
- When accessed via `idFromString()`, even if the ID was originally created from a name.
- For [names longer than 1,024 bytes](https://developers.cloudflare.com/durable-objects/api/id/#name).

This works the same way in local development with `wrangler dev` as it does in production. Run `npm update wrangler` to ensure you are on a version with this support.

For more information, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#name).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/#page","headline":"Access Durable Object name via `ctx.id.name`","description":"Retrieve the name of a named Durable Object from within the object itself.","url":"https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/og.png?v=54a41f9e6f7f3763","dateModified":"2026-03-15","datePublished":"2026-03-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
