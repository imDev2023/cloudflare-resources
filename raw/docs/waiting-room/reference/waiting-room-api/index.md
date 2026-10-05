---
description: API commands for managing waiting rooms.
title: API commands
image: https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/og.png?v=6647b72275fe40b0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waiting-room/llms.txt  
> Use this file to discover all available pages before exploring further.

# API commands

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Waiting Room redirect visitors to virtual waiting rooms when they are trying to access web pages that have high volumes of traffic.

The [Cloudflare Waiting Room API](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/list/) provides an interface for programmatically managing waiting rooms.

## Request URL format

To invoke a [Cloudflare Waiting Room API](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/list/) operation, append the endpoint to the Cloudflare API base URL:

```shell
https://api.cloudflare.com/client/v4
```

For authentication instructions, refer to [Getting Started: Requests](https://developers.cloudflare.com/fundamentals/api/) in the Cloudflare API documentation.

For help with endpoints and pagination, refer to [Getting Started: Endpoints](https://developers.cloudflare.com/fundamentals/api/).

## Manage your waiting room

| Operation | Method + URL stub | Notes |
| --- | --- | --- |
| [List waiting rooms](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/list/) | `GET zones/{:zone_identifier}/waiting_rooms` | List all waiting rooms for a zone. |
| [Create waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/create/) | `POST zones/{:zone_identifier}/waiting_rooms` | Create a waiting room. |
| [Waiting room details](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/get/) | `GET zones/{:zone_identifier}/waiting_rooms/{:identifier}` | Fetch a waiting room. |
| [Update waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/update/) | `PUT zones/{:zone_identifier}/waiting_rooms/{:identifier}` | Update a waiting room. |
| [Delete waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/delete/) | `DELETE zones/{:zone_identifier}/waiting_rooms/{:identifier}` | Delete a waiting room. |
| [Patch waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/edit/) | `PATCH zones/{:zone_identifier}/waiting_rooms/{:identifier}` | Patch a configured waiting room. |

## Fetch the current status of a waiting room

| Operation | Method + URL stub | Notes |
| --- | --- | --- |
| [Get the current status of a waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/statuses/methods/get/) | `GET zones/{:zone_identifier}/waiting_rooms/{:identifier}/status` | <ul><li>Returns `queueing` if the queue is activated (clients are put in the waiting room).</li><li>Returns `not_queueing` if the queue is not activated or if the waiting room is suspended.</li></ul> |
