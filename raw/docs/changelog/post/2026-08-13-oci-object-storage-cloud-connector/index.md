---
description: Route matching traffic to public Oracle Cloud Object Storage buckets using path-style or virtual-hosted S3-compatible endpoints.
title: Oracle Cloud Infrastructure Object Storage support in Cloud Connector
image: https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/og.png?v=ab5f2db3556b0559
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 13, 2026

## Oracle Cloud Infrastructure Object Storage support in Cloud Connector

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.

OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional `oraclecloud.com` and dedicated `customer-oci.com` path-style endpoints.

Public buckets only

Cloud Connector does not sign requests or provide OCI credentials. Your bucket must allow anonymous object reads. Private buckets and pre-authenticated request URLs are not supported.

#### API example

Set `provider` to `oci_storage` and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:

```json
{
	"expression": "http.request.uri.path wildcard \"/assets/*\"",
	"provider": "oci_storage",
	"description": "Route assets to OCI Object Storage",
	"enabled": true,
	"parameters": {
		"host": "<BUCKET_NAME>.vhcompat.objectstorage.<REGION>.oci.customer-oci.com"
	}
}
```

For endpoint formats and bucket requirements, refer to [Supported cloud providers in Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/#page","headline":"Oracle Cloud Infrastructure Object Storage support in Cloud Connector","description":"Route matching traffic to public Oracle Cloud Object Storage buckets using path-style or virtual-hosted S3-compatible endpoints.","url":"https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/og.png?v=ab5f2db3556b0559","dateModified":"2026-08-13","datePublished":"2026-08-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
