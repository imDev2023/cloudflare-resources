---
description: Manage leaked credentials detection rules and custom detections using the API.
title: Common API calls
image: https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/og.png?v=373bc972a7710738
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Common API calls

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following examples address common scenarios of using the Cloudflare API to manage and configure leaked credentials detection.

If you are using Terraform, refer to [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/).

## General operations

The following API examples cover basic operations such as enabling and disabling the leaked credentials detection.

### Turn on leaked credentials detection

To turn on leaked credentials detection, use a `POST` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Update the Leaked Credential Checks status for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
	--request POST \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"enabled": true
	}'
```

### Turn off leaked credentials detection

To turn off leaked credentials detection, use a `POST` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Update the Leaked Credential Checks status for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
	--request POST \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"enabled": false
	}'
```

### Get status of leaked credentials detection

To obtain the current status of the leaked credentials detection, use a `GET` request similar to the following:

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

*Get the Leaked Credential Checks status for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
	--request GET \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

```json
{
	"result": {
		"enabled": true
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

## Custom detection location operations

The following API examples cover operations on [custom detection locations](https://developers.cloudflare.com/waf/detections/leaked-credentials/#custom-detection-locations) for leaked credentials detection.

### Add a custom detection location

To add a custom detection location, use a `POST` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Create a custom detection location for a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks/detections" \
	--request POST \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"username": "lookup_json_string(http.request.body.raw, \"user\")",
		"password": "lookup_json_string(http.request.body.raw, \"secret\")"
	}'
```

### Get existing custom detection locations

To get a list of existing custom detection locations, use a `GET` request similar to the following:

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

*List the custom detection locations of a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks/detections" \
	--request GET \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

```json
{
	"result": [
		{
			"id": "<DETECTION_ID>",
			"username": "lookup_json_string(http.request.body.raw, \"user\")",
			"password": "lookup_json_string(http.request.body.raw, \"secret\")"
		}
		// (...)
	],
	"success": true,
	"errors": [],
	"messages": []
}
```

### Delete a custom detection location

To delete a custom detection location, use a `DELETE` request similar to the following:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>

</details>

*Delete a custom detection location from a zone.bash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks/detections/$DETECTION_ID" \
	--request DELETE \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```
