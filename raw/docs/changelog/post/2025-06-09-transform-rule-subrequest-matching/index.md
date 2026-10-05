---
description: Transform Rules now support the cf.worker.upstream_zone field, letting you conditionally apply rules based on which zone sent Workers subrequest.
title: Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules
image: https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/og.png?v=87b0d18c314aaa6b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 9, 2025

## Match Workers subrequests by upstream zone — cf.worker.upstream\_zone now supported in Transform Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use the [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field in [Transform Rules](https://developers.cloudflare.com/rules/transform/) to control rule execution based on whether a request originates from [Workers](https://developers.cloudflare.com/workers/), including subrequests issued by Workers in other zones.

![Match Workers subrequests by upstream zone in Transform Rules](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1446,height=988,format=webp/_astro/transform-rule-subrequest-matching.BeUBEN67.png)

**What's new:**

- `cf.worker.upstream_zone` is now supported in Transform Rules expressions.
- Skip or apply logic conditionally when handling [Workers subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

For example, to add a header when the subrequest comes from another zone:

Text in **Expression Editor** (replace `myappexample.com` with your domain):

```txt
(cf.worker.upstream_zone != "" and cf.worker.upstream_zone != "myappexample.com")
```

Selected operation under **Modify request header**: *Set static*

**Header name**: `X-External-Workers-Subrequest`

**Value**: `1`

This gives you more granular control in how you handle incoming requests for your zone.

Learn more in the [Transform Rules](https://developers.cloudflare.com/rules/transform/) documentation and [Rules language fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) reference.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/#page","headline":"Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules","description":"Transform Rules now support the cf.worker.upstream_zone field, letting you conditionally apply rules based on which zone sent Workers subrequest.","url":"https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/og.png?v=87b0d18c314aaa6b","dateModified":"2025-06-09","datePublished":"2025-06-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
