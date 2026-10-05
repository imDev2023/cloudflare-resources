---
description: Retrieve filters or rules with GET API requests.
title: GET examples
image: https://developers.cloudflare.com/firewall/api/cf-filters/get/og.png?v=86a3b99deb683fef
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# GET examples

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/get/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Get all filters

This example returns all filters in zone with ID `{zone_id}`.

*Requestbash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
  "result": [
    {
      "id": "<FILTER_ID_1>",
      "paused": false,
      "description": "Login from office",
      "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
    },
    {
      "id": "<FILTER_ID_2>",
      "paused": false,
      "description": "Login",
      "expression": "(http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
    },
    {
      "id": "<FILTER_ID_3>",
      "paused": false,
      "description": "not /api",
      "expression": "not http.request.uri.path matches \"^/api/.*$\""
    },
    {
      "id": "<FILTER_ID_4>",
      "paused": false,
      "description": "/api",
      "expression": "http.request.uri.path matches \"^/api/.*$\""
    },
    {
      "id": "<FILTER_ID_5>",
      "paused": false,
      "expression": "ip.src eq 93.184.216.0"
    }
  ],
  "success": true,
  "errors": [],
  "messages": [],
  "result_info": {
    "page": 1,
    "per_page": 25,
    "count": 5,
    "total_count": 5,
    "total_pages": 1
  }
}
```

## Get by filter ID

This example returns the filter with ID `{filter_id}`.

*Requestbash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
  "result": {
    "id": "<FILTER_ID>",
    "paused": false,
    "description": "Login from office",
    "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"
  },
  "success": true,
  "errors": [],
  "messages": []
}
```
