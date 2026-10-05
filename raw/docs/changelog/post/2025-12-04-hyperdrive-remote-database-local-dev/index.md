---
description: You can now connect directly to remote databases from wrangler dev using localConnectionString, with TLS support enabling secure connections while keeping your Worker code running locally
title: Connect to remote databases during local development with wrangler dev
image: https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/og.png?v=d2433160b97f1728
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 4, 2025

## Connect to remote databases during local development with wrangler dev

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now connect directly to remote databases and databases requiring TLS with `wrangler dev`. This lets you run your Worker code locally while connecting to remote databases, without needing to use `wrangler dev --remote`.

The `localConnectionString` field and `CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_<BINDING_NAME>` environment variable can be used to configure the connection string used by `wrangler dev`.

```jsonc
{
  "hyperdrive": [
    {
      "binding": "HYPERDRIVE",
      "id": "your-hyperdrive-id",
      "localConnectionString": "postgres://user:password@remote-host.example.com:5432/database?sslmode=require"
    }
  ]
}
```

Learn more about [local development with Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/local-development/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/#page","headline":"Connect to remote databases during local development with wrangler dev","description":"You can now connect directly to remote databases from wrangler dev using localConnectionString, with TLS support enabling secure connections while keeping your Worker code running locally","url":"https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/og.png?v=d2433160b97f1728","dateModified":"2025-12-04","datePublished":"2025-12-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
