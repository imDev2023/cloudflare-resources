---
description: Scale browser automation with more concurrent browsers, faster launches, and higher Quick Actions request throughput by default.
title: Run more headless browsers concurrently with Browser Run
image: https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/og.png?v=ab9d74902e6e2f18
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 20, 2026

## Run more headless browsers concurrently with Browser Run

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use [Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) for one-request tasks such as screenshots, PDFs, and capturing page content.

If you are on the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/), your default [limits](https://developers.cloudflare.com/browser-run/limits/#workers-paid) are now higher:

| Limit | Previous | New |
| --- | --- | --- |
| Concurrent browsers | 120 | **200** |
| New browser instances / second | 1 | **3** |
| Quick Actions requests / second | 10 | **30** |

You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many [Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, [request higher limits ↗︎](https://forms.gle/CdueDKvb26mTaepa9).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/#page","headline":"Run more headless browsers concurrently with Browser Run","description":"Scale browser automation with more concurrent browsers, faster launches, and higher Quick Actions request throughput by default.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/og.png?v=ab9d74902e6e2f18","dateModified":"2026-08-20","datePublished":"2026-08-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
