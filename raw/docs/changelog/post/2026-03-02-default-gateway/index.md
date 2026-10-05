---
description: AI Gateway now automatically creates a gateway for you on your first request.
title: Get started with AI Gateway automatically
image: https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/og.png?v=a75ba15a2800d324
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 2, 2026

## Get started with AI Gateway automatically

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now start using AI Gateway with a single API call — no setup required. Use `default` as your gateway ID, and AI Gateway creates one for you automatically on the first request.

To try it out, [create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `AI Gateway - Read`, `AI Gateway - Edit`, and `Workers AI - Read` permissions, then run:

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/$CLOUDFLARE_ACCOUNT_ID/default/compat/chat/completions \
  --header "cf-aig-authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    "messages": [
      {
        "role": "user",
        "content": "What is Cloudflare?"
      }
    ]
  }'
```

AI Gateway gives you logging, caching, rate limiting, and access to multiple AI providers through a single endpoint. For more information, refer to [Get started](https://developers.cloudflare.com/ai-gateway/get-started/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/#page","headline":"Get started with AI Gateway automatically","description":"AI Gateway now automatically creates a gateway for you on your first request.","url":"https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/og.png?v=a75ba15a2800d324","dateModified":"2026-03-02","datePublished":"2026-03-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
