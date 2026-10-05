---
description: Web Analytics introduces performance optimizations and safety thresholds for accounts tracking a large volume of websites.
title: Improved reliability for account-wide Web Analytics dashboards
image: https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/og.png?v=ec5468d06c32d00f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 14, 2026

## Improved reliability for account-wide Web Analytics dashboards

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.

For larger accounts (with >100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.

Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.

If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/#page","headline":"Improved reliability for account-wide Web Analytics dashboards","description":"Web Analytics introduces performance optimizations and safety thresholds for accounts tracking a large volume of websites.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/og.png?v=ec5468d06c32d00f","dateModified":"2026-07-14","datePublished":"2026-07-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
