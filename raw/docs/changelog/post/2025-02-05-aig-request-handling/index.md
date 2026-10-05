---
description: AI Gateway has added additional request handling, with request timeouts and request retries
title: Request timeouts and retries with AI Gateway
image: https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/og.png?v=fb1732dd03f15af5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 6, 2025

## Request timeouts and retries with AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway adds additional ways to handle requests - [Request Timeouts](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-timeouts) and [Request Retries](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries), making it easier to keep your applications responsive and reliable.

Timeouts and retries can be used on both the [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) or directly to a [supported provider](https://developers.cloudflare.com/ai-gateway/usage/providers/).

**Request timeouts** A [request timeout](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-timeouts) allows you to trigger [fallbacks](https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/) or a retry if a provider takes too long to respond.

To set a request timeout directly to a provider, add a `cf-aig-request-timeout` header.

*Provider-specific endpoint examplebash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \
 --header 'Authorization: Bearer {cf_api_token}' \
 --header 'Content-Type: application/json' \
 --header 'cf-aig-request-timeout: 5000'
 --data '{"prompt": "What is Cloudflare?"}'
```

**Request retries** A [request retry](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries) automatically retries failed requests, so you can recover from temporary issues without intervening.

To set up request retries directly to a provider, add the following headers:

- cf-aig-max-attempts (number)
- cf-aig-retry-delay (number)
- cf-aig-backoff ("constant" | "linear" | "exponential)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/#page","headline":"Request timeouts and retries with AI Gateway","description":"AI Gateway has added additional request handling, with request timeouts and request retries","url":"https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/og.png?v=fb1732dd03f15af5","dateModified":"2025-02-06","datePublished":"2025-02-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
