---
description: Control whether request and response bodies are stored in AI Gateway logs.
title: Log AI Gateway request metadata without storing payloads
image: https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/og.png?v=dee41ef3b6532add
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 17, 2026

## Log AI Gateway request metadata without storing payloads

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports the `cf-aig-collect-log-payload` header, which controls whether request and response bodies are stored in logs. By default, this header is set to `true` and payloads are stored alongside metadata. Set this header to `false` to skip payload storage while still logging metadata such as token counts, model, provider, status code, cost, and duration.

This is useful when you need usage metrics but do not want to persist sensitive prompt or response data.

```bash
curl https://gateway.ai.cloudflare.com/v1/$ACCOUNT_ID/$GATEWAY_ID/openai/chat/completions \
  --header "Authorization: Bearer $TOKEN" \
  --header 'Content-Type: application/json' \
  --header 'cf-aig-collect-log-payload: false' \
  --data '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "What is the email address and phone number of user123?"
      }
    ]
  }'
```

For more information, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/#collect-log-payload-cf-aig-collect-log-payload).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/#page","headline":"Log AI Gateway request metadata without storing payloads","description":"Control whether request and response bodies are stored in AI Gateway logs.","url":"https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/og.png?v=dee41ef3b6532add","dateModified":"2026-03-17","datePublished":"2026-03-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
