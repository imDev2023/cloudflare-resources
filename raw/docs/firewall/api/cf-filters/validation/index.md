---
description: Validate firewall rule expressions via the API.
title: Expression validation
image: https://developers.cloudflare.com/firewall/api/cf-filters/validation/og.png?v=932666611ac48532
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# Expression validation

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/validation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Filters API supports an endpoint for validating expressions.

## Examples

### Validate expression via query string

*Requestbash*

```bash
curl "https://api.cloudflare.com/client/v4/filters/validate-expr?expression=ip.src==34" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
  "result": null,
  "success": false,
  "errors": [
    {
      "message": "Filter parsing error:\n`ip.src==34`\n          ^^ couldn't parse address in network: invalid IP address syntax\n"
    }
  ],
  "messages": null
}
```

Note the validation error in the response. In this example, the error is due to an invalid IP address format:

```txt
Filter parsing error:
`ip.src==34`
          ^^ couldn't parse address in network: invalid IP address syntax
```

### Validate expression via JSON object

*Requestbash*

```bash
curl "https://api.cloudflare.com/client/v4/filters/validate-expr" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>" \
--header "Content-Type: application/json" \
--data '{
  "expression": "ip.src in {2400:cb00::/32 2405:8100::/2000 2c0f:f248::/32 2a06:98c0::/29}"
}'
```

*Responsejson*

```json
{
  "result": null,
  "success": false,
  "errors": [
    {
      "message": "Filter parsing error:\n`ip.src in {2400:cb00::/32 2405:8100::/2000 2c0f:f248::/32 2a06:98c0::/29}`\n                                        ^^^^ number too large to fit in target type while parsing with radix 10\n"
    }
  ],
  "messages": null
}
```

Note the validation error in the response. In this example, the value for the subnet mask, `/2000`, is not a valid IPv6 CIDR mask:

```txt
Filter parsing error:
`ip.src in {2400:cb00::/32 2405:8100::/2000 2c0f:f248::/32 2a06:98c0::/29}`
                                       ^^^^ number too large to fit in target type while parsing with radix 10
```
