---
description: There are four new DEX and WARP client data sets available to all Cloudflare One customers.
title: DEX Logpush jobs
image: https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/og.png?v=b38cfafb83e8c668
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 12, 2025

## DEX Logpush jobs

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.

We've released four new WARP and DEX device data sets that can be exported via [Cloudflare Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/). These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.

1. [DEX Application Tests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/)
2. [DEX Device State Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_device_state_events/)
3. [WARP Config Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_config_changes/)
4. [WARP Toggle Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/)

To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard > Analytics & Logs > Logpush to get started.

![DEX logpush job creation dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2549,height=1283,format=webp/_astro/dex_logpush_datasets.CtCk36pX.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/#page","headline":"DEX Logpush jobs","description":"There are four new DEX and WARP client data sets available to all Cloudflare One customers.","url":"https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/og.png?v=b38cfafb83e8c668","dateModified":"2025-11-12","datePublished":"2025-11-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
