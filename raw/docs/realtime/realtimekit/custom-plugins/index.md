---
description: Create plugins that run inside RealtimeKit meetings.
title: Custom Plugins
image: https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/og.png?v=b09ca7355addf79a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Custom Plugins

Last updated Sep 3, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Plugins are interactive real-time applications that run inside a meeting, such as a shared whiteboard or a document viewer. RealtimeKit lets you build your own plugins and render them alongside the meeting UI.

A custom plugin is a DOM element that you register with the Core SDK. When a participant activates it, RealtimeKit makes it active for everyone in the session and renders it through the UI Kit.

To learn how plugins are registered and controlled through the SDK, refer to [Plugins](https://developers.cloudflare.com/realtime/realtimekit/core/plugins/).

## Guides

- [Build your own plugins](https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/build-your-own-plugins/)
