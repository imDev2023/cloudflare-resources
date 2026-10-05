---
description: Control how Cloudflare fetches large files from your origin by configuring Origin Range Requests with the Rulesets API.
title: Configure Origin Range Requests with the Rulesets API
image: https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/og.png?v=79020c197e69e7a1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## Configure Origin Range Requests with the Rulesets API

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.

Set `origin_range_requests.mode` to `on`, `off`, or `default` for any traffic matched by a Cache Rule.

To override Cloudflare's default Origin Range Requests behavior, set the mode to `off`. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:

```json
{
  "expression": "true",
  "action": "set_cache_settings",
  "action_parameters": {
    "origin_range_requests": {
      "mode": "off"
    }
  }
}
```

Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores `Range` and returns a complete `200 OK`, Cloudflare can use the response but must download the complete file. Origins should honor `Accept-Encoding: identity` and return consistent, unencoded partial responses.

For configuration details and mode behavior, refer to [Origin Range Requests in Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#origin-range-requests). For client responses and the complete origin contract, refer to [Range request behavior](https://developers.cloudflare.com/cache/reference/range-requests/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/#page","headline":"Configure Origin Range Requests with the Rulesets API","description":"Control how Cloudflare fetches large files from your origin by configuring Origin Range Requests with the Rulesets API.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/og.png?v=79020c197e69e7a1","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
