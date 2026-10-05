---
description: Cloudflare is removing five fields from the meta object of DNS records.
title: Removed unused meta fields from DNS records
image: https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/og.png?v=dbff365ac243ba57
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 2, 2025

## Removed unused meta fields from DNS records

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare is removing five fields from the `meta` object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.

The affected fields are:

- the `auto_added` boolean
- the `managed_by_apps` boolean and corresponding `apps_install_id`
- the `managed_by_argo_tunnel` boolean and corresponding `argo_tunnel_id`

An example record returned from the API would now look like the following:

*Updated API Responsejson*

```json
{
	"result": {
		"id": "<ID>",
		"zone_id": "<ZONE_ID>",
		"zone_name": "example.com",
		"name": "www.example.com",
		"type": "A",
		"content": "192.0.2.1",
		"proxiable": true,
		"proxied": false,
		"ttl": 1,
		"locked": false,
		"meta": {
			"auto_added": false,
			"managed_by_apps": false,
			"managed_by_argo_tunnel": false,
			"source": "primary"
		},
		"comment": null,
		"tags": [],
		"created_on": "2025-03-17T20:37:05.368097Z",
		"modified_on": "2025-03-17T20:37:05.368097Z"
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

For more guidance, refer to [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/#page","headline":"Removed unused meta fields from DNS records","description":"Cloudflare is removing five fields from the meta object of DNS records.","url":"https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/og.png?v=dbff365ac243ba57","dateModified":"2025-02-02","datePublished":"2025-02-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
