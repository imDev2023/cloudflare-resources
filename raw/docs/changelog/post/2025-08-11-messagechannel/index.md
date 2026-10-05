---
description: The MessageChannel and MessagePort APIs are now available in Workers
title: MessageChannel and MessagePort
image: https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/og.png?v=f1a81a235e11f6fd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 11, 2025

## MessageChannel and MessagePort

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A minimal implementation of the [MessageChannel API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel) is now available in Workers. This means that you can use `MessageChannel` to send messages between different parts of your Worker, but not across different Workers.

The `MessageChannel` and `MessagePort` APIs will be available by default at the global scope with any worker using a compatibility date of `2025-08-15` or later. It is also available using the `expose_global_message_channel` compatibility flag, or can be explicitly disabled using the `no_expose_global_message_channel` compatibility flag.

```js
const { port1, port2 } = new MessageChannel();

port2.onmessage = (event) => {
	console.log('Received message:', event.data);
};

port2.postMessage('Hello from port2!');
```

Any value that can be used with the `structuredClone(...)` API can be sent over the port.

#### Differences

There are a number of key limitations to the `MessageChannel` API in Workers:

- Transfer lists are currently not supported. This means that you will not be able to transfer ownership of objects like `ArrayBuffer` or `MessagePort` between ports.
- The `MessagePort` is not yet serializable. This means that you cannot send a `MessagePort` object through the `postMessage` method or via JSRPC calls.
- The `'messageerror'` event is only partially supported. If the `'onmessage'` handler throws an error, the `'messageerror'` event will be triggered, however, it will not be triggered when there are errors serializing or deserializing the message data. Instead, the error will be thrown when the `postMessage` method is called on the sending port.
- The `'close'` event will be emitted on both ports when one of the ports is closed, however it will not be emitted when the Worker is terminated or when one of the ports is garbage collected.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/#page","headline":"MessageChannel and MessagePort","description":"The MessageChannel and MessagePort APIs are now available in Workers","url":"https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/og.png?v=f1a81a235e11f6fd","dateModified":"2025-08-11","datePublished":"2025-08-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
