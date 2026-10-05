---
description: Understand which tasks drive AI usage, where models may exceed task needs, and where faster or less expensive models may work.
title: Identify model overuse and potential savings with User Insights
image: https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/og.png?v=69d4f06b31506a75
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 29, 2026

## Identify model overuse and potential savings with User Insights

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway User Insights now gives you more context about the traffic flowing through your gateway. It shows what users and agents are doing with AI, and where a selected model may be more capable than a task requires.

On the analysis side, User Insights groups conversations by task, tracks conversation turns, and helps you compare model fit with cost and latency.

![User Insights task and model analysis grouped by task categories](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1434,height=606,format=webp/_astro/user-insights-task-analysis.CS2pm7wg.png)

The Potential Savings view highlights requests that may work with faster or less expensive models without compromising output quality. These are the same signals that Cloudflare's [Auto Router](https://developers.cloudflare.com/ai-gateway/features/auto-router/) uses to select a model based on task and cost.

![Potential Savings view comparing tasks and suggested models](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1506,height=669,format=webp/_astro/user-insights-potential-savings.C7j_Gjcn.png)

These new insights are available to all AI Gateway customers at no additional cost. For more information, refer to [User Insights](https://developers.cloudflare.com/ai-gateway/observability/user-insights/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/#page","headline":"Identify model overuse and potential savings with User Insights","description":"Understand which tasks drive AI usage, where models may exceed task needs, and where faster or less expensive models may work.","url":"https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/og.png?v=69d4f06b31506a75","dateModified":"2026-09-29","datePublished":"2026-09-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
