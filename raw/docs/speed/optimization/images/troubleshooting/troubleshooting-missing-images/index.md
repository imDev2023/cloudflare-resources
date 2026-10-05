---
description: Fix missing or broken images after enabling image optimization.
title: Troubleshoot missing images
image: https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/og.png?v=3ec30b41d8bc48ae
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/speed/llms.txt  
> Use this file to discover all available pages before exploring further.

# Troubleshoot missing images

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If images are missing from your website, other Cloudflare features may be interfering with those images.

To troubleshoot:

1. Perform one of the following actions:
   - [Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache) for the URL of the missing image file.
   - [Temporarily pause Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/).
   - Disable [Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/).
2. Retest the image load in a private browser tab.
3. If the issue is not fixed, try another of the actions suggested in Step 1.
