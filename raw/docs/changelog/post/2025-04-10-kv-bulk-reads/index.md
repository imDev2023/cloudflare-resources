---
description: You can now retrieve up to 100 keys in a single bulk read request to Workers KV.
title: Read multiple keys from Workers KV with bulk reads
image: https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/og.png?v=20dd0baac61b102e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 17, 2025

## Read multiple keys from Workers KV with bulk reads

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.

This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by [Workers simultaneous connection limits](https://developers.cloudflare.com/workers/platform/limits/#simultaneous-open-connections).

```js
// Read single key
const key = "key-a";
const value = await env.NAMESPACE.get(key);

// Read multiple keys
const keys = ["key-a", "key-b", "key-c", ...] // up to 100 keys
const values : Map<string, string?> = await env.NAMESPACE.get(keys);

// Print the value of "key-a" to the console.
console.log(`The first key is ${values.get("key-a")}.`)
```

Consult the [Workers KV Read key-value pairs API](https://developers.cloudflare.com/kv/api/read-key-value-pairs/) for full details on Workers KV's new bulk reads support.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/#page","headline":"Read multiple keys from Workers KV with bulk reads","description":"You can now retrieve up to 100 keys in a single bulk read request to Workers KV.","url":"https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/og.png?v=20dd0baac61b102e","dateModified":"2025-04-17","datePublished":"2025-04-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
