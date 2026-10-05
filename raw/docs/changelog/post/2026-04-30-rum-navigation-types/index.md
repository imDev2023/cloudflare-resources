---
description: Monitor browser caching effectiveness and navigation behavior with new Navigation Type metrics in Web Analytics.
title: Web Analytics adds Navigation Type filtering and reporting
image: https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/og.png?v=9da88d444966cb7e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2026

## Web Analytics adds Navigation Type filtering and reporting

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Web Analytics now supports **Navigation Type** reporting and filtering.

This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.

Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of "Back-forward" navigations versus "Back-forward Cache", those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.

The same applies for regular "Navigate" entries — where "Navigate Cache", "Navigate Prefetch Cache" and "Prerender" would provide instant document retrieval — and "Reload", where "Reload cache" would be more optimal.

A high volume of "Reload" entries can also indicate a potential stability problem with your website.

By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.

For more information, refer to [Navigation Types](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/#navigation-types).

#### Key benefits

- **Monitor Cache Effectiveness:** See how often your site is served from the HTTP cache or bfcache.
- **Identify Performance Bottlenecks:** Filter by the different types to understand performance opportunity of improving browser cache hit ratio.

#### Analyze navigation types in the Cloudflare dashboard

You can now find the **Navigation Type** dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using "equals", "does not equal", "in", or "not in" matchers.

![Navigation Type filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2646,height=1040,format=webp/_astro/dash-web_analytics-navigation-type-filter.Cculflhp.png)

To check the list of popular navigation types, select **Page views** on the Web Analytics sidebar and scroll down to the bottom:

![Navigation Types list in Page Views tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2076,height=500,format=webp/_astro/dash-web_analytics-navigation-types-list.CWaiEQzO.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/#page","headline":"Web Analytics adds Navigation Type filtering and reporting","description":"Monitor browser caching effectiveness and navigation behavior with new Navigation Type metrics in Web Analytics.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/og.png?v=9da88d444966cb7e","dateModified":"2026-04-30","datePublished":"2026-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
