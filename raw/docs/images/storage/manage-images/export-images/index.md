---
description: Download the original version of images stored in Cloudflare Images via the dashboard or API.
title: Export images
image: https://developers.cloudflare.com/images/storage/manage-images/export-images/og.png?v=2a27eb152a3ed374
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Export images

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/storage/manage-images/export-images/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Images supports image exports via the Cloudflare dashboard and API which allows you to get the original version of your image.

## Export images via the Cloudflare dashboard

1. In the Cloudflare dashboard, go to the **Hosted Images** page. [Go to **Hosted images** ↗](https://dash.cloudflare.com/?to=/:account/images/hosted)
2. Find the image or images you want to export.
3. To export a single image, select **Export** from its menu. To export several images, select the checkbox next to each image and then select **Export selected**.

Your images are downloaded to your machine.

## Export images via the API

Make a `GET` request as shown in the example below. `<IMAGE_ID>` must be fully URL encoded in the API call URL.

`GET accounts/<ACCOUNT_ID>/images/v1/<IMAGE_ID>/blob`
