---
title: RTKPlugins
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/og.png?v=f954e6c4554a10c8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKPlugins

Last updated Jul 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The RTKPlugins module consists of all the plugins in the meeting. It has 2 maps:

- `all`: Consists of all the plugins in the meeting.
- `active`: Consists of the plugins that are currently in use.

- [RTKPlugins](#module_RTKPlugins)
  - [.all](#module_RTKPlugins+all)
  - [.active](#module_RTKPlugins+active)

### meeting.plugins.all

All plugins accessible by the current user.

**Kind**: instance property of [`RTKPlugins`](#module_RTKPlugins)  

### meeting.plugins.active

All plugins that are currently enabled in the room.

**Kind**: instance property of [`RTKPlugins`](#module_RTKPlugins)
