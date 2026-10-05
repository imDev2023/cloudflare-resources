---
description: Delete filters or rules with DELETE API requests.
title: DELETE examples
image: https://developers.cloudflare.com/firewall/api/cf-filters/delete/og.png?v=7424e24a196e746f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# DELETE examples

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/delete/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Delete multiple filters

This example deletes filters with IDs `{filter_id_1}` and `{filter_id_2}`.

*Requestbash*

```bash
curl --request DELETE \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/filters?id={filter_id_1}&id={filter_id_2}" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
  "result": [
    {
      "id": "<FILTER_ID_1>"
    },
    {
      "id": "<FILTER_ID_2>"
    }
  ],
  "success": true,
  "errors": [],
  "messages": []
}
```

## Delete a single filter

This example deletes a single filter with ID `{filter_id}`.

*Requestbash*

```bash
curl --request DELETE \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}" \
--header "X-Auth-Email: <EMAIL>" \
--header "X-Auth-Key: <API_KEY>"
```

*Responsejson*

```json
{
  "result": [
    {
      "id": "<FILTER_ID>"
    }
  ],
  "success": true,
  "errors": [],
  "messages": []
}
```
