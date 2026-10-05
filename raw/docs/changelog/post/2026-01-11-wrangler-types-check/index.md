---
description: A new flag for `wrangler types` lets you verify your generated types are up to date without modifying any files.
title: Validate your generated types with `wrangler types --check`
image: https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/og.png?v=82ec6197b190aebb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 12, 2026

## Validate your generated types with \`wrangler types --check\`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now supports a `--check` flag for the `wrangler types` command. This flag validates that your generated types are up to date without writing any changes to disk.

This is useful in CI/CD pipelines where you want to ensure that developers have regenerated their types after making changes to their Wrangler configuration. If the types are out of date, the command will exit with a non-zero status code.

```sh
npx wrangler types --check
```

If your types are up to date, the command will succeed silently. If they are out of date, you'll see an error message indicating which files need to be regenerated.

For more information, see the [Wrangler types documentation](https://developers.cloudflare.com/workers/wrangler/commands/general/#types).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/#page","headline":"Validate your generated types with `wrangler types --check`","description":"A new flag for wrangler types lets you verify your generated types are up to date without modifying any files.","url":"https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/og.png?v=82ec6197b190aebb","dateModified":"2026-01-12","datePublished":"2026-01-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
