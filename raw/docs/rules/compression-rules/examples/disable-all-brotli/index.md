---
description: Create a compression rule to turn off Brotli compression for all incoming requests of a given zone.
title: Disable Brotli compression
image: https://developers.cloudflare.com/rules/compression-rules/examples/disable-all-brotli/og.png?v=1271a563f8567ede
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Disable Brotli compression

Create a compression rule to turn off Brotli compression for all incoming requests of a given zone.

Last updated Aug 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/compression-rules/examples/disable-all-brotli/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following example rule will disable Brotli compression for all incoming requests of a given zone. The only available compression algorithm will be Gzip.

**When incoming requests match**

- All incoming requests

**Then**

- **Compression options**: Custom
- **Define a custom order for compression types**: `Gzip`

If the client does not support Gzip compression, the response will be uncompressed.

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
						"ref": "always_use_gzip",
						"expression": "true",
						"action": "compress_response",
						"action_parameters": {
								"algorithms": [
										{
												"name": "gzip"
										}
								]
						}
				}
		]
	}'
```

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.
