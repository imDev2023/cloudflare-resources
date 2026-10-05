---
description: Get a Durable Object client with a single line of code.
title: New getByName() API to access Durable Objects
image: https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/og.png?v=0b60a13c7da56507
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 21, 2025

## New getByName() API to access Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create a client (a [Durable Object stub](https://developers.cloudflare.com/durable-objects/api/stub/)) to a Durable Object with the new `getByName` method, removing the need to convert Durable Object names to IDs and then create a stub.

```js
// Before: (1) translate name to ID then (2) get a client 
const objectId = env.MY_DURABLE_OBJECT.idFromName("foo"); // or .newUniqueId()
const stub = env.MY_DURABLE_OBJECT.get(objectId); 

// Now: retrieve client to Durable Object directly via its name 
const stub = env.MY_DURABLE_OBJECT.getByName("foo");

// Use client to send request to the remote Durable Object
const rpcResponse = await stub.sayHello();
```

Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.

To learn more, visit the Durable Objects [API Documentation](https://developers.cloudflare.com/durable-objects/api/namespace/#getbyname) or the [getting started guide](https://developers.cloudflare.com/durable-objects/get-started/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/#page","headline":"New getByName() API to access Durable Objects","description":"Get a Durable Object client with a single line of code.","url":"https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/og.png?v=0b60a13c7da56507","dateModified":"2025-08-21","datePublished":"2025-08-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
