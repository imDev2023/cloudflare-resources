---
description: Use Cloudflare Pipelines to ingest real time data streams, and load into R2.
title: Cloudflare Pipelines now available in beta
image: https://developers.cloudflare.com/changelog/post/2025-04-10-launching-pipelines/og.png?v=467ebe79f7b63234
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 10, 2025

## Cloudflare Pipelines now available in beta

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-10-launching-pipelines/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) is now available in beta, to all users with a [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/) plan.

Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a [Worker](https://developers.cloudflare.com/workers). Ingested data is automatically batched, written to output files, and delivered to an [R2 bucket](https://developers.cloudflare.com/r2) in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.

Create your first pipeline with a single command:

*Create a pipelinebash*

```bash
$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket

🌀 Authorizing R2 bucket "my-bucket"
🌀 Creating pipeline named "my-clickstream-pipeline"
✅ Successfully created pipeline my-clickstream-pipeline

Id:    0e00c5ff09b34d018152af98d06f5a1xvc
Name:  my-clickstream-pipeline
Sources:
  HTTP:
    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/
    Authentication:  off
    Format:          JSON
  Worker:
    Format:  JSON
Destination:
  Type:         R2
  Bucket:       my-bucket
  Format:       newline-delimited JSON
  Compression:  GZIP
Batch hints:
  Max bytes:     100 MB
  Max duration:  300 seconds
  Max records:   100,000

🎉 You can now send data to your pipeline!

Send data to your pipeline's HTTP endpoint:
curl "https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/" -d '[{ ...JSON_DATA... }]'

To send data to your pipeline from a Worker, add the following configuration to your config file:
{
  "pipelines": [
    {
      "pipeline": "my-clickstream-pipeline",
      "binding": "PIPELINE"
    }
  ]
}
```

Head over to our [getting started guide](https://developers.cloudflare.com/basin-pipelines/getting-started/) for an in-depth tutorial to building with Pipelines.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-10-launching-pipelines/#page","headline":"Cloudflare Pipelines now available in beta","description":"Use Cloudflare Pipelines to ingest real time data streams, and load into R2.","url":"https://developers.cloudflare.com/changelog/post/2025-04-10-launching-pipelines/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-10-launching-pipelines/og.png?v=467ebe79f7b63234","dateModified":"2025-04-10","datePublished":"2025-04-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
