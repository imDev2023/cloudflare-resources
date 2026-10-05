---
description: Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through [Bring Your Own Key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).
title: Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store
image: https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/og.png?v=1b22e4ca67f88484
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2025

## Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store

[Secrets Store](https://developers.cloudflare.com/secrets-store/) [AI Gateway](https://developers.cloudflare.com/ai-gateway/) [SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through [Bring Your Own Key ↗︎](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/). Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.

You can now create a secret directly from your AI Gateway [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/ai-gateway) by navigating into your gateway -> **Provider Keys** -> **Add**.

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1842,format=webp/_astro/add-secret-ai-gateway.B-SIPr6s.png)

You can also create your secret with the newly available **ai\_gateway** scope via [wrangler ↗︎](https://developers.cloudflare.com/workers/wrangler/commands/), the [Secrets Store dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store), or the [API ↗︎](https://developers.cloudflare.com/api/resources/secrets_store/).

Then, pass the key in the request header using its Secrets Store reference:

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/my-gateway/anthropic/v1/messages \
 --header 'cf-aig-authorization: ANTHROPIC_KEY_1 \
 --header 'anthropic-version: 2023-06-01' \
 --header 'Content-Type: application/json' \
 --data  '{"model": "claude-3-opus-20240229", "messages": [{"role": "user", "content": "What is Cloudflare?"}]}'
```

Or, using Javascript:

```plaintext
import Anthropic from '@anthropic-ai/sdk';


const anthropic = new Anthropic({
 apiKey: "ANTHROPIC_KEY_1",
 baseURL: "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/my-gateway/anthropic",
});


const message = await anthropic.messages.create({
 model: 'claude-3-opus-20240229',
 messages: [{role: "user", content: "What is Cloudflare?"}],
 max_tokens: 1024
});
```

For more information, check out the [blog ↗︎](https://blog.cloudflare.com/ai-gateway-aug-2025-refresh)!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/#page","headline":"Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store","description":"Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through Bring Your Own Key.","url":"https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/og.png?v=1b22e4ca67f88484","dateModified":"2025-08-25","datePublished":"2025-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
