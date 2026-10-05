---
description: API endpoints for managing filters and firewall rules.
title: Endpoints
image: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/og.png?v=0541b9f27e384b4a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# Endpoints

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To invoke a Cloudflare Firewall Rules API operation, append the endpoint to the Cloudflare API base URL:

```txt
https://api.cloudflare.com/client/v4/
```

For authentication instructions, refer to [Getting Started: Requests](https://developers.cloudflare.com/fundamentals/api/) in the Cloudflare API documentation.

For help with endpoints and pagination, refer to [Getting Started: Endpoints](https://developers.cloudflare.com/fundamentals/api/).

Note

The Firewall Rules API endpoints require a value for `<ZONE_ID>`.

To retrieve a list of zones associated with your account, use the [List Zones](https://developers.cloudflare.com/api/resources/zones/methods/list/) operation and note the zone ID associated with the domain whose firewall rules you want to manage.

The Cloudflare Firewall Rules API supports the operations outlined below. Visit the pages in this section for examples.

| Operation | Method & Endpoint | Notes |
| --- | --- | --- |
| [Create firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/create/) | `POST zones/<ZONE_ID>/firewall/rules` | Handled as a single transaction. If there is an error, the entire operation fails. |
| [List firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/list/) | `GET zones/<ZONE_ID>/firewall/rules` | Lists all current firewall rules. Results return paginated with 25 items per page by default. Use optional parameters to narrow results. |
| [Get a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/get/) | `GET zones/<ZONE_ID>/firewall/rules/<RULE_ID>` | Retrieve a single firewall rule by ID. |
| [Update firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_update/) | `PUT zones/<ZONE_ID>/firewall/rules` | Handled as a single transaction. All rules must exist for operation to succeed. If there is an error, the entire operation fails. |
| [Update a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/update/) | `PUT zones/<ZONE_ID>/firewall/rules/<RULE_ID>` | Update a single firewall rule by ID. |
| [Delete firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_delete/) | `DELETE zones/<ZONE_ID>/firewall/rules` | Delete existing firewall rules. Must specify list of firewall rule IDs. Empty requests result in no deletion. Returns HTTP status code 200 if a specified rule does not exist. |
| [Delete a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/delete/) | `DELETE zones/<ZONE_ID>/firewall/rules/<RULE_ID>` | Delete a firewall rule by ID. |
