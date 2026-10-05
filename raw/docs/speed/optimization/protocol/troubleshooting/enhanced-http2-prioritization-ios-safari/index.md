---
description: Fix Enhanced HTTP/2 Prioritization issues on iOS and Safari.
title: Enhanced HTTP/2 Prioritization negatively affects iOS/Safari devices
image: https://developers.cloudflare.com/speed/optimization/protocol/troubleshooting/enhanced-http2-prioritization-ios-safari/og.png?v=6452e27b1e4a3cf1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/speed/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enhanced HTTP/2 Prioritization negatively affects iOS/Safari devices

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/speed/optimization/protocol/troubleshooting/enhanced-http2-prioritization-ios-safari/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Occasionally, [Enhanced HTTP/2 Prioritization](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/) can negatively affect the experience of visitors using Safari on macOS or any browser on iOS.

These visitors may notice not being able to load the site properly, such as images not displaying or content taking too long to load.

## Solution

If visitors using using Safari on macOS or any browser on iOS are experiencing issues with your site loading properly, try [disabling Enhanced HTTP/2 Prioritization](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/#enable-enhanced-http2-prioritization).

Note

Sometimes, [HTTP/2](https://developers.cloudflare.com/speed/optimization/protocol/http2/) will cause **Enhanced HTTP/2 Prioritization** to be re-enabled automatically.

If you notice this happening, also disable **HTTP/2**.
