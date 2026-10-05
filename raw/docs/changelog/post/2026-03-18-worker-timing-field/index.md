---
description: Use the new cf.timings.worker_msec field to build rules based on Cloudflare Worker execution time.
title: Worker execution timing field now available in Rules
image: https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/og.png?v=12ddfc257625e2a9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2026

## Worker execution timing field now available in Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `cf.timings.worker_msec` field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.

You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.

#### Field details

| Field | Type | Description |
| --- | --- | --- |
| `cf.timings.worker_msec` | Integer | The time spent executing a Cloudflare Worker in milliseconds. Returns `0` if no Worker was invoked. |

Example filter expression:

```plaintext
cf.timings.worker_msec > 500
```

For more information, refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/#page","headline":"Worker execution timing field now available in Rules","description":"Use the new cf.timings.worker_msec field to build rules based on Cloudflare Worker execution time.","url":"https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/og.png?v=12ddfc257625e2a9","dateModified":"2026-03-18","datePublished":"2026-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
