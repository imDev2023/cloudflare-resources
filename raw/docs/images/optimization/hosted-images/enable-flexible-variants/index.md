---
description: Turn on flexible variants in Cloudflare Images to allow dynamic resizing beyond predefined variant options.
title: Enable flexible variants
image: https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/og.png?v=d81e90a409a68ee4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enable flexible variants

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Flexible variants allow you to create variants with dynamic resizing which can provide more options than regular variants allow. This option is not enabled by default.

## Enable flexible variants via the Cloudflare dashboard

1. In the Cloudflare dashboard, go to the **Hosted Images** page. [Go to **Hosted images** ↗](https://dash.cloudflare.com/?to=/:account/images/hosted)
2. Select the **Delivery** tab.
3. Enable **Flexible variants**.

## Enable flexible variants via the API

Make a `PATCH` request to the [Update a variant endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit/).

```bash
curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '{"flexible_variants": true}'
```

After activation, you can use [optimization parameters](https://developers.cloudflare.com/images/optimization/features/#parameters) on any Cloudflare image. For example,

`https://imagedelivery.net/{account_hash}/{image_id}/w=400,sharpen=3`

Note

Flexible variants cannot be used for images that require a [signed delivery URL](https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/).
