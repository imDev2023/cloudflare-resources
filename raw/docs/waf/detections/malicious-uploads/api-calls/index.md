---
description: Manage malicious upload detection using the Cloudflare API.
title: Common API calls
image: https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/og.png?v=373bc972a7710738
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Common API calls

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following examples address common scenarios of using the Cloudflare API to manage and configure WAF content scanning.

If you are using Terraform, refer to [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/).

## General operations

The following API examples cover basic operations such as enabling and disabling WAF content scanning.

### Enable WAF content scanning

To enable content scanning, use a `POST` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Enable Content Scanning for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/enable" \
	--request POST \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

### Disable WAF content scanning

To disable content scanning, use a `POST` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Disable Content Scanning for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/disable" \
	--request POST \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

### Get WAF content scanning status

To obtain the current status of the content scanning feature, use a `GET` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Zone WAF Read</code>
- <code>Account WAF Write</code>
- <code>Account WAF Read</code>

</details>

*Get the Content Scanning status for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/settings" \
	--request GET \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

## Custom expression operations

The following API examples cover operations on custom scan expressions for content scanning.

### Get existing custom scan expressions

To get a list of existing custom scan expressions, use a `GET` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Zone WAF Read</code>
- <code>Account WAF Write</code>
- <code>Account WAF Read</code>

</details>

*List the Content Scanning custom expressions of a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads" \
	--request GET \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

```json
{
	"result": [
		{
			"id": "<EXPRESSION_ID>",
			"payload": "lookup_json_string(http.request.body.raw, \"file\")"
		}
	],
	"success": true,
	"errors": [],
	"messages": []
}
```

### Add a custom scan expression

Use a `POST` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Create Content Scanning custom expressions for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads" \
	--request POST \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '[
		{
				"payload": "lookup_json_string(http.request.body.raw, \"file\")"
		}
	]'
```

### Delete a custom scan expression

Use a `DELETE` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Delete a Content Scanning custom expression from a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads/$EXPRESSION_ID" \
	--request DELETE \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```
