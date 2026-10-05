---
description: Call third-party and Workers AI models through one Cloudflare REST API, with AI Gateway features applied automatically.
title: Call any AI model through AI Gateway's new REST API
image: https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/og.png?v=bc31d116546c2a72
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 21, 2026

## Call any AI model through AI Gateway's new REST API

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now uses the AI REST API on `api.cloudflare.com`. You can call any model — whether from OpenAI, Anthropic, Google, or hosted on Workers AI — through one unified API, using the same endpoints and authentication regardless of provider. Four endpoints are available:

- `POST /ai/run` — universal endpoint for all models and modalities
- `POST /ai/v1/chat/completions` — OpenAI SDK compatible
- `POST /ai/v1/responses` — OpenAI Responses API compatible
- `POST /ai/v1/messages` — Anthropic SDK compatible

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "openai/gpt-5.5",
    "messages": [{"role": "user", "content": "What is Cloudflare?"}]
  }'
```

All AI Gateway features — logging, caching, rate limiting, and guardrails — are applied automatically. Third-party models are billed through [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), so you do not need to manage separate provider API keys.

Third-party model requests are routed through your account's default gateway, which is created automatically on first use. To route requests through a specific gateway, add the `cf-aig-gateway-id` header.

If you are already calling Workers AI models through the existing REST API, that path (`/ai/run/@cf/{model}`) continues to work. To call Workers AI models through AI Gateway, use the `@cf/` model prefix (for example, `@cf/moonshotai/kimi-k2.6`) and include the `cf-aig-gateway-id` header to specify which gateway to route through.

For more details and examples, refer to the [REST API documentation](https://developers.cloudflare.com/ai-gateway/usage/rest-api/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/#page","headline":"Call any AI model through AI Gateway's new REST API","description":"Call third-party and Workers AI models through one Cloudflare REST API, with AI Gateway features applied automatically.","url":"https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/og.png?v=bc31d116546c2a72","dateModified":"2026-05-21","datePublished":"2026-05-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
