---
title: RTKPlugin
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/og.png?v=102d497d6646fe98
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKPlugin

Last updated Jul 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The RTKPlugin module represents a single plugin in the meeting. A plugin can be obtained from one of the plugin arrays in `meeting.plugins`. For example,

```ts
const plugin1 = meeting.plugins.active.get(pluginId);
const plugin2 = meeting.plugins.all.get(pluginId);
```

- [RTKPlugin](#module_RTKPlugin)
  - [.component](#module_RTKPlugin+component)
  - [.activateForSelf()](#module_RTKPlugin+activateForSelf)
  - [.deactivateForSelf()](#module_RTKPlugin+deactivateForSelf)
  - [.activate()](#module_RTKPlugin+activate)
  - [.deactivate()](#module_RTKPlugin+deactivate)

### plugin.component

The component for this plugin, as provided in the plugin config.

**Kind**: instance property of [`RTKPlugin`](#module_RTKPlugin)  

### plugin.activateForSelf()

**Kind**: instance method of [`RTKPlugin`](#module_RTKPlugin)  

### plugin.deactivateForSelf()

**Kind**: instance method of [`RTKPlugin`](#module_RTKPlugin)  

### plugin.activate()

Activate this plugin for all participants.

**Kind**: instance method of [`RTKPlugin`](#module_RTKPlugin)  

### plugin.deactivate()

Deactivate this plugin for all participants.

**Kind**: instance method of [`RTKPlugin`](#module_RTKPlugin)
