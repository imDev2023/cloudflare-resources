---
description: Accounts without an existing key-value backed Durable Object namespace can no longer create new ones and should use the SQLite storage backend instead.
title: New Durable Object namespaces must use the SQLite storage backend
image: https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/og.png?v=eb5a543cec7c9f47
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 9, 2026

## New Durable Object namespaces must use the SQLite storage backend

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the [SQLite storage backend](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class), which has been recommended for all new Durable Objects since it became [generally available ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/) in 2024.

Create a new class with a `new_sqlite_classes` migration:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "migrations": [
    {
      "tag": "v1",
      "new_sqlite_classes": [
        "MyDurableObject"
      ]
    }
  ]
}
```

```toml
[[migrations]]
tag = "v1"
new_sqlite_classes = ["MyDurableObject"]
```

SQLite-backed Durable Objects have feature parity with the key-value backend — including the [key-value storage API](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#synchronous-kv-api) — and additionally support relational [SQL queries](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#sql-api) and [point-in-time recovery](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api) to restore an object's storage to any point in the past 30 days.

If you attempt to create a new key-value backed namespace (a `new_classes` migration) on an affected account, the deployment fails with the following error:

```txt
Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.
```

This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.

For more information, refer to [Durable Objects migrations](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/#page","headline":"New Durable Object namespaces must use the SQLite storage backend","description":"Accounts without an existing key-value backed Durable Object namespace can no longer create new ones and should use the SQLite storage backend instead.","url":"https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/og.png?v=eb5a543cec7c9f47","dateModified":"2026-07-09","datePublished":"2026-07-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
