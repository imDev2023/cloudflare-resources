---
description: Adaptive analytics datasets now retain at least 31 days of data on all plans, so Free and Pro domains can view and query the last 30 days of HTTP, security, and DNS analytics.
title: 30 days of analytics data on every plan
image: https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/og.png?v=81d0b3d70847ef41
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## 30 days of analytics data on every plan

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Every plan now gets at least 30 days of analytics data. Adaptive analytics datasets, such as HTTP requests, security events, and DNS analytics, retain at least 31 days of data for Free and Pro domains, and you can query up to 30 days in a single request. Previously, Free and Pro domains could see between 24 hours and 8 days of history depending on the dataset.

A full month of history lets you investigate an issue after it happens, compare today with the same day in previous weeks, and tell a one-time spike from a longer trend. The change applies in the Cloudflare dashboard, in [Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/), and through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

Domain analytics also now live in one place. In the Cloudflare dashboard, select a domain and go to **Analytics** to see Traffic, Performance, Security, Cache, Origin, DNS, and Visitors as tabs that share one time range and one set of filters. Account-level analytics are under **Observability** > **Analytics**.

This change does not alter which datasets or fields your plan can access. Aggregated datasets, such as `httpRequests1hGroups`, keep their existing per-plan limits. To check the exact retention and query window for a zone or account, query the [settings](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/) for each dataset.

For plan-specific limits, refer to [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/#availability), [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/#availability), and [GraphQL Analytics API limits](https://developers.cloudflare.com/analytics/graphql-api/limits/#node-limits-and-availability).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/#page","headline":"30 days of analytics data on every plan","description":"Adaptive analytics datasets now retain at least 31 days of data on all plans, so Free and Pro domains can view and query the last 30 days of HTTP, security, and DNS analytics.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/og.png?v=81d0b3d70847ef41","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
