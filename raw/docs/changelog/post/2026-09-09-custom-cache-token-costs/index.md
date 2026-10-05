---
description: Set custom cache-read and cache-write token rates for requests routed through AI Gateway.
title: AI Gateway custom costs support cache tokens
image: https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/og.png?v=4c56412cd6c6d7e7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 9, 2026

## AI Gateway custom costs support cache tokens

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.

Add `per_cache_read_token` or `per_cache_write_token` to the `cf-aig-custom-cost` header:

```json
{
	"per_token_in": 0.000001,
	"per_token_out": 0.000002,
	"per_cache_read_token": 0.0000001,
	"per_cache_write_token": 0.0000005
}
```

Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to `per_token_in`. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.

Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.

For more information, refer to [Custom costs](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/#page","headline":"AI Gateway custom costs support cache tokens","description":"Set custom cache-read and cache-write token rates for requests routed through AI Gateway.","url":"https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/og.png?v=4c56412cd6c6d7e7","dateModified":"2026-09-09","datePublished":"2026-09-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
