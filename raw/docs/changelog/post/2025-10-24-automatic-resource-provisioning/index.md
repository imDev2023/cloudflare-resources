---
description: Wrangler can now automatically provision KV, R2, and D1 resources when deploying your Worker
title: Automatic resource provisioning for KV, R2, and D1
image: https://developers.cloudflare.com/changelog/post/2025-10-24-automatic-resource-provisioning/og.png?v=d768ac73df45f1bc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 24, 2025

## Automatic resource provisioning for KV, R2, and D1

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-24-automatic-resource-provisioning/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Previously, if you wanted to develop or deploy a worker with attached resources, you'd have to first manually create the desired resources. Now, if your Wrangler configuration file includes a KV namespace, D1 database, or R2 bucket that does not yet exist on your account, you can develop locally and deploy your application seamlessly, without having to run additional commands.

Automatic provisioning is launching as an open beta, and we'd love to hear your feedback to help us make improvements! It currently works for KV, R2, and D1 bindings. You can disable the feature using the `--no-x-provision` flag.

To use this feature, update to wrangler@4.45.0 and add bindings to your config file *without* resource IDs e.g.:

```jsonc
{
	"kv_namespaces": [{ "binding": "MY_KV" }],
	"d1_databases": [{ "binding": "MY_DB" }],
	"r2_buckets": [{ "binding": "MY_R2" }],
}
```

`wrangler dev` will then automatically create these resources for you locally, and on your next run of `wrangler deploy`, Wrangler will call the Cloudflare API to create the requested resources and link them to your Worker.

Though resource IDs will be automatically written back to your Wrangler config file after resource creation, resources will stay linked across future deploys even without adding the resource IDs to the config file. This is especially useful for shared templates, which now no longer need to include account-specific resource IDs when adding a binding.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-24-automatic-resource-provisioning/#page","headline":"Automatic resource provisioning for KV, R2, and D1","description":"Wrangler can now automatically provision KV, R2, and D1 resources when deploying your Worker","url":"https://developers.cloudflare.com/changelog/post/2025-10-24-automatic-resource-provisioning/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-24-automatic-resource-provisioning/og.png?v=d768ac73df45f1bc","dateModified":"2025-10-24","datePublished":"2025-10-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
