---
description: Update filters or rules with PUT API requests.
title: PUT examples
image: https://developers.cloudflare.com/firewall/api/cf-filters/put/og.png?v=f719bf015b6a6f4c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# PUT examples

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/put/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Update multiple filters

This example updates two filters with IDs `<FILTER_ID_1>` and `<FILTER_ID_2>` using a single API call.

*Requestbash*

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/filters" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>" \
--header "Content-Type: application/json" \
--data '[
  {
    "id": "<FILTER_ID_1>",
    "paused": false,
    "expression": "ip.src eq 93.184.216.0",
    "description": "IP of example.org"
  },
  {
    "id": "<FILTER_ID_2>",
    "expression": "http.request.uri.path matches \"^/api/.*$\"",
    "description": "/api"
  }
]'
```

*Responsejson*

```json
{
  "result": [
    {
      "id": "<FILTER_ID>",
      "paused": false,
      "description": "IP of example.org",
      "expression": "ip.src eq 93.184.216.0"
    },
    {
      "id": "<FILTER_ID_2>",
      "paused": false,
      "description": "/api",
      "expression": "http.request.uri.path matches \"^/api/.*$\""
    }
  ],
  "success": true,
  "errors": [],
  "messages": []
}
```

## Update a single filter

This example updates the filter with ID `{filter_id}`.

*Requestbash*

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>" \
--header "Content-Type: application/json" \
--data '{
  "id": "<FILTER_ID>",
  "paused": false,
  "description": "Login from office",
  "expression": "ip.src in {2400:cb00::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
}'
```

*Responsejson*

```json
{
  "result": {
    "id": "<FILTER_ID>",
    "paused": false,
    "description": "Login from office",
    "expression": "ip.src in {2400:cb00::/32 2a06:98c0::/29} and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
  },
  "success": true,
  "errors": [],
  "messages": []
}
```
