---
description: Create a compression rule to turn on Zstandard compression for response content types where Cloudflare applies compression by default.
title: Enable Zstandard compression for default content types
image: https://developers.cloudflare.com/rules/compression-rules/examples/enable-zstandard/og.png?v=397ec7213b055efa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enable Zstandard compression for default content types

Create a compression rule to turn on Zstandard compression for response content types where Cloudflare applies compression by default.

Last updated Aug 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/compression-rules/examples/enable-zstandard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following example rule will turn on Zstandard compression for response content types where [Cloudflare applies compression by default](https://developers.cloudflare.com/speed/optimization/content/compression/). If the client does not support Zstandard compression, it will use Brotli or Gzip compression as a fallback.

**When incoming requests match**

- Custom filter expression:
  - *Media Type* *is in* `text/html, text/richtext, text/plain, text/css, text/x-script, text/x-component, text/x-java-source, text/x-markdown, application/javascript, application/x-javascript, text/javascript, text/js, image/x-icon, image/vnd.microsoft.icon, application/x-perl, application/x-httpd-cgi, text/xml, application/xml, application/rss+xml, application/vnd.api+json, application/x-protobuf, application/json, multipart/bag, multipart/mixed, application/xhtml+xml, font/ttf, font/otf, font/x-woff, image/svg+xml, application/vnd.ms-fontobject, application/ttf, application/x-ttf, application/otf, application/x-otf, application/truetype, application/opentype, application/x-opentype, application/font-woff, application/eot, application/font, application/font-sfnt, application/wasm, application/javascript-binast, application/manifest+json, application/ld+json, application/graphql+json, application/geo+json`

**Then**

- **Compression options**: Custom
- **Define a custom order for compression types**: `Zstandard`, `Brotli`, `Gzip`

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
						"ref": "use_zstd_compression",
						"expression": "(http.response.content_type.media_type in {\"text/html\" \"text/richtext\" \"text/plain\" \"text/css\" \"text/x-script\" \"text/x-component\" \"text/x-java-source\" \"text/x-markdown\" \"application/javascript\" \"application/x-javascript\" \"text/javascript\" \"text/js\" \"image/x-icon\" \"image/vnd.microsoft.icon\" \"application/x-perl\" \"application/x-httpd-cgi\" \"text/xml\" \"application/xml\" \"application/rss+xml\" \"application/vnd.api+json\" \"application/x-protobuf\" \"application/json\" \"multipart/bag\" \"multipart/mixed\" \"application/xhtml+xml\" \"font/ttf\" \"font/otf\" \"font/x-woff\" \"image/svg+xml\" \"application/vnd.ms-fontobject\" \"application/ttf\" \"application/x-ttf\" \"application/otf\" \"application/x-otf\" \"application/truetype\" \"application/opentype\" \"application/x-opentype\" \"application/font-woff\" \"application/eot\" \"application/font\" \"application/font-sfnt\" \"application/wasm\" \"application/javascript-binast\" \"application/manifest+json\" \"application/ld+json\" \"application/graphql+json\" \"application/geo+json\"})",
						"action": "compress_response",
						"action_parameters": {
								"algorithms": [
										{
												"name": "zstd"
										},
										{
												"name": "brotli"
										},
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
