---
description: Cloudflare's API handles rate limiting automatically in the SDKs and how to respond appropriately in your code.
title: Introducing new headers for rate limiting on Cloudflare's API
image: https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/og.png?v=c7835bc1dc1d51a5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 3, 2025

## Introducing new headers for rate limiting on Cloudflare's API

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's API now supports rate limiting headers using the pattern developed by the [IETF draft on rate limiting ↗︎](https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html). This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.

Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.

As always, if you need any help with rate limits, please contact Support.

#### Changes

#### New Headers

**Headers that are always returned:**

- `Ratelimit`: List of service limit items, composed of the limit name, the remaining quota ( `r`) and the time next window resets ( `t`). For example: `"default";r=50;t=30`
- `Ratelimit-Policy`: List of quota policy items, composed of the policy name, the total quota ( `q`) and the time window the quota applies to ( `w`). For example: `"burst";q=100;w=60`

**Returned only when a rate limit has been reached (error code: 429):**

- Retry-After: Number of Seconds until more capacity is available, rounded up

#### SDK Back offs

- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached.

#### GraphQL and Edge APIs

These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL.

#### For more information

- [Rate limits at Cloudflare ↗︎](https://developers.cloudflare.com/fundamentals/api/reference/limits/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/#page","headline":"Introducing new headers for rate limiting on Cloudflare's API","description":"Cloudflare's API handles rate limiting automatically in the SDKs and how to respond appropriately in your code.","url":"https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/og.png?v=c7835bc1dc1d51a5","dateModified":"2025-09-03","datePublished":"2025-09-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
