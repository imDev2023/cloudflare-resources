---
description: Cloudflare introduces Custom Errors (beta), building on Custom Error Responses with new asset storage capabilities
title: "Custom Errors (beta): Stored Assets &amp; Account-level Rules"
image: https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/og.png?v=55ff1ae9e2d9ca7d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 11, 2025

## Custom Errors (beta): Stored Assets & Account-level Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're introducing [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.

This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.

This brings the following new capabilities:

- **Custom error assets** – Fetch and store external error pages at the edge for use in error responses.
- **Account-Level custom errors** – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.

You can use Cloudflare API to upload your existing assets for use with Custom Errors:

```bash
curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets" \
--header "Authorization: Bearer <API_TOKEN>" \
--header 'Content-Type: application/json' \
--data '{
  "name": "maintenance",
  "description": "Maintenance template page",
  "url": "https://example.com/"
}'
```

You can then reference the stored asset in a Custom Error rule:

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint" \
--header "Authorization: Bearer <API_TOKEN>" \
--header 'Content-Type: application/json' \
--data '{
  "rules": [
		{
			"action": "serve_error",
			"action_parameters": {
				"asset_name": "maintenance",
				"content_type": "text/html",
				"status_code": 503
			},
			"enabled": true,
			"expression": "http.request.uri.path contains \"error\""
		}
	]
}'
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/#page","headline":"Custom Errors (beta): Stored Assets & Account-level Rules","description":"Cloudflare introduces Custom Errors (beta), building on Custom Error Responses with new asset storage capabilities","url":"https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/og.png?v=55ff1ae9e2d9ca7d","dateModified":"2025-02-11","datePublished":"2025-02-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
