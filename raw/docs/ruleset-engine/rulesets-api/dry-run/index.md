---
description: Validate rules and rulesets in the Cloudflare dashboard or with the Rulesets API without deploying changes.
title: Validate rule changes before deployment
image: https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/og.png?v=743eb1fcf2f86071
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ruleset-engine/llms.txt  
> Use this file to discover all available pages before exploring further.

# Validate rule changes before deployment

Last updated Sep 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare can validate a rule or ruleset before deployment. Validation checks the complete configuration without persisting or publishing changes.

Validation includes:

- Expression syntax and the availability of fields, functions, and operators
- Actions, action parameters, and phase compatibility
- Permissions, plan entitlements, and rule quotas
- References to resources used by the rule

## Dashboard validation

The Cloudflare dashboard automatically validates supported rule changes before deployment. If validation fails, the dashboard displays the error without publishing the change.

Dashboard validation is available for custom rules and rate limiting rules under **Security** > **Security rules**.

[Go to **Security rules** ↗](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)

It is also available when you create or update rules under **Rules** > **Overview**.

[Go to **Overview** ↗](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)

## API validation

Supported Rulesets API mutation endpoints accept the `dry_run=true` query parameter. You can use this parameter with `POST`, `PUT`, `PATCH`, and `DELETE` operations at the account or zone level.

A dry run performs the same authorization and server-side validation checks as the requested operation. It does not create, update, delete, or publish any configuration.

Only `true` and `false` are valid values for `dry_run`. An omitted value defaults to `false`. Any other value returns a `400` response.

### Example

The following request validates a rule update without applying it:

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

*Update a zone ruleset rulebash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules/$RULE_ID?dry_run=true" \
	--request PATCH \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"action": "block",
		"expression": "ip.src.country eq \"GB\"",
		"description": "Block requests from the United Kingdom",
		"enabled": true
	}'
```

The API returns the same errors and status codes as the corresponding write operation. A successful operation that normally returns `200` returns `result: null`. An operation that normally returns `204 No Content` continues to return `204`.

For supported operations and request schemas, refer to the [Rulesets API reference](https://developers.cloudflare.com/api/resources/rulesets/).
