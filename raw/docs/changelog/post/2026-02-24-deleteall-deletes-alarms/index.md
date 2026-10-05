---
description: Clean up a Durable Object's storage with a single API call.
title: deleteAll() now deletes Durable Object alarm
image: https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/og.png?v=d156ba6ddcda0b30
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 24, 2026

## deleteAll() now deletes Durable Object alarm

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`deleteAll()` now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of `2026-02-24` or later. This change simplifies clearing a Durable Object's storage with a single API call.

Previously, `deleteAll()` only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate `deleteAlarm()` call to fully clean up all storage for an object. The `deleteAll()` change applies to both KV-backed and SQLite-backed Durable Objects.

```js
// Before: two API calls required to clear all storage
await this.ctx.storage.deleteAlarm();
await this.ctx.storage.deleteAll();

// Now: a single call clears both data and the alarm
await this.ctx.storage.deleteAll();
```

For more information, refer to the [Storage API documentation](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#deleteall).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/#page","headline":"deleteAll() now deletes Durable Object alarm","description":"Clean up a Durable Object's storage with a single API call.","url":"https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/og.png?v=d156ba6ddcda0b30","dateModified":"2026-02-24","datePublished":"2026-02-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
