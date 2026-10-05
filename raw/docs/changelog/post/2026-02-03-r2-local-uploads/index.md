---
description: R2 Local Uploads reduces total request duration for uploads by up to 75%. It writes object data to a nearby location, then asynchronously copies it to your bucket. Data is available immediately.
title: Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta
image: https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/og.png?v=42b6700de8babcbc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 3, 2026

## Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Local Uploads](https://developers.cloudflare.com/r2/buckets/local-uploads/) is now available in open beta. Enable it on your [R2](https://developers.cloudflare.com/r2/) bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to [How R2 works](https://developers.cloudflare.com/r2/how-r2-works/) for details on how data is written to your bucket.

In our tests, we observed **up to 75% reduction in Time to Last Byte (TTLB)** for upload requests when Local Uploads is enabled.

![Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1506,height=596,format=webp/_astro/local-uploads-latency.R4pUgVuI.png)

This feature is ideal when:

- Your users are globally distributed
- Upload performance and reliability is critical to your application
- You want to optimize write performance without changing your bucket's primary location

To enable Local Uploads on your bucket, find **Local Uploads** in your bucket settings in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/r2/overview), or run:

```sh
npx wrangler r2 bucket local-uploads enable <BUCKET_NAME>
```

Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard [Class A operation costs](https://developers.cloudflare.com/r2/pricing/) same as upload requests made without Local Uploads.

For more information, refer to [Local Uploads](https://developers.cloudflare.com/r2/buckets/local-uploads/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/#page","headline":"Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta","description":"R2 Local Uploads reduces total request duration for uploads by up to 75%. It writes object data to a nearby location, then asynchronously copies it to your bucket. Data is available immediately.","url":"https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/og.png?v=42b6700de8babcbc","dateModified":"2026-02-03","datePublished":"2026-02-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
