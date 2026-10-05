---
description: The Workers Routes API now returns a correct response and the Secrets API has been added to the Cloudflare API docs.
title: Fixed and documented Workers Routes and Secrets API
image: https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/og.png?v=9362f072cf6bc28e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2025

## Fixed and documented Workers Routes and Secrets API

[Workers](https://developers.cloudflare.com/workers/) [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Workers Routes API

Previously, a request to the Workers [Create Route API](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/create/) always returned `null` for "script" and an empty string for "pattern" even if the request was successful.

*Example requestbash*

```bash
curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \
-X PUT \
-H "Authorization: Bearer $CF_API_TOKEN" \
-H 'Content-Type: application/json' \
--data '{ "pattern": "example.com/*", "script": "hello-world-script" }'
```

*Example bad responsejson*

```json
{
	"result": {
		"id": "bf153a27ba2b464bb9f04dcf75de1ef9",
		"pattern": "",
		"script": null,
		"request_limit_fail_open": false
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

Now, it properly returns all values!

*Example good responsejson*

```json
{
	"result": {
		"id": "bf153a27ba2b464bb9f04dcf75de1ef9",
		"pattern": "example.com/*",
		"script": "hello-world-script",
		"request_limit_fail_open": false
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

#### Workers Secrets API

The [Workers](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/) and [Workers for Platforms](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/) secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) (>4.2.0) and [cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) (>4.1.0).

Note the `cloudflare_workers_secret` and `cloudflare_workers_for_platforms_script_secret` [Terraform resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:

- [Secrets Store](https://developers.cloudflare.com/api/resources/secrets_store/) with the "Secrets Store Secret" binding on Workers and Workers for Platforms Script Upload
- "Secret Text" Binding on [Workers Script Upload](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/update/) and [Workers for Platforms Script Upload](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/)
- Workers (and WFP) Secrets API

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/#page","headline":"Fixed and documented Workers Routes and Secrets API","description":"The Workers Routes API now returns a correct response and the Secrets API has been added to the Cloudflare API docs.","url":"https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/og.png?v=9362f072cf6bc28e","dateModified":"2025-04-15","datePublished":"2025-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
