---
description: Enable IBM Cloud Logs as a Logpush destination
title: IBM Cloud Logs as Logpush destination
image: https://developers.cloudflare.com/changelog/post/2025-08-13-ibm-cloud-logs-destination/og.png?v=697afeb73defe58b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 13, 2025

## IBM Cloud Logs as Logpush destination

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-13-ibm-cloud-logs-destination/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush now supports IBM Cloud Logs as a native destination.

Logs from Cloudflare can be sent to [IBM Cloud Logs ↗︎](https://www.ibm.com/products/cloud-logs) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/). The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.

For more information, refer to [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-13-ibm-cloud-logs-destination/#page","headline":"IBM Cloud Logs as Logpush destination","description":"Enable IBM Cloud Logs as a Logpush destination","url":"https://developers.cloudflare.com/changelog/post/2025-08-13-ibm-cloud-logs-destination/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-13-ibm-cloud-logs-destination/og.png?v=697afeb73defe58b","dateModified":"2025-08-13","datePublished":"2025-08-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
