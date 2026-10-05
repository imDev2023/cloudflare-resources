---
description: Cloud Connector now integrates with Cloudflare R2 for object storage.
title: Cloud Connector Now Supports R2
image: https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/og.png?v=9062e578d41ae866
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 22, 2024

## Cloud Connector Now Supports R2

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, you can use [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) to route traffic to your [R2 buckets](https://developers.cloudflare.com/r2/) based on URLs, headers, geolocation, and more.

Example setup:

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules" \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '[
  {
    "expression": "http.request.uri.path wildcard \"/images/*\"",
    "provider": "cloudflare_r2",
    "description": "Connect to R2 bucket containing images",
    "parameters": {
      "host": "mybucketcustomdomain.example.com"
    }
  }
]'
```

Get started using [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/#page","headline":"Cloud Connector Now Supports R2","description":"Cloud Connector now integrates with Cloudflare R2 for object storage.","url":"https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/og.png?v=9062e578d41ae866","dateModified":"2024-11-22","datePublished":"2024-11-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
