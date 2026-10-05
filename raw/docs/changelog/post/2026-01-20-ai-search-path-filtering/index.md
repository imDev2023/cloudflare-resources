---
description: Control which paths to include or exclude from indexing.
title: AI Search path filtering for website and R2 data sources
image: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/og.png?v=9e2f1908538fc5d9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2026

## AI Search path filtering for website and R2 data sources

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now includes [path filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/) for both [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/#path-filtering) and [R2](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/#path-filtering) data sources. You can now control which content gets indexed by defining include and exclude rules for paths.

By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.

![Path filtering configuration in AI Search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2346,height=1360,format=webp/_astro/path-filtering.BCH7HN-Q.png)

Path filtering uses [micromatch ↗︎](https://github.com/micromatch/micromatch) patterns, so you can use `*` to match within a directory and `**` to match across directories.

| Use case | Include | Exclude |
| --- | --- | --- |
| Index docs but skip drafts | `**/docs/**` | `**/docs/drafts/**` |
| Keep admin pages out of results | — | `**/admin/**` |
| Index only English content | `**/en/**` | — |

Configure path filters when creating a new instance or update them anytime from **Settings**. Check out [path filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/) to learn more.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/#page","headline":"AI Search path filtering for website and R2 data sources","description":"Control which paths to include or exclude from indexing.","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/og.png?v=9e2f1908538fc5d9","dateModified":"2026-01-20","datePublished":"2026-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
