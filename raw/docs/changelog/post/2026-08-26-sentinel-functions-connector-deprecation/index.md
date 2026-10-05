---
description: Cloudflare Enterprise customers must migrate to the Cloudflare for Microsoft Sentinel CCF connector by 2026-09-14.
title: Azure Functions-based Microsoft Sentinel connector deprecation
image: https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/og.png?v=3e5b207ddc12302d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## Azure Functions-based Microsoft Sentinel connector deprecation

[Logpush Connectors](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) [Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Enterprise customers using the [Azure Functions-based Microsoft Sentinel connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview) must migrate to the [Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) by 2026-09-14.

Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.

To migrate, follow the [Microsoft Sentinel integration setup guide](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/).

#### Additional resources

- [Download Cloudflare's CCF Sentinel Solution ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview)
- [Microsoft Sentinel data lake overview ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)
- [About the CCF platform ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector)

For more information, refer to Microsoft's [Azure Monitor HTTP Data Collector API deprecation notice ↗︎](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/#page","headline":"Azure Functions-based Microsoft Sentinel connector deprecation","description":"Cloudflare Enterprise customers must migrate to the Cloudflare for Microsoft Sentinel CCF connector by 2026-09-14.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/og.png?v=3e5b207ddc12302d","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
