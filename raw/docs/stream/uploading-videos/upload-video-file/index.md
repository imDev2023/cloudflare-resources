---
description: Upload video files under 200 MB to Cloudflare Stream using the dashboard or API.
title: Basic video uploads
image: https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/og.png?v=491f102a460f2f60
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/stream/llms.txt  
> Use this file to discover all available pages before exploring further.

# Basic video uploads

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Basic Uploads

For files smaller than 200 MB, you can use simple form-based uploads.

## Upload through the Cloudflare dashboard

1. In the Cloudflare dashboard, go to the **Stream** page. [Go to **Videos** ↗](https://dash.cloudflare.com/?to=/:account/stream/videos)
2. Drag and drop your video into the **Quick upload** area. You can also click to browse for the file on your machine.

After the video finishes uploading, the video appears in the list.

## Upload with the Stream API

Make a `POST` request with the `content-type` header set to `multipart/form-data` and include the media as an input with the name set to `file`.

*Upload video POST requestbash*

```bash
curl --request POST \
--header "Authorization: Bearer <API_TOKEN>" \
--form file=@/Users/user_name/Desktop/my-video.mp4 \
https://api.cloudflare.com/client/v4/accounts/{account_id}/stream
```

Note

Note that cURL's `--form` flag automatically configures the `content-type` header and maps `my-video.mp4` to a form input called `file`.
