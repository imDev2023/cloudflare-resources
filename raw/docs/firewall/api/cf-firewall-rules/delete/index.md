---
description: Delete filters or rules with DELETE API requests.
title: DELETE examples
image: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/og.png?v=7424e24a196e746f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# DELETE examples

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

The `DELETE` operation does not delete any filter related to the firewall rule. To delete the filter, use the [Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/).

## Delete multiple rules

This example deletes firewall rules with IDs `{rule_id_1}` and `{rule_id_2}`.

*Requestbash*

```bash
curl --request DELETE \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules?id={rule_id_1}&id={rule_id_2}" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
	"result": [
		{
			"id": "<RULE_ID_1>"
		},
		{
			"id": "<RULE_ID_2>"
		}
	],
	"success": true,
	"errors": [],
	"messages": []
}
```

## Delete a single rule

This example deletes the rule with ID `{rule_id}`.

*Requestbash*

```bash
curl --request DELETE \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
	"result": [
		{
			"id": "<RULE_ID>"
		}
	],
	"success": true,
	"errors": [],
	"messages": []
}
```
