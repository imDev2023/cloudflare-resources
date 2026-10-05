---
description: Create a compression rule to set Gzip compression as the preferred compression method for CSV files.
title: Use Gzip compression for CSV files
image: https://developers.cloudflare.com/rules/compression-rules/examples/gzip-for-csv/og.png?v=aaff1874a06e7969
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Use Gzip compression for CSV files

Create a compression rule to set Gzip compression as the preferred compression method for CSV files.

Last updated Aug 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/compression-rules/examples/gzip-for-csv/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following example rule will configure Gzip compression as the preferred compression method for CSV files. If the visitor does not support this algorithm, Cloudflare will try to compress the response using a different algorithm supported by the visitor.

**When incoming requests match**

- Custom filter expression:
  - *File extension* *equals* `csv`

**Then**

- **Compression options**: Custom
- **Define a custom order for compression types**: `Gzip`, `Auto`

The following example sets the rules of an existing [entry point ruleset](https://developers.cloudflare.com/ruleset-engine/about/rulesets/#entry-point-ruleset) (with ID `{ruleset_id}`) for the `http_response_compression` phase to a single compression rule, using the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Response Compression Write</code>
- <code>Config Settings Write</code>
- <code>Dynamic URL Redirects Write</code>
- <code>Cache Settings Write</code>
- <code>Custom Errors Write</code>
- <code>Origin Write</code>
- <code>Managed headers Write</code>
- <code>Zone Transform Rules Write</code>
- <code>Mass URL Redirects Write</code>
- <code>Magic Firewall Write</code>
- <code>L4 DDoS Managed Ruleset Write</code>
- <code>HTTP DDoS Managed Ruleset Write</code>
- <code>Sanitize Write</code>
- <code>Transform Rules Write</code>
- <code>Select Configuration Write</code>
- <code>Bot Management Write</code>
- <code>Zone WAF Write</code>
- <code>Account WAF Write</code>
- <code>Account Rulesets Write</code>
- <code>Logs Write</code>
- <code>Logs Write</code>

</details>

*Update a zone rulesetbash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
	--request PUT \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"rules": [
				{
						"ref": "use_gzip_for_csv",
						"expression": "http.request.uri.path.extension eq \"csv\"",
						"action": "compress_response",
						"action_parameters": {
								"algorithms": [
										{
												"name": "gzip"
										},
										{
												"name": "auto"
										}
								]
						}
				}
		]
	}'
```

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.
