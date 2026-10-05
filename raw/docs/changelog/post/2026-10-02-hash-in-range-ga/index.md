---
description: Use hash_in_range() in HTTP Ruleset Engine expressions to select a portion of requests.
title: hash_in_range() is globally available for HTTP products
image: https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/og.png?v=f5c092ebf0412ae3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## hash\_in\_range() is globally available for HTTP products

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`hash_in_range()` is globally available for HTTP products on all plans. It hashes fields into an integer within a specified range. Use this result to select a portion of requests.

Use `cf.random_seed` to select approximately 10% of requests at random:

```txt
hash_in_range(0, 100, cf.random_seed) < 10
```

With Cloudflare for SaaS, use [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/) to control rollout progression. Define `rollout_pct` as a custom key for each hostname. Set its value to an integer from 0 to 100. The expression selects approximately that percentage of requests:

```txt
hash_in_range(0, 100, cf.random_seed) < coalesce(lookup_json_integer(cf.hostname.metadata, "rollout_pct"), 0)
```

If `rollout_pct` is missing, `coalesce()` supplies `0`. The rule then matches no requests.

For details, refer to the [`hash_in_range()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hash_in_range).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/#page","headline":"hash_in_range() is globally available for HTTP products","description":"Use hash_in_range() in HTTP Ruleset Engine expressions to select a portion of requests.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/og.png?v=f5c092ebf0412ae3","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
