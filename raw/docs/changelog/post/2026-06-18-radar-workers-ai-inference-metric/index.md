---
description: Workers AI model and task popularity now reflects the number of inferences rather than the number of unique accounts
title: Updated Workers AI popularity metric in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/og.png?v=61101259883a4824
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 18, 2026

## Updated Workers AI popularity metric in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has changed how it measures [Workers AI](https://developers.cloudflare.com/workers-ai/) model and task popularity.

Previously, popularity was based on the number of unique accounts running inferences against each model or task. It is now based on the **number of inferences**, giving a more representative view of actual usage volume. This change will affect all new measurements as well as historical data. As a result, the model and task distributions shown on Radar may differ from what you saw previously, and historical trends may shift accordingly.

The [Workers AI model popularity ↗︎](https://radar.cloudflare.com/ai-insights#workers-ai-model-popularity) chart shows the distribution of inferences across models.

![Screenshot of the Workers AI model popularity chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=938,format=webp/_astro/workers-ai-model-popularity.CMw_WVXg.png)

The [Workers AI task popularity ↗︎](https://radar.cloudflare.com/ai-insights#workers-ai-task-popularity) chart shows the distribution of inferences across tasks.

![Screenshot of the Workers AI task popularity chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=938,format=webp/_astro/workers-ai-task-popularity.ZoA-NO8k.png)

The same data is available via the following API endpoints:

- [`/ai/inference/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2/)
- [`/ai/inference/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2/)

Explore the data on the [AI Insights page ↗︎](https://radar.cloudflare.com/ai-insights).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/#page","headline":"Updated Workers AI popularity metric in Cloudflare Radar","description":"Workers AI model and task popularity now reflects the number of inferences rather than the number of unique accounts","url":"https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/og.png?v=61101259883a4824","dateModified":"2026-06-18","datePublished":"2026-06-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
