---
description: A new API endpoint lets you create, update, and delete multiple Worker secrets in a single request.
title: New Workers bulk secrets API endpoint
image: https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/og.png?v=21c76aa93780a342
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 3, 2026

## New Workers bulk secrets API endpoint

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create, update, or delete multiple secrets for your Worker in a single request using the [bulk secrets endpoint](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/).

- Include a secret with a value to create or update.
- Set a secret to `null` to delete.
- Secrets not included in the request are left unchanged.

The following example creates `API_KEY`, updates the already existing `DB_PASSWORD`, and deletes `OLD_SECRET`:

```json
{
  "secrets": {
    "API_KEY": { "type": "secret_text", "name": "API_KEY", "text": "my-api-key" },
    "DB_PASSWORD": { "type": "secret_text", "name": "DB_PASSWORD", "text": "my-db-password" },
    "OLD_SECRET": null
  }
}
```

You can do the same from the command line using [`wrangler secret bulk`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#secret-bulk):

```sh
npx wrangler secret bulk < secrets.json
```

To delete a key, set its value to `null` in the JSON file. Deletion is not supported with `.env` files.

Each request supports up to **100 total operations** (creates, updates, and deletes combined).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/#page","headline":"New Workers bulk secrets API endpoint","description":"A new API endpoint lets you create, update, and delete multiple Worker secrets in a single request.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/og.png?v=21c76aa93780a342","dateModified":"2026-06-03","datePublished":"2026-06-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
