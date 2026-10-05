---
description: Expanded security insights with new API endpoints for aggregated authentication request data
title: Leaked Credentials Insights in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/og.png?v=c5ba010b42d1ccd8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2025

## Leaked Credentials Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its security insights, providing visibility into aggregate trends in authentication requests, including the detection of leaked credentials through [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) scans.

We have now introduced the following endpoints:

- [`/leaked_credential_checks/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/): Retrieves summaries of HTTP authentication requests distribution across two different dimensions.
- [`/leaked_credential_checks/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/): Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.

The following dimensions are available, displaying the distribution of HTTP authentication requests based on:

- `compromised`: Credential status (clean vs. compromised).
- `bot_class`: [Bot class](https://developers.cloudflare.com/radar/concepts/bot-classes) (human vs. bot).

Dive deeper into leaked credential detection in this [blog post ↗︎](https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/) and learn more about the expanded Radar security insights in our [blog post ↗︎](https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/#page","headline":"Leaked Credentials Insights in Cloudflare Radar","description":"Expanded security insights with new API endpoints for aggregated authentication request data","url":"https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/og.png?v=c5ba010b42d1ccd8","dateModified":"2025-03-18","datePublished":"2025-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
