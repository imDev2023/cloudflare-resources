---
description: Sync individual files on demand and limit website crawling to a specific sitemap.
title: AI Search now with more granular controls over indexing
image: https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/og.png?v=2d827da17b518532
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 9, 2026

## AI Search now with more granular controls over indexing

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Get your content updates into [AI Search](https://developers.cloudflare.com/ai-search/) faster and avoid a full rescan when you do not need it.

#### Reindex individual files without a full sync

Updated a file or need to retry one that errored? When you know exactly which file changed, you can now [reindex it directly](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) instead of rescanning your entire data source.

Go to **Overview** > **Indexed Items** and select the sync icon next to any file to reindex it immediately.

![Sync individual files from Indexed Items](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2118,height=782,format=webp/_astro/individual-file-indexing.CQgoIj85.png)

#### Crawl only the sitemap you need

By default, AI Search crawls all sitemaps listed in your `robots.txt`, up to the [maximum files per index limit](https://developers.cloudflare.com/ai-search/platform/limits-pricing/#limits). If your site has multiple sitemaps but you only want to index a specific set, you can now [specify a single sitemap URL](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap) to limit what the crawler visits.

For example, if your `robots.txt` lists both `blog-sitemap.xml` and `docs-sitemap.xml`, you can specify just `https://example.com/docs-sitemap.xml` to index only your documentation.

Configure your selection anytime in **Settings** > **Parsing options** > **Specific sitemaps**, then trigger a sync to apply the changes.

![Specify a sitemap in Parsinh options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1973,height=387,format=webp/_astro/specify-sitemap.pLCkwmJ-.png)

Learn more about [indexing controls](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) and [website crawling configuration](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/#page","headline":"AI Search now with more granular controls over indexing","description":"Sync individual files on demand and limit website crawling to a specific sitemap.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/og.png?v=2d827da17b518532","dateModified":"2026-02-09","datePublished":"2026-02-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
