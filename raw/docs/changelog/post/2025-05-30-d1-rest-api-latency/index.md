---
description: D1 REST API request latency improvements.
title: 50-500ms Faster D1 REST API Requests
image: https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/og.png?v=73251b96381d9090
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 29, 2025

## 50-500ms Faster D1 REST API Requests

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Users using Cloudflare's [REST API](https://developers.cloudflare.com/api/resources/d1/) to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.

Latency improvements range from 50-500 ms depending on request location and [database location](https://developers.cloudflare.com/d1/configuration/data-location/) and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.

D1 query endpoints like `/query` and `/raw` have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/#page","headline":"50-500ms Faster D1 REST API Requests","description":"D1 REST API request latency improvements.","url":"https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/og.png?v=73251b96381d9090","dateModified":"2025-05-29","datePublished":"2025-05-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
