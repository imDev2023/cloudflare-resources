---
description: Restrict R2 bucket data storage and processing to the United States.
title: New `us` jurisdiction for R2
image: https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/og.png?v=c8a1a54a515506e7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 17, 2026

## New \`us\` jurisdiction for R2

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 now supports a `us` [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions), which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.

Use the jurisdiction-specific S3 endpoint to create and access buckets in the `us` jurisdiction:

`https://<ACCOUNT_ID>.us.r2.cloudflarestorage.com`

To access a bucket in the `us` jurisdiction from Workers, set `jurisdiction` in your R2 binding:

```jsonc
{
	"r2_buckets": [
		{
			"binding": "MY_BUCKET",
			"bucket_name": "<YOUR_BUCKET_NAME>",
			"jurisdiction": "us"
		}
	]
}
```

```toml
[[r2_buckets]]
binding = "MY_BUCKET"
bucket_name = "<YOUR_BUCKET_NAME>"
jurisdiction = "us"
```

Once an R2 bucket is created, its jurisdiction cannot be changed.

For setup instructions and the full list of supported jurisdictions, refer to [R2 data location](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/#page","headline":"New `us` jurisdiction for R2","description":"Restrict R2 bucket data storage and processing to the United States.","url":"https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/og.png?v=c8a1a54a515506e7","dateModified":"2026-08-17","datePublished":"2026-08-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
