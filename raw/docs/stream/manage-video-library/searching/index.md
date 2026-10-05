---
description: Search your Cloudflare Stream video library by name using the Stream API.
title: Search for videos
image: https://developers.cloudflare.com/stream/manage-video-library/searching/og.png?v=1d3524161262ff37
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/stream/llms.txt  
> Use this file to discover all available pages before exploring further.

# Search for videos

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/stream/manage-video-library/searching/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can search for videos by name through the Stream API by adding a `search` query parameter to the [list media files](https://developers.cloudflare.com/api/resources/stream/methods/list/) endpoint.

## What you will need

To make API requests you will need a [Cloudflare API token ↗︎](https://www.cloudflare.com/a/account/my-account) and your Cloudflare [account ID ↗︎](https://www.cloudflare.com/a/overview/).

## cURL example

This example lists media where the name matches `puppy.mp4`.

```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream?search=puppy" \
     -H "Authorization: Bearer <API_TOKEN>" \
     -H "Content-Type: application/json"
```
