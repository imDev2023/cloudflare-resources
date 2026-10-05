---
description: Dynamic tokens available for use in custom error page HTML.
title: Error tokens
image: https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/og.png?v=bb91e5e6ccfb210a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error tokens

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## For Error Pages

Each custom error token provides diagnostic information or specific functionality that appears on the error page. Certain error pages require a page-specific custom error token.

To display a custom page for each error, create a separate page per error. For example, to create an error page for both **IP/Country Block** and **Interactive Challenge**, you must design and publish two separate pages.

The following custom error tokens are required by their respective error pages:

| Token | Required for |
| --- | --- |
| `::CAPTCHA_BOX::` | Interactive Challenge <br>Country Challenge (Managed Challenge)<br>Managed Challenge / I'm Under Attack Mode (Interstitial Page) |
| `::IM_UNDER_ATTACK_BOX::` | Non-Interactive Challenge |
| `::CLOUDFLARE_ERROR_500S_BOX::` | 5XX Errors |
| `::CLOUDFLARE_ERROR_1000S_BOX::` | 1XXX Errors |

Each custom error token has a default look and feel. However, you can use CSS to stylize each custom error tag using each tag's class ID. All the external resources like images, CSS, and scripts will be inlined during the process. As such, all external resources need to be available (that is, they must return `200 OK`) otherwise an error will be thrown.

## For Custom Error Assets, inline responses, and Error Pages

A custom error asset, inline response, or error page may also include the following error tokens, which will be replaced with their real values before sending the response to the visitor:

| Token | Description |
| --- | --- |
| `::CLIENT_IP::` | The visitor's IP address. |
| `::RAY_ID::` | A unique identifier given to every request that goes through Cloudflare. |
| `::GEO::` | The country or region associated with the visitor's IP address. |
