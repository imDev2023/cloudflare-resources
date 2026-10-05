---
description: A new command to retrieve your current authentication credentials for use with other tools and scripts.
title: Retrieve your authentication token with `wrangler auth token`
image: https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/og.png?v=bdabaff9fe6a9f50
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 18, 2025

## Retrieve your authentication token with \`wrangler auth token\`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now includes a new [`wrangler auth token`](https://developers.cloudflare.com/workers/wrangler/commands/general/#auth-token) command that retrieves your current authentication token or credentials for use with other tools and scripts.

```sh
wrangler auth token
```

The command returns whichever authentication method is currently configured, in priority order: API token from `CLOUDFLARE_API_TOKEN`, or OAuth token from `wrangler login` (automatically refreshed if expired).

Use the `--json` flag to get structured output including the token type:

```sh
wrangler auth token --json
```

The JSON output includes the authentication type:

```jsonc
// API token
{ "type": "api_token", "token": "..." }

// OAuth token
{ "type": "oauth", "token": "..." }

// API key/email (only available with --json)
{ "type": "api_key", "key": "...", "email": "..." }
```

API key/email credentials from `CLOUDFLARE_API_KEY` and `CLOUDFLARE_EMAIL` require the `--json` flag since this method uses two values instead of a single token.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/#page","headline":"Retrieve your authentication token with `wrangler auth token`","description":"A new command to retrieve your current authentication credentials for use with other tools and scripts.","url":"https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/og.png?v=bdabaff9fe6a9f50","dateModified":"2025-12-18","datePublished":"2025-12-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
